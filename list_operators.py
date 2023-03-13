#    list operators


# list can indexed like a string 
# list is mutable
# list index have fix index we can add extra number in list we just change the list item in the list


#list indexing
alist=["red","green","yellow","blue","white"]
# print(alist[0:2])
# print(alist[1:3])
# print(len(alist))
 
# sort the index
# result=alist.sort()   # list will be sort out by its order a to z
# print(f"the a list before sort : {alist}")
# print(f"list after a sorting : {result}")


# avalue=[33,45,66,34,57,98,80,20]
#print(avalue[0::2]) #it will take 1 in increament
# result=avalue.sort(reverse=True)  # we can sort the value by ascending and discending order
# print(result)

#============ reverse list ============================

avalue=[33,45,66,34,57,98,80,20]
result= avalue.reverse()
print(f"list before reverse {avalue} , list after reverse {result}")


#==============insert list ==================================
# insert the list element in the list

avalue=[33,45,66,34,57,98,80,20]
result=avalue.insert(2,67)    # here we insert the element 67 in 2nd position
print(result)

# ============ pop list element ===============================
# it will pop means it will take element from the list
# 
avalue=[33,45,66,34,57,98,80,20] 
result=avalue.pop(5)     #it will take out the element from the list
# result= avlue.pop()     # if the value not given it will take last element by default
print(result)

# =========== Remove ==================================
avalue=[33,45,66,34,57,98,80,20]
result=avalue.remove(100) # error if element is not present in the list
print(result)

# =====================================================
values = [10, 45,2,20, 90,66,88, 'fds', True]
values.sort()   # sort not work here
print(values.sort())






