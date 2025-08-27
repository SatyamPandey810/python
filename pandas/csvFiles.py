import pandas as pd

# Write CSV (coma,spareted values)
dis={"A":[1,2,3,4,5],"B":[6,7,8,9,10],"D":[11,12,13,14,15]}
var=pd.DataFrame(dis)
print(var)
# var.to_csv("Test_new.csv")
# without index
# var.to_csv("Test_new2.csv",index=False)

#override old header with new
var.to_csv("Test_new4.csv",index=False,header=["ram","shyaam",'ghanshyaam'])

