import cv2

img =  cv2.imread("dog.jpg", cv2.IMREAD_ANYCOLOR)
cv2.imshow("house", img) # Display the image
cv2.waitKey(0) # Wait for a key press
cv2.destroyAllWindows() 