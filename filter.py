import cv2
import numpy as np

# Load image
image = cv2.imread('sneara.jpeg')

# Define a blur filter/kernel
blur_filter = np.ones((3, 3), dtype=np.float32) / 9.0

# Apply convolution using OpenCV
filtered_image = cv2.filter2D(image, -1, blur_filter)

# Display the original and filtered images
cv2.imshow('Original Image', image)
cv2.imshow('Filtered Image', filtered_image)
cv2.waitKey(0)
cv2.destroyAllWindows()