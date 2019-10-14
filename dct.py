# -*- coding: utf-8 -*-
"""
Created on Mon Sep  9 14:21:33 2019

@author: Syed Mohiuddin
"""
import numpy as np
from scipy.fftpack import dct
from matplotlib import pyplot as plt
from numpy import genfromtxt

x = genfromtxt('out1.csv', delimiter=',') 
y = genfromtxt('out2.csv', delimiter=',')

a = dct(x, type=2, axis = 1) #to run over column, set axis=0
b = dct(y, type=2, axis = 1) #to run over column, set axis=0

i = np.absolute(a)
j = np.sum(i, axis=0)

l = np.absolute(b)
m = np.sum(l, axis=1)

#plt.plot(a)
#plt.plot(b)
#plt.show()









