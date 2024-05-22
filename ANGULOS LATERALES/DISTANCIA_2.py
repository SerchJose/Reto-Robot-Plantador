import VL53L0X

def main():
    # Create a VL53L0X object
    tof = VL53L0X.VL53L0X()

    # Start ranging
    tof.start_ranging(VL53L0X.VL53L0X_BETTER_ACCURACY_MODE)

    try:
        while True:
            # Get distance in mm
            distance = tof.get_distance()
            print("Distance: {} mm".format(distance))
    except KeyboardInterrupt:
        # Stop ranging on KeyboardInterrupt
        tof.stop_ranging()

if __name__ == "__main__":
    main()
