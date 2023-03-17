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

class Employee:
    name='Pooja'
    surname= 'Nikam'
    email= 'poojaniakm@gmail.com'
    rank=111
    
    def dept(self):
        print(f"ename : {self.name},esurname : {self.surname},eemail :{self.email}")
    def details():
        print("Innovant")
# Employee.details()
emp=Employee()
# Employee.dept() # type error.position required
Employee.dept(emp)














