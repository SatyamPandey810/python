# class Car:
#     name="TATA"
#     model="2020"

# si=Car();    
# print(si.name);

# constructor ---------
    # name="Maruti"
    # color="Red"
    
# class Car:
#     # Default constructor
#     def _init__(self):
#         pass
       
#      # parameterize constructor  
#     def __init__(self,name,color):
#         # print(fullName)
#         self.name=name;
#         self.color=color;
#         print("Adding a new student in database")

# car=Car("Maruti","Red")    
# print(car.name,car.color)
# car2=Car("TATA","Blue")
# print(car2.name,car2.color)

# class Student:
#     college="ABC";
#     name="john due"  #class attribute
#     def __init__(self,name,marks):
#         self.name=name;  # object attribute 
#         self.marks=marks;
# student=Student("raju",450)       

# print(student.name,student.marks);
# # print(student.college)
# print(Student.college)
# print(student.name)


# methods -----------------------
# class Car:
#     def __init__(self,name,marks):
#         self.name=name
#         self.marks=marks
        
#     def hello(self):
#         print("wellcome student",self.name)
        
#     def mark(self):
#         return self.marks
    
    
# car=Car("raju",30)  
# car.hello()
# print(car.mark())


#practice
# class Student:   
#     def __init__(self,name,marks):
#         self.name=name;
#         self.marks=marks    
#     @staticmethod 
#     def hello():
#         print("hello worlds")       
#     def get_avg(self):
#          sum=0
#          for item in self.marks:
#              sum+=item;
#              print("hii",self.name,"your avarage is :",sum/3)      
# student=Student("ram",[98,97,93])        
# # print(student.name,student.marks) 
# student.get_avg()    
# student.hello()  
# student.hello() 

###### Abstactions---------------------------------------------------------------------------------------------
# class Car():
#     def __init__(self):
#         self.acc=False
#         self.bre=False
#         self.clutch=False
#     def car_start__(self):
#        self.acc=True
#        self.bre=True
#        self.clutch=True
#        print("start the car....")      
       
# car=Car()
# # print(car)
# car.car_start__()

#Practice
# class Account():
#     def __init__(self,bal,acc):
#         self.acc=acc;
#         self.bal=bal;
        
#     def debit(self,amount):
#         self.bal-=amount
#         print("Rs",amount,"was debited")
#         print("Total balance is :" ,self.get_balance())
           
#     def credit(self,amount):
#         self.bal+=amount
#         print("Rs",amount,"was created")    
#         print("Total balance is :" ,self.get_balance())
                   
   
#     def get_balance(self):
#        return self.bal
   
# account=Account(10000,12345)        
# print(account.bal)

# account.debit(1000)
# account.credit(200)
        
# class Pocket:
#     def __init__(self,bal,acc):
#         self.bal=bal;
#         self.acc=acc;
        
#     def debit(self,amount):
#         self.bal-=amount
#         print("Rs.",amount, "is debited")    
#         print("Total balance is",self.total_balance())

#     def credit(self,amount):
#         self.bal+=amount
#         print(amount,"is credited")   
#         print("Total balance is",self.total_balance())

#     def total_balance(self):
#        return self.bal    
        
# pocket=Pocket(8000,1223443)        

# pocket.debit(2000)
# pocket.credit(1000)
# pocket.total_balance()

# del keyword==-----==-=-=-=-=-=-=---=-=-=-=-===\
# class Car:
#     def __init__(self,name):
#         self.name=name      
        
# s1=Car("ram")      
# del s1  
# print(s1.name)

# private property and methods
# property private---------------------------
# class Bank:
#     def __init__(self,accno,pasbok):
        
#         self.accno=accno
#         self.__pasbok=pasbok
        
#     def resetPassword(self):
#         print(self.__pasbok)        
        
# bank=Bank("12345","abcde")        

# bank.resetPassword()
# print(bank.accno)
# print(bank.pasbok)
  
# method private=================
# class Bank:
#     __name="HDFC BANK"    
#     def __hello(self ):
#         print("Hello world")
#     def wellcome(self):
#         self.__hello()      
# bank=Bank()    
# # print(bank.name)
# bank.wellcome()

