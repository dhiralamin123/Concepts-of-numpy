# -*- coding: utf-8 -*-
"""
Created on Mon Apr 26 09:07:29 2021

@author: Monak
"""

import numpy as np

arr=np.array([1,2,3,4,5])
print(arr[2])

arr=np.array([1,23,4,5])
print(arr[1])


arr=np.array([1,23,4,5])
print(arr[1] + arr[3])
print(arr[1] - arr[3])
print(arr[1] / arr[3])

arr=np.array([[1,2,3,4,5], [6,7,8,9,10]])
print(arr)
print(arr[0,1])
print(arr[1,4])


arr=np.array([[[1,2,3],[12,3,4]], [[4,5,6],[7,8,9]]])
print(arr[0,1,2])
print(arr[1,1,2])

#negative indexing

arr=np.array([[1,2,3,4,5], [6,7,8,9,10]])
print(arr[1,-5])