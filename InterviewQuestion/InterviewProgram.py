#Write a program to swap two number
'''
a=12
b=14

temp=a
a=b
b=temp
print(a)
print(b)

a,b=b,a
print(a)
print(b)
'''


# how to check the number is  prime or not?
'''
num=int(input(" User number "))

if num >1:
    for i in range(2,int(num/2)+1):
        if num % i == 0:
            print(num,"not prime")
            break
    else:
        print(num,"is prime")

else:
    print(num,"the number is prime number")'''

# num=int(input("Enter any number : "))

# if num > 1:
#     for i in range(2,int(num/2)+1):
#         if num %2==0:
#             print(num,"not prime")
#             break
#     else:
#         print(num,"prime number")



# n=int(input("Enter number: "))
# for i in range(2,n):
#     if n%i==0:
#         print("not prime number")
#         break
#     else:
#         print("prime number")

   

# num=int(input("Enter the number "))
# f=0 
# i=2
# while i <= num:
#     if num % i==0:
#         f=1
#         break
#     i=i+1
# if f == 0:
#     print("Entered number is prime")
# else:
#     print("Enterd number is not prime")
   
#3. How to find factorial of a number ?



# def factorial(df):
#     if df < 0:
#         return 0
#     elif df==0 or df==1:
#         return 1
#     else:
#         fact=1
#         while (df>1):
#             fact *=df
#             df -=1
#         return fact
# print("Factorial of",num,"is",factorial(num))


# def factors(df):
#     n=1
#     for i in range(2,df+1):
#         n*=i
#     return n
# num=5
# print(factors(num))


# # 4. Print Fibonacci series.

# def fibonacci(df):
#     if df < 0:
#         print("Invalid syntex")
#     elif df == 0:
#         return 0
#     elif df == 1 or df == 2:
#         return 1
#     else:
#         return fibonacci(df-1) + fibonacci(df-2)
    
# num = 3
# print(fibonacci(num))



'''5. How to find the sum of elements in an array?'''
# arr=[12,13,14,15]
# sum=0
# for i in arr:
#     sum=sum + i
# print(sum)



'''How to find maximum and minimum elements in an array'''
# alist=[12,24,67,1,23,0,111]
# maxi=alist[0]
# mini=alist[0]
# for i in range(len(alist)):
#     if alist[i] < mini:
#         mini=alist[i]
#     if alist[i]>maxi:
#         maxi=alist[i]
# print(maxi)
# print(mini)




'''7. How to find the length of the list?'''
# alist=[12,24,67,1,23]
# print(len(alist))/

'''8. How to swap first and last elements in the list'''
# alist=[34,56,78,1,2,3,4,56,7]
# size=len(alist)
# temp=alist[0]
# alist[0]=alist[size - 1]
# alist[size - 1]= temp
# print(alist)

'''How to swap any two elements in the list?'''
# def swap(df,p1,p2):
#     df[p1],df[p2]=df[p2],df[p1]
 #     return df
# print(swap(alist,0,4))

'''10. How to remove the Nth occurrence of a given word list'''
# alist=['pooja','Nikam','arun','alpana','pooja','alpana']
# w='pooja'
# N=0
# def RemoveIthWord(lst, word, N):
#     newList = []
#     count = 0
 #    # iterate the elements
#     for i in lst:
#         if(i == word):
#             count = count + 1
#             if(count != N):
#                 newList.append(i)
#         else:
#             newList.append(i)
 #     lst = newList
 #     if count == 0:
#         print("Item not found")
#     else:
#         print("Updated list is: ", lst)
 #     return newList
# print(RemoveIthWord(alist,w,N))



'''11. How to search an element in the list?'''

# alist=[1,2,3,4,56]
# print(alist.index(2))

'''
12. How to clear the list?
'''
# alist=[1,2,3,4,56]
# print(alist.clear())
# print(alist)

'''13. How to reverse a list?'''
# print(alist.reverse())
# print(alist)

'''14. How to clone or copy a list?
'''
# newlist=alist.copy()
# print(alist)
# print(newlist)

'''15. How to count occurrences of an element in a list?'''
# alist=[1,2,3,4,56,2,2,3,67,34,56,33,3,3,3]
# print(alist.count(3))

