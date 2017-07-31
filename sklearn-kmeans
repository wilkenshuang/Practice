# -*- coding: utf-8 -*-
"""
Created on 2017-07-31 10:22:22

@author: wilkenshuang
"""

from sklearn.datasets import load_breast_cancer
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt

data=load_breast_cancer()
Data=data.data
kmeans=KMeans(4,n_init=5,max_iter=10,random_state=0).fit(Data)

label=kmeans.labels_
centroids=kmeans.cluster_centers_
color=['r','g','b','y']
colors=[color[i] for i in label]
plt.scatter(Data[:,0],Data[:,1],c=colors)
plt.scatter(centroids[:,0],centroids[:,1],s=100,c='c')
