# Python Script Collection: Text Detection and Recognition

This repository contains Python scripts for detecting and recognizing text within images using popular optical character recognition (OCR) techniques. These scripts apply deep learning models and OCR libraries to identify and extract text from images.

## Table of Contents

- [Getting Started](#getting-started)
- [File Descriptions](#file-descriptions)
- [Requirements](#requirements)
- [Usage](#usage)
- [License](#license)

## Getting Started

These scripts leverage pre-trained models and OCR libraries to perform text detection and recognition tasks. Ensure that you have Python 3.x and all required libraries installed.

## File Descriptions

1. **EAST.py**: Implements the EAST (Efficient and Accurate Scene Text Detector) model to detect text areas within an image. This script locates regions containing text and draws bounding boxes around them.

2. **tesseract.py**: Uses Tesseract OCR, an open-source text recognition library, to recognize and extract text from images. This script is ideal for converting image-based text to digital format.

3. **Text detection and recognition.py**: Combines text detection and recognition into one script, likely using the EAST model for detection and Tesseract for recognition, to locate and extract text from images.

## Requirements

- Python 3.x
- OpenCV (for image processing)
- Tesseract-OCR (for text recognition)
- TensorFlow or a compatible deep learning framework (for EAST model)

To install required libraries:

```bash
pip install opencv-python pytesseract tensorflow
```

## Usage
```python
python script_name.py

#example:

python EAST.py
```