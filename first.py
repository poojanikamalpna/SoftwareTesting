# import datetime
# ndate=datetime.datetime.now()
# print(ndate)

# from math import pi
# r=float(input("Enetr the radius of the circle : "))
# print("area of the circle with radius " + str(r)+ "is :"+ str(pi*r**2))


# fname =input("enter the first name :")
# lname=input(" Enter the last name ")
# print("hello" +" "+ lname + " "+ fname)

# num=35723
# print(list(str(num)))
# print(tuple(str(num)))

# exte="abc.java"
# s_exte=exte.split(".")
# print(s_exte[-1])

# color_list = ["Red","Green","White" ,"Black"]
# print(color_list[0],color_list[-1])

# edate=(11,12,2014)
# print("the examination start from : %i/%i/%i"%edate)

# a=int(input("Enter the integer : "))
# n1=int("%s"%a)
# n2=int("%s%s"%(a,a))
# n3=int("%s%s%s"%(a,a,a))
# print(n1+n2+n3)

# print(abs.__doc__)

# import calendar
# y=2023
# m=4
# print(calendar.month(y,m))

# from datetime import date
# sdate=date(2014,7,2)
# sdate2=date(2014,7,11)
# delta=sdate2-sdate
# print(delta.days)    #output 9 days between those days

# from math import pi
# r=int(input("radius of the sphere : "))
# print("Volume odf the sphere is " +str(4/3) + str(pi*r**3))



# def difference(n):
#     if n <= 17:
#         return 17 -n
#     else:
#         return(n-17)*2

# print(difference(23))
# print(difference(14))

# def near_thousand(df):
#     return ((abs(1000-df)<= 100) or (abs(2000-df) <=100))
# print(near_thousand(900))




# def sum(n,n1,n2):
#     sum = n+n1+n2
#     if n == n1 == n2:
#         sum = sum *3
#     return sum
    

# print(sum(1,2,3))
# print(sum(2,2,2))
# n= "#"

# while i >  0:
#     print(i * n)
#     i-=1

# for i in n:
#     num=1
#     num=num*i
#     print(num)   

# def newly(df):
    
#     if len(df)>=2 and df[0:2]== "Is":
#         return df
    
#     return "Is" + df
# print(newly("this pooja"))


# def large(df,n):
#     result=""
#     for i in range(n):
#         result=result+ df
#     return result
    
# print(large("pooja",2))

# user=int(input("User input number: "))
# def oddeven(df):
#     if df%2 == 0:
#         return "this number is even"
#     else: 
#         return  "df is odd"
# print(oddeven(user))

# alist=[1,2,3,4,4,4,4,6,2,4]
# print(alist.count(4))

# def countnum(df):
#     count=0
#     for i in df:
#         if i==4:
#             count=count + 1
#     return count
# print(countnum(alist))


# def stringcount(df,n):
#     flen=2
#     if flen > len(df):
#         flen=len(df)
#         substr= df[:flen]
#         result=""
#         for i in range(n):
#             result=df + substr
#         return result
# print(stringcount("p",2))
# print(stringcount("pooja",3))

# def vowels(df):
#     vow='aeiou'
#     return df in vow
# print(vowels("o"))

# def contain(df,n):
#     for i in df:
#         if n==i:
#             return True
#     return False

# print(contain([1,2,3,4,5,6,],3)) 
# A=[1,2,3,4,5,6,]
# def concat(df):
#     result=''
#     for i in df:
#         result=result+ str(i)
#     return result
# print(concat(A))

# def histogram(df):
#     for i in df:
#         output=''
#         times= i
#         while (times > 0):
#             output+='*'
#             times=times - 1
#         print( output)
# histogram([2,4,5,7])


# base=int(input("Enter the base of the triangle : "))
# height=int(input("Enter the height of tyhe triangle : "))
# def area(b,h):
#     area=b*h/2
#     return area
# print(area(10,20))

# def gcd(x,y):
#     gcd=1
#     if x % y == 0:
#         return y
#     for k in range(int(y/2),0,-1):
#         if x % k == 0 and y % k == 0:
#             gcd=k
#             break
#     return gcd
# print(gcd(20,345))


