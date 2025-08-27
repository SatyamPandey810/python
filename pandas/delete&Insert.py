import pandas as pd

## insert data
# var=pd.DataFrame({"A":[1,2,3,4],"B":[9,8,7,6]})
# var.insert(1,"python",var['A'])    # with copy
# var.insert(1,"python",[11,12,13,14]) # sapret
# print(var)

## limited data copy using slice
# var=pd.DataFrame({"A":[1,2,3,4],"B":[9,8,7,6]})
# var.insert(1,"python_12",var['A'][:2]) 
# print(var)


## delete data
var=pd.DataFrame({"A":[1,2,3,4],"B":[9,8,7,6],"C":[11,12,13,14]})
print(var)
var1=var.pop("B")
print("Deleted data->")
print(var1)
