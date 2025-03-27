import cv2

img =  cv2.imread(r"C:\Users\pc\Downloads\images.jpeg", cv2.IMREAD_GRAYSCALE)
cv2.imshow("house", img) # Display the image
cv2.waitKey(0) # Wait for a key press
cv2.destroyAllWindows() 