# '''dictionary'''
# a={"id": 111,
#    "name":"pooja",
#    "lname": "nikam",
#    "occupation": "software engineer"}
# # print(a.items())
# # print(a.keys())
# a["lname"]='nikam arun'
# # a['newkey']='arun nikam'
# print(a)


# def vowels(df):
#     vows=list("aeiouAEIOU")
#     for i in vows:
#      if i in vowels: 
#         print(vows)  
# #      return vows
# # print(vowels("Automation Testing"))
        

# def Add(pooja):
#    alist=0
#    for i in pooja:
#       alist=alist+i
#    print (alist)
# A=[34,56,78]
# Add(A)   #result = 168


# string = "welcome to python programming"
# sub_str = "to"

# # print(string.find(sub_str))

# if(string.find(sub_str)==-1):
#    print("not fount")
# else:
#    print("found") 


# import turtle
# import time
# pen = turtle.Turtle()
# def pooja():
#     for i in range(200):
#         pen.right(1)
#         pen.forward(1)
# def heart():
#     pen.fillcolor('red')
#     pen.begin_fill()
#     pen.left(140)
#     pen.forward(113)
#     pooja()
#     pen.left(120)
#     pooja()
#     pen.forward(112)
#     pen.end_fill()
#     time.sleep(10)
# def text1():
#     pen.up()
#     pen.setpos(-68, 95)
#     pen.down()
#     pen.color('yellow')
#     pen.write(" I LOVE YOU , MY LOVE")
#     time.sleep(10)

# # heart()
# # text1()
# # pen.ht()

# numbers = [    
#     386, 462, 47, 418, 907, 344, 236, 375, 823, 566, 597, 978, 328, 615, 953, 345, 
#     399, 162, 758, 219, 918, 237, 412, 566, 826, 248, 866, 950, 626, 949, 687, 217, 
#     815, 67, 104, 58, 512, 24, 892, 894, 767, 553, 81, 379, 843, 831, 445, 742, 717, 
#     958,743, 527
#     ]
# for i in numbers:
#     if i == 237:
#         print(i)
#         break
#     elif i%2 == 0:
        
#         print(i)

# def lcm(x,y):
#     if x > y:
#         z = x
#     else :
#         z=y
#     while (True):
#         if (z % x == 0) and (z% y == 0):
#             lcm = z
#             break
#         z+=1
#     return lcm
# print(lcm(25,35))

'''33. Write a Python program to sum three given integers. However, if two values are equal, the sum will be zero.'''
# def sum(x,y,z):
#     if x == y or y == z or z== x:
#         return 0
#     else:
#         sum = x+ y+ z
#     return sum
# print(sum(1,2,5))

'''34. Write a Python program to sum two given integers. However, if the sum is between 15 and 20 it will return 20'''

# def sum(x,y):
#     sum = x +y
#     if 15 < sum > 20:
#         return 20
#     else:
#         return sum

# print(sum(8,6)) 
'''OR'''
# def sum(x,y):
#     sum= x + y
#     if sum in range(15,20):
#         return 20
#     else:
#         return sum
# print(sum(6,10))

'''35. Write a Python program that returns true if the two given integer values are equal or their sum or difference is 5.'''
# def sum(x,y):
#     if (x + y)== 5 or (x - y) == 5 or (x==y):
#         return True
#     else:
#         return False
# print(sum(10,5))
# print(sum(13,3))

'''36. Write a Python program to add two objects if both objects are integers'''
# def personaldetail():
#     name,age="pooja",19
#     adress="Nandgaon"
#     print("Name  {}\nAge {}\nAdress {}".format(name,age,adress) )
# personaldetail()

'''38. Write a Python program to solve (x + y) * (x + y).
Test Data : x = 4, y = 3
Expected Output : (4 + 3) ^ 2) = 49'''


# write a python program for remainder?

x=20
y=3
z=x%y
w=x//y
print(z)
print(w)








            


















