bool condition = true ;
#include <Servo.h>
const int light_pin = 13;
const int fan_pin = 8;
const int door_pin = 10;
const int alarm_pin = 7;
Servo door;

void setup() {
Serial.begin(9600);
door.attach(door_pin);
pinMode(fan_pin, OUTPUT);
pinMode(light_pin, OUTPUT);
pinMode(alarm_pin, OUTPUT);
}
void loop() {

if (Serial.available() > 0) {

String msg = Serial.readString();
Serial.println(msg);
if (msg == "alarm") {
digitalWrite(alarm_pin, HIGH);
Serial.println("Alarm is ON");
delay(2000); 
digitalWrite(alarm_pin, LOW);
Serial.println("Alarm is OFF");
}
if (msg == "lighton") {
digitalWrite(light_pin, HIGH);
Serial.println("Light is ON");
}
else if (msg == "lightoff") {
      printf("%s",&msg);
      digitalWrite(light_pin, LOW) ;
    } 
    else if (msg == "turnon") {
      digitalWrite(fan_pin, HIGH) ;
    }else if(msg == "turnoff" ) {
      printf("%s",&msg);
      digitalWrite(fan_pin, LOW) ;
    }
    else if (msg == "open") {
      door.write(90);
    }else if(msg == "close" ) {
      printf("%s",&msg);
      door.write(0);
    }
    else if(msg == "alarm" ) {
      printf("%s",&msg);
      digitalWrite(alarm_pin, HIGH) ;
      delay(1000);
      digitalWrite(alarm_pin, LOW) ;
      
    }

}}
