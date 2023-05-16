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



# num=int(input("Enter the number "))
# f=0 
# i=2
# while i <= (num/2):
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


# def fabinacciu(df):
#     if df < 0: 
#         print("invalid suntax")
#     elif df == 0 :
#         return 0
        
#     elif df == 1 or df ==2:
#         return 1
#     else:
#         return fabinacciu(df-1)+ fabinacciu(df-2)
    
# num =5
# print(fabinacciu(num))

'''5. How to find the sum of elements in an array?'''
# arr=[12,13,14,15]
# sum=0
# for i in arr:
#     sum=sum + i
#     print(sum)

'''How to find maximum and minimum elements in an array'''
# alist=[12,24,67,1,23]
# print(min(alist))
# print(max(alist))

'''7. How to find the length of the list?'''
# alist=[12,24,67,1,23]
# print(len(alist))/

'''8. How to swap first and last elements in the list'''
alist=[1,2,3,4,56,7]
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
# alist=['pooja','Nikam','arun']
# w='pooja'
# N=0

# def RemoveIthWord(lst, word, N):
#     newList = []
#     count = 0
 
#     # iterate the elements
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
alist=[1,2,3,4,56,2,2,3,67,34,56,33,3,3,3]
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

# def polidrome(df):
#     for i in df:
#         if df[0] == df[::-1]:
#             print("given string is polidrome")
#         else:
#             print("The given string is not polidrome")
#     return df
# strp='abcdbca'
# print(polidrome(strp))

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
A="the python developer&*^%$ name is pooja arun nikam"
def spchar(df):
    char="!@#$%^&*()_+?><"
    df.split()
    c=0
    for i in range(len(df)):
        if df[i] in char:
            c+=1

    if c:
        return "sp char present"
    else:
        return "sp char not present"
    
print(spchar(A))


        
        







        
 









         

 


    












# 6. How to find maximum and minimum elements in an array?
#  16. Find the sum of the elements in list
