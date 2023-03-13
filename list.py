# []
# ()
# {}

a=['red','green','blue','white','black']
# print(len(a))


'''
list indexing
print(a[0])  # red
print(a[1])   # green
print(a[5])   # list index out of range

print(a[2:])  #   ['blue', 'white', 'black']
print(a[1:3])   # ['green', 'blue']
print(a[-3:])    # ['blue', 'white', 'black']

'''


## Assignment : do all operations you performed for string 

# in the list can asign value 
# that means list is mutable=we can change the value in list so for that lets see forward 

colors=['red','green','blue','white','black']
# newitem= 'coral'
# colors[3]=newitem
# print(colors)
# colors[5]='yellow'    # if list is out off range we cant assign the new item in its
# print(colors)
# colors[4]='yellow'
# print(colors)

print(colors[:-1])   #['red', 'green', 'blue', 'white']
print(colors[-1::])  #  ['black]
print(colors[-1:])
