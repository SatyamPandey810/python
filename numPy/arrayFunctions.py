import numpy as np

########### Concatenate ##################
# 1D
# var=np.array([1,2,3,4])
# var2=np.array([5,6,7,8])
# con=np.concatenate((var,var2))
# print(con)

#2D
# var=np.array([[1,2,3,4]])
# var2=np.array([[9,10,11,12]])
# con=np.concatenate((var,var2),axis=1) # axis=1 stand for horizontal direction and axis=0 stand for vertical direction
# print(con)
# with stack function
# st=np.stack((var,var2),axis=1) 
# print(st)

# stack with horizontal direction
# var=np.array([1,2,3,4])
# var2=np.array([5,6,7,8])
# a_new=np.vstack((var,var2))
# print(a_new)

# dstack stand for hight along mergeing 
# hstact stand for horizontal(column) merging 
# vstack stand for vertical(row) merging


################################ Split ##################################
# 1D
# var=np.array([1,2,3,4,5,6,7,8])
# spil=np.array_split(var,3)
# print(spil)
# print(type(spil))
# print(spil[2])

#2D
# var=np.array([[1,2,0,8],[3,4,5,6]])
# print(var.ndim)
# spil=np.array_split(var,3)
# spil1=np.array_split(var,3,axis=1)

# # print(spil)
# print()
# print(spil1)

# 3D
# arr_3d = np.arange(1, 28).reshape(3, 3, 3)

# # Split along axis 0 into 2 uneven parts
# uneven_split = np.array_split(arr_3d, 2, axis=0)
# print("\nUneven split along axis 0:\n", uneven_split)

############################ Searching an array ########################
# var = np.array([1,2,3,4,5,3,4,5,6,7,2,4,5])
# x=np.where(var==2)
# x=np.where((var%2)==0)
# print(x)

######Search shorted array
# var=np.array([1,2,3,4,6,7,8,9])
# x=np.searchsorted(var,[5,3,0],side='right')
# print(x)

#################  Sort array ##############
# var = np.array([3,2,1,4,8,6,5,7,9,0])
# var=np.array(['b','a','c','d'])
# x=np.sort(var)
# print(x)

# 2D
# var=[[4,3,2,6,1,5],[11,15,10,50,33,13]]
# print(np.sort(var))

################# filter array ##############
# var = np.array([1,2,3,4])
# y=[True,False,True,False]
# new_array=var[y]
# print(new_array)
# 2D
# var=np.array([1,2,3,4],[1,2,3,4])
# f=[True,False,False,True]
# new_arr=var[f]
# print(new_arr)

################# shuffle array ############## data change every time

# var=np.array([1,2,3,4,5,6])
# np.random.shuffle(var)
# print(var)

################# unique array ############## only unique data find not repating data

# var=np.array([1,2,3,4,5,6,3,2]) 
# x=np.unique(var)
# x=np.unique(var,return_index=True) # Find the data index where is where
# x=np.unique(var,return_counts=True) # Find the count number each if repating
# print(x)


################# resize ###################
# var=np.array([1,2,3,4,5,6]) 
# y=np.resize(var,(3,2))
# print(y)

################# flatten ################
# var=np.array([1,2,3,4]) 
# print(var)
# print()
# x=var.flatten(order="C")
# print(x)

################# revel ############### 

var=np.array([1,5,3,4,2]) 
x=np.ravel(var)
print(x)









