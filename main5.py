
import cv2  
img = cv2.imread("dog.jpg")  
# get dimensions of image  
dimensions = img.shape  
p = img.size

i,j,k = img.shape


for i in range(i):
    for j in range(j):
        img[i,j]=0,255,255


cv2.imshow("house", img) # Display the image
cv2.waitKey(0) # Wait for a key press
cv2.destroyAllWindows() 
       