

"""

#!Conditional Statements

#**if-elif-else (SYNTAX)

if(condition) :

Statement1

elif(condition):

Statement2

else:

StatementN

"""


age = 19 ;

if(age>18):
    print("You can vote & apply for license")
    print("You can drive")
elif(age==18):
    print("You are beginer now")
else:
    print("Not now")    


marks = int(input("Studen marks :  "))

if(marks >= 90):
    print("Grad is A++")
elif(90 > marks & marks >= 80):
    print("Grad is B")
elif(80 >  marks & marks >= 70):
    print("Grad is C")    
else:
    print("Grad is D")
