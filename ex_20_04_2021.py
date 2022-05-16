import numpy as np

# Example 1: Get the data type of an array object

# data type of array and conversion

"""
arr = np.array([1, 2, 3, 4])
print(arr)
print(arr.dtype)

arr = np.array([1.5, 2.56, 3.12, 4.89])
print(arr)
print(arr.dtype)


arr = np.array(['a','b','c'])
print(arr)
print(arr.dtype)

arr = np.array([1, 2, 3, 4], dtype='f')
print(arr)
print(arr.dtype)

arr = np.array([1, 2, 3, 4], dtype='i8')
print(arr)
print(arr.dtype)

arr = np.array([0, 2.1, 3.1])
print(arr)
print(arr.dtype)
arr = arr.astype('i')
print(arr)
print(arr.dtype)
newarr = arr.astype(str)
print(newarr)
print(newarr.dtype)

newarr = arr.astype(bool)
print(newarr)
print(newarr.dtype)

newarr = arr.astype(complex)
print(newarr)
print(newarr.dtype)

"""

# copy and view
"""
arr = np.array([1, 2, 3, 4, 5])
x = arr.copy()
#arr[0] = 42

print(arr)
arr[0]=42
print(x)
print(arr)

y=arr.view()
print(y)
y[1]=202
print(arr)

x[1]=100
print(arr)
"""


# shape and reshape
arr = np.array([[1, 2, 3, 4], [5, 6, 7, 8]])
print(arr.shape)

arr = np.array([1, 2, 3, 4, 5, 6, 7, 8], ndmin=3)
print(arr)
print(arr.shape)

arr=np.array([1,2,3,4,5,6])
print(arr)
# 2 rows and 3 columns
arr1=arr.reshape(2,3)
print(arr1)

# 3 rows and 2 columns
arr2=arr.reshape(3,2)
print(arr2)

# 6 rows and 1 column
arr2=arr.reshape(6,1)
print(arr2)

arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])
newarr = arr.reshape(2, 3, 2)
print(newarr)

arr = np.array([1, 2, 3, 4, 5, 6, 7, 8])
newarr = arr.reshape(2, 2, -1)
print(newarr)

arr = np.array([[1, 2, 3], [4, 5, 6]])
newarr = arr.reshape(-1)
print(newarr)