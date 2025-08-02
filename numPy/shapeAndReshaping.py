import numpy as np

# Shape
# var=np.array([[1,2,3,4],[1,2,3,4]])
# print(var)
# print()
# print(var.shape)

# var1=np.array([1,2,3,4],ndmin=4)
# print(var1)
# print(var1.ndim)
# print(var1.shape)


## reshape

# var = np.array([1,2,3,4,5,6])
# x = var.reshape(6,1)
# print(x)
# print(x.ndim)

# var1=np.array([1,2,3,4,5,6,7,8,9,10,11,12])
# x1=var1.reshape(2,3,2)
# print(x1)
# print(x1.ndim)

var1=np.array([1,2,3,4,5,6,7,8,9,10,11,12])
x1=var1.reshape(2,3,2)
print(x1)
print(x1.ndim)
print()
one=x1.reshape(-1)
print(one)
print(one.ndim)
