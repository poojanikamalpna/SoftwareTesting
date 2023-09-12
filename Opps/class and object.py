# Write OOP classes to handle the following scenarios:
# A user can create and view 2D coordinates
# A user can find out the distance between 2 coordinates
# A user can find find the distance of a coordinate from origin
# A user can check if a point lies on a given line
# A user can find the distance between a given 2D point and a given line

# class Point:

#     def __init__(self,x,y):
#         self.x_cod= x
#         self.y_cod= y

#     def __str__(self):
#         return '<{},{}>'.format(self.x_cod,self.y_cod)
    
#     def euclidean_dist(self,other):
#         return ((self.x_cod - other.x_cod)**2 + (self.y_cod - other.y_cod)**2)**0.5
    
#     def distunce_origin(self):
#         return self.euclidean_dist(Point(0,0))
    
# class Line:

#     def __init__(self,A,B,C):
#         self.A=A
#         self.B=B
#         self.C=C

#     def __str__(self):
#         return'{}+{}+{}=0'.format(self.A,self.B,self.C)
    
#     def point_on_line(line,point):
#         if line.A*point.x_cod + line.B*point.y_cod + line.C == 0:
#             return 'point lies on line'
#         else:
#             return 'points not lies on the line'
        
# l1=Line(2,3,4)
# p1=Point(1,1)
# print(l1.point_on_line(p1))

    
# p1=Point(0,0)
# p2=Point(10,10)
# print(p1.euclidean_dist(p2))
# print(p1.distunce_origin())

##==========================================================================================

'''Reference Variable'''
# class Person:
#     def __init__(self):
#         self.name='pooja'
#         self.company='Microsoft'

# Person()
# p=Person()
# q=p
# print(id(p))
# print(id(q))


#==============================================================================================

'''Call by reference'''

# class Person:

#     def __init__(self,name,gender):
#         self.name=name
#         self.gender=gender

# def greet(Person):
#     print('Hi  I am ',Person.name,'ans I am ',Person.gender)

# p=Person('pooja','female')
# print(p)
# greet(p)

# class Person:
#     def __init__(self,name,gender):
#         self.name=name
#         self.gender=gender

# def greet(person):
#     person.name='pooja'
#     return person

# p=Person('Komal','female')
# print(id(p))
# print(p)
# x=greet(p)
# print(x)
# print(id(x))  
# atrributes are mutable in this function
# We can access the attribute outside the class 
# this is reference call to the clas s
# object is just variable to store the instance or class or object when its is created



# class Employee:
#     name='pooja'
#     lname='nikam'
#     salary=3000000

#     def info():
#         print("abe saale yaha kaha dhund raha hai")

#     def get_info(self):
#         print(f"name= {self.name},lname={self.lname},salary={self.salary}")

#     def update_details(self,name,lname,salary):
#         self.name=name
#         self.lname=lname
#         self.salary=salary

# emp=Employee()
# emp.get_info()
# emp.update_details('komal','chede',40000)
# emp.get_info()
# Employee.company='microsoft'
# emp=Employee()  # we can add the attribute  from the outside of the class
# print(emp.company)

# e=Employee()
# s=e
# print(id(e))
# print(id(s))      # call of reference















