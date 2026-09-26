# A = float(input("enter the first number:"))
# B = float(input("enter the second number:"))

# print("the sum of two numbers is:", A + B)


# side = int(input("enter the side of square:"))

# print("area of square is:", side * side)


# First = float(input("enter the first number: "))
# second = float(input("enter the second number: "))

# print("average of two numbers is=", (First + second) / 2)


# A = int(input("enter the first number: "))
# B = int(input("enter the second number: "))

# print( not "true" if A >= B else not "false")

# str1 = "This is the string. \nwelcome to the python language."
# print(str1)

# str1 = "ankit kumar"
# print(str1[3:]) #indexing[3:9]

# str1 = "python language"
# print(str1[:-3]) #slicing[-15:-3]

# Name = input("enter your name :")
# print("length of your name is :", len(Name))
 
# str1 = "this is the string."
# str2 = "hello how are you."
# str3 = '''hello what is the your name.'''

# str = 'This is th string"s character'
# print(str)


# str1 = "ankit"
# str2 = "kumar"
# final_str = (str1+str2)

# print(final_str)


# str = ("anki tkumar")

# print(len(str))


# str1 = "ankit"
# len1 = (len(str1))
# print(len1)

# str2 = "kumar"
# len2 = (len(str2))
# print(len2)

# final_str = (str1+str2)
# print(len(final_str))


# str = "pythonprogramming"
# print(str[:8]) #0:7
# print(str[2:len(str)]) #2:length of the string

# str = "ankit kumar" #negative indexing (slicing)
# print(str[-5:-2]) #kum

# str = "My name is ankit kumar and i am from patna"
# print(str.endswith("tna")) #return true if string ends with substring


# str = "my name is ankit kumar"
# str = str.capitalize()  #It make changes on the orginal string
# print(str) 

# str = "python is easy programming language"
# print(str.replace("python" , "java")) # replcae the old character wit new one

# str = "python is very important and very advance programming language"
# print(str.find("very")) #give the position or first index of its first occurrence

# str = "python is an high level and easy programming language"
# print(str.count("n")) #give the no. of occurrence of the substr in string

# name = input("enter the name: ")
# print("welocme:",name)
# print(len(name))  # wap to input the name and find its length


# str = "the prize of $ is $95.90"
# print(str.count("$")) # wap to find the occurrence of $ in the string

# Light = "green"

# if(Light == ("red")):
#     print("please stop")
# if(Light == ("green")):
#     print("you can go")


# age = 27

# if(age >= 18):
#     print("you can vote & and apply for driving license")
# elif(age <= 18):
#     print("you cannot vote & apply for driving license")


# Light = "pink"

# if(Light == "red"):
#     print("please stop")
# elif(Light == "yellow"):
#     print("please wait")
# elif(Light == "green"):
#     print("you can go now")
# else:
#     print("light is defective")

# str = ("my name is ankit kumar")
# str = (str.capitalize())
# print(str)

#function and recursion
# def cal_sum(a, b, c):
#     sum = a + b + c
#     avg = sum / 2

#     return sum
# print(cal_sum(12, 234, 345))

# def cal_avg(a, b):
#     return (a + b / 2)

# print(cal_avg(123, 344))

# def print_factor(n):
#     factor = 1
#     for i in range(1, n + 1):
#         factor *= 1
#         print(factor)

#     print(print_factor(8))
# list = input("enter the value :")
# def print_len(list):
#     return list
# print(len(list))

# cities = ["delhi", "goa", "madras", "mumbai", "delhi", "indore"]

# def print_item(list):
#     for item in list:
#         print(item, end=" ")

# print_item(cities) 

#pattern recognition problem in nested loop.
# """
# * * * *
# * * * *
# * * * *
# * * * *
# * * * * 
# """
# for i in range(1, 6):
#     for j in range(1, 6):
#         print("*", end=" ")
#     print()
# """
# # *
# # * *
# # * * *
# # * * * *
# # * * * * *
# #"""
# r = 5
# for i  in range(1, r+1):
#     for j in range(1, i+1):
#         print("*", end=" ")
#     print()   

# """
# * * * * *
# * * * *
# * * * 
# * *
# *
# """

# n = 5
# for i in range(n, 0, -1):
#     for j in range(i):
#         print("*", end=" ")
#     print()

