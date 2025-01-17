from imutils.video import VideoStream
import datetime
import imutils
import time
import cv2
import numpy as np

video_path = None
buffsize = 64
indx = 0

# Lower and upper boundaries of a "red" object in HSV color space
red_range = [(0, 50, 50), (10, 255, 255)]

# Initialize the list of tracked points
path = np.zeros((buffsize, 2), dtype="int")

if video_path is None:
    vs = VideoStream().start()
    # Warm up the camera
    time.sleep(2)
else:
    vs = cv2.VideoCapture(video_path)

while True:
    frame = vs.read()
    frame = frame if video_path is None else frame[1]

    # If there is no more frame in the video, continue
    if frame is None:
        continue

    frame = imutils.resize(frame, width=500)

    blur = cv2.GaussianBlur(frame, (9, 9), 0)
    hsv = cv2.cvtColor(blur, cv2.COLOR_BGR2HSV)

    mask = cv2.inRange(hsv, red_range[0], red_range[1])
    mask = cv2.erode(mask, None, iterations=2)
    mask = cv2.dilate(mask, None, iterations=2)

    cnts = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)[0]

    if len(cnts) > 0:
        # Find the largest contour in the mask
        cnt = max(cnts, key=cv2.contourArea)

        ((x, y), radius) = cv2.minEnclosingCircle(cnt)
        M = cv2.moments(cnt)
        center = (int(M["m10"] / M["m00"]), int(M["m01"] / M["m00"]))

        if radius > 10:
            cv2.circle(frame, (int(x), int(y)), int(radius), (0, 255, 255), 2)
            cv2.circle(frame, center, 5, (0, 0, 255), -1)

            # Update the path list
            if indx < buffsize:
                path[indx] = (center[0], center[1])
                indx += 1
            else:
                path[0 : indx - 1] = path[1:indx]
                path[indx - 1] = (center[0], center[1])

    for i in range(1, len(path)):
        # If either of the tracked points are None, ignore them
        if path[i - 1] is None or path[i] is None:
            continue
        # Otherwise, compute thickness and draw lines
        thickness = int(np.sqrt(len(path) / float(i + 1)) * 2.5)
        cv2.line(
            frame,
            (path[i - 1][0], path[i - 1][1]),
            (path[i][0], path[i][1]),
            (0, 0, 255),
            thickness,
        )

    # Create a black and white image with red object highlighted in white
    result_image = cv2.bitwise_and(frame, frame, mask=mask)

    # Display the original frame and the black and white image
    cv2.imshow("Original Frame", frame)
    cv2.imshow("Black and White Image", result_image)

    # Check for the 'q' key to exit the loop
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

# Release the video stream and close OpenCV windows
vs.release()
cv2.destroyAllWindows()
