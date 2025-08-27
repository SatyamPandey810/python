import pandas as pd

# x=pd.Series([1,2,3,4],index=["a",'b','c','d'],dtype=float,name='pandas')
# print(x)
# print(x['a'])
# print(type(x))

# dis
# dis=pd.Series({'name':['java','python','html'],'por':[12,13,14,15]})
# print(dis)

a=pd.Series(12,index=[1,2,3,4,5,6])
b=pd.Series(13,index=[1,2,3,4])
print(a+b)