''' 16. Find the sum of the elements in list'''
# def sum(df):
#     n=0
#     for i in df:
#         n=n+i
#     return n
# print(sum(alist))

'''17. How to multiply all the numbers in the list? '''
# def multiply(df):
#     n=1
#     for i in df:
#         n=n*i
#     return n
# print(multiply(alist))

'''18. How to find the smallest and largest numbers on the list?'''
# alist1=[1,2,3,4,5,6,67]
# def largenum(df):
#     max= df[0]
#     for i in df:
#         if i > max:
#             max = i
#     return max
# print(largenum(alist1))
# def smallnum(df):
#     min=df[0]
#     for i in df:
#         if i < min:
#             min=i
#     return min
# print(smallnum(alist1))

'''19. How to find the second largest number in a list?'''

# alist=[12,13,24,13,56,78,99,100,222,1111]
# alist.sort()
# print("second largest number",alist[-2])

'''20. How to check string is palindrome or not?'''
# astr="madam"
# reverse=astr[::-1]
# if (astr == reverse):
#     print('yes it is pollindrome')
# else:
#     print('no its not pallindrome') 

'''21. How to reverse words in a string?'''
# a="pooja"
# print(a[::-1])

'''23. How to find the length of a string?'''
# a="pooja"
# print(len(a))

'''22. How to find a substring in a string?'''
# A="the python developer name is pooja arun nikam"
# print(A.find('python'))
    
'''24. How to check if the string contains any special character?'''
# A="the python developer&*^%$ name is pooja arun nikam"
# def spchar(df):
#     char="!@#$%^&*()_+?><"
#     df.split()
#     c=0
#     for i in range(len(df)):
#         if df[i] in char:
#             c+=1

#     if c:
#         return "sp char present"
#     else:
#         return "sp char not present"
    
# print(spchar(A))   
# 

# a=astr.split()
# newlist=[]
# for i in a:
#     a=i[::-1]
#     newlist.append(a)
#     newlist1=" ".join(newlist)
# print(newlist1)


# w=astr.split(" ")
# new_word=[i[::-1] for i in w]
# new_str=" ".join(new_word)

# print(new_str)

# astr="my name is pooja nikam"
# words=astr.split()
# newlist=[]
# for i in words:
#     new=i[::-1]
#     newlist.append(new)
#     newstr=" ".join(newlist)
# print(newstr)

# num=5
# for i in range(0,num):
#     for j in range(0,i+1):
#         print("*",end='')
#     print()



# Longest common prefix srings among array of string
# astr=["flower","flow","flight"]

# def longest(n):
#     if not str: return ""
#     for i in range(len(n[0])):
#         char=n[0][i]
#         for j in range(1,len(n)):
#             if i == len(n[j]) or n[j][i] !=char:
#                 return n[:i]
#     return n[i]
# print(longest(astr))
                 

 
# c5re8de1n9c7e
# 1. find the duplicate char and its count from string ?
# /2. find the count of digits in a string
# 3. Make addition of digits from this string
# astr="c5re8de1n9c7e"
# li=[]
# for i in astr:
#     if astr.count(i) > 1:
#         li.append(i)
#         lists=" ".join(li)
# print(lists)

# '''2'''
# result=[int(i) for i in astr if i.isdigit()]
# print(len(result))


# '''3'''
# sum=0
# for i in result:
#     sum=sum + i
# print(sum)


# def pollindrome(df):
#     if df== df[::-1]:
#         print("given string is pollindron")
#     else:
#         print("string is not pollindrom")
#     if df[:int(len(df)/2)] ==df[int(len(df)/2):]:
#         print("given string is symmentric")
#     else:
#         print("given string not symmnetric")
# pollindrome("madam")
# pollindrome("khokho")
        

# def polindrom(df):
#     half=int(len(df)/2)
#     astr=df[half:]
#     astr1=df[:half]
#     if astr == astr1:
#         print("given string are symmentric")
#     else:
#         print("given string are not symmnetric")
#     if df == df[::-1]:
#         print("string are pollindrom")
#     else:
#         print("string not pollindrom")
# polindrom("amaama")


'''Find out of the space between the string'''

