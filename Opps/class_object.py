# Functions in oop is called method
# and data stores in classes called attribute.
# class name should be capitalized.This helps to differentiate a class from a normal variable or function name.

# class Employee:
#     def cs(self):
#         print("pooja","software developer","poojanika2gmail.com")
# emp=Employee() 
# emp.cs()

#========================================================================================

# class company:
#     def dept(self):
#         print("name:'pooja'","number: '111'","mobile:'12444'")
# cmp=company()
# # company.dept(cmp)#TypeError: company.dept() takes 0 positional arguments but 1 was given self is not given
# cmp.dept()   


#===========================================================================================

# Class object with attribute

# class Employee:
#     name='Pooja'
#     surname= 'Nikam'
#     email= 'poojaniakm@gmail.com'
#     rank=111
    
#     def dept(self):
#         print(f"ename : {self.name},esurname : {self.surname},eemail :{self.email}")
#     def details():
#         print("Innovant")
# # Employee.details()
# emp=Employee()
# # Employee.dept() # type error.position required
# Employee.dept(emp)

'''CLASS AND OBJECT'''
# class Employee:
#     name="pooja"
#     surname="nikam"
#     company="Microsoft"
#     salary=200000
    
#     def getinfo(self):
#         print(f"name of employee:{self.name},surname{ self.surname}")
#     def details():
#         print("innovant")
# emp=Employee()
# emp.getinfo()


'''CLASS WITH MULTIPLE OBJECT'''

# class Employees:
#     name="pooja"
#     surname="nikam"
#     company="Microsoft"
#     salary=200000

#     def __init__(self):
#         print("I am working software tester worth 35 lpa")

#     def info(self):
#         print(f"name of emp: {self.name}  {self.surname} working in company  {self.company} worth {self.salary}")

#     def empdetails(self,name,surname,company,salary):
#         self.name=name
#         self.surname=surname
#         self.company=company
#         self.salary=salary
# emp1=Employees()
# # emp1.empdetails("nikita","chandore","andupandu",20000)
# emp1.info()
# emp2=Employees()
# emp2.info()

'''Inheritance'''
#Single Inheritance

# class Family:

#     def __init__(self):
#         print("Welcome doston")

#     def info(self):
#         print("we are family")

# class dad(Family):
#     print("Big boss")

# f=Family()
# f.info()


#Multiple Inheritance

class Family:

    def __init__(self):
        print("We are family")

    def getinfo(self,name,surname,company):
        self.name=name
        self.surname=surname
        self.company=company
class Dad:
    print("bigg Boss of our home")

class Mom(Family,Dad):
    print("i am mom")

f=Family()
f.getinfo("pooja","nikam","nikam and nikam sons")
print(f.name)
d=Dad()



















