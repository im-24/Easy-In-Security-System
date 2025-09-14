# Easy-In: Security and Control System  

This project combines an **Arduino Uno** (as a microcontroller) with Python libraries such as **OpenCV (cv2)** and **MediaPipe** to build a security and control system.  

The system detects faces and classifies them into three categories:  

- **Owner** → Can control connected devices using hand gestures.  
- **Unwanted** → Access is locked, and an alert is triggered.  
- **Geust** → Recognized, but with limited or no control privileges.  

---

## Requirements  

### Python Requirements  
- Python 3.10  
- `mediapipe`        → bash `pip install mediapipe`  
- `face-recognition` → bash `pip install face-recognition`  
- `opencv-python`    → bash `pip install opencv-python`  
- `dlib`             → bash `pip install dlib`  

If `dlib` installation fails:  
1. Install CMake → bash `pip install cmake`  
2. Install a compiler:  
   - Windows → Visual Studio Build Tools  
   - Linux/macOS → usually preinstalled (`g++` / `clang`)  
3. Retry → bash `pip install dlib`  

---

### Arduino Uno Requirements  

**Hardware:**  
- PC camera or external USB/IP camera  
- Arduino Uno R3  
- USB cable  
- Breadboard + jumper wires  
- Yellow LED  
- 3.3 kΩ resistor  
- Positional micro servo  
- DC motor  
- NPN transistor (BJT)  
- 9V battery  
- 1 kΩ resistor  
- Piezo buzzer  

**Software:**  
- Arduino IDE  

**Libraries:**  
- `Servo.h`  

**Serial Commands (from Python → Arduino):**  
- `"alarm"` → trigger alert when unwanted face detected  
- `"lighton"` → turn LED on  
- `"lightoff"` → turn LED off  
- `"turnon"` → start DC motor (fan)  
- `"turnoff"` → stop DC motor (fan)  
- `"open"` → rotate servo +90° (open door)  
- `"close"` → rotate servo -90° (close door)  

**Wiring:**  
- LED → pin 13  
- DC motor → pin 8  
- Servo motor → pin 10  
- Piezo buzzer → pin 7  

---

## Usage  

1. Make sure Python and a compiler are installed.  
2. Install dependencies
bash
pip install cmake
pip install mediapipe face-recognition opencv-python dlib

3. Save two pictures with the name 'owner.jpg' for the user and 'unwanted.jpg' for the unwanted person in the same folder as the program. Make sure the images are in jpg format and shows clearly the face
4. Depending on the camera you're using change the url variable in 'easy-in.py' file (line 20) to refere the link of the camera ( 0 for the pc default camera or the url for external camera / video )
5. Plug the USB cable in Arduino UNO and upload Arduino program (only one time )
6. Run the program easy-in with the command :
python easy_in.py

 The script will open a window shows the camera and respond as follows:
- if Unsaved face is captured : draws a yellow rectangle on the face labeled 'Geust'
- if Saved face is captured :
    - Unwanted : draws a red rectangle labeled 'Unwanted', wont respond to any command and start alert 
    - Owner : draws green rectangle labeled 'owner' and responds to the commands:
 
7. The owner is able to use hand gestures to control the elements that are plugged to arduino , place the hand in front of the camera vertically and use the following commands (finger up represented by 1 , finger down represented by 0 ):


|command                      |  Thumb    |   Index   |    Middle |   Ring    |   Little  |
|-----------------------------|:---------:|:---------:|:---------:|:---------:|:---------:|
|light up the LED             |      1    |      1    |      1    |      1    |     1     |
|light off the LED            |      0    |      0    |      0    |      0    |     0     |
|turn on the fan (DC motor)   |      0    |      1    |      1    |      1    |     0     |
|turn off the fan (DC motor)  |      1    |      0    |      0    |      0    |     1     |
|open the door   (servo +90)  |      0    |      1    |      1    |      1    |     1     |
|close the door  (servo -90)  |      0    |      0    |      1    |      1    |     1     |



## Important Notes :
- The system cannot match hands to faces. If both the owner and guest/unwanted appear together, conflicts may occur.
- The program uses a lot of memory and may crash if run for too long.
- Performance depends on hardware—slower PCs may lag.
- Make sure you are using the right port to connect arduino (COM4 for windows or search for the port name in )

# Disclaimer
**The author is not responsible for any misuse or damages caused by this script. Use at your own risk.**

*Enjoy !*
