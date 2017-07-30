# -*- coding: utf-8 -*-
"""
Created on Wed Mar 15 17:19:10 2017

@author: wilkenshuang
"""

import cv2
import numpy as np
import time
import matplotlib.pyplot as plt

def printMat(image,thresh):
    height,weight=gray.shape[0],gray.shape[1]
    for i in range(height):
        for j in range(weight):
            if float(image[i,j]>thresh):
                image[i,j]=1
            else:
                image[i,j]=0
    return image
                
def rebuild_img2(u,sigma,v,p):
    m=len(u)
    n=len(v)
    a=np.zeros((m,n))
    count=int(sum(sigma))
    cursum=0
    k=0
    while cursum<=count*p:
        uk=u[:,k].reshape(m,1)
        vk=v[k].reshape(1,n)
        a+=sigma[k]*np.dot(uk,vk)
        cursum+=sigma[k]
        k+=1
    
    a[a<0]=0
    a[a > 255] = 255
    #按照最近距离取整数，并设置参数类型为uint8
    return np.rint(a).astype("uint8")

def rebuild_img(u,sigma,v,p):
    m=len(u)
    n=len(v)
    a=np.zeros((m,n))
    count=int(sum(sigma))
    k=int(p*len(sigma))
    value=sigma[:k]
    uk=u[:,:k]
    vk=v[:k,:]
    sigMat=np.diag(value)    
    a=np.dot(np.dot(uk,sigMat),vk)
    a=np.floor(a)
    a[a<0]=0
    a[a > 255] = 255
    
    return np.rint(a).astype("uint8")#按照最近距离取整数，并设置参数类型为uint8

img = cv2.imread('D:\practice\Anacode_working\\building.jpg')
a = np.array(img)
p=0.1 #奇异值保留参数
u, sigma, v = np.linalg.svd(a[:, :, 0])
R = rebuild_img(u, sigma, v, p)

u, sigma, v = np.linalg.svd(a[:, :, 1])
G = rebuild_img(u, sigma, v, p)

u, sigma, v = np.linalg.svd(a[:, :, 2])
B = rebuild_img(u, sigma, v, p)

I = np.stack((R, G, B), 2)
cv2.imshow('pic',I)#显示图片
        




