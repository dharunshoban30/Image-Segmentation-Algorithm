# 💧 Watershed Algorithm in Segmentation of Skin Lesions in Dermoscopic Images
 
## Overview
This project focuses on the segmentation of skin lesions in dermoscopic images using the Watershed Algorithm. The project aims to develop an algorithm that accurately identifies and separates lesions from healthy skin regions. The code and visualizations are structured into multiple Python scripts and Jupyter notebooks, demonstrating each step of the image segmentation process.

## Project Details 
1. **Project Objective:**
   The primary goal of this project is to design an image segmentation algorithm that accurately segments skin lesions in dermoscopic images. The segmented results are compared against the ground truth images using metrics such as **Precision, Recall, Adapted Rand Error, and Intersection over Union (IoU)**.

2. **Project Motivation:**
   Skin cancer is one of the most common forms of cancer worldwide, and early detection significantly improves treatment outcomes. Automated segmentation of skin lesions can assist medical professionals in early diagnosis and potentially save lives. This project aims to contribute to this goal by providing a reliable segmentation algorithm that can be used in medical diagnostics or integrated into telemedicine platforms.

3. **Possible Applications:**
   - Medical Diagnostics: Assists dermatologists in identifying and diagnosing skin lesions.
   - Telemedicine: Enables patients to upload images for preliminary analysis.
   - Research: Provides a tool for analyzing large datasets of skin lesion images for research purposes.
   - Mobile Apps: Can be integrated into smartphone applications for self-assessment.

## Methodology
The image segmentation approach uses a multi-step process involving several preprocessing, processing, and post-processing techniques. Below is a summary of the key steps:
  - **Image Conversion:** Convert the input image to grayscale using OpenCV (cv2.cvtColor()), which simplifies the processing by reducing the image to a single channel.
  - **Adaptive Thresholding:** Apply a combination of Otsu's thresholding and inverse binary thresholding to create a binary image where lesions are highlighted.
  - **Morphological Operations:** Use opening and closing operations to remove noise and refine the segmented areas.
  - **Area Segmentation:** Calculate sure foreground and background regions using distance transform and dynamic thresholding.
  - **Connected Component Labelling:** Assign unique labels to individual lesions using connected component analysis.
  - **Watershed Algorithm:** Apply the Watershed segmentation algorithm to distinguish between different regions in the image.
  - **Gaussian Blur:** Apply a Gaussian Blur to smooth the segmented regions for better visual appearance.

The main Python script for the image segmentation algorithm is contained in `imageSegment.py`, and the visualizations for each step are presented in the Jupyter notebook `visualSegment.ipynb`.

## Setup Instructions
To execute the code, follow these steps:
1. **Setup Environment**:
    - Ensure you have Python and your preferred IDE installed.
    - Install necessary libraries using the following commands:
      ```bash
      pip install numpy pandas matplotlib scikit-learn
      ```

2. **Download Dataset**:
    - Ensure the `dataset` folder is available in the same directory as the codes.

3. **Running the Codes**:
    - Open the IDE and navigate to the `visualSegment.py` file.
    - Run the file in the terminal to see the results.
    - To look at the visualizations, run all the cells in `imageSegment.py` notebook in the IDE or in Jupyter Notebook. 