#  inheritance================================-------------------------------------------------------------======
# single inheritance
# class Car:
#     color="White"
#     @staticmethod
#     def start():
#         print("start car....")
#     @staticmethod
#     def stop():
#         print("stop car")    

# class Toyota(Car):        
#     def __init__(self,name):
#         self.name=name
        
# car1=Toyota("fourtuner")        
# print(car1.name)
# print(car1.start())
# print(car1.color)

# multi-level inheritance
# class Car:
#     color="White"
#     @staticmethod
#     def start():
#         print("start car....")
#     @staticmethod
#     def stop():
#         print("stop car")    

# class Toyota(Car):        
#     def __init__(self,brand):
#         self.brand=brand
        
# class Fortuner(Toyota):
#     def __init__(self,type):
#         self.type=type       
        
# car1=Toyota("toyota hi brand hai")    
# print(car1.color)

# car2 =Fortuner("diesel")
# car2.start()
# print(car2.type)

#Multiple inheritance
# class Parent1:
#     varA="hello i am parent-1"
# class Parent2:
#     varB="hello i am parent-2"    
# class Child(Parent1,Parent2):
#     varChild=("Hello all i am child")    
    
# child=Child()    
# print(child.varA)
# print(child.varB)
# print(child.varChild)

#super keyword
# class A:
#     def __init__(self):
#         print("hello i am parent constructor")

# class B(A):
#     def __init__(self):
#         super().__init__()
#         print("hello i am child constructor")
        
# b=B()        
# print(b)
 
# class Car:
#     def __init__(self,type):
#         self.type=type
#     @staticmethod
#     def start():
#         print("car startd..")
# class Tyota(Car):
#     def __init__(self,type,name):
#        super().__init__(type)
#        self.name=name 
#        super().start()
# c1=Tyota("tata","petrol")       
# print(c1.name)
# print(c1.type)
# c1.start()

# class Person:
#     name="deepak"
#     def nameChagne(self,name):
#         Person.name=name
        
# person=Person()        
# person.nameChagne("rahul")
# print(Person.name)
# print(person.name)
        
 #class methods
# class Person:
#     name="deepak"
#     @classmethod
#     def changeName(cls,name):
#         cls.name=name

# p=Person()
# p.changeName("rahul kumar")
# print(p.name)
# print(Person.name)

# property
# class Student:
#     def __init__(self,hindi,math,english):
#      self.hindi=hindi
#      self.math=math
#      self.english=english
   
#     @property
#     def perCul(self):
#         return str((self.hindi+self.math+self.english)/3) +"%"     
            
# s1=Student(10,30,20)

# s1.hindi=98
# print(s1.perCul)

# s1.getPer()
# print(s1.per)

## Polymorphism 
# class Complex():
#     def __init__(self,num,img):
#         self.num=num
#         self.img=img
        
#     def number(self):
#         print(self.num,"i +",self.img,"j")     

# c1=Complex(1,2)
# c1.number()

# c2=Complex(4,5)
# c2.number()

#practice
# class Cricle:
#     def __init__(self,redius):
#         self.redius=redius
        
        
#     def area(self):
#             return (22/7)*self.redius ** 2
        
#     def perimeter(self):
#             return 2 * (22/7) * self.redius

# c1=Cricle(21)
# print(c1.perimeter)
# print(c1.area())

# class Employee:
#     def __init__(self,role,dept,salary):
#         self.role=role
#         self.dept=dept
#         self.salary=salary
    
#     def showDetails(self):
#         print("role",self.role)    
#         print("dept",self.dept)
#         print("salary",self.salary)


# class Engineer(Employee):
#     def __init__(self,name,age):
#         self.name=name
#         self.age=age
#         super().__init__("Engineer" ,"IT","750000")


# emp=Engineer("rahul",40)        
# emp.showDetails()


class Order:
   def __init__(self,item,price):
        self.item=item
        self.price=price
   def __gt__(self,ord2):
        return self.price>ord2.price
    
    
ord1=Order("chips",20)    
ord2=Order("Drink",90)
print(ord1>ord2)