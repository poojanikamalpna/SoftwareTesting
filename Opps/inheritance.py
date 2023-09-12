# class Employee:
#     def __init__(self,n,s,c):
#         self.name=n
#         self.surname=s 
#         self.contact=c 
#         self.email=n +"."+ s + '@company.com'

#     def getdetails(self):
#         return '{} {}  {}'.format(self.name,self.surname,self.email)
    
# emp1=Employee("pooja","nikam",12345)
# print(emp1.getdetails())

# class User:
#     def __init__(self):
#         self.name="Pooja"
#         self.gender="Nikam"

#     def login(self):
#         print("login to the udemy")

# class Student(User):
#     def __init__(self):
#         self.roll_no=100

#     def enroll(self):
#         print("enroll the student")

# u=User()
# s=Student()
# print(s.name)  # its throw error 
# s.enroll()
# print(s.roll_no)
        
#if both the classes having the custructors  the object goes to the child class custructor
#it is show that if both classes having custructor '''overiding''' the custructor overiding has happen
 
    

# class Phone:
#     def __init__(self,price,brand,camera):
#         print("the object inside the phone")
#         self.price=price
#         self.brand=brand
#         self.camera=camera

#     def buy(self):
#         print("buying phone")

# class Smartphone(Phone):
#     pass

# s=Smartphone(200000,"Apple",15)
# print(s.brand)
# s.buy()


'''PRIVATE ATTRIBUTE CANT ACCESS IN INHERITANCE EXCEPT GETTER AND SETTER METHOD WE USED HERE'''

# class Phone:
#     def __init__(self,price,brand,camera):
#         print("phone object access the parent class")
#         self.__price=price
#         self.brand=brand
#         self.camera=camera
# # this is getter method`
#     def show(self):
#         print(self.__price)

# class Smartphone(Phone):

#     def check(self):
#         print(self.__price)

# s=Smartphone(200000,"Apple",13)
# s.show()  # It show the the price 



# class Parent:

#     def __init__(self,num):
#         self.__num=num

#     def get_num(self):
#         return (self.__num)
    
# class Child(Parent):

#     def __init__(self,val,num):
#         self.val=val

#     def get_val(self):
#         return self.val
    
# c=Child(100,100)
# c.num              #throwed error : AttributeError: 'Child' object has no attribute 'num'



# class Parent:
#     def __init__(self,price,brand,camera):
#         print("topic is overriding")
#         self.price=price
#         self.brand=brand
#         self.camera=camera

#     def buy(self):
#         print("buying a phone")

# class Child(Parent):

#     def buy(self):
#         print("There is OverRiding has happened here")

# c=Child(10000,"Apple",13)
# c.buy()

'''Super key in class '''
# class Phone:

#     def __init__(self,price,brand,camera):
#         print("this is custructor")
#         self.price=price
#         self.brand=brand
#         self.camera=camera

#     def buy(self):
#         print("buying a phone")

# class Smartphone(Phone):

#     def buy(self):
#         print("this is super clkass method ")
#         super().buy()

# c=Smartphone(10000,"Apple",13)  # when we use super () key in child class it goes first childe class method and after that went to 
# c.buy()                         #super means parent class and acces 


# class Phone:

#     def __init__(self,price,brand,camera):
#         print("tnside the custructor")
#         self.price=price
#         self.brand=brand
#         self.camera=camera

#     def buy(self):
#         print("here we learn super key")

# class Smartphone(Phone):

#     def __init__(self,price,brand,camera,os,ram):
#         super().__init__(price,brand,camera)
#         self.os=os
#         self.ram=ram
    # we cant access the super key from outside the class
    # we cant access the Attribute in the class using super key
    #Super is always used inside the child class

#     def buy(self):
#         print(" buying a phone")

# s=Smartphone(200000,"samsung",13,"Android",8)
# print(s.brand)


# Type of Inheritance#

#single =class passes to the single child class
#multilevel = grandparent->father->child
#heirarchical= father->mutliple child classes
#multiple=multiple parent classes to the single child class
#hybrid= combination of multple and heirachical









