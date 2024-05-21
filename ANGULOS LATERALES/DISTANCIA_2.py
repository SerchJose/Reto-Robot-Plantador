import time
from vl53l0x import VL53L0X

# Create a VL53L0X object
tof = VL53L0X()

# Start ranging
tof.start_ranging(VL53L0X.GOOD_ACCURACY_MODE)

# Read distance
try:
    while True:
        distance = tof.get_distance()
        print(f"Distance: {distance} mm")
        time.sleep(0.5)
except KeyboardInterrupt:
    # Stop ranging on Ctrl+C
    tof.stop_ranging()