# """
# 1
# 1 2
# 1 2 3
# 1 2 3 4
# 1 2 3 4 5
# """

# n = 6
# for i in range(1, 6):
#     for j in range(1, i+1):
#         print(j, end=" ")
#     print()

# """
# 1 2 3 4 5
# 1 2 3 4
# 1 2 3 
# 1 2 
# 1
# """
# n = 6
# for i in range(n, 0, -1):
#     for j in range(i, 0, -1):
#         print(j, end=" ")
#     print()

# """
#      *
#     * *
#    * * *   
#   * * * *
# * * * * * *   
# """

# n = 6
# for i in range(1, n + 1):
#     spaces = n - i
#     stars = 2 * i - 1

#     print(" " * spaces + "*" * stars)

# practice json and csv file operations using csv and json module in python.

# import json 

# output = {"name" : "ankit", "age" : 19, "course" : "data science"}

# with open("output.json", "w") as file:
#     json.dump(output, file, indent= 4)

# with open("output.json", "r") as file:
#     data = json.load(file)

# print(data)
# print(type(data))

# json_string = json.dumps(output)   #this method is used to convert python object into json string.
# print(json_string)
# print(type(json_string))

# python_object = json.loads(json_string)   # ths method is used to convert json string into python object.
# print(python_object)
# print(type(python_object))

# import csv

# rows = [
#     ["name","age","marks"],
#     ["ankit",19,88],
#     ["amit",21,81]
# ]

# with open("rows.csv", "w", newline="") as file:  #this method is used to write csv file(data).
#     writer = csv.writer(file)
#     writer.writerows(rows)
    
# with open("rows.csv", "r", newline="") as file:   #this method is used to read csv file(data).
#     reader = csv.reader(file)

#     for rows in file:
#         print(rows)

# rows = [
#     {"name":"ankit","age":19,"marks":88},
#     {"name":"arjun","age":21,"marks":90},
#     {"name":"raju","age":20,"marks":99},
# ]

# with open("rows.csv", "w", newline="") as file:  #this method is used to write dictionary csv file(data).
#     fieldnames = ["name", "age", "marks"]
#     writer = csv.DictWriter(file, fieldnames=fieldnames)
#     writer.writeheader()
#     writer.writerows(rows)

# with open("rows.csv", "r") as file:   #this method is used to read dictionary csv file(data).
#     reader = csv.DictReader(file)

#     for rows in reader:
#         print(rows["name"], rows["age"] ,rows["marks"])

# how to convert json into csv & csv into json.

# import csv
# import json

# with open("rows.csv", "r")as csvfile:  # this method is used to read csv file.
#     reader = csv.DictReader(csvfile)

#     data = list(reader)      # we store csv dictreader in data variable.

# with open("conveted.json", "w")as jsonfile:    # this method is used to create a json file with csc data which is converted into it.
#     json.dump(data, jsonfile, indent=4)

#     print("csv converted into json successfully...")

# practice list , dictionary, set comprehensions:

# list comprehension.
# list1 = [12, 45, 3, 6, 0, 89, 43, 3 ,33] # syntax for using list comprehension.
# print("using list comprehension", [item for item in list1 if item % 3 == 0])

# for item in list1:
#     divide_by_3 = []
#     for item in list1:
#         if item % 3 == 0:
#            divide_by_3.append(item)
# print("without using list comprehension", divide_by_3)

# without using list comprehension.
# number = []
# for i in range(100):
#     if i % 3 == 0:
#         number.append(i)
# print(number)

#using list comprehension.
# list = [i for i in range(100) if i % 3 == 0]
# print(list)

# Examples of list comprehension:
# list = [x**2 for x in range(10)]
# print(list)

# using if condition in list comprehension:
# even = [x for x in range(10) if x % 2 == 0]  # filtering even numbers.
# print(even)

# using if-else condition in list comprehension:
# numbers = ["Even" if x % 2 == 0 else "Odd" for x in range(10)]  # replacing even numbers with 'Even' & odd with 'Odds'
# print(numbers)

# using nested loops in list comprehension:
# pairs = [(x, y) for x in range(2) for y in range(3)]  # creating pairs from two lists.
# print(pairs)

