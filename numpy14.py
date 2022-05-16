# -*- coding: utf-8 -*-
"""
Created on Mon Apr 26 09:30:36 2021

@author: Monak
"""
import numpy as np

arr=np.array([1,2,3,4,5,6,7,8,9])
print(arr[1:4])
print(arr[4:])
print(arr[:4])
print(arr[-5:-2])

print(arr[1:9:3])
#(arr[1:9:3])fiirst is start,second is end, third is space

arr=np.array([[1,2,3,4],[6,7,8,9]])
print(arr[1,1:4])
print(arr[0,-5::2])
print(arr[0:2,2:4])
print(arr[0:2,2:4])

arr=np.array([1,2,3,4,5,6,7,8,9])
print(arr[::2])