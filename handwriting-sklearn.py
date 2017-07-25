# -*- coding: utf-8 -*-
"""
Created on Wed Mar 15 17:19:10 2017

@author: wilkenshuang
"""

import numpy as np
import matplotlib.pyplot as plt

from sklearn.datasets import load_digits
from sklearn.neighbors import KernelDensity
from sklearn.decomposition import PCA
from sklearn.svm import SVC
from mpl_toolkits.mplot3d import Axes3D
from sklearn.model_selection import GridSearchCV

# load the data
digits = load_digits()
data = digits.data
label=digits.target
pca=PCA(n_components=15,whiten=False)

classifier=SVC(gamma=0.001)
SampNum=len(digits.images)
classifier.fit(data[:int(np.ceil(SampNum/2)),:],label[:int(np.ceil(SampNum/2))])
PreLab=classifier.predict(data[int(np.ceil(SampNum/2)):,:])
count=0
for i in range(len(PreLab)):
    if PreLab[i]==label[i+int(np.ceil(SampNum/2))]:
        count+=1
accuracy=count/len(PreLab)