# using function in list comprehension:
# language = ["python", "java", "c++", "javascript"]
# upper_words = [language.upper() for language in language]  # convert list of strings in uppercase.
# print(upper_words)

# list comprehension with nested list comprehension:
# Matrix = [[1,2], [3, 4], [5, 6], [7, 8]]
# flattend = [num for row in Matrix for num in row]  # Flattending 2D list.
# print(flattend)

# dictionary comprehension:
# square = {x : x * x for x in range(1,11)}    # key:value for item in iterables.
# print(square)

#using f-string with if condition in dictionary comprehension:
# dict1 = {i : f"items{i}" for i in range(1,11) if i % 2 == 0}
# print(dict1)

# dictionary comprehension:
# name = ["ankit", "ajay", "raju", "vijay"]

# dict = {name : len(name) for name in name}
# print(dict)

#set comprehension:

# unique_numbers = {x for x in [1, 2, 4, 4, 2, 1, 3, 6, 6, 3]}  # start with curly braces without(:) is known as set.
# print(unique_numbers)

# number = {x * 2 for x in range(1, 11) if x % 2 == 0}  # we can use range() function & if conditions in set comprehension. 
# print(number)

# set comprehension with conditions: 
# value = range(1, 5)               # we store range values in (value) named variable.
# numbers = {x ** 2 for x in value if x % 2 == 0}
# print(numbers)

# set comprehension with unique numbers:
# cars_unique = {cars_unique for cars_unique in ["bmw", "audi", "lexus", "bmw", "audi", "mercedes", "lexus"]}
# print(cars_unique)                   # in sets only unique values will be print, duplicate value will not.
# print(type(cars_unique))

# pairs = {x for x in range(1, 19) if x % 2 == 0}
# print(pairs)

#Lambda functions:

# without using lambda function:
# def add(a, b):    # it take multi line to define function and peform operation.
#     return a+b
# print("without using lambda function :")
# print("without using lambda function", add(19, 2))

# using lambda function:
# total_sum = lambda x, y: x+y   # it perform in a single expression without full definition def.
# print("using lambda function",total_sum(19, 2))

# lambda function with multiple argument:
# average = lambda x, y, z: (x + y + z)/3   # lambda function with multiple arguments.
# print(average(5, 10, 46))
#Ex:
# cube = lambda x: x*x*x
# print(cube(5))
#Ex2:
# square = lambda x: x**2
# print(square(19))

# using if-else or ternaary operator with lambda function:
# vote = lambda age: "eligible" if age >= 18 else "not eligible"  # we can use single line if/else expression with lambda function.
# print(vote(18))
#Ex2:
# Maximum = lambda x, y: x if x > y else y
# print(Maximum(99, 99.2))

# using lambda function with map() function:
# numbers = [1, 4, 5, 3, 8, 12]
# value = map(lambda x: x * x, numbers)  # suppose i want to print the square of all given no. in list with the help of map().
# print(list(value))      # we use list to represent the transformed element because it doesn't directly the list, it return special map object.

#Ex2: print dobule of given no. in list using map() with lambda function:
# value = [1, 4, 5, 8, 2, 5, 2]
# double = map(lambda x: x**2 , value)        
# print(list(double))

# using lambda function with filter() function:
# element = [1, 4, 7, 3, 9, 2, 10]
# pairs = filter(lambda x: x < 6, element)  # filter() filters the element based on predicate/condition and return new sequence of list.
#  # print(list(pairs))
#Ex2:
# unique = filter(lambda x: x % 2 == 0, element)
# print(list(unique))
#Ex3:
# element = [12, 45, 67, 56, 67, 89, 2]
# pair = list(filter(lambda x: x <= 45, element))
# print(pair)

# using lambda function with reduce() function:
# from functools import reduce     # firstly, we need to import it from functools module from python.
# val = [12 ,45, 6, 32, 89, 50]
# sum = reduce(lambda x, y: x + y, val)   # it perform functions on each element and produce the final result in a single value.
# print(sum)                                          # reduce = combine
#Ex2:
# product = reduce(lambda x, y : x * y, val)
# print(product)
#Ex3:
# Division = reduce(lambda x, y: x / y, val)
# print(Division)

# using lambda function with sort() function:
# marks = [[1, 4],[5, 2], [3, 7], [9, 8]]             # we create a pair of list within the list.
# result = sorted(marks, key = lambda x: x[1])       # we sort the pair of list in ascending order.
# print(result)
#Ex2: using sort() function in reverse order:

