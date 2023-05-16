#       String

# A="innovant"
# A='Pooja'
# A='''pooja
# arun
# nikam
# is innovant student'''
# print(A)
# print(type(A))
# p o o j A
# 0 1 2 3 4
# -5 -4 -3-2 -1

# length,count,replace,startwith and endswith,capitalize and upper ,lower

# A="welcome"
# result=A.find("co",2,6)
# print(f"index of 'co' is in {A} : {result} ")

# print(A[0:7])
# a="Hello , World"
# print(a[1])

# for x in "banana":
#     print(x)

# a="Pooja"
# print(len(a))

# txt="   the best things in a life are mostly free"
# print("free" in txt)
# if "free" in txt:
#     print("Yes","free is present in txt")

# print(txt[2:])
# print(txt[: :2])

# print(txt.upper())
# print(txt.lower())
# print(txt.strip())
# print(txt.capitalize())

# a="pooja"
# b="nikam"
# c=a+b
# print(c)
# name="pooja"
# age=26
# txt="My name is {}.I am {} old"
# print(txt.format(name,age))

#      ** Escape charecter **
# escape charecter use when we want to use double quets in a double quets so
# txt = "We are the so-called "Vikings" from the north."
# print(txt)                  ----------Invalid syntax

# txt = "We are the so-called \"Vikings\" from the north."
# print(txt)          --------------We are the so-called "Vikings" from the north.

# txt = "We are the so-called \\Vikings from the north."
# print(txt)            -------------We are the so-called \Vikings from the north.


# txt = "We are the so-called \bVikings from the north."
# print(txt)
# 7. Write a Python program to find the first appearance of the substrings 'not' and 'poor' in a given string. If 'not' follows 'poor', replace the whole 'not'...'poor' substring with 'good'. Return the resulting string. Go to the editor
# Sample String : 
# a='The lyrics is not that poor!'
# # 'The lyrics is poor!'

# def replacer(df):
#     str1=df.find("not")
#     str2=df.find("poor")
#     if str2>str1 and str1>0 and str2>0:
#         df=df.replace("not","").replace("poor","good")
#         return df
    
# print(replacer(a))

'''8. Write a Python function that takes a list of words and return the longest word and the length of the longest one'''
alist=["pooja","Innovant","sagar"]

def longestword(df):
    alist=[]
    for i in range(len(df)):
        list.append(len(i),i)
        df.sort()
    return df[-1][0],df[-1][1]
print(longestword(alist))
