# -*- coding: utf-8 -*-
"""
Created on Sun Sep  8 19:05:37 2019

@author: Syed Mohiuddin
"""
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA

df = pd.read_csv("out2.csv", header = None)
X = df.iloc[:,0:70].values
y = df.iloc[:, 70:].values


train_img, test_img, train_lbl, test_lbl = train_test_split( X, y, test_size=1/7.0, random_state=0)

scaler = StandardScaler()
scaler.fit(train_img)

train_img = scaler.transform(train_img)
test_img = scaler.transform(test_img)

pca = PCA(.95)
pca.fit(train_img)

train_img = pca.transform(train_img)
test_img = pca.transform(test_img)

print(pca.n_components_)
