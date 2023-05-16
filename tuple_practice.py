'''
Q.1  Write a program to create tuple  in user input
a=input("Enter the number : ")
print(f"tuple containing  item {tuple(a)}")  # its take one as string item in the tuple

Q.2. Write a Python program to create a tuple with different data type
X=("tuple",11,12.1,True)
print(X)

#3. Write a Python program to create a tuple of numbers and print one item.
a=input("Enter the number : ")
print(f"Print the tuple number {tuple(a)} , first position in tuple : {tuple(a[0])}") #Print the tuple number ('1', '2', '3', '4', '5', '6', '7', '8', '9', '1', '0') , first position in tuple : ('1',)

4. Write a Python program to unpack a tuple into several variables
a=(1,2,3,4,5,6,7,8,5,9)
print(*(a))

# anather way is 

Tuplex=1,2,3
print(Tuplex)
t1,t2,t3=Tuplex
print(t1+t2+t3)

5. Write a Python program to add an item to a tuple  #tuple is immutable so

tuplex=(1,2,3,4,5,6,7,8)
print(tuplex)
tuplex=tuplex + (9,)     # tuple can be concatinated in the tuple
print(tuplex)   
# add item in specific number
tuplex= tuplex[:]+(15,4,20)+ tuplex[:]
print(tuplex) 
# converting tuple to list
listx= list(tuplex)
listx.append(30)
print(listx)
'''
# Q.6 Write a Python program to convert a tuple to a string.
a=("p","o","o","j","a")
str="".join(a)
print(str)

'''

# 7. Write a Python program to get the 4th element from the last element of a tuple
# a=(1,2,3,4,5,6,7,8,9)
# print(a[3])  # It gives 4rth place element in tuple a


# 8. Write a Python program to create the colon of a tuple. 
from copy import deepcopy
tuplex=("pooja",12,[],True)  # list in tuple item
print(tuplex)   
# Make a copy of tuplex by using deepcopy
tupley=deepcopy(tuplex)
tupley[2].append(111)   # We just add integer in the list at the end tuple are immutable
print(tupley)
print(tuplex)

'''

#9. Write a Python program to find repeated items in a tuple
# a=(1,2,2,3,4,5,6,7,7)
# print(len(a))
# # a=a.count(7)
# # print(a)
# for i in len(a):
    




































