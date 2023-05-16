from abc import ABC,abstractmethod
class Father(ABC):
    def __init__(self):
        print("Fther class initiated")

    @abstractmethod
    def speak(self):
        pass

    @abstractmethod
    def walk(self):
        pass

    def hobby(self):
        print("I am from father class")

class Mom(Father):

    def __init__(self)-> None:
        print("i am from father class")

    def speak(self):
        print("Speask hindi")

    def walk (self):
        print("Walk fast")

    def hobby(self):
        print("Gaming")

class Child(Father):
    def __init__(self):
        pass 
     
    def speak(self):
         print("speak hindi")

    def walk(self):
         print("walk slow")

    def hobby(self):
        print("hobby to speak English")

#father=Father()    # TypeError: Can't instantiate abstract class Father with abstract methods speak, walk
'''We cant create the object of abstract class '''
mobj=Mom()
mobj.speak()
mobj.walk()
mobj.hobby()

cobj=Child()
cobj.walk()
cobj.hobby()
cobj.speak()

##human = Human() #TypeError: Can't instantiate abstract class Human with abstract methods speak, walk
# we can not create object of abstract class.. means class have atleast one abstract method
# Abstract class is basically meant for inheritance and contract
# abstract class can have abstract + non abstract methods
# Every inheriting class of abstract class has to provide implementation for abstract mehtod other wise class will be incomplete
# and we can not create object of that class
cobj.__class__()

    