# -*- coding: utf-8 -*-
"""
imageSegment.py

YOUR WORKING FUNCTION

"""

import cv2
import numpy as np

input_dir = 'dataset/test'
output_dir = 'dataset/output'

def segmentImage(img):
    # Convert images to grayscale
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Apply adaptive thresholding
    _, thresh = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)

    # Morphological opening and closing operation
    kernel_open = np.ones((3, 3), np.uint8)
    opening = cv2.morphologyEx(thresh, cv2.MORPH_OPEN, kernel_open, iterations=2)
    kernel_close = np.ones((5, 5), np.uint8)
    closing = cv2.morphologyEx(opening, cv2.MORPH_CLOSE, kernel_close, iterations=4)

    # Background area determination
    sure_bg = cv2.dilate(closing, kernel_close, iterations=3)

    # Distance transform to find sure foreground area 
    dist_transform = cv2.distanceTransform(closing, cv2.DIST_L2, 5)
    # Dynamic threshold based on a fraction of the mean and a smaller fraction of the standard deviation of the distance transform
    threshold_value = dist_transform.mean() + 0.3 * dist_transform.std()
    _, sure_fg = cv2.threshold(dist_transform, threshold_value, 255, 0)

    # Finding unknown region
    sure_fg = np.uint8(sure_fg)
    unknown = cv2.subtract(sure_bg, sure_fg)

    # Marker labelling
    _, markers = cv2.connectedComponents(sure_fg)
    # Add one to all labels 
    markers = markers + 1
    # Mark the region of unknown with zero
    markers[unknown == 255] = 0

    # Apply watershed algorithm
    markers = cv2.watershed(img, markers)
    img[markers == -1] = [255, 0, 0]

    # Generate final binary mask
    outImg = np.where(markers > 1, 1, 0).astype('uint8')

    # Apply Gaussian blur to smooth the segmented regions
    outImg = cv2.GaussianBlur(outImg, (7, 7), 0)

    return outImg