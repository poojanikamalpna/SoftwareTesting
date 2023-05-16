# Lambda function is ananmous function
# It is write in single line
# lambda function use we need only one time or one instance .

#lets create a adult function
'''def isAdult(age):
    if age > 18:
        return "Adult"
    else :
        return "Minor"
    
print(isAdult(29))'''

#====================================================================================

# By Using Lambda Function

isadult=lambda age : "Adult" if age > 18 else "monor"
# print(isadult(30))
print((lambda age : "Adult" if age > 18 else "minor")(13))


#=====================================================================================



