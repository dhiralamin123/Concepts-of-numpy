"""
What is NumPy?
-------------
NumPy is a python library used for working with arrays.

It also has functions for working in domain of linear algebra, 
fourier transform, and matrices.

NumPy was created in 2005 by Travis Oliphant. It is an open 
source project and you can use it freely.

NumPy stands for Numerical Python.

Why Use NumPy ?
---------------
In Python we have lists that serve the purpose of arrays, but they are slow to process.

NumPy aims to provide an array object that is up to 50x faster that traditional Python lists.

The array object in NumPy is called ndarray, it provides a lot of supporting functions that make 
working with ndarray very easy.

Arrays are very frequently used in data science, where speed and resources are very important.

Data Science: is a branch of computer science where we study how to store, use and analyze data for 
deriving information from it.

Why is NumPy Faster Than Lists?
-------------------------------
NumPy arrays are stored at one continuous place in memory unlike lists, so processes can access and 
manipulate them very efficiently.

This behavior is called locality of reference in computer science.

This is the main reason why NumPy is faster than lists. Also it is optimized to work with 
latest CPU architectures.

Which Language is NumPy written in?
-----------------------------------
NumPy is a Python library and is written partially in Python, but most of the parts that require 
fast computation are written in C or C++.
"""

#Checking NumPy Version
#The version string is stored under __version__ attribute.

#Example
import numpy as np

print(np.__version__)

"""
Create a NumPy ndarray Object
-----------------------------
NumPy is used to work with arrays. The array object in NumPy 
is called ndarray.

We can create a NumPy ndarray object by using the array() 
function.
"""

arr = np.array([1, 2, 3, 4, 5])
print(arr)
print(type(arr))



"""
To create an ndarray, we can pass a list, tuple or any 
array-like object into the array() method, and it will be 
converted into an ndarray:
"""

#Example
#Use a tuple to create a NumPy array:

arr = np.array((1, 2, 3, 4, 5))
print(arr)


"""
Dimensions in Arrays
====================
A dimension in arrays is one level of array depth (nested arrays).

[1] 0-D Arrays
    ==========
    0-D arrays, or Scalars, are the elements in an array. Each value in an array is a 0-D array.


"""

arr = np.array(42)
print(arr)

"""
[2] 1-D Arrays
    ==========
    An array that has 0-D arrays as its elements is called uni-dimensional or 1-D array.

    These are the most common and basic arrays.
"""

arr = np.array([1, 2, 3, 4, 5])
print(arr)


"""
[3] 2-D Arrays
    ==========
An array that has 1-D arrays as its elements is called a 2-D array.

These are often used to represent matrix or 2nd order tensors.
0"""

arr = np.array([[1, 2, 3], [4, 5, 6]])
print(arr)

"""
[4] 3-D arrays
    ==========
    An array that has 2-D arrays (matrices) as its elements is called 3-D array.

    These are often used to represent a 3rd order tensor.
"""

arr = np.array([[[1, 2, 3], [4, 5, 6]], [[1, 2, 3], [4, 5, 6]]])
print(arr)


"""
Check Number of Dimensions?
===========================
NumPy Arrays provides the ndim attribute that returns an integer that tells us how many dimensions the array have.
"""


a = np.array(42)
b = np.array([1, 2, 3, 4, 5])
c = np.array([[1, 2, 3], [4, 5, 6]])
d = np.array([[[1, 2, 3], [4, 5, 6]], [[1, 2, 3], [4, 5, 6]]])

print(a.ndim)
print(b.ndim)
print(c.ndim)
print(d.ndim)


"""
Higher Dimensional Arrays
=========================
An array can have any number of dimensions.

When the array is created, you can define the number of 
dimensions by using the ndmin argument.
"""

arr = np.array([1, 2, 3, 4], ndmin=5)

print(arr)
print('number of dimensions :', arr.ndim)

"""
Note: In this array the innermost dimension (5th dim) has 4 
elements, the 4th dim has 1 element that is the vector, 
the 3rd dim has 1 element that is the matrix with the vector, 
the 2nd dim has 1 element that is 3D array and 1st dim has 1 
element that is a 4D array.
"""
