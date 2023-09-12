#1. Write a Python program to sum all the items in a list

# alist=[12,13,14,15,16,60]
# def Sum_list(items):
#     n=0
#     for x in items:
#         n=n+x
#     return n
# print(Sum_list(alist))

'''Practice'''
# def addition(df):
#     n=0
#     for i in df:
#         n=n+i
#     return n
# print(addition(alist))

#==========================================================================================================================
'''2. Write a Python program to multiply all the items in a list'''

# def multiply(df):
#     n=1
#     for x in df:
#         n=n*x
#     return n
# print(multiply(alist))

'''Practice'''
# def multiple(df):
#     n=1
#     for i in df:
#         n=n*i
#     return n
# print(multiple(alist))


# def divisible(df):
#     n=1
#     for i in df:
#         n=n/i
#     return n
# print(divisible(alist))


#=============================================================================================================================
'''3. Write a Python program to get the largest number from a list'''

# def largeNum(df):
#      max = df[ 0 ]
#      for i in df:
#           if  i > max :
#                max = i 
#      return max
# print(largeNum(alist)) 


'''Practice'''

# def largenum(df):
#     max=df[0]
#     for i in df:
#         if i > max:
#             max=i
#     return max
# print(largenum(alist))


#==============================================================================================================================

'''4. Write a Python program to get the smallest number from a list'''

# def SmallNum(df):
#     min=df[0]
#     for i in df:
#         if i <min :
#             min=i
#     return min
# print(SmallNum(alist))

'''Practice'''

# def smallnum(df):
#     min=df[0]
#     for i in df:
#         if i < min:
#             min=i
#     return min
# print(smallnum(alist))

 #================================================================================================================================= 

'''5. Write a Python program to count the number of strings from a given list of strings.
 The string length is 2 or more and the first and last characters are the same'''

# def CountNum(df):
#     w=0
#     for astr in df:
#         if len(astr) > 1 and astr[0]==astr[-1]:
#             w+=1
#     return w
# print(CountNum(["pooja","abc","xyz","aba","1221"]))

'''practice'''
# alist=['abc', 'xyz', 'aba', '1221','Jungkookj']
# def countstr(df):
#     str=0
#     for i in df:
#         if len(i) > 1 and i[0]==i[-1]:
#             str+=1
#     return str
# print(countstr(alist))


#===================================================================================================================================

'''6. Write a Python program to get a list, 
sorted in increasing order by the last element in each tuple from a given list of non-empty tuples'''
#listNum = [(10, 3), (8, 2),(99, 44), (24, 88), (11, 1)]


# result=listNum.sort(key= lambda i:i[1], reverse=True)
# print(listNum)       # [(24, 88), (99, 44), (10, 3), (8, 2), (11, 1)]
# print(result)        # resulte show None because its changed inside the list thats why show None after exicution

# result=listNum.sort(key=lambda i:i[-1],reverse=True)
# print(listNum)
# print(result)

# result=listNum.sort(key= lambda i:i[-1],reverse=True)
# print(result)


#=====================================================================================================================================

'''7. Write a Python program to remove duplicates from a list'''
# alist=[12,13,14,15,12,16,60]
# duplicate=set()
# unique=[]
# for i in alist:
#     if i not in duplicate:
#         duplicate.add(i)
#         unique.append(i)
# print(duplicate)

# duplicate=set()
# uniq_item=[]
# for i in alist:
#     if i not in duplicate:
#         uniq_item.append(i)
#         duplicate.add(i)
# print(duplicate)


#====================================================================================================================
'''8. Write a Python program to check if a list is empty or not.'''
# alist=[1]
# if not alist:
#     print("list is empty")
# else:
#     print("list is not empty")
#======================================================================================================================
'''9. Write a Python program to clone or copy a list'''
 
# alist=[1,2,3,4,5]
# blist=alist.copy()
# print(alist)
# print(blist)
# new_list=list(alist)
# print(new_list)
#====================================================================================================================

'''10. Write a Python program to find the list of words that are longer than n from a given list of words'''
# alist=['Pooja','Arun','Nikam','Shivan',"diksha"]

# for i in alist:
#     if len(i) < len(alist):

import Add
A=[23,10]
add(A)

        


