from imutils.video import VideoStream
from pyzbar import pyzbar
import imutils
import datetime
import argparse
import time
import cv2

vid = cv2.VideoCapture(0)

while True:
    ret, frame = vid.read()
    
    barcodes = pyzbar.decode(frame)
    #cv2.imshow("frame", frame)
    
    for barcode in barcodes:
        # draw bounding box around the detected object
         (x, y, w, h) = barcode.rect
         cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 0, 255), 2)

        # the barcode data is a bytes object so if we want to draw it on
         # our output image we need to convert it to a string first
         barcodeData = barcode.data.decode("utf-8")
         barcodeType = barcode.type

        # draw the barcode description and type on the image
         text = "{} ({})".format(barcodeData, barcodeType)
         cv2.putText(frame, text, (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX,0.5, (0, 0, 255), 2)
         
         cv2.imshow("Frame", frame)
         cv2.waitKey(0)
         cv2.destroyAllWindows()
        
    timestamp = datetime.datetime.now()
    ts = timestamp.strftime("%A %d %B %Y %I:%M:%S%p")
    cv2.putText(frame, ts, (10, frame.shape[0] - 10),
    cv2.FONT_HERSHEY_SIMPLEX, 0.35, (0, 0, 255), 1)
    
    cv2.imshow("Frame", frame)
    key = cv2.waitKey(1) & 0xFF
    
    if key == ord("q"):
        break
    
cv2.destroyAllWindows()
