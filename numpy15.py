# -*- coding: utf-8 -*-
"""
Created on Mon Apr 26 10:21:02 2021

@author: Monak
"""

import numpy as np

arr=np.array([1,2,3,4])
print(arr.dtype)

arr=np.array(['apple','mango','watermallon'])
print(arr.dtype)

arr = np.array([1, 2, 3, 4], dtype='f')
print(arr)
print(arr.dtype)

arr = np.array([1, 2, 3, 4], dtype='i4')
print(arr)
print(arr.dtype)

arr = np.array([1, 2, 3, 4], dtype='i8')
print(arr)
print(arr.dtype)


arr=np.array([1.5,2.2,3.4], dtype='i')
print(arr)
print(arr.dtype)

#change float to integer using i use astype

arr=np.array([1.2,2.7,3.9,4.3])
print(arr.dtype)
ngarr=arr.astype('i')
print(ngarr.dtype)
print(ngarr)


#boolean
arr=np.array([1.2,2.7,3.9,4.3])
print(arr.dtype)
ngarr=arr.astype('bool')
print(ngarr.dtype)
print(ngarr)

arr=np.array([1.2,2.7,3.9,4.3], dtype='b')
print(arr)
print(arr.dtype)


