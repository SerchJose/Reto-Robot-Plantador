import numpy as np
import cv2


def get_limits(color):
    c = np.uint8([[color]])  # BGR values
    hsvC = cv2.cvtColor(c, cv2.COLOR_BGR2HSV)
    hue = hsvC[0][0][0]  # Get the hue value

    radsh_hue_low=0
    radsh_hue_up=10

    lowerLimit = np.array([radsh_hue_low, 20, 20], dtype=np.uint8)
    upperLimit = np.array([radsh_hue_up, 255, 255], dtype=np.uint8)
    
    return lowerLimit, upperLimit




    