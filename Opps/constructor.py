# class Customer:
#     billid=111
#     billingname='pooja'
#     billadress="Nandgaon"
#     contact=1234
#     bill=5000

#     def __init__(self):
#         print("I am constructor of customer")
    
#     def getbilldetails(self):
#         return f"ID:{self.billid}, name : {self.billingname}, adress: {self.billadress}, contact: {self.contact}, bill: {self.bill}"
# cst=Customer()
# # cst=Customer()
# billobject=cst.getbilldetails()
# print(billobject)
# P=cst.getbilldetails()

# class Employee:
#     empid=111
#     fname="pooja"
#     lname="Nikam"
#     contact=12345
#     adress="Pune"

#     def __init__(self):
#         self.empid=1111
#         self.fname="Arun"
#         self.lname="Nikam"
#         self.iscorrectionrequired=False
#         print("I am Constructor of Employee")


#     def __init__(self,id,fname,lname,correction):
#         self.empid=id
#         self.fname=fname
#         self.lname=lname
#         self.iscorrectionrequired=correction

#     def iscorrectionrequired(self):
#         return self.iscorrectionrequired
    
#     def getemployeedetails(self):
#         return f"ID :{self.empid} , name: {self.fname}, lname: {self.lname}, contact:{self.adress}, adress: {self.adress}"

  
# emp=Employee(11,"priya","kirtane",True)
# info=emp.iscorrectionrequired()
# print(info)



#Parameterised Cunstructor

# class Adition:
#     firstnumber=0
#     secondnumber=0

#     def __init__(self,first,second):
#         self.firstnumber=first
#         self.secondnumber=second

#     def getResult(self):
#         return self.firstnumber + self.secondnumber
    
# addobj=Adition(299,300)
# print(addobj.getResult())

        
# class employee:
#     ename = "pooja"
#     lname = "Nikam"
#     salary = 400000
#     adress= "pune"

#     def depatment(self):
#         print(f"ename:{self.ename},lname:{self.lname},salary: {self.salary},adress:{self.adress}")

#     def getinfo():
#         print("innovant")
# employee.getinfo()
# emp=employee()
# emp.depatment()
# print(employee.salary)

# class Employee():
#     ename="pooja"
#     lname="Nikam"
#     salary=350000
#     address="Puna"

#     def getdetails():
#         print("Hiii I am software developer")

#     def getemployeedetail(self):
#         print(f"ename= {self.ename},lname ={self.lname},salary={self.salary},address={self.address}")

#     def updateinfo(self,ename,lname,salary,contact):
#         self.ename=ename
#         self.lname=lname
#         self.salary=salary
#         self.contact=contact

# emp=Employee()
# emp2=Employee()
# emp.getemployeedetail()
# emp2.getemployeedetail()
# Employee.getdetails()
# Employee.updateinfo(emp2,"komal","Chede",450000,23456)
# Employee.getemployeedetail(emp2)



# class Family:
#     father= "Arun"
#     mother="Alpana"
#     sister="Diksha"
#     brother="Shivam"


#     def familytree():
#         print("we are family..we stay together forever")

#     def family(self):
#         print(f"father={self.father},mother={self.mother},sister={self.sister},brother={self.brother}")
        
    
#     def updatefamily(self,father,mother,sister,brother):
#         self.father=father
#         self.mother=mother
#         self.sister=sister
#         self.brother=brother

# Family.familytree()
# fam=Family()
# fam.family()
# Family.updatefamily(fam,"arun","alpana","pooja","shiv")
# fam.family()
# # print(Family.mother)
# # print(Family.brother)
# Family.family(fam)


'''Parameterised custructor'''

# class Employee:
#     eid=111
#     ename="pooja"
#     esurname="Nikam"
#     company="Microsoft"

#     def __init__(self,ename,esurname,company,contact):
#         self.ename=ename
#         self.esurname=esurname
#         self.company=company
#         self.contact=contact
        

#     def getdetails(self):
#         print("i am software engineer")
        

# emp=Employee("pooja","Nikam","Microsoft",12345)

# emp.getdetails(emp,"p","J","e",23)
        
 


























