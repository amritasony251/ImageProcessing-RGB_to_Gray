from PIL import Image
import numpy as np
import cv2

img = cv2.imread("ee.jpg")
img_out = img.copy()

width, height, bit = np.shape(img)

for j in range(0,height) :
 for i in range(0,width) :
    temp = img_out[i][j][0]*0.3 +  img_out[i][j][1]*0.59 + img_out[i][j][2]*0.11
    img_out[i][j][0] = temp
    img_out[i][j][1] = temp
    img_out[i][j][2] = temp

cv2.imshow('image',img_out)
cv2.waitKey(0)
           
#print("width : " + str(width) + " height : " + str(height) + " bits : " + str(bit))



