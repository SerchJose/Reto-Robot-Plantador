#include <Wire.h>
#include <MPU6050_light.h>

MPU6050 mpu1(Wire); 
MPU6050 mpu2(Wire); 

unsigned long timer = 0;

const int RPWM1 = D5; 
const int LPWM1 = D6; 
const int RPWM2 = D7; 
const int LPWM2 = D8; 

const float kp = 0.5; 
const float ki = 0.05; 
const float kd = 0.05; 

float intError1 = 0; 
float prevError1 = 0; 

float intError2 = 0; 
float prevError2 = 0; 

void setup() {
  Serial.begin(115200);
  Wire.begin();

  mpu1.setAddress(0x68);
  mpu1.begin();
  mpu1.calcGyroOffsets();

  mpu2.setAddress(0x69);
  mpu2.begin();
  mpu2.calcGyroOffsets();

  pinMode(RPWM1, OUTPUT);
  pinMode(LPWM1, OUTPUT);
  pinMode(RPWM2, OUTPUT);
  pinMode(LPWM2, OUTPUT);

  digitalWrite(RPWM1, LOW);
  digitalWrite(LPWM1, LOW);
  digitalWrite(RPWM2, LOW);
  digitalWrite(LPWM2, LOW);
}

void loop() {
  mpu1.update();
  mpu2.update();

  if ((millis() - timer) > 10) {
    timer = millis();

    float in_x1 = mpu1.getAngleX(); 
    float in_y1 = mpu1.getAngleY(); 
    float gz1 = mpu1.getAngleZ(); 

    float acx1 = mpu1.getAccX(); 
    float acy1 = mpu1.getAccY(); 
    float acz1 = mpu1.getAccZ(); 

    float in_x2 = mpu2.getAngleX(); 
    float in_y2 = mpu2.getAngleY(); 
    float gz2 = mpu2.getAngleZ(); 

    float acx2 = mpu2.getAccX(); 
    float acy2 = mpu2.getAccY(); 
    float acz2 = mpu2.getAccZ(); 

    Serial.print("MPU1: ");
    Serial.print(in_x1);  Serial.print(", "); 
    Serial.print(in_y1);  Serial.print(", "); 
    Serial.print(gz1);    Serial.print(", "); 
    Serial.print(acx1);   Serial.print(", "); 
    Serial.print(acy1);   Serial.print(", "); 
    Serial.print(acz1);   Serial.print("; "); 

    Serial.print("MPU2: ");
    Serial.print(in_x2);  Serial.print(", "); 
    Serial.print(in_y2);  Serial.print(", "); 
    Serial.print(gz2);    Serial.print(", "); 
    Serial.print(acx2);   Serial.print(", "); 
    Serial.print(acy2);   Serial.print(", "); 
    Serial.print(acz2);   Serial.println(); 

    float reference = 0; 
    float error1 = reference - in_x1; 
    float error2 = reference - in_x2; 

    Serial.print("Position 1: ");   Serial.println(in_x1); 
    Serial.print("Error 1: ");   Serial.println(error1); 

    Serial.print("Position 2: ");   Serial.println(in_x2); 
    Serial.print("Error 2: ");   Serial.println(error2); 

    intError1 += error1;
    float derError1 = error1 - prevError1;
    float control1 = kp * error1 + ki * intError1 + kd * derError1;

    control1 = constrain(control1, -127, 127);

    prevError1 = error1;

    intError2 += error2;
    float derError2 = error2 - prevError2;
    float control2 = kp * error2 + ki * intError2 + kd * derError2;

    control2 = constrain(control2, -127, 127);

    prevError2 = error2;

    float pwmValue1 = abs(control1);
    float pwmValue2 = abs(control2);

    if ((error1 > 1) && (error2 < -1) && (error1 < 15) && (error2 > -15)) {
      analogWrite(RPWM1, pwmValue1); 
      analogWrite(LPWM1, 0); 
      analogWrite(RPWM2, 0); 
      analogWrite(LPWM2, pwmValue1); 

      Serial.print("Motor 1: Clockwise, Velocity: ");
      Serial.println(pwmValue1);
      Serial.print("Motor 2: CounterClockwise, Velocity: ");
      Serial.println(pwmValue1);
    } 
    else if ((error1 < -1) && (error2 > 1) && (error1 > -15) && (error2 < 15)) {
      analogWrite(RPWM1, 0); 
      analogWrite(LPWM1, pwmValue2); 
      analogWrite(RPWM2, pwmValue2); 
      analogWrite(LPWM2, 0); 

      Serial.print("Motor 1: CounterClockwise, Velocity: ");
      Serial.println(pwmValue2);
      Serial.print("Motor 2: Clockwise, Velocity: ");
      Serial.println(pwmValue2);
    } 
    else {
      analogWrite(RPWM1, 0); 
      analogWrite(LPWM1, 0); 
      analogWrite(RPWM2, 0); 
      analogWrite(LPWM2, 0); 

      Serial.println("Motors stopped.");
    }

    delay(100);
  }
}