# a=[1,2,3]
# b=[1,2,3]
# print(a==b)
# print(a is b)


# calulate the leap year

# year=int(input("Enter the year : "))
# if (year % 400 ==0 ) and (year % 100 == 0):
#     print("the year is leap year")
# elif (year %  4 ==0) and (year % 100 !=0):
#     print("the year is leap year ")
# else:
#     print("year is not leap year")


# factorization 

# n=int(input("Enter the factorial number : "))
# if n < 0:
#     print("Invalid")
# elif  n ==1 :
#     print(1)
# else:
#     fact=1
#     for i in range(1,n+1):
#         fact=fact*i
#     print(fact)

# how to arrange sring using for loop (In a sorted way)
# string manipulation

# lets use memorization technique use to stored and reuse the value to optimizes recursion method
# def factorial(n, memo={}):
#     if n in memo:
#         return memo[n]
#     if n == 0:
#         return 1
#     else:
#         result = n * factorial(n - 1, memo)
#         memo[n] = result
#         return result

# memo={}
# def fact(n):
   
#     if n == 0:
#         return 1
#     if n in memo:
#         return memo[0]
#     memo[n]=n*fact(n-1)
#     return memo[n]
# print(fact(6))
# print(memo)

# 
# a="Vipul"  # Revesrse string
# b=""
# for i in a:
#     b=i+b
# print(b)



# import numpy as np
# a=np.zeros((5,5))
# print(a)

# import pandas as pd
# df=pd.DataFrame()
# names=["pooja","Arun","Nikam"]
# occu=["Software deve","Teacher"," "]
# df["names"]=names
# df["occu"]=occu
# print(df)


# astr=["Pooja"," Arun"," Nikam"]
# # print(astr.index("a"))

# print(sorted(astr))



# a=5
# def my_f():
#     global a
#     a=3
# my_f()  # nothing



# memo={}
# def fact(n):
#     if  n == 0:
#         return 1
#     if n in memo:
#         return memo[n]
#     memo[n]=n*fact(n-1)
#     return memo[n]
# print(fact(10))


# def factorial(n):
#     if n == 0:
#         return 1
#     fact=1
#     for i in range(1,n+1):
#         fact *=i
#     return fact
# print(factorial(6))



# def outer():
#     x=10
#     def inner():
#         nonlocal x
#         x+=1
#         return x
#     return inner()
# print(outer())


         
# z=set("abc")
# z.add("san")
# z.update(set(["p","q"]))
# print(z)

# for i in [1,2,3,4][::-1]:
#     print(i,end=" ")
# def con():
#     return bool("False")
# print(con())

# even odd
# n=5
# print("Evan" if n % 2 == 0 else "odd" )



# patturn problem

# for i in range(1,11):
#     for j in range(1,i+1):
#         print("*",end=" ")
#     print()

# reverse the list


# reversee a list
# alist=[1,2,3,4,5,6,7,8,9,22,33]
# rev=[]
# for i in alist:
#     rev.insert(0,i)
# print(rev)

# rev=[alist[i] for i in range(len(alist)-1,-1,-1)]
# print(rev)


# date = (11, 12, 2014)
# print("%i/%i/%i"%date)


# n=int(input("Enter any number : "))
# n1=int("%s"%n)
# n2=int("%s%s"%(n,n))
# n3=int("%s%s%s"%(n,n,n))
# result=n1+n2+n3
# print(result)


# import calendar

# date=calendar.calendar(1996)
# print(date)


# astr='''a string that you "don't" have to escape
# This
# is a ....... multi-line'''

# from datetime import date
# d1=date(2014, 7, 2) 
# d2=date(2014, 7, 11)
# res=d1-d2
# print(res)


'''convert the string into uppercase'''
# astr="pooja"
# result=astr.casefold()
# print(result)


# my_string_1 = "THIS IS CONVERT INTO LOWER CASE"
# print(my_string_1.lower())

# text = "Straße"
# print(text.lower())

# x=ord("z")
# y=ord("Z")
# print(x-y)

# def uppercase(s):
#     result=""
#     for i in s:
#         if 'a'<=i<='z':
#             result+=chr(ord(i)-32)
#         else:
#             result+=i
#     return result
# print(uppercase("AshutoshTiwsari1"))


