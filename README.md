Classical Computer Vision & Lane Line Extractor

Project Overview

This project implements a basic lane-line extraction pipeline using Python and OpenCV. It processes a road image to identify lane markings using colour filtering, Gaussian blur, Canny edge detection, and a Region of Interest (ROI) mask.

Technologies Used

* Python 3
* OpenCV
* NumPy

Computer Vision Pipeline

1. Image Loading: Loads the input road image.
2. HSV Colour Filtering: Identifies pixels corresponding to white and yellow lane markings.
3. Gaussian Blur: Smooths the mask to reduce noise.
4. Canny Edge Detection: Detects edges in the image.
5. Region of Interest (ROI): Keeps edges within the road region.
6. Lane Visualisation: Highlights detected edges in green and compares the result with the original image.

Project Structure

Lane-Line-Extractor/
├── images/
│   └── road.jpg
├── output/
│   ├── 01_original.jpg
│   ├── 02_hsv_mask.jpg
│   ├── 03_blurred.jpg
│   ├── 04_canny.jpg
│   ├── 05_roi.jpg
│   ├── 06_lane_detection.jpg
│   └── 07_comparison.jpg
├── lane_detector.py
└── README.md

How to Run

1. Install the required libraries:

python3 -m pip install opencv-python numpy

2. Place the input road image at images/road.jpg.
3. Run the program:

python3 lane_detector.py

4. The processed images will be saved in the output/ folder.

Output Screenshots

The program generates intermediate images for each stage of the pipeline. The final comparison image shows the original road image beside the lane-detection result.

Learning Outcome

This project demonstrates the basic steps of a classical computer vision pipeline and how image processing techniques can be combined to highlight lane markings in road images.


