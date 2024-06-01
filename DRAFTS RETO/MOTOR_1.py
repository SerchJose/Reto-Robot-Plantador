import RPi.GPIO as GPIO
import time

# Define motor control pins
RPWM = 18
LPWM = 19

# Set up GPIO mode
GPIO.setmode(GPIO.BCM)

# Set up the motor control pins as output
GPIO.setup(RPWM, GPIO.OUT)
GPIO.setup(LPWM, GPIO.OUT)

# Set up PWM for motor control
pwm_r = GPIO.PWM(RPWM, 1000)  # Set frequency to 1kHz
pwm_l = GPIO.PWM(LPWM, 1000)  # Set frequency to 1kHz

# Start PWM with 0 duty cycle (motor stopped)
pwm_r.start(0)
pwm_l.start(0)

def motor_forward(speed):
    pwm_r.ChangeDutyCycle(speed)
    pwm_l.ChangeDutyCycle(0)

def motor_backward(speed):
    pwm_r.ChangeDutyCycle(0)
    pwm_l.ChangeDutyCycle(speed)

def motor_stop():
    pwm_r.ChangeDutyCycle(0)
    pwm_l.ChangeDutyCycle(0)

try:
    while True:
        # Run motor forward at full speed
        motor_forward(100)
        time.sleep(2)  # Run for 2 seconds

        # Run motor backward at full speed
        motor_backward(100)
        time.sleep(2)  # Run for 2 seconds

        # Stop the motor
        motor_stop()
        time.sleep(2)  # Stop for 2 seconds

except KeyboardInterrupt:
    pass

# Clean up GPIO
pwm_r.stop()
pwm_l.stop()
GPIO.cleanup()
