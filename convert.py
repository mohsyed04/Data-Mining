# -*- coding: utf-8 -*-
"""
Created on Sun Sep  8 14:09:56 2019

@author: Syed Mohiuddin
"""

import csv 

with open("dataset1.txt", 'r') as file:
    line_array = file.read().splitlines()
    cell_array = [line.split() for line in line_array]
    list1 = list(filter(None, cell_array))  #remove empty lists
    #print(list2)
    
#convert list to csv
with open("out1.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerows(list1)

with open("dataset2.txt", 'r') as file:
    line_array = file.read().splitlines()
    cell_array = [line.split() for line in line_array]
    list2 = list(filter(None, cell_array))  #remove empty lists
    #print(list2)
    
#convert list to csv
with open("out2.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerows(list2)

