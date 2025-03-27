
import cv2  
img = cv2.imread("images.jpeg")  
# get dimensions of image  
dimensions = img.shape  
print(dimensions)
p = img.size
print("total number of pixel = ",p)
i,j,k = img.shape
print("height of image = ",i)

print("width of image = ",j)
print("channel of image = ",k)

for i in range(i):
    for j in range(j):
        rgb=img[i,j]
        print(rgb , end=" ")
