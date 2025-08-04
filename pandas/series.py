import pandas as pd

# x=[3,4,5,6]
# a=pd.Series(x,index=['a','b','c','f'],dtype="float",name='python')
# print(a)

# print(a[2]) 
# print(type(a))

# dictionary
# dic={"name":["python","javaScript","node"],"age":12,"por":[12,13,14],"rank":[1,2,3]}
# var=pd.Series(dic)
# print(var)

# s=pd.Series(10,index=[1,2,3,4,5,6,7])
# print(type(s))
# print(s)
# print(s.dtype)

s=pd.Series(10,index=[1,2,3,4,5,6,7])
s1=pd.Series(10,index=[1,2,3,4])

print(s+s1)

