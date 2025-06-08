import cv2
import numpy as np

# Create a blank black image
img = np.zeros((400, 400, 3), dtype=np.uint8)

# Draw 10 concentric circles using for loop
for r in range(20, 200, 20):
    cv2.circle(img, (200, 200), r, (0, 255 - r, r), 2)

cv2.imshow("Concentric Circles", img)
cv2.waitKey(0)
cv2.destroyAllWindows()
