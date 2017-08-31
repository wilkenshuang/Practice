# -*- coding: utf-8 -*-
"""
Created on Sun Feb 19 12:50:34 2017

@author: wilkenshuang
"""

import cv2
import numpy as np
from matplotlib import pyplot as plt
from PIL import Image
def Cannythreshold(lowerthreshold):
    detected_edges=cv2.GaussianBlur(gray,(3,3),0)
    detected_edges=cv2.Canny(detected_edges,lowerthreshold,lowerthreshold*ratio,apertureSize=kernel_size)
    dst=cv2.bitwise_and(gray,gray,mask=detected_edges)
    cv2.imshow('canny window',dst)
lowerthreshold=0
max_lowerthreshold=100
ratio=4
kernel_size=3
img=cv2.imread("messi.jpg")
gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
cv2.namedWindow('canny window')
cv2.createTrackbar('Min threshold','canny window',lowerthreshold,max_lowerthreshold,Cannythreshold)
Cannythreshold(0)
laplacian=cv2.Laplacian(img,cv2.CV_8U)
sobelx=cv2.Sobel(img,-1,1,0,ksize=3)
plt.subplot(221),plt.imshow(img,cmap='gray'),plt.title('original')
plt.subplot(222),plt.imshow(laplacian,cmap='gray'),plt.title('laplacian')
plt.subplot(223),plt.imshow(sobelx,cmap='gray'),plt.title('sobelx')
if cv2.waitKey(0)==27:
    cv2.destroyAllWindows()