# def lowercase(s):
#     result=""
#     for i in s:
#         if 'A'<=i<='Z':
#             result+=chr(ord(i)+32)
#         else:
#             result+=i
#     return result
# print(lowercase('POOJA'))



'''first non repeatative charector in the string'''
# astr="Pooja"
# adict={i:astr.count(i) for i in astr}
# print(adict)


# def first(s):
#     adict={}
#     for i in s:
#         if i in adict:
#             adict[i]+=1
#         else:
#             adict[i]=1
#     for i in range(len(s)):
#         if adict[s[i]]==1:
#             return i
#     return -1
# print(first("ashutosh tiwari"))



'''pallindrom'''

# def pallindrom(s):
#     i=0
#     j=len(s)-1

#     while i < j:
#         if s[i]!=s[j]:
#             return False
#         i+=1
#         j-=1
#     return True
# print(pallindrom("12321"))


'''frequency of occurance of char in string'''

astr="Hello"

# adict={i:astr.count(i) for i in astr if astr.count(i)>1}
# print(adict)

# def freq(s):
#     adict={}
#     for i in s:
#         if i in adict:
#             adict[i]+=1
#         else:
#             adict[i]=1
#     max_char=""
#     max_count=0
#     for char,count in adict.items():
#         if count > max_count:
#             max_char=char
#             max_count=count
#     return max_char,max_count
# print(freq("python interpretour"))


'''find the longest word in string'''
# astr="Hello, I am python programmer"

# def long_str(s):
#     astr=s.split()
#     max_length=0
#     for i in astr:
#         if len(i) > max_length:
#             max_length=len(i)
#             max_length+=1
#     return max_length,i
# print(long_str(astr))




# from collections import Counter
# alist=["1","2","A","B","A","1"]

# print(Counter(alist))



'''Check that a string contains only a certain set of characters'''
# import re
# strings = """Hello my Number is 12345.6789 and
#             my friend's number is 987654.321"""

# result=re.findall("\d+",strings)
# print(result)


# find the common letters in two string

# astr="pooja"
# astr1='poonam'

# a=set(astr)
# b=set(astr1)
# res=a&b
# print(res)


# count the number of words present in the sentence


# astr1='Pooja is the software developer in the microsoft and reena also the software dveloper in the microsoft'

# astr=astr1.split()
# adict={i:astr.count(i) for i in astr}
# print(adict)



# converting two lists into dict?
# l1=["pooja","Reena","Alpana","Diksha"]
# l2=[988767,575673,978334,334556]

# res=dict(zip(l1,l2))
# print(res)

# Find the missing number in an list?

# alist=[1,2,4,5,6,7,8,10]

# for i in range(1,11):
#     if i not in alist:
#         print(i,end=" ")


# find out the pair with given sum of value?
# sum=17

# alist=[5,7,4,3,9,8,19,21]

# def dig_sum(df,n):
#     df.sort()
#     left=0
#     right=len(df)-1
#     while (left <= right):
#         if (df[left]+df[right] > n):
#             right=right - 1

#         elif (df[left]+df[right] < n):
#             left=left +1
        
#         elif (df[left]+df[right]==n):
#             print("Value of psir are",df[left],"&",df[right])
#             right=right-1
#             left=left + 1
# dig_sum(alist,30)

# def dig_sum(df,n):
#     df.sort()
#     left=0
#     right=len(df)-1
#     while (left<=right):
#         if (df[left]+df[right]>n):
#             right=right - 1
#         elif (df[left]+df[right]<n):
#             left=left + 1
#         elif  (df[left]+df[right]==n):
#             print("Value of pair are ",df[left],"&",df[right])
#             right=right-1
#             left=left + 1

    
# dig_sum(alist,sum)




# class Node:
#     def __init__(self,key):
#         self.key=key
#         self.left=None
#         self.right=None

# def height_tree(A):
#     if (A == None):
#         return 0
#     else:
#         ldepth=height_tree(A.left)
#         rdepth=height_tree(A.right)

#         if  (ldepth > rdepth):
#             return (1+ldepth)
#         else:
#             return (1+rdepth)
        
