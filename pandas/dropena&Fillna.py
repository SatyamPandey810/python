import pandas as pd

var=pd.read_csv("//home//ltp-deepmindz//my-app//python//customer.csv")
# print(var)
print(var.dropna())
print(var.dropna(axis=0))
print(var.dropna(how='any'))