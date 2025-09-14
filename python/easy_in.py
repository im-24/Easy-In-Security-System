#python version 3.10.11
import cv2
import serial.tools.list_ports
import mamoduel
import face_recognition

lightstat = True
fanstat = True
doorstat =True
status = [lightstat , fanstat ,doorstat  ]
wCam , hCam = 640 , 480

url = 'http://192.168.100.5:8080/video'
cap = cv2.VideoCapture(url)
cap.set (3,wCam)
cap.set (4,hCam)
ptime = 0
tipIds = [4 ,8 , 12, 16, 20]
if not cap.isOpened():
    print("❌ Could not open video stream:", url)
    exit()

# Charger l'image du propriétaire
owner_image = face_recognition.load_image_file("owner.jpg")
owner_encoding = face_recognition.face_encodings(owner_image)[0]

# Charger l'image de la personne indésirable
unwanted_image = face_recognition.load_image_file("unwanted.jpg")
unwanted_encodings = face_recognition.face_encodings(unwanted_image)


# Vérifier si un visage est détecté dans l'image de la personne indésirable
if len(unwanted_encodings) > 0:
    unwanted_encoding = unwanted_encodings[0]
else:
    exit()

# Initialiser les encodages de visages connus et leurs noms
known_face_encodings = [owner_encoding, unwanted_encoding]
known_face_names = ["Owner", "Unwanted"]

ports= serial.tools.list_ports.comports()
seriaInst = serial.Serial()
portslist = []

seriaInst.baudrate = 9600
seriaInst.port = 'COM4'
seriaInst.open()

while True:
    success , frame = cap.read()

    if not success:
        break

    # Convertir l'image capturée de BGR (OpenCV) à RGB (face_recognition)
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    # Localiser les visages et calculer leurs encodages
    face_locations = face_recognition.face_locations(rgb_frame)
    face_encodings = face_recognition.face_encodings(rgb_frame, face_locations)

    # Parcourir chaque visage détecté
    for (top, right, bottom, left), face_encoding in zip(face_locations, face_encodings):
        # Comparer l'encodage du visage détecté avec les encodages connus
        matches = face_recognition.compare_faces(known_face_encodings, face_encoding)
        name = "Guest"  # Par défaut, toute personne inconnue est un invité
        color = (0, 255, 255)  # Jaune pour les invités

        # Si une correspondance est trouvée
        if True in matches:
            first_match_index = matches.index(True)
            name = known_face_names[first_match_index]

            # Définir la couleur en fonction du type de personne
            if name == "Owner":
                color = (0, 255, 0)  # Vert pour le propriétaire
            elif name == "Unwanted":
                color = (0, 0, 255)  # Rouge pour la personne indésirable

        # Dessiner un rectangle autour du visage
        cv2.rectangle(frame, (left, top), (right, bottom), color, 2)

        # Dessiner une étiquette avec le nom en dessous du visage
        cv2.rectangle(frame, (left, bottom - 35), (right, bottom), color, cv2.FILLED)
        cv2.putText(frame, name, (left + 6, bottom - 6), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (255, 255, 255), 2)


        if name== "Unwanted":
            msg = "alarm"
            seriaInst.write(msg.encode('utf-8'))

        if name=="Owner":
                hD = mamoduel.handDetector(detectionCon=0.75)
                mylist = hD.findPosition(rgb_frame)
                if len(mylist) != 0:
                    fingers = []

                    if mylist[tipIds[0]][1] < mylist[tipIds[0] - 2][1]:
                        fingers.append(1)
                    else:
                        fingers.append(0)


                    for id in range (1,5):
                        if mylist[tipIds[id]][2] < mylist[tipIds[id]-2][2] :
                            fingers.append(1)
                        else :
                            fingers.append(0)
                    print (fingers)

                    if fingers == [1,1,1,1,1]:
                        if status[0]:
                            msg= "lighton"
                            print(msg)
                            seriaInst.write(msg.encode('utf-8'))
                            status[0] = not(status[0])
                    elif fingers == [0,0,0,0,0]:
                        if not(status[0]):
                            msg = "lightoff"
                            print(msg)
                            seriaInst.write(msg.encode('utf-8'))
                            status[0] = not(status[0])

                    elif fingers == [0, 1, 1, 1, 0]:
                        if status[1]:
                            msg = "turnon"
                            print(msg)
                            seriaInst.write(msg.encode('utf-8'))
                            status[1] = not (status[1])
                    elif fingers == [1, 0, 0, 0, 1]:
                        if not (status[1]):
                            msg = "turnoff"
                            print(msg)
                            seriaInst.write(msg.encode('utf-8'))
                            status[1] = not (status[1])

                    if fingers == [0, 1, 1, 1, 1]:
                        if status[2]:
                            msg = "open"
                            print(msg)
                            seriaInst.write(msg.encode('utf-8'))
                            status[2] = not (status[2])
                    elif fingers == [0, 0, 1, 1, 1]:
                        if not (status[2]):
                            msg = "close"
                            print(msg)
                            seriaInst.write(msg.encode('utf-8'))
                            status[2] = not (status[2])

        #fps funciton


    cv2.imshow('Mobile Camera', frame)
    cv2.waitKey(1)
cap.release()
cv2.destroyAllWindows()
