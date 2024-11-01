import numpy as np
from imutils.video import VideoStream
import imutils
import cv2

prototxt_path = "MobileNetSSD_deploy_prototxt.txt"
model_path = "MobileNetSSD_deploy.caffemodel"
image_path = "autok.png"

conf_limit = 0.25

vid = cv2.VideoCapture(0)

CLASSES = [
    "background",
    "aeroplane",
    "bicycle",
    "bird",
    "boat",
    "bottle",
    "bus",
    "car",
    "cat",
    "chair",
    "cow",
    "diningtable",
    "dog",
    "horse",
    "motorbike",
    "person",
    "pottedplant",
    "sheep",
    "sofa",
    "train",
    "tv/monitor",
]

COLORS = np.random.uniform(0, 255, size=(len(CLASSES), 3))
print("Loading model...")
net = cv2.dnn.readNetFromCaffe(prototxt_path, model_path)

while True:
    ret, image = vid.read()
    image = imutils.resize(image, width=600)

    (h, w) = image.shape[:2]
    blob = cv2.dnn.blobFromImage(
        cv2.resize(image, (300, 300)), 0.007843, (300, 300), 127.5
    )

    print("Sending image through the network...")
    net.setInput(blob)
    detections = net.forward()

    for i in np.arange(0, detections.shape[2]):
        # extract the confidence
        confidence = detections[0, 0, i, 2]

        if confidence > conf_limit:
            idx = int(detections[0, 0, i, 1])
            box = detections[0, 0, i, 3:7] * np.array([w, h, w, h])
            (startX, startY, endX, endY) = box.astype("int")
            label = "{}: {:.2f}%".format(CLASSES[idx], confidence * 100)
            print("{}".format(label))

            cv2.rectangle(image, (startX, startY), (endX, endY), COLORS[idx], 2)
            y = startY - 15 if startY - 15 > 15 else startY + 15
            cv2.putText(
                image, label, (startX, y), cv2.FONT_HERSHEY_SIMPLEX, 0.5, COLORS[idx], 2
            )

    cv2.imshow("Image", image)
    key = cv2.waitKey(1) & 0xFF

    if key == ord("q"):
        break

cv2.waitKey(0)
cv2.destroyAllWindows()
