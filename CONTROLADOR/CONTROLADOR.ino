//Libraries
#include <Wire.h>
#include <MPU6050_light.h>

// Define Both MPU6050 Objects

MPU6050 mpu1(Wire);             // Right Side MPU6050
MPU6050 mpu2(Wire);             // Left Side MPU6050

unsigned long timer = 0;

// Define Motor Pins

// Right Side Motor
const int RPWM1 = D5;           // Clockwise direction
const int LPWM1 = D6;           // CounterClockwise direction
// Left Side Motor
const int RPWM2 = D7;           // Clockwise direction
const int LPWM2 = D8;           // CounterClockwise direction


// Control System Variables
const float kp = 0.5;             // Proportionag Gain
const float ki = 0.05;          // Integral Gain
const float kd = 0.05;          // Derivative Gain

float intError1 = 0;            // Integral error for MPU1
float prevError1 = 0;           // Previous error for MPU1

float intError2 = 0;            // Integral error for MPU2
float prevError2 = 0;           // Previous error for MPU2

void setup() {
  Serial.begin(115200);
  Wire.begin();

  // Initialize The First MPU6050 And Set Its Address
  mpu1.setAddress(0x68);
  mpu1.begin();
  mpu1.calcGyroOffsets();

  // Initialize The First MPU6050 And Set Its Address
  mpu2.setAddress(0x69);
  mpu2.begin();
  mpu2.calcGyroOffsets();

  // Set Motor Pins As Outputs
  pinMode(RPWM1, OUTPUT);
  pinMode(LPWM1, OUTPUT);
  pinMode(RPWM2, OUTPUT);
  pinMode(LPWM2, OUTPUT);

  // Set Motor Pins In Low
  digitalWrite(RPWM1, LOW);
  digitalWrite(LPWM1, LOW);
  digitalWrite(RPWM2, LOW);
  digitalWrite(LPWM2, LOW);
}

