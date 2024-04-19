import cv2
import numpy as np

def detect_red(image):
    # Convert BGR to HSV
    hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
    
    # Define range of red color in HSV
    lower_red = np.array([0, 100, 100])
    upper_red = np.array([10, 255, 255])

    # Threshold the HSV image to get only red colors
    mask1 = cv2.inRange(hsv, lower_red, upper_red)

    lower_red = np.array([160, 100, 100])
    upper_red = np.array([179, 255, 255])

    # Threshold the HSV image to get only red colors
    mask2 = cv2.inRange(hsv, lower_red, upper_red)

    # Combine the masks
    mask = cv2.bitwise_or(mask1, mask2)

    # Count the number of red pixels
    total_pixels = np.sum(mask > 0)

    # Calculate the percentage of red pixels
    percentage_red = (total_pixels / (image.shape[0] * image.shape[1])) * 100

    return percentage_red

def main():
    cap = cv2.VideoCapture(0)

    while True:
        ret, frame = cap.read()
        if not ret:
            print("Failed to capture frame from webcam")
            break

        # Detect red in the frame
        red_percentage = detect_red(frame)

        print("Percentage of red:", red_percentage)

        # Check if the percentage of red is more than 50%
        if red_percentage > 50:
            print("More red")

        # Display the frame
        cv2.imshow('Frame', frame)

        # Exit if 'q' is pressed
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # Release the capture
    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()