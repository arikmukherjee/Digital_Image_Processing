
import cv2  
img = cv2.imread("dog.jpg")  
# get dimensions of image  
dimensions = img.shape  
print(dimensions)
p = img.size
print("total number of pixel = ",p)
i,j,k = img.shape
print("height of image = ",i)

print("width of image = ",j)
print("channel of image = ",k)
