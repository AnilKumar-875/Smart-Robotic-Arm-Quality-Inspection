# Smart Robotic Arm Quality Inspection

## Overview

This project simulates a robotic quality inspection system using Python and OpenCV.

The system:
- Reads multiple product images
- Converts images to grayscale
- Applies thresholding
- Detects contours
- Calculates contour area
- Classifies products as Good or Defective
- Generates a CSV inspection report automatically

## Technologies Used

- Python
- OpenCV
- CSV
- OS Module

## Project Structure

```
images/
project_1.py
report.csv
result_image_1.jpeg
result_image_2.jpeg
result_image_3.jpeg
inspection_result.png
```

## Sample Output

| Image | Area | Status |
|---------|---------|---------|
| image_1.jpeg | 27048 | Good |
| image_2.jpeg | 49794 | Good |
| image_3.jpeg | 50176 | Good |

## Author

Anil Kumar

EEE Student interested in Robotics and ROS 2.
