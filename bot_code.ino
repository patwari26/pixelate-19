#include<SoftwareSerial.h>
void setup() {
  // put your setup code here, to run once:
Serial.begin(9600);
pinMode(12,OUTPUT);   //motor 1 is connected here
pinMode(8,OUTPUT);    //motor 1 is connected here
pinMode(7,OUTPUT);    //motor 2 is connected here
pinMode(4,OUTPUT);    //motor 2 is connected here
pinMode(10,OUTPUT);   //pwm1
pinMode(9,OUTPUT);    //pwm2
}

void loop() {
  // put your main code here, to run repeatedly:
if(Serial.available()>0){
     char var = Serial.read();
      {
           if(var == 'b'){
            backward();
           }
           if(var == 'f'){
            forward();
           }
           if(var == 'l'){
            left();
           }
           if(var == 'r'){
            right();
           }
           if(var=='s'){
            stop_bot();
           }
      }
}  
}
void backward(void){
     digitalWrite(12,HIGH);
     digitalWrite(8,LOW);
     digitalWrite(7,HIGH);
     digitalWrite(4,LOW);
     analogWrite(10,60);
     analogWrite(9,60);
     Serial.println("move forward");
}
void forward(void){
     digitalWrite(12,LOW);
     digitalWrite(8,HIGH);
     digitalWrite(7,LOW);
     digitalWrite(4,HIGH);
     analogWrite(10,60);
     analogWrite(9,60);
     Serial.println("move backward");
}
void left(void){
     digitalWrite(12,HIGH);
     digitalWrite(8,LOW);
     digitalWrite(7,LOW);
     digitalWrite(4,HIGH);
     analogWrite(10,70);
     analogWrite(9,70);
     Serial.println("turn right");
}
void right(void){
     digitalWrite(12,LOW);
     digitalWrite(8,HIGH);
     digitalWrite(7,HIGH);
     digitalWrite(4,LOW);
     analogWrite(10,70);
     analogWrite(9,70);
     Serial.println("turn left");
}
void blink_led(void){
     digitalWrite(13,HIGH);
     delay(1000);
     digitalWrite(13,LOW);
     Serial.println("LED on");
}
void stop_bot(void){
     digitalWrite(12,LOW);
     digitalWrite(8,LOW);
     digitalWrite(7,LOW);
     digitalWrite(4,LOW);
     Serial.println("PS completed.");
}

