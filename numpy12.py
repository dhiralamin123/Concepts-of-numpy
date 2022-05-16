# -*- coding: utf-8 -*-
"""
Created on Sun Apr 18 11:30:55 2021

@author: Monak
"""

import numpy as np



arr= np.array([1,2.2,3.3,4,5])
print(arr)
print(type(arr))

arr=np.array((1,2,3,4,5))
print(arr)

a=np.array(42)
print(a)
b=np.array([1,2,3,4,5])
c=np.array([[1,2,3],[5,6,7]])
d=np.array([[[1,2,3],[1,2,3],[[4,5,6],[6,7,8]]]])

print(a.ndim)
print(b.ndim)
print(c.ndim)
print(d.ndim)

arr=np.array([1,2,3,4], ndmin=5)
print(arr)
print('number of dimesion',arr.ndim)

import numpy as np
arr = np.array([[1, 2, 3, 4], [5, 6, 7, 8]])
print(arr.shape)