import numpy as np

"""
arr = np.array([1, 2, 3])

for x in arr:
  print(x)
  
arr = np.array([[1, 2, 3], [4, 5, 6]])

for x in arr:
    for y in x:
        print(y)


arr = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])

for x in arr:
    for y in x:
        for z in y:
            print(z)



arr = np.array([[[1, 2], [3, 4]], [[5, 6], [7, 8]]])

for x in np.nditer(arr):
  print(x)


arr = np.array([[1, 2], [3, 4], [5, 6]])

for x in np.nditer(arr):
  print(x)

arr = np.array([[1, 2, 3, 4], [5, 6, 7, 8]])

for x in np.nditer(arr[:, ::2]):
  print(x)

arr = np.array([1, 2, 3])

for idx, x in np.ndenumerate(arr):
  print(idx, x)


arr = np.array([[1, 2, 3, 4], [5, 6, 7, 8]])
for idx, x in np.ndenumerate(arr):
  print(idx, x)  
"""

# combine array
"""
arr1 = np.array([1, 2, 3])
arr2 = np.array([4, 5, 6])
arr = np.concatenate((arr1, arr2))
print(arr)

arr1 = np.array([[1, 2], [3, 4]])
arr2 = np.array([[5, 6], [7, 8]])
arr = np.concatenate((arr1, arr2))
print(arr)

arr = np.concatenate((arr1, arr2), axis=1)
print(arr)

arr1 = np.array([1, 2, 3])
arr2 = np.array([4, 5, 6])
arr = np.stack((arr1, arr2), axis=1)
print(arr)

arr = np.hstack((arr1, arr2))
print(arr)

arr = np.vstack((arr1, arr2))
print(arr)

arr = np.dstack((arr1, arr2))
print(arr)
"""

# splitting array
"""
arr = np.array([1, 2, 3, 4, 5, 6])
newarr = np.array_split(arr, 3)
print(newarr)

arr = np.array([1, 2, 3, 4, 5, 6])
newarr = np.array_split(arr, 4)
print(newarr)

print(newarr[0])
print(newarr[1])
print(newarr[2])
print(newarr[3])


arr = np.array([[1, 2], [3, 4], [5, 6], [7, 8], [9, 10], [11, 12]])
newarr = np.array_split(arr, 3)
print(newarr)


for i in range(3):
    print("array ",i, "=\n", newarr[i])
"""

"""
arr = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12], [13, 14, 15], [16, 17, 18]])
newarr = np.array_split(arr, 3, axis=1)
print(newarr)

arr = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12], [13, 14, 15], [16, 17, 18]])
newarr = np.hsplit(arr, 3)
print(newarr)
"""

# sorting
arr=np.array([3,4,2,1,0,34])
print(arr)
arr.sort() # ascending
print(arr) 
print(arr[::-1]) # descending

# condition
arr = np.array([1, 2, 3, 4, 5, 6, 7, 8])
x = np.where(arr>5)
print(arr[x])
print("index=",x)

x = np.where(arr%2==0)
print(arr[x])
print("index=",x)

x = np.where(arr%2!=0)
print(arr[x])
print("index=",x)

x = np.where((arr>3) & (arr<7))
print(arr[x])
print("index=",x)
