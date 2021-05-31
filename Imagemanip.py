# -*- coding: utf-8 -*-
"""
Created on Tue Sep  1 14:35:40 2020

@author: satya
"""

from PIL import Image
import matplotlib.image as mpimg 
import matplotlib.pyplot as plt 
import cv2
img=Image.open("C:\\Users\satya\Desktop\deadcells.jpg")
#img.show()
print("Image size is "+str(img.size))
savepath="C:\\Users\satya\Desktop\Python Stuff\test.jpg"
img=cv2.imread("C:\\Users\satya\Desktop\deadcells.jpg")
cv2.imshow("Image",img)
cv2.waitKey(0)
cv2.destroyAllWindows()

img = mpimg.imread('C:\\Users\satya\Desktop\deadcells.jpg') 
plt.imshow(img) 