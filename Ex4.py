"""
NumPy Data Types
================

Data Types in Python
--------------------
By default Python have these data types:

strings - used to represent text data, the text is given under quote marks. eg. "ABCD"
integer - used to represent integer numbers. eg. -1, -2, -3
float - used to represent real numbers. eg. 1.2, 42.42
boolean - used to represent True or False.
complex - used to represent a number in complex plain. eg. 1.0 + 2.0j, 1.5 + 2.5j

Data Types in NumPy
-------------------
NumPy has some extra data types, and refer to data types with one character, like i for integers, u for unsigned integers etc.

Below is a list of all data types in NumPy and the characters used to represent them.

i - integer
b - boolean
u - unsigned integer
f - float
c - complex float
m - timedelta
M - datetime
O - object
S - string
U - unicode string
V - fixed chunk of memory for other type ( void )

Checking the Data Type of an Array
----------------------------------
The NumPy array object has a property called dtype that 
returns the data type of the array:

"""

import numpy as np
# Example 1: Get the data type of an array object

arr = np.array([1, 2, 3, 4])
print(arr.dtype)


# Example 2: Get the data type of an array containing strings

arr = np.array(['apple', 'banana', 'cherry'])
print(arr.dtype)


"""
Creating Arrays With a Defined Data Type
----------------------------------------
We use the array() function to create arrays, this function 
can take an optional argument: dtype that allows us to define the expected data type of the array elements:
"""

# Example 3: Create an array with data type string

arr = np.array([1, 2, 3, 4], dtype='f')
print(arr)
print(arr.dtype)


# For i, u, f, S and U we can define size as well.

# Example 4: Create an array with data type 4 bytes integer

arr = np.array([1, 2, 3, 4], dtype='i4')
print(arr)
print(arr.dtype)


"""
What if a Value Can Not Be Converted?
-------------------------------------
If a type is given in which elements can't be casted then NumPy will raise a ValueError.

ValueError: In Python ValueError is raised when the type of passed argument to a function is unexpected/incorrect.

"""

# Example 5: A non integer string like 'a' can not be converted to integer (will raise an error):

#arr = np.array(['a', '2', '3'], dtype='i')

"""
Converting Data Type on Existing Arrays
---------------------------------------
The best way to change the data type of an existing array, 
is to make a copy of the array with the astype() method.

The astype() function creates a copy of the array, and allows you to specify the data type as a parameter.

The data type can be specified using a string, like 'f' for float, 'i' for integer etc. or you can use the data type directly like float for float and int for integer.
"""

# Example 6: Change data type from float to integer by using 'i' as parameter value:

arr = np.array([1.1, 2.1, 3.1])
print(arr)
print(arr.dtype)
newarr = arr.astype('i')
print(newarr)
print(newarr.dtype)


# Example 7: Change data type from float to integer by using int as parameter value:


arr = np.array([1.1, 2.1, 3.1])
newarr = arr.astype(int)
print(newarr)
print(newarr.dtype)


# Example 8: Change data type from integer to boolean

arr = np.array([1, 0, 3])
newarr = arr.astype(bool)
print(newarr)
print(newarr.dtype)


arr = np.array([1, 0, 3],dtype='b')
print(arr)
print(arr.dtype)