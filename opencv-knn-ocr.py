# -*- coding: utf-8 -*-
"""

@author: wilkenshuang
"""

import cv2
import numpy as np
import time

def ExtractData(filename):
    image=cv2.imread(filename)
    gray=cv2.cvtColor(image,cv2.COLOR_RGB2GRAY)    
    cells=[np.hsplit(row,100) for row in np.vsplit(gray,50)]
    ImgMatrix=np.zeros((5000,400))
    for i in range(50):
        for j in range(100):
            img=cells[i][j].flatten()
            ImgMatrix[i*50+j,:]=img
            ImgMatrix=ImgMatrix.astype('float32')
    ImgLabel=np.repeat(np.arange(10),500).astype('float32')
    ImgLabel=ImgLabel.reshape((len(ImgLabel),1))
    return ImgMatrix,ImgLabel

def updataKNN(knn,train,trainLabel,newData=None,newDataLabel=None):
    if newData!=None and newDataLabel!=None:
        print(train.shape,newData.shape)
        newData=newData.reshape(-1,400).astype('float32')
        train=np.vstack((train,newData))
        trainLabel=np.hstack((trainLabel,newDataLabel))
    knn.train(train,cv2.ml.ROW_SAMPLE,trainLabel)
    return knn,train,trainLabel

def findRoi(frame,threshValue):
    rois=[]
    gray=cv2.cvtColor(frame,cv2.COLOR_RGB2GRAY)
    #gray=frame
    gray2=cv2.dilate(gray,None,iterations=2)
    gray2=cv2.erode(gray2,None,iterations=2)
    edges=cv2.absdiff(gray,gray2)
    x=cv2.Sobel(edges,cv2.CV_16S,1,0)
    y=cv2.Sobel(edges,cv2.CV_16S,0,1)
    absx=cv2.convertScaleAbs(x)
    absy=cv2.convertScaleAbs(y)
    dst=cv2.addWeighted(absx,0.5,absy,0.5,0)
    ret,ddst=cv2.threshold(dst,threshValue,255,cv2.THRESH_BINARY)
    im,contours,hierarchy=cv2.findContours(ddst,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
    for i in contours:
        x,y,w,h=cv2.boundingRect(i)
        if w>10 and h>20:
            rois.append((x,y,w,h))
    return rois,edges

def findDigit(knn,roi,threshValue):
    ret,th=cv2.threshold(roi,threshValue,255,cv2.THRESH_BINARY)
    th=np.resize(th,(20,20))
    output=np.reshape(th,(-1,400)).astype('float32')
    ret,results,neighours,dist=knn.findNearest(output,3)
    return int(results[0][0]),th

def concatenate(images):
    n=len(images)
    output=np.zeros(20*20*n).reshape((-1,20))
    for i in range(n):
        output[20*i:20*(i+1),:]=images[i]
    return output

start=time.clock()
knn=cv2.ml.KNearest_create()
filename='C:\Anaconda_working\digits.png'
TrainData,Labels=ExtractData(filename)


knn.train(TrainData,cv2.ml.ROW_SAMPLE,Labels)

cap = cv2.VideoCapture(0)
width = cap.get(cv2.CAP_PROP_FRAME_WIDTH)
height = cap.get(cv2.CAP_PROP_FRAME_HEIGHT)
videoFrame = cv2.VideoWriter('frame.avi',cv2.VideoWriter_fourcc('M','J','P','G'),25,(int(width),int(height)),True)

count=0
while True:
    ret,frame=cap.read()
    threshValue=50
    rois, edges = findRoi(frame, threshValue)
    digits=[]
    for i in rois:
        x,y,w,h=i
        digit,th=findDigit(knn,edges[x:x+w,y:y+h],threshValue)
        digits.append(np.resize(th,(20,20)))
        cv2.rectangle(frame,(x,y),(x+w,y+h),(153,153,0),1)
        cv2.putText(frame, str(digit), (x,y), cv2.FONT_HERSHEY_SIMPLEX, 1, (127,0,255), 2)
    newEdges=cv2.cvtColor(edges,cv2.COLOR_GRAY2BGR)
    newFrame = np.hstack((frame,newEdges))
    cv2.imshow('frame',newFrame)
    k=cv2.waitKey(0)
    if k == 27:
        break
    elif k==ord('c'):
        Nd=len(digits)
        output=concatenate(digits)
        showDigits = cv2.resize(output,(60,60*Nd))
        cv2.imshow('digits', showDigits)
        cv2.imwrite(str(count)+'.png', showDigits)
        count += 1
        if cv2.waitKey(0) & 0xff == ord('e'):
            pass
        print('input the digits(separate by space):')
        numbers = input().split(' ')
        Nn = len(numbers)
        if Nd != Nn:
            print('update KNN fail!')
            continue
        try:
            for i in range(Nn):
                numbers[i] = int(numbers[i])
        except:
            continue
        knn, TrainData, Labels = updataKNN(knn, TrainData, Labels, output, numbers)
        print('update KNN, Done!')

print('Numbers of trained images:',len(TrainData))
print('Numbers of trained image labels', len(Labels))
cap.release()
cv2.destroyAllWindows()



#width = cap.get(cv2.CAP_PROP_FRAME_WIDTH)
#height = cap.get(cv2.CAP_PROP_FRAME_HEIGHT)
#videoFrame = cv2.VideoWriter('frame.avi',cv2.VideoWriter_fourcc('M','J','P','G'),25,(int(width),int(height)),True)
#ret,frame=cap.read()



end=time.clock()
print('Process time: %s s' %(end-start))
