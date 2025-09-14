#include <Servo.h>



const int light = 13;

const int fan = 8;

const int door_pin = 10;

const int alarm = 7;

int msg = 0;

Servo door;


void setup() {


Serial.begin(9600);

pinMode(alarm, OUTPUT);

pinMode(light, OUTPUT);

pinMode(alarm, OUTPUT);

pinMode (fan, OUTPUT);

door.attach(door_pin);


}

 

void loop() {


if (msg == 0) {
  
digitalWrite(alarm, HIGH); 
  
delay(3000);

digitalWrite(alarm, LOW); 
  
msg++ ;
  
Serial.print(msg);

}

else if (msg == 1) {
  delay(3000);

digitalWrite(light, HIGH); 
msg++;

}

else if (msg ==2) {
 delay(3000);

digitalWrite(light, LOW); 

msg++ ;

}

else if (msg == 3) {
  Serial.print("open the door");
 door.write(180);
    msg++;
   

}

else if (msg == 4) {
delay(3000);
  door.write(90);  
msg++ ;


}

else if (msg == 5) {

delay(3000);
  digitalWrite(fan, HIGH);
msg++ ;


}

else if (msg == 6) {
delay(3000);
digitalWrite(fan, LOW); 
 
msg++ ;
  
}

else {
  delay(3000);


msg++ ;


}

}

