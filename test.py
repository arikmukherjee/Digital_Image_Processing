import cv2
import sys

# Read the image
img = cv2.imread(cv2.samples.findFile("starry_night.jpg"))

# Check if image was successfully loaded
if img is None:
    sys.exit("Could not read the image.")

# Display the image
cv2.imshow("Display window", img)

# Wait for a key press
k = cv2.waitKey(0)

# If 's' is pressed, save the image
if k == ord("s"):
    cv2.imwrite("starry_night.png", img)