void loop() {
  // Update both MPU6050
  mpu1.update();
  mpu2.update();

  // Start Timer
  if ((millis() - timer) > 10) {
    timer = millis();
/*
    // Read Data From The First MPU6050
    int in_x1 = round(mpu1.getAngleX()-0.3);                               // Angle On The X Axis
    int in_y1 = round(mpu1.getAngleY()-1.9);                        // Angle On The Y Axis
    int gz1 = round(mpu1.getAngleZ());              // Angle On The Z Axis

    int acx1 = round(mpu1.getAccX());                                  // Acceleration On The X Axis
    int acy1 = round(mpu1.getAccY());                                  // Acceleration On The Y Axis
    int acz1 = round(mpu1.getAccZ()+9);                             // Acceleration On The Z Axis

    // Read Data From The Second MPU6050
    int in_x2 = round(mpu2.getAngleX()-0.5);                               // Angle On The X Axis
    int in_y2 = round(mpu2.getAngleY()-13);                         // Angle On The Y Axis
    int gz2 = round(mpu2.getAngleZ()+1);              // Angle On The Z Axis

    int acx2 = round(mpu2.getAccX());                                  // Acceleration On The X Axis
    int acy2 = round(mpu2.getAccY());                                  // Acceleration On The Y Axis
    int acz2 = round(mpu2.getAccZ()+9);                              // Acceleration On The Z Axis
*/

    int in_x1 = mpu1.getAngleX();                               // Angle On The X Axis
    int in_y1 = mpu1.getAngleY();                        // Angle On The Y Axis
    int gz1 = mpu1.getAngleZ();              // Angle On The Z Axis

    int acx1 = mpu1.getAccX();                                  // Acceleration On The X Axis
    int acy1 = mpu1.getAccY();                                  // Acceleration On The Y Axis
    int acz1 = mpu1.getAccZ();                             // Acceleration On The Z Axis

    // Read Data From The Second MPU6050
    int in_x2 = mpu2.getAngleX();                               // Angle On The X Axis
    int in_y2 = mpu2.getAngleY();                         // Angle On The Y Axis
    int gz2 = mpu2.getAngleZ();              // Angle On The Z Axis

    int acx2 = mpu2.getAccX();                                  // Acceleration On The X Axis
    int acy2 = mpu2.getAccY();                                  // Acceleration On The Y Axis
    int acz2 = mpu2.getAccZ();                              // Acceleration On The Z Axis

    // Print data from the first MPU6050
    Serial.print("MPU1: ");
    Serial.print(in_x1);  Serial.print(", ");                     // Print Angle On The X Axis
    Serial.print(in_y1);  Serial.print(", ");                     // Print Angle On The Y Axis
    Serial.print(gz1);    Serial.print(", ");                     // Print Angle On The Z Axis
    Serial.print(acx1);   Serial.print(", ");                     // Print Acceleration On The X Axis
    Serial.print(acy1);   Serial.print(", ");                     // Print Acceleration On The Y Axis
    Serial.print(acz1);   Serial.print("; ");                     // Print Acceleration On The Z Axis

    // Print data from the second MPU6050
    Serial.print("MPU2: ");
    Serial.print(in_x2);  Serial.print(", ");                     // Print Angle On The X Axis
    Serial.print(in_y2);  Serial.print(", ");                     // Print Angle On The Y Axis
    Serial.print(gz2);    Serial.print(", ");                     // Print Angle On The Z Axis
    Serial.print(acx2);   Serial.print(", ");                     // Print Acceleration On The X Axis
    Serial.print(acy2);   Serial.print(", ");                     // Print Acceleration On The Y Axis
    Serial.print(acz2);   Serial.println();                       // Print Acceleration On The Z Axis

    float reference = 0;                                          // Target angle for MPU1 is 0°
    float error1 = reference - in_x1;                             // Error MPU1
    float error2 = reference - in_x2;                             // Error MPU2

    Serial.print("Position 1: ");   Serial.println(in_x1);        // Print Current Position 1
    Serial.print("Error 1: ");   Serial.println(error1);          // Print Error1

    Serial.print("Position 2: ");   Serial.println(in_x2);        // Print Current Position 2
    Serial.print("Error 2: ");   Serial.println(error2);          // Print Error2

// PID Controller Calculations for MPU1
    intError1 += error1;
    float derError1 = error1 - prevError1;
    float control1 = kp * error1 + ki * intError1 + kd * derError1;

    // Constrain control signal to [-1, 1]
    control1 = constrain(control1, 0, 1);

    // Update previous error for MPU1
    prevError1 = error1;

// PID Controller Calculations for MPU2
    intError2 += error2;
    float derError2 = error2 - prevError2;
    float control2 = kp * error2 + ki * intError2 + kd * derError2;

    // Constrain control signal to [-1, 1]
    control2 = constrain(control2, 0, 1);

    // Update previous error for MPU2
    prevError2 = error2;

    // Controllers
    if ((error1 > 1) && (error2 < -1) && (error1 < 15) && (error2 > -15)) {
      analogWrite(RPWM1, abs(control1) * 127);  // Control Motor 1 in Clockwise direction
      analogWrite(LPWM1, 0);  // Stop Motor 1 in CounterClockwise direction
      analogWrite(RPWM2, 0);  // Stop Motor 2 in Clockwise direction
      analogWrite(LPWM2, abs(control1) * 127);  // Control Motor 2 in CounterClockwise direction

      Serial.print("Motor 1: Clockwise, Velocity: ");
      Serial.println(abs(control1) * 127);
      Serial.print("Motor 2: CounterClockwise, Velocity: ");
      Serial.println(abs(control1) * 127);
    } 
    else if ((error1 < -1) && (error2 > 1) && (error1 > -15) && (error2 < 15)) {
      analogWrite(RPWM1, 0);  // Stop Motor 1 in Clockwise direction
      analogWrite(LPWM1, abs(control2) * 127);  // Control Motor 1 in CounterClockwise direction
      analogWrite(RPWM2, abs(control2) * 127);  // Control Motor 2 in Clockwise direction
      analogWrite(LPWM2, 0);  // Stop Motor 2 in CounterClockwise direction

      Serial.print("Motor 1: CounterClockwise, Velocity: ");
      Serial.println(abs(control2) * 127);
      Serial.print("Motor 2: Clockwise, Velocity: ");
      Serial.println(abs(control2) * 127);
    } 
    else {
      analogWrite(RPWM1, 0);  // Stop Motor 1 in Clockwise direction
      analogWrite(LPWM1, 0);  // Stop Motor 1 in CounterClockwise direction
      analogWrite(RPWM2, 0);  // Stop Motor 2 in Clockwise direction
      analogWrite(LPWM2, 0);  // Stop Motor 2 in CounterClockwise direction

      Serial.println("Motors stopped.");
    }

    delay(100);
  }
}
