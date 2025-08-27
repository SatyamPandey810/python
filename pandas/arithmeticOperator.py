import pandas as pd


# var=pd.DataFrame({"A":[1,2,3,4],"B":[10,11,12,13]})
# var["C"] = var["A"] + var["B"]  # - * / ** % all arithmatic
# print(var)


var=pd.DataFrame({"A":[1,2,3,4],"B":[10,11,12,13]})
var['python']=var['B']<=12
print(var)