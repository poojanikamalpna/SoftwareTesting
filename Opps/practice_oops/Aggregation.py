#  Aggregation is the class which own the another class like relation customer have a aaddress,like restaurant have a menu its shows like that relation

class Customer:
    def __init__(self,name,gender,address):
        self.name=name
        self.gender=gender
        self.address=address

    def print_address(self):
        print(self.address.get_city(),self.address.pin,self.address.state)


    def edit_profile(self,new_name,new_city,new_pin,new_state):
        self.name=new_name
        self.address.edit_address(new_city,new_pin,new_state)

class Address:

    def __init__(self,city,pin,state):
        self.__city=city
        self.pin=pin
        self.state=state

    def get_city(self):
        return self.__city
    
    def edit_address(self,new_city,new_pin,new_state):
        self.__city=new_city
        self.pin=new_pin
        self.state=new_state
    

addr=Address("hadapsar",423123,"Pune")
cust1=Customer("Pooja","female",addr)
cust1.print_address()

cust1.edit_profile("ankita","Mumabai",1111,"Maharashtra")
cust1.print_address()
