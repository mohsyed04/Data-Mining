# -*- coding: utf-8 -*-
"""
Created on Sat Oct 12 10:55:27 2019

@author: Syed Mohiuddin
"""

import pandas as pd
from matplotlib import pyplot as plt

data = pd.read_csv('out1.csv', header=None)
data2 = pd.read_csv('out2.csv', header=None)


x = data.describe()
y = data2.describe() 

plt.plot(x)
plt.show()

plt.plot(y)
plt.show()

sample1 = data.sample(n = 10)
sample2 = data2.sample(n = 10)

i = sample1.apply(pd.DataFrame.describe, axis=1)
j = sample2.apply(pd.DataFrame.describe, axis=1)

"""
i.transpose().plot.line()
j.transpose().plot.line()

plt.plot(x)
plt.show()

plt.plot(y)
plt.show()
"""