# root=Node(1)
# root.left=Node(2)
# root.right=Node(3)
# root.left.left=Node(4)
# root.left.left.right=Node(5)
# root.left.left.left=Node(7)
# root.right.right=Node(6)


# print(height_tree(root))
        

# class Node:
#     def __init__(self,key):
#         self.key=key
#         self.left=None
#         self.right=None
# def height_tree(A):
#     if (A ==None):
#         return 0
#     else:
#         ldepth=height_tree(A.left)
#         rdepth=height_tree(A.right)
#         if (ldepth > rdepth):
#             return (1+ldepth)
#         else:
#             return (1+rdepth)

# root=Node(1)
# root.left=Node(2)
# root.right=Node(3)
# root.left.left=Node(4)
# root.left.right=Node(5)
# root.left.left.left=Node(7)
# root.left.left.left.left=Node(8)
# root.right.right=Node(6)
# print(height_tree(root))



# Ineverse pattern
# n=10
# for i in range(n):
#     for j in range(i,n):
#         print("*",end=" ")
#     for j in range(n,i):
#         print(" ",end=" ")
#     print()


#  pyramid pattern

# n=10
# for i in range(n):
#     for j in range(i,n):
#         print(" ",end=" ")
#     for j in range(i+1):
#         print("*",end=" ")
#     for j in range(i+1):
#         print("*",end=" ")
#     print()


# Reverse pattern

# n=5
# for i in range(n):
#     for j in range(i,n):
#         print(" ",end=" ")
#     for j in range(i):
#         print("*",end=" ")
#     for j in range(i+1):
#         print("*",end=" ")
#     print()


# n=5
# for i in range(n):
#     for j in range(i+1):
#         print(" ",end=" ")
#     for j in range(i,n-1):
#         print("*",end=" ")
#     for j in range(i,n):
#         print("*",end=" ")
#     print()

    
# l1=[1,2]
# l2=[3,4]
# l3=[5,6]

# result=[l1,l2,l3] 
# print(result)



# astr=["My","name","is","Pooja"]
# nstr="".join(astr)
# print(nstr)
# nlist=[]
# for i in nstr:
#     if nstr.count(i)>1:
#         nlist.append(i)
# print(nlist)



'''nested list'''
# alist=[[1,2],[3,4],[3,5],[5,6]]
# alist=[i for sublist in alist for i in sublist]
# print(list(set(alist)))

# student = [[77.7, 'ggg'], [88.8, 'uu'], [99, 'aa']]
# nlist=[[name,marks] for marks,name in student]
# nlist.sort()
# print(nlist)


# data = [[1, 2], [3, 4], [5, 6]]
# nlist= [i for sublist in data for i in sublist]

# for i in data:
#     for j in i:
#         print(j,end=" ")



# nested = [[7, 8], [9, 10], [11, 12]]
# nlist=[i for sublist in nested for i in sublist]
# print(nlist)



# numbers = [[1, 2], [3, 4], [5, 6]]
# Output: [[2, 1], [4, 3], [6, 5]]

# nlist=[i[::-1] for i in numbers]
# print(nlist)

# nums = [[10, 20], [30, 40], [50]]

# sum=0
# nlist=[i for sublist in nums for i in sublist]
# for i in nlist:
#     sum=sum+i
# print(sum)


# people = [['Alice', 24], ['Bob', 27], ['Charlie', 22]]

# nlist=[i[1] for i in people   ]
# print(nlist)

# records = [['a', 10], ['b', 30], ['c', 45]]
# # utput: [['b', 30], ['c', 45]]
# nlist=[i for i in records if i[1]>25]
# print(nlist)


# student_scores = [[60, 'Amy'], [90, 'John'], [75, 'Zara']]
# Output: [[60, 'Amy'], [75, 'Zara'], [90, 'John']]

# nlist=[[age,name] for age,name in student_scores ]
# nlist.sort()
# print(nlist)

# data = [['name', 'Alice'], ['age', 25], ['country', 'India']]
# Output: {'name': 'Alice', 'age': 25, 'country': 'India'}
# ndict={i:j for i,j in data }
# print(ndict)


# numbers = [[1, 2], [3, 4], [5, 6]]

# nlist=[i[::-1] for i in numbers[::-1]]
# print(nlist)
















 
        



         

 


    













