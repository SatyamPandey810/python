# num=12345

# one=5*10+4
# two=54*10+3
# three=543*10+2
# result=5432*10+1

# if(result==num):
#     print("it is polindrom")
# else:
#     print("not polindrom")    

num = 12345
n = num
res = 0

while n > 0:
    ld = num % 10
    res = res * 10 + ld
    n = num // 10

print(res)


# num = 121
# n = num
# rev = 0

# while n > 0:
#     digit = n % 10
#     rev = rev * 10 + digit
#     n = n // 10

# if(rev==num):
#   print("Num is polindrom")
# else:
#   print("Num is not polindrom")  










 