import cv2
import mediapipe as mp


class handDetector():
    def __init__(self, mode=False, maxHands=2, complexity=1, detectionCon=0.5, trackCon=0.5):
        self.mode = mode
        self.maxHands = maxHands
        self.complexity = complexity
        self.detectionCon = detectionCon
        self.trackCon = trackCon

        self.mpHands = mp.solutions.hands
        self.hands = self.mpHands.Hands(self.mode, self.maxHands, self.complexity,
                                        self.detectionCon, self.trackCon)

        self.mpDraw = mp.solutions.drawing_utils

    def findHands(self, imgRGB):
        self.results = self.hands.process(imgRGB)
        if self.results.multi_hand_landmarks:
            for handslm in self.results.multi_hand_landmarks:
                self.mpDraw.draw_landmarks(imgRGB, handslm, self.mpHands.HAND_CONNECTIONS)
        return imgRGB

    def findPosition(self, img, handNb=0):

        lmList = []
        self.results = self.hands.process(img)
        if self.results.multi_hand_landmarks:

            hands = self.results.multi_hand_landmarks[handNb]
            for handslm in self.results.multi_hand_landmarks:
                self.mpDraw.draw_landmarks(img,handslm, self.mpHands.HAND_CONNECTIONS)
            for id, lm in enumerate(hands.landmark):
                h, w, c = img.shape
                cx, cy = int(lm.x * w), int(lm.y * h)
                lmList.append([id, cx, cy])

            if lmList[2][1] > lmList[17][1]:
                v=lmList[4]
                lmList[4]=lmList[2]
                lmList[2]=v



        return lmList