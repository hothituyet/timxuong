# -*- coding: utf-8 -*-
"""
Created on Thu Jan  6 14:07:50 2022

@author: Vostro 3468
"""
import cv2
import numpy as np  


kernel = np.array([[0, 1, 0],
                   [1, 1, 1],
                   [0, 1, 0]], np.uint8)
img = cv2.imread('D:/Downloads/u.png', 0)
ret,img = cv2.threshold(img,127, 255, 0)

size = np.size(img)
skel = np.zeros(img.shape, np.uint8)

img1= img.copy()



while (cv2.countNonZero(img1)!=0):

    opening = cv2.morphologyEx(img1,cv2.MORPH_OPEN,kernel)
    subset = cv2.subtract(img1,opening)
    skel = cv2.bitwise_or(subset,skel)

    eroded = cv2.erode (img1,kernel)
    img1 = eroded.copy()
    
 
cv2.imshow('ban dau',img)
cv2.imshow('xuong',skel)
cv2.waitKey(0)
cv2.destroyAllWindows()