# This is my first python program!
# print("hello world") #"print" is a in-built function in python and anything under the double quote("") is known as string.

# print("My name is : BekkaarXCoder.\nMy age is 19 \nI am currently learning python.") # we can write in single sentence with the help of (\n).
# variable and data types :

# name = "BekkaarXCoder"  #name = variable & "bekkaarxcoder" = string.
# age = 19                #age = varibale & 19 = integer.
# height = 5.7            #height = variable & 5.7 = float.
# value = True
# a = None

# print(type(name))       #type function is used to check the type of data stored in variables.
# print(type(age))
# print(type(height))
# print(type(value))
# print(type(a))

# print sum
# a = 12394
# b = 49565
# sum = a + b  # (+) is an arithmetic operator
# print(sum)

#Taking input from the user and & printing it.
# name = input("name :")
# age = int(input("age :"))
# height = float(input("height :"))

# print("Hello My name is", name, "and I am", age, "years old", "and My height is", height ,)

# conditional statement:
#1 EX: Age Restriction for voting:
# age = int(input("enter the age :"))

# if(age >= 18):
#     print("you are eligible for voting.")

# elif(age < 18):
#     print("you are not eligible for voting.")

# else:
#     print("election not held.")

#2 EX: calculator:
# num1 = int(input("enter the first number :"))
# num2 = int(input("enter the second number :"))
# operator = input("enter the operation :")

# if(operator == "+"):
#     print("addition of two number :", num1 + num2)

# elif(operator == "-"):
#     print(num1 - num2)

# elif(operator == "*"):
#     print(num1 * num2)

# elif(operator == "/"):
#     print(num1 / num2)

# elif(operator == "%"):
#     print(num1 % num2)

# elif(num1 / num2 == 0):
#     print("number cannot be divided by zero")

# else:
#     print("no operation found")

#Single line conditional statement:
# language = input("enter your language :")
# type = "yes" if language == "python" else "no"
# print(type)

#clever if/else conditional statement:
# age = int(input("enter the age :"))
# type = ("yes", "no") [age <= 18]
# print(type)

# arithmetic operator:
a = 10
b = 29
print(a + b)
print(a - b)
print(a * b)
print(a / b)
print(a % b)
print(a ** b)

