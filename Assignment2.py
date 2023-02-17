# swap two numbers

# a=10
# b=30

## write a program here to swap values inside variables
# 1. using max one third variable 
# 2. Without any third variable
# 3. take input from user and do same

# 1.
a=10
b=30
print(f"value of a before sort : {a} , value of b before sort : {b}")

#lets create tenp variable 

temp= a        # temp=a : a=10 and b-30
a=b            # a=30   and  b=10
b=temp
print(f"value of a after sorting : {a}, value of b after sorting : {b}")


#2.

a=a+b         # a=10+30=40     here a=40
print(f"value of a {a} and value of b {b}")
b=a-b           # b=a-b  40-30=10     i.e  b=10
print(f"value of a {a} and value of b {b}")
a=a-b
print(f"swaped value of a {a} and swaped value of b {b}")


3.
print("welcome to swapping the two numbers")
a=int(input("Enter the   1st number to swap : "))
b=int(input("Enter the 2nd number to swap :  "))

# a=a*b
# b=a/b
# a=a/b
# print(f"swap value of a : {a} and swap value od b : {b}")


#4

# swap number without calculations

a=int(input("Enter the 1st number : "))
b=int(input("Enter the  2nd number ;  "))
a,b = b,a 
print(f"swap the number a : {a} and swap the number b :{b}")

