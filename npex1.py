import numpy as np
print(np.__version__)

a=np.array(34)
print(a)

a=np.array([1,2,3,4,5])
print(a)

b=np.array([[1,2,3],[4,5,6]])
print(b)

print(b.shape)
print(a.shape)
print(np.sqrt(a))
print(np.sqrt(b))

a=np.arange(1,5)
print(a)

b=np.arange(10,45)
print(b)

no=np.array([-1,-4,2,3])
print(no)
print(np.abs(no))
print(np.sin(no))
print(np.cos(no))
print(np.tan(no))
print(np.exp(no))

a=np.array([2,4,5])
b=np.array([6,7,0])
c=np.add(a,b)
print(c)
c=np.subtract(a,b)
print(c)
c=np.multiply(a,b)
print(c)
c=np.divide(b,a)
print(c)

a=np.array([[1,2],[4,5]])
b=np.array([[6,7],[8,9]])

print(np.add(a,b))

a=np.array(["dhiral","neel","sagar","sandeep","mehul"])
print(a)

a=np.ones(5)
print(a)
a=np.ones((3,4))
print(a)

b=np.zeros(3)
print(b)

print(3*a)
print(10*a)

print(a.transpose())

print(a.ndim)
a=np.linspace(1,5,10)
print(a)
