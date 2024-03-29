import cv2
import numpy as np

cap = cv2.VideoCapture(r"D:\College\External Courses\CrocoMarine ROV Competitions\Distance_Estimation_Using_YOLOv8\Data\Videos\Sample 5.mp4")

frame_width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
frame_height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

# Define the lower and upper bounds for the color range
lower_color = np.array([0, 0, 0])  # Lower bound for black color
upper_color = np.array([20, 255, 255])  # Upper bound for reddish-orange color

while True:
    ret, frame = cap.read()
    if not ret:
        break

    frame = cv2.resize(frame, (640, 480))

    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # Create a mask to detect colors within the specified range
    mask = cv2.inRange(hsv, lower_color, upper_color)

    # Find contours around non-black areas
    contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    # Check if contours are found
    if contours:
        # Find the contour with the largest area
        max_contour = max(contours, key=cv2.contourArea)
    
        # Draw bounding box around the largest contour
        if max_contour is not None:
            x, y, w, h = cv2.boundingRect(max_contour)
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

    cv2.imshow('Frame', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
