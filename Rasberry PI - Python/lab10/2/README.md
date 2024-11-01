# Python Script Collection: Object Detection

This repository contains Python scripts for performing object detection, allowing the identification and localization of objects within images or a live camera feed. These scripts demonstrate essential computer vision techniques for object detection.

## Table of Contents

- [Getting Started](#getting-started)
- [File Descriptions](#file-descriptions)
- [Requirements](#requirements)
- [Usage](#usage)

## Getting Started

Each script is capable of detecting and labeling objects within either static images or real-time camera feeds. Ensure that you have Python 3.x and any necessary libraries installed.

## File Descriptions

1. **2_A_Object_detection_camera.py**: This script performs object detection using a live camera feed. It highlights and labels detected objects in real time, showcasing object detection with video input.

2. **2_Object_detection_image.py**: Detects objects within a static image, identifying and labeling objects within a single frame. This script is suitable for batch processing or analyzing specific images.

## Requirements

- Python 3.x
- TensorFlow or PyTorch (depending on the model used for object detection)
- OpenCV (for image processing and camera access)
- Additional libraries like `numpy` for handling arrays

To install the required libraries, use:

```bash
pip install tensorflow opencv-python numpy
```

## Usage

```python
python script_name.py

#example:

python 2_A_Object_detection_camera.py
```