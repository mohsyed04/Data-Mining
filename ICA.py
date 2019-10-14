# -*- coding: utf-8 -*-
"""
Created on Wed Oct  2 14:19:30 2019

@author: Syed Mohiuddin
"""
import numpy as np
from sklearn.decomposition import FastICA
from matplotlib import pyplot as plt
from numpy import genfromtxt

X = genfromtxt('out1.csv', delimiter=',') 
Y = genfromtxt('out2.csv', delimiter=',')


transformer_X = FastICA(n_components= 60, whiten = True, random_state=0)
X_transformed = transformer_X.fit_transform(X)

transformer_Y = FastICA(n_components= 60, whiten = True, random_state=0)
Y_transformed = transformer_Y.fit_transform(Y)

#plt.plot(np.absolute(Y_transformed))
#plt.show()