# students = [("rahul", 97), ("arjun", 88), ("smriti", 81), ("ankit", 99)]
# marks = sorted(students, key=lambda x : x[1], reverse=True)
# print(marks)

# we can write them in different ways:

# students.sort(key = lambda student: student[1])
# print(students)
# students = [
#     ("raju", 81),
#     ("arvind", 85),
#     ("rajesh", 88),
#     ("sanjeev", 91)
# ]

# students.sort(key = lambda students : students[1], reverse=True)   # it sort the list in reverse order.
# print(students)

# practice with Exception handling using try(), except(), else(), finally:
# Now we write an normal program to print the table of any no:
# but i think there is an error in my first 10 to 12 line of code, so i put it into a try block and it help to catch the error and except block will be executed.
# try:    # it there is no error in code, it will execute or if any error occurred
#     num = int(input("enter the number :"))
#     print(f"multiplication of", num, "is :")
#     a = [1, 12]
#     print(a[num])

#     # for i in range(1, 11):
#     #     print(f"{num} x {i} = {i*num}")

# except ValueError:
#     print("sorry!, the value you Entered is not an integer.")

# except SyntaxError:  # we can handle many errors by using multiple except block and it will help to handle the error.
#     print("sorry! there is an invalid syntax.")

# except IndexError:
#     print("sorry! there is an index error.")


# print("sorry there is an problem in the program.")  # this line will print which shows that our program will always executing, it will not stop, that's why we use try,except block.
# print("program ended")

# using error handling in my program:
# try:   # suppose I think there is an error in my program, so i put it into an try block, if there is any error, it will catch and except block will be executed.
#     num1  = int(input("enter the first no:"))
#     num2 = int(input("enter the second no:"))
  
#     sum = num1 + num2
#     print(f"sum of", num1, "and", num2, "is", sum)

# except ValueError:   # is any error occurred in my code of try block, then i can handle it with except block.
#     print("sorry the value you entered is not integer")
# except SyntaxError:   # we can handle multiple errors and with the help of multiple except block.
#     print("sorry there is syntax error occurred in your program")


# print("End of program")  # this will help to make our program to always run and avoid the program hault/stopness.
# using an finally with try and except block:
# try:
#     num = int(input("enter the no :"))
#     a = [1, 4]
#     print(a[num])

# except ValueError:
#     print("there is an value error.")

# except IndexError:
#     print("there is an index error.")

# finally:  # this block is always executed whether error occurred or not, it also used to cleanup the code, no matter what happens,but at end what we have to do is more important.
#     print("end of program.")
#Ex: why we use finally block , we can print anything at the end , but when we put the try,except block in function, it will not print, that's why we use finally block to cleanup the code and doing concluding task.
# try:

#     l = [1, 5 ,7 ,8]
#     i = int(input("enter the no :"))
#     print(l[i])

# except IndexError:
#     print("there is an index error.")

# except ValueError:
#     print("there is an value error.")

# else:
#     print("program successfully run.")

# finally:
#     print("program ended...")  # this will always executed beacause it helps to cleanup the code and always executed.

# practice with custom errors: we handle multiple errors to execute our program, but sometimes we create error to stop
# the execution of program at the first error which doesn't effect our rest of program.

# n = int(input("enter the value between 3 and 5 :"))
# print(n)

# if(n > 3 and n > 5):

#    raise ValueError("the value you entered is not between 3 and 5.") # we can raise a custom error according to our purpose and stop the execution at earliest.

# raise a custom error based on condition:
# try:
#     balance = int(input("enter the balance amount :"))
#     withdraw = int(input("enter the withdraw amount :"))

#     if (withdraw > balance):
#         raise ValueError("insufficient balance")

# except ValueError as e :
#     print("error :", e)
#Ex: using try, except, with raise a custom error:
# while True:
#     try:
#         value = input("enter the value ( 3-5 or quiet) :")

#         if value.lower == "quiet" :
#             print("program ended successfully.")

#             value = int(value)

#         if  value > 3 or value < 5:
#             raise ValueError("entered the value between 3 and 5.")

#         print("you entered :", value)        
#     except ValueError as e:
#         print("Error :", e)




