
# Constructor

# class Computer:
    

#     def __init__(self):
#         self.name="pooja"
#         self.age=25
        
#     def update(self):
#         self.age=30
    
    

# c1=Computer()
# c2=Computer()
# c1.name="rashi"
# c1.age=23
# c1.update()
# print(c1.name)
# print(c1.age)   # age=25       before Updation
# print(c1.age)   # age=30      after updation

# Default constructor
# class Geeks:

#     def __init__(self):
#         self.geek="Geek for geeks"

#     def printg(self):
#         print(self.geek)
# obj=Geeks()
# obj.printg()


# Parametrize constructor
class Computer:
    def __init__(self):
        self.name="intel"
        self.company="microsoft"

    def update(self,n,c):
        self.name=n
        self.company=c

obj=Computer()
# print(obj)
obj.update("apple","appletab")
print(obj.name)
print(obj.company)




