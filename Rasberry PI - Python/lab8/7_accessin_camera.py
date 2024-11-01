from picamera.array import PiRGBArray
from picamera import PiCamera
import time
import cv2

camera = PiCamera()
capture = PiRGBArray(camera)

time.sleep(1.0)
camera.capture(capture, format="bgr")
image = capture.array

cv2.imshow("Image", image)
cv2.waitKey(0)
cv2.destroyAllWindows()
