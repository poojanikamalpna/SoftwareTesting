class Customer:
    billid=111
    billingname='pooja'
    billadress="Nandgaon"
    contact=1234
    bill=5000

    def __init__(self):
        print("I am constructor of customer")
    
    def getbilldetails(self):
        return f"ID:{self.billid}, name : {self.billingname}, adress: {self.billadress}, contact: {self.contact}, bill: {self.bill}"
cst=Customer()
cst=Customer()
billobject=cst.getbilldetails()
print(billobject)
P=cst.getbilldetails()

class Employee:
    empid=111
    fname="pooja"
    lname="Nikam"
    contact=12345
    adress="Pune"

    def __init__(self):
        self.empid=1111
        self.fname="Arun"
        self.lname="Nikam"
        self.iscorrectionrequired=False
        print("I am Constructor of Employee")


    def __init__(self,id,fname,lname,correction):
        self.empid=id
        self.fname=fname
        self.lname=lname
        self.iscorrectionrequired=correction

    def iscorrectionrequired(self):
        return self.iscorrectionrequired
    
    def getemployeedetails(self):
        return f"ID :{self.empid} , name: {self.fname}, lname: {self.lname}, contact:{self.adress}, adress: {self.adress}"

  
emp=Employee(11,"priya","kirtane",True)
info=emp.getemployeedetails()
print(info)



#Parameterised Cunstructor

class Adition:
    firstnumber=0
    secondnumber=0

    def __init__(self,first,second):
        self.firstnumber=first
        self.secondnumber=second

    def getResult(self):
        return self.firstnumber + self.secondnumber
    
addobj=Adition(299,300)
print(addobj.getResult())

        

























