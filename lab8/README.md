# Python Script Collection: Camera Access and Barcode Recognition

This repository contains Python scripts focused on accessing camera feeds, capturing images, recording videos, and recognizing barcodes. These scripts demonstrate the use of camera modules and basic image processing for real-time applications.

## Table of Contents

- [Getting Started](#getting-started)
- [File Descriptions](#file-descriptions)
- [Requirements](#requirements)
- [Usage](#usage)

## Getting Started

Each script is designed to work with a compatible camera device (e.g., USB camera, Raspberry Pi Camera). Ensure you have Python 3.x and any additional libraries required by individual scripts installed on your system.

## File Descriptions

1. **7_accessin_camera.py**: A script to access the camera and display its feed, demonstrating basic camera functionality and frame capture.

2. **7_Cam_image.py**: Captures a single image from the camera and saves it, useful for taking snapshots or monitoring scenes at specific intervals.

3. **8_Pi_Cam_Video.py**: Designed for the Raspberry Pi Camera, this script records video from the Pi camera module, ideal for video surveillance or recording projects.

4. **9_A_Barcode_Recognition_in_video.py**: Recognizes barcodes in a live video feed, allowing real-time barcode scanning applications using camera input.

5. **9_Barcode_recognition.py**: Focuses on barcode recognition within static images, extracting and processing barcode data for inventory or tracking systems.

6. **Barcode_recog_in_video.py**: Similar to `9_A_Barcode_Recognition_in_video.py`, this script also detects barcodes in a live video feed, possibly including additional processing steps.

7. **Cam_image.py**: Another image capture script that saves images from a camera feed, useful for regular snapshots or monitoring applications.

8. **Pi_cam_video.py**: A duplicate or variant of `8_Pi_Cam_Video.py`, designed to work specifically with the Raspberry Pi Camera for video recording.

## Requirements

- Python 3.x
- OpenCV (required for camera access and image processing)
- pyzbar (for barcode recognition in images and video)

To install required libraries:

```bash
pip install opencv-python pyzbar