import numpy as np

######### indexing #############
# 1D
# var=np.array([1,2,3,4])
# print(var.ndim)
# print(var[-3])
# print(var[1])

#2D
# var=np.array([[1,2,3,4],[1,2,3,4]])
# print(var.ndim)

# print(var)
# print(var.ndim)
# print()
# print(var[0,1])
# print(var[0,-3])
# print()
# print(var[1,2])
# print(var[1,-2])

# 3D
# var=np.array([[[1,2,3,4],[7,8,9,10]]])
# print(var.ndim)

# print(var[0,0,3])
# print(var[0,0,-1])
# print()
# print(var[0,1,0])
# print(var[0,1,-4])


############## Slicing #############

# 1D
# var=np.array([1,2,3,4,5,6,7,8])
# print(var.ndim)
# print(var[1:5])
# print(var[1:])
# print(var[1:-3])
# print(var[:5])

# stop point
# print(var[::2])

## 2D
# var=np.array([[1,2,3,4,5,0,12],[9,8,7,6,10,15,33]])
# print(var.ndim)
# print(var[0,1:3])
# print(var[1,0:4])

# 3D
# var=np.array([[[1,2,3,4,5,6],[8,9,10,11,12,13]]])
# # print(var.ndim)
# print(var[0,0,1:3])
# print(var[0,1,::2])






