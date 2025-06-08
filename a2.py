import cv2
import numpy as np

# Create separate R, G, B channels (uint8 values between 0 and 255)
height, width = 300, 300  # example size

# Example: Create color gradients or patterns for demo
R = np.full((height, width), 255, dtype=np.uint8)   # Red plane (fully red)
G = np.zeros((height, width), dtype=np.uint8)       # Green plane (zero)
B = np.full((height, width), 100, dtype=np.uint8)   # Blue plane (some blue)

# Merge B, G, R into a single color image (OpenCV uses BGR order)
color_image = cv2.merge([B, G, R])

# Display the color image
cv2.imshow("Color Image from R, G, B Planes", color_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
