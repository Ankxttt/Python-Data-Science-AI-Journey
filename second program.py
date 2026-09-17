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
# *
# * *
# * * *
# * * * *
# * * * * *
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

import csv

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

rows = [
    {"name":"ankit","age":19,"marks":88},
    {"name":"arjun","age":21,"marks":90},
    {"name":"raju","age":20,"marks":99},
]

with open("rows.csv", "w", newline="") as file:  #this method is used to write dictionary csv file(data).
    fieldnames = ["name", "age", "marks"]
    writer = csv.DictWriter(file, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(rows)

# with open("rows.csv", "r") as file:   #this method is used to read dictionary csv file(data).
#     reader = csv.DictReader(file)

#     for rows in reader:
#         print(rows["name"], rows["age"] ,rows["marks"])

# how to convert json into csv & csv into json.

import csv
import json

with open("rows.csv", "r")as csvfile:
    reader = csv.DictReader(csvfile)

    data = list(reader)

with open("conveted.json", "w")as jsonfile:
    json.dump(data, jsonfile, indent=4)

    print("csv converted into json successfully...")


