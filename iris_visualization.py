# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

'''
利用PCA对IRIS数据库进行数据降维处理。
PCA只是将整组数据整体映射到最方便表示这组数据的坐标轴上，映射时没有利用任何数据内部的分类信息，
因此整组数据在表示上更加方便(降低了维数并将信息损失降到最低)，但在分类上也许会变得更加困难。
'''

import numpy as np
from matplotlib import pyplot as plt
from sklearn.datasets import load_iris
from mpl_toolkits.mplot3d import Axes3D
from sklearn.decomposition import PCA

data=load_iris()

fig=plt.figure(1)
ax=Axes3D(fig)
X_reduce=PCA(n_components=3).fit_transform(data.data)
X_reduce2=PCA(n_components=2).fit_transform(data.data)
ax.scatter(X_reduce[:,0],X_reduce[:,1],X_reduce[:,2],c=Y,cmap=plt.cm.Paired)
ax.set_title("First three PCA directions")
ax.set_xlabel("1st eigenvector")
ax.w_xaxis.set_ticklabels([])
ax.set_ylabel("2nd eigenvector")
ax.w_yaxis.set_ticklabels([])
ax.set_zlabel("3rd eigenvector")
ax.w_zaxis.set_ticklabels([])

plt.figure(2)
#plt.clf()
plt.scatter(X_reduce2[:,0],X_reduce2[:,1],c=Y,cmap=plt.cm.Paired)

plt.show()
