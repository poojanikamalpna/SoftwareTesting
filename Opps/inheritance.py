# class Employee:
#     def __init__(self,n,s,c):
#         self.name=n
#         self.surname=s 
#         self.contact=c 
#         self.email=n + " . "+ s + '@company.com'

#     def getdetails(self):
#         return '{} {}'.format(self.name,self.surname,self.email)
    
# emp1=Employee("pooja","nikam",12345)
# info=emp1.getdetails()
# print(info)


class Employee:
    emid=101
    ename="pooja"
    esurname="nikam"
    adress="pune"
    salary=300000

    def getemployeedetail(self):
        print(f"EMP Id {self.emid},emp name {self.ename},suraname {self.esurname},adress {self.adress}")

    def getcompany():
        print("innovant")

emp=Employee()
# print(emp.adress)
emp.getemployeedetail()

class tempemployee(Employee):
    






