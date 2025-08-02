import numpy as np

# 1D
# var=np.array([1,2,3,4,5,6])
# for i in var:
#     print(i)

# 2D
# var=np.array([[1,2,3,4,5],[0,9,8,7,6]])
# print(var.ndim)
# for i in var:
#     print(i)

# print()   
 
# for k in var:
#     for l in k:
#         print(l)

# with nditer function iterating
# for a in np.nditer(var):
#     print(a)

# 3D
# var=np.array([[[1,2,3,4,5],[0,6,7,8,9]]])
# print(var.ndim)
# for a in var:
#     for b in a:
#         for c in b:
#             print(c)
       
# with nditer function iterating and change the data type
# for a in np.nditer(var,flags=['buffered'],op_dtypes=["S"]):
    # print(a.dtype)
    
#  ndenumerate funcction iterating with index number
# for i,d in np.ndenumerate(var):
#     print(i,d)       
            
            
            
################# copy V/s view    ############## 

#Copy     
# var=np.array([1,2,3,4,5,6])
# co=var.copy()
# var[1]=200
# print(co)
# print(var)


# views
var=np.array([1,2,3,4,5,6])
vi=var.view()
var[1]=40
print(vi)