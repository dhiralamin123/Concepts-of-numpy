# -*- coding: utf-8 -*-
"""
Created on Tue Apr 27 09:27:31 2021

@author: Monak
"""

import numpy as np

arr=np.array([1,2,3,4])
x=arr.copy()
arr[0]=34
print(arr)
print(x)

arr=np.array([1,2,3,4])
x=arr.view()
arr[0]=34
print(arr)
print(x)


arr=np.array([1,2,3,4])
x=arr.copy()
y=arr.view()
print(arr)
print(x.base)
print(y.base)