import cv2
import numpy as np
import matplotlib.pyplot as plt

# Load image in grayscale
image = cv2.imread('dog.jpg', cv2.IMREAD_GRAYSCALE)

# Choose a row or column to extract profile (e.g., middle row)
row = image.shape[0] // 2  # Middle row
profile = image[row, :]    # Intensity values along that row

# Display the grayscale image with a line showing the profile row
image_with_line = cv2.cvtColor(image, cv2.COLOR_GRAY2BGR)
cv2.line(image_with_line, (0, row), (image.shape[1], row), (0, 0, 255), 1)
cv2.imshow("Image with Profile Line", image_with_line)

# Plot the intensity profile
plt.figure(figsize=(10, 4))
plt.title(f'Intensity Profile of Row {row}')
plt.plot(profile, color='black')
plt.xlabel('Column Index')
plt.ylabel('Intensity')
plt.grid(True)
plt.tight_layout()
plt.show()

cv2.waitKey(0)
cv2.destroyAllWindows()
