# Question on string

#1. Write a Python program to calculate the length of a string.

# avalue="Pooja"
# print(len(avalue))
# #2. Write a Python program to count the number of characters (character frequency) in a string. Go to the editor
# #Sample String : google.com'

def charFrequency(df):
    dict={}
    for i in df:
        x=dict.keys()
        if i in x:
            dict[i]+=1
        else:
            dict[i]=1
    return(dict)
print(charFrequency('pooja'))


# def charFrequency(df):
#     dict={}
#     for i in df:
#         x=dict.keys()
#         if i in x:
#             dict[i]+=1
#         else:
#             dict[i]=1
#     return dict
# print(charFrequency("Innovant"))

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
# the students is not that much poor

# def first_appearance(df):
#     str=df.find('not')
#     str1=df.find('poor')
#     if str1 > str and str>0 and str1>0:
#         df = df.replace('not ','').replace('poor', 'good').replace(' ',' ')
#         return df
#     else:
#         return df
# print(first_appearance('the students is not that much poor'))
# print(first_appearance('the man is so poor'))

# 8. Write a Python function that takes a list of words and return the longest word and the length of the longest one.
A=["pooja","Shubhangi","Arun","Nikam","ghodake"]
def long_word(df):
    list=[]
    for i in range(len(df)):
        list.append(len(i),i)
        df.sort()
    return df[-1][0], df[-1][1]
result = (["PHP", "Exercises", "Backend"])
print("\nLongest word: ",result[1])
print("Length of the longest word: ",result[0])


    




















