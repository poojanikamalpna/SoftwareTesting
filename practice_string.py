# Question on string

#1. Write a Python program to calculate the length of a string.

# avalue="Pooja"
# print(len(avalue))

# #2. Write a Python program to count the number of characters (character frequency) in a string. 
# #Sample String : google.com'
# A="google.com"
# def charFrequency(df):
#     dict={}
#     for i in df:
#         x=dict.keys()
#         if i in x:
#             dict[i]+=1

#         else:
#             dict[i]=1
#     return(dict)
# print(charFrequency('pooja'))

    


#3. Write a Python program to get a string made of the first 2 and last 2 characters of a given string. 
# If the string length is less than 2, return the empty string instead
# def lstring(df):
#    if len(df)<2:
#     return " "
#    return df[0:2 ] + df[ -2:]

# print(lstring("innovant"))
# print(lstring("inn"))
# print(lstring("in"))



#4. Write a Python program to get a string from a given string 
# where all occurrences of its first char have been changed to '$', except the first char itself.
#  Normal jindagi                 avalue = "welcome"
#                                 print(avalue.replace("c","$"))    
 
# mentos jindagi
# def occurance_char(df):
#     char=df[0]
#     df=df.replace(char,"$")
#     df=char + df[1:]
#     return df
# print(occurance_char("foreverfor"))
        

#5. Write a Python program to get a single string from two given strings,
#  separated by a space and swap the first two characters of each string.

# def char_mix(a,b):
#     a_new=b[:2] + a[2:]
#     b_new=a[:2] + b[2:]
#     return a_new + " "+b_new
# print(char_mix("abc","xyz"))

# def swap_string(a,b):
#     anew=b[:2]+a[2:]
#     bnew=a[:2]+b[2:]
#     return anew + " " +bnew
# print(swap_string("pooja","nikam"))



#6. Write a Python program to add 'ing' at the end of a given string (length should be at least 3). 
# If the given string already ends with 'ing', add 'ly' instead. 
# If the string length of the given string is less than 3, leave it unchanged.
# def add_str(df):
#     length=len(df)
#     if length > 2:
#         if df[-3:]=="ing":
#             df+="ly"
#         else:
#             df+="ing"
#     return df
# print(add_str("sily"))
# print(add_str("pushing"))


# 7. Write a Python program to find the first appearance of the substrings 'not' and 'poor' in a given string. 
# If 'not' follows 'poor', replace the whole 'not'...'poor' substring with 'good'.
#  Return the resulting string.
A="the students is not that much poor"

# def first_appearance(df):
#     str=df.find('not')
#     str=df.find('poor')
#     if str > str and str>0:
#         df = df.replace('not ','').replace('poor', 'good').replace(' ',' ')
#         return df
#     else:
#         return df
# print(first_appearance('the students is not that much poor'))
# print(first_appearance('the man is so poor'))
def replacer(df):
    str1=df.find("not")
    str1=df.find("poor")
    if str1 > str1 and str1 >0:
        df=df.replace("not","").replace("poor","good").replace("","")
        return df
    else:
        return df
print(replacer(A))
                                                                    
    


# def appearance(df):
#     str=df.find("not")
#     str1=df.find("poor")
#     if df :
#         df=df.replace("not","").replace("poor","good").replace("not poor ","good")
#         return df
#     else:
#         return df
# print(appearance("pooja is not poor in python"))

# 8. Write a Python function that takes a list of words and return the longest word and the length of the longest one.
# A=(["pooja","Shubhangi","Arun","Nikam","ghodake"])
# alist=[]
# for i in A:
#     alist.append((len(i),i))
#     alist.sort(reverse= True)
# print(alist,"Maximum word is : ",alist[0])


'''9.Write a Python program to remove the nth index character from a nonempty string.'''
# def Remove_str(df,n):
#     first_str=df[:n]
#     last_str=df[n+1:]
#     return first_str + last_str
# print(Remove_str("python",3))    

'''10. Write a Python program to change a given string to a newly string where the first and last chars have been exchanged'''
# def exchange(df):
#     return df[-1:]+df[1:-1]+df[:1]
# print(exchange("pooja"))

# 11. Write a Python program to remove characters that have odd index values in a given string.

# def odd(df):
#     count=""
#     for i in range(len(df)):
#         if i % 2 == 0:
#             count=count +df[i]
#     return count
# print(odd("InnovantITAcadamy"))

# 12. Write a Python program that prints the calendar for a given month and year

# from datetime import date
# x=date(2014, 7, 2)
# y=date(2014, 7, 11)
# day=x-y
# print(day)


# 15. Write a Python program to get the volume of a sphere with radius six.

# radius=12
# volume=4/3*3.14*radius**3
# print(volume)

# 16. Write a Python program to calculate the difference between a given number and 17.
#  If the number is greater than 17, return twice the absolute difference.

# num=35
# if num > 17  :
#     diff=(abs(num - 17))**2
#     print(diff)
# else:
#     diff=abs(num - 17)
#     print(diff)

# 17. Write a Python program to test whether a number is within 100 of 1000 or 2000.

# num=int(input("Enter any number : "))
# print((abs(1000 < num) <= 100) or (abs(2000 <= 100)))

# 18. Write a Python program to calculate the sum of three given numbers. If the values are equal, return three times their sum

# n1=int(input("Enter number : "))
# n2=int(input("Enter number : "))
# n3=int(input("Enter number : "))
# sum=n1+n2+n3
# if n1==n2==n3:
#     print(n1**3)
# else:
#     print(sum)

# 19. Write a Python program to get a newly-generated string from a given string where "Is" has been added to the front.
# Return the string unchanged if the given string already begins with "Is".


































