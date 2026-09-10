# stop_sign_detection

This project is an autonomous stop sign detection algorithm developed using Python and OpenCV. It detects red stop signs in a given image dataset, calculates their center coordinates, draws a bounding box, and saves the output images.

## Features
- **Color Segmentation:** Uses the HSV color space to accurately isolate red pixels under various lighting conditions.
- **Contour Detection:** Finds the largest valid contour to eliminate background noise.
- **Center Calculation:** Computes and prints the exact (X, Y) pixel coordinates of the stop sign's center.
- **Automated Processing:** Iterates through all images in the dataset and processes them sequentially.

## Requirements
To run this script, you need Python installed on your system along with the following libraries:
- OpenCV (`opencv-python`)
- NumPy (`numpy`)

You can install the required libraries using pip:
```bash
pip3 install opencv-python numpy
