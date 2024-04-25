import cv2
from PIL import Image
from util1 import get_limits
import os
import sys
import time

sys.path.append(os.path.join(os.path.dirname(__file__), '../../..'))

from xarm.wrapper import XArmAPI
from configparser import ConfigParser

yellow = [0, 255, 255]  # yellow in BGR colorspace
cap = cv2.VideoCapture(0) #External
#cap1 = cv2.VideoCapture(0) #Webcam
x=0
y=0

"""
Just for test example
"""
if len(sys.argv) >= 2:
    ip = sys.argv[1]
else:
    try:
        from configparser import ConfigParser
        parser = ConfigParser()
        parser.read('../robot.conf')
        ip = parser.get('xArm', 'ip')
    except:
        ip = ('192.68.1.158')
        if not ip:
            print('input error, exit')
            sys.exit(1)
###############################
arm = XArmAPI(ip, is_radian=True)
arm.motion_enable(enable=True)
arm.set_mode(0)
arm.set_state(state=0)

arm.reset(wait=True)

while True:
    #External
    ret, frame = cap.read() 
    hsvImage = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    lowerLimit, upperLimit = get_limits(color=yellow)
    mask = cv2.inRange(hsvImage, lowerLimit, upperLimit)
    mask_ = Image.fromarray(mask)
    bbox = mask_.getbbox()
    if bbox is not None:
        x1, y1, x2, y2 = bbox
        frame = cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 5)
        pepe=200
        if x==200:
            arm.set_position(x=200, y=0, z=0, roll=-180, pitch=0, yaw=0, speed=100, is_radian=False, wait=True)
        elif x==100:
            arm.set_position(x=0, y=50, z=0, roll=-180, pitch=0, yaw=0, speed=100, is_radian=False, wait=True)
            arm.set_gripper_mode(0)
            arm.set_gripper_enable(True)
            arm.set_gripper_speed(5000)
            arm.set_gripper_position(600, wait=True)
        arm.reset(wait=True)

        arm.disconnect()
        print(pepe)
        ord=('q')
        
    cv2.imshow('frame', frame)
    cv2.imshow('mask', mask)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

    
cap.release()


cv2.destroyAllWindows()

