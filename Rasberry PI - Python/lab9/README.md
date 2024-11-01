# Python Script Collection: Object Detection and Tracking

This repository contains Python scripts focused on object detection, tracking, and modifications to object tracking styles. These scripts demonstrate the basics of computer vision, including color-based object detection and movement tracking.

## Table of Contents

- [Getting Started](#getting-started)
- [File Descriptions](#file-descriptions)
- [Requirements](#requirements)
- [Usage](#usage)

## Getting Started

Each script is designed to work with a camera input and utilizes color detection to identify and track specific objects. Ensure Python 3.x and necessary libraries are installed on your system.

## File Descriptions

1. **3_A_Red_object_detection.py**: Detects red objects in the camera feed. This script highlights objects based on color detection, allowing for basic tracking of red items within the frame.

2. **3_B_Removing_object_track.py**: Tracks and removes objects from the frame based on certain criteria. This script demonstrates how to identify and eliminate specific objects in real time.

3. **3_C_Modified_track_style.py**: A variation on object tracking with modified styling, possibly adding effects or visual cues to enhance the tracking experience.

4. **green.py**: Similar to `3_A_Red_object_detection.py`, but detects green objects within the camera feed, showcasing how color filters can be adjusted to track objects of different colors.

## Requirements

- Python 3.x
- OpenCV (for object detection and camera access)

To install required libraries:

```python
pip install opencv-python
```