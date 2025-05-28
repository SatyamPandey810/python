# bioData={
#     "name":"Jhon due",
#     "age":(1,3,4,6),
#     "number":123456,
#     "isActive":True,
#     "hobby":["cricket","football"]        
# }
# bioData["name"]="name"
# print(bioData["name"] );
# print(type(bioData))
# print(bioData.values())

# Nasted dictionary
dist={
    "name":"john due",
    "subject":{
        "1st":"html",
        "2nd":"CSS"
    },
    "age":12
};
# print(list(dist.keys())) #return all keys
# print(dist["subject"]["2nd"]);
# print(len(dist))
# print(list(dist.values())) #return values
# pairs=list(dist.items()) #return all key value pairs as tuples
# print(pairs[1])

# print(dist.get("name")) # return value as a key
# print(dist["name"])     # return value as a key

# dist.update({"city":"Noida"}) # add key value in dist
# print(dist)


# -------------=== Set ===-----------------
# collection={1,2,3,4,5,6, "hello world",True};
# print(len(collection));  # total number of items
# print(collection);

# empty set
# collection=set();

#add
# collection.add(1)
# collection.add((2,3,4))   #tupple

#remove
# collection.remove(1)
# collection.remove()

# print(collection.clear())
# print(len(collection))
# print(collection)

#pop
# collection={"hello","my name","is" ,"john","due"};
# print(type(collection));
# print(collection.pop());

#union
# set1={1,2,3,4}
# set2={4,5,6,7,8}
# set4={9,10,11}
# set3=set2.union(set1,set4)
# print(set3)

#intersection
# set={1,2,3}
# set1={3,4,1}
# set2=set.intersection(set1)
# print(set2)

# practice- dictionary
# stock={
#     "cat":"a small animal",
#     "table":["a piece of furniture","list of fact and "],
# }

# print(stock)

#practice- set()
# sub={"python","java","C++","python","javaScript",
# "java","python","java","C++","C"}
# print([sub,sub1])
# sub2=sub.union(sub)
# print(len(sub2),"total classroom need for all student")

#practice- dictionary{}
# sub1=int(input("Enter first subject marks :"))
# sub2=int(input("Enter second subject marks :"))
# sub3=int(input("Enter third subject marks :"));

# marks={
#     "python":sub1,
#     "java":sub2,
#     "node":sub3   
# }

# print(marks)

# if(marks["python"]>20):    
#   print("pass in python")
# else:
#     print("fail in python")

# if(marks["java"]>10):    
#   print("pass in java")
# else:
#     print("fail in java")
    
# if(marks["node"]>10):    
#   print("pass in node")
# else:
#     print("fail in node")
    
