import pandas as pd

# Write CSV (coma,spareted values)
# dis={"A":[1,2,3,4,5],"B":[6,7,8,9,10],"D":[11,12,13,14,15]}
# var=pd.DataFrame(dis)
# print(var)
# var.to_csv("Test_new.csv")
# without index
# var.to_csv("Test_new2.csv",index=False)

#override old header with new
# var.to_csv("Test_new4.csv",index=False,header=["ram","shyaam",'ghanshyaam'])




## read csv files
## rows get
# csv_1=pd.read_csv("//home//ltp-deepmindz//my-app//python//customer.csv",nrows=1) #nrows geting on number of rows
# print(csv_1)
## skip rows
# csv_2=pd.read_csv("//home//ltp-deepmindz//my-app//python//customer.csv",skiprows=[0,3]) 
# print(csv_2)

# cols get
# csv_2=pd.read_csv("//home//ltp-deepmindz//my-app//python//customer.csv",usecols=['Company']) 
# print(csv_2)

# csv_2=pd.read_csv("//home//ltp-deepmindz//my-app//python//customer.csv",usecols=[0,3])
# print(csv_2)

## index cols
# csv_3=pd.read_csv("//home//ltp-deepmindz//my-app//python//customer.csv",index_col=['City'])
##  header
# csv_3=pd.read_csv("//home//ltp-deepmindz//my-app//python//customer.csv",header=2)
# print(csv_3)

## cols name
csv_3=pd.read_csv("//home//ltp-deepmindz//my-app//python//customer.csv",names=["col1",'col2','col3','col4','col5','col6','col7'])




