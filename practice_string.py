# Question on string

#1. Write a Python program to calculate the length of a string.

# avalue="Pooja"
# print(len(avalue))
# #2. Write a Python program to count the number of characters (character frequency) in a string. Go to the editor
# #Sample String : google.com'

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






















