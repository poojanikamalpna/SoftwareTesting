
class Innovant:
    studentid=111
    st_name='pooja'
    surname='nikam'
    contact='1234567'

    def python_prep():
        print('student completed python')

    def sql_prep(self):
        print(f'sql is prepared  {self.studentid},  {self.st_name},  {self.surname}, {self.contact}')

    def update_student(selfie,studentid,st_name,surname,company):
        selfie.studentid=studentid
        selfie.st_name=st_name
        selfie.surname=surname
        selfie.company=company

inn=Innovant()
inn2=Innovant()
# inn.python_prep()  when we write cammand like this its shows position argument error bcz in brackete inn is  indirectly goes 
# to that brackete so 
Innovant.python_prep()
inn.sql_prep()
# inn2.python_prep()      position error
inn2.sql_prep()
Innovant.update_student(inn,112,'komal','chede','IBM')
Innovant.update_student(inn2,112,"komal","chede","IBM")
inn.sql_prep()




# class Employee:         # class => keyword to define class , Employee => class name, it can be anything and first char of each word has to be capital
#     empid = 1001            #attribute  # int
#     name = 'Savan'          #attribute   # str
#     address = 'Pune'          #attribute
#     salary = '9000000'          #attribute

#     def getInfo(self):       # method defination  # user defined
#         print(f"Emp id = {self.empid}, Name : {self.name}, address : {self.address}, salary : {self.salary}")       # function body

#     def updateInfo(selfie, empid, name, company) :       # self is object , empid is parameter, self.empid is referece to self attribute
#         selfie.empid = empid
#         selfie.name = name
#         selfie.company = company        # newly added attribute to only emp object


# emp = Employee()
# emp2 = Employee()
# emp.getInfo()   #Emp id = 1001, Name : Savan, address : Pune, salary : 9000000
# emp2.getInfo()
# Employee.updateInfo(emp, 2002, "Priya", "IBM")      ## selfie = emp, empid = 2002

# emp.getInfo()
# emp2.getInfo()

# print(emp.company)      #IBM
# print(emp2.company)


class Company:
    campanyid=1011
    companyname='Microsoft'
    owner='bill gate'
    city='redmond'
    contact=123456785

    def get_ifo(self):
        print(f"ID: {self.campanyid}, name: {self.companyname}, owner: {self.owner}, city: {self.city}, contact:{ self.contact}")

    def update_info(selfie,companyid,companyname,owner,city,ceo):
        selfie.campanyid=companyid
        selfie.companyname=companyname
        selfie.owner=owner
        selfie.city=city
        selfie.ceo=ceo

cmp=Company()
cmp1=Company()
cmp.get_ifo()
cmp1.get_ifo()
Company.update_info(cmp,1111,"Tesla","Elon musk","whashington Dc","pooja nikam")
cmp.get_ifo()
cmp1.get_ifo()





































