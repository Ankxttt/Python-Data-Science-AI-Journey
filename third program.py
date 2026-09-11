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

# first program.py

# Marks = int(input("enter the marks :"))

# if(Marks >= 90):
#     print("Grade A")
# elif(Marks >= 80 and Marks < 90):
#     print("Grade B")
# elif(Marks >= 70 and Marks < 80):
#     print("Grade C")
# elif(Marks <= 70):
#     print("Grade D")

# else:
#     print("Grade of students ->")

# age = 79

#nesting

# if(age >= 18):
#     if(age >=80):
#         print("cannot vote")
#     else:
#         print("can vote")
# else:
#     print("cannot vote")



# num = int(input("enter the number: "))

# if(num % 2 == 0):

#     print(num , "is even number.")

# else:

#     print(num , "is odd number.")

# a = int(input("enter the value: "))
# b = int(input("enter the value: "))
# c = int(input("enter the value: "))

# if(a > b and a > c):
    
#     print("a is greater number. ")

# elif(b > c):
#     print("b is greater number. ")

# else:
#     print("c is greater number. ")


# num = int(input("enter the number: "))

# if(num % 7 == 0):
#     print(num , "is multiple of 7")

# else:
#     print(num , "is not multiple of 7")

# age1 = 18
# age2 = 29
# age3 = 27
# age4 = 34

# age = [18,29,27,34]
# print(list.sort(age))
# print(age)

# marks = [24.4,84.12,93.22,81.1]
# print(marks)
# print(type(marks))
# print(marks[3])
# print(len(marks))

# students = ["ankit" , 18 , 91.2]
# print(students[0])
# students[0] = "kumar" #list are mutable
# print(students)

# marks = [80, 82, 91, 28, 36]
# print(marks[1 : len(marks)]) # slicing in list

# marks = [81, 82, 62, 91, 78, 28]
# print(marks[-5 : -1]) #negative slicing in list


# marks = [28, 18, 48, 26]
# marks.append(45) # adding element at the end of the list
# print(marks)

# age = [18, 47, 17, 35]
# age.append(45)
# age.sort()
# print(age) 

# marks = [28,82,18,2,45,19]
# marks.sort(reverse = True)
# print(marks)

# list = ["ankt", "raju", "ranveer"]
# list.reverse() #change the index of element
# print(list)

# list = ["ankit", "arvind", "raju", "allahvadia"]
# list.sort(reverse = True)  #arranging the list in descending order
# print(list)

# list = [17, 54, 18, 57]
# list.insert(3,45) #insert element at the specific position
# print(list)

# list = [28, 34, 67, 45, 34, 28]
# list.remove(34) #remove element from the list according to their first occurrence 
# print(list)

# list = [28, 18, 29, 47, 99]
# list.pop(4)  #remove element from specific position
# print(list)

# tup = (1,)
# print(tup) #assign value as a tupple

# tup = ()
# print(tup)
# print(type(tup))

# tup = (12, 45, 56, 78,) #it is compulsory to add comma as the end of the list
# print(tup) 
# print(type(tup))

# tup = (23, 45, 78, 45,)
# print(tup[2 : 3]) #slicing is same as in list and string
# print(type(tup))

# tup = (12, 34, 24, 67, 24, 35, 24)
# print(tup.count(34)) #count the total occurrence of element

# tup = (13,67,45,97,45,24,)
# print(tup.index(45)) #return the position of the first occurrence of the element

# Movies = []

# Movie1 = (input("enter the first favourite movie:"))
# Movie2 = (input("enter the second favourite movie:")) #program to input favourite movies and save in the list
# Movie3 = (input("enter the third favourite movie:"))

# Movies.append(Movie1)
# Movies.append(Movie2)
# Movies.append(Movie3)

# print(Movies)

# list1 = [1, 2, 1,]

# copy_list1 = list.copy(list1)
# copy_list1.reverse()  #copy method is used to print palindrome element

# if(copy_list1 == list1):
#     print("list is palindrome")
# else:
#     print("not palindrome")

# grade = ("A", "B", "C", "A", "C", "A", "B")

# print(grade.count("a"))


# list = ["a", "b", "b", "a", "c"]
# list.sort() # sort element from ascending to descending order and save in list
# print(list)
# print(type(list))

# list = []

# list1 = (input("enter the value of a: "))
# list2 = (input("enter the value of b: "))
# list3 = (input("enter the value of c: "))

# list.append(list1)
# list.append(list2)
# list.append(list3)

# print(list)


# list = []

# list1 = (input("enter value a : "))
# list2 = (input("enter value b : "))
# list3 = (input("enter value c : "))

# list.append(list1)
# list.append(list2)
# list.append(list3)

# print(list)
# print(type(list))

# tup = (1, 2, 4, 4, 6, 8)
# print(tup.count(4))
# print(type(tup))

# Movie = (input("enter the first movie"))
# Movie = (input("enter the second movie"))
# Movie = (input("enter the third movie"))

# student = {
#     ("name") : "ankit kumar",
#     ("age") : "18",
# }

# print(student)
# print(type(student))

# info = {"ankit", 18, 91, "bihar"}

# info.pop()

# print(info)
# print(type(info))

# while True :
#     print("hello world")

# count = 1
# while count <= 5:
#     print(count)
#     count +=1

# print("loop ended")

# i = 5
# while i < 6 :
#     print("hello")
#     i -= 1

# print("loop ended")

# count = 1
# while count <= 100 :   #wap to print no. from 1 to 100.
#     print(count)
#     count += 1

# i = 1
# while i <= 10 :
#     print(3 * i) # wap to print multplication of 3.
#     i += 1

# i = 100
# while i >= 1 :  # wap to print no. from 100 to 1.
#     print(i)
#     i -= 1

# nums = [1, 3, 5, 9, 29, 68, 92, 100]

# idx = 0
# while idx < len(nums):  # wap to to print the element from the list while using the loop. 
#     print(nums[idx])
#     idx += 1

# nums = int(input("enter the number :"))

# i = 1
# while i <= 10:  # wap to print the multiplication of the no. given the user.
#     print(nums*i)
#     i += 1

# info = [1, 34, 56, 78, 91, 100]

# i = 0
# while i < len(info): # wap to print the element from the list using loop.
#     print(info[i])
#     i += 1

# nums = (1, 23, 45, 56, 78, 98, 100)

# x = 56

# i = 0 
# while i < len(nums) :
#     if(nums[i] == x):
#         print("element found at idx :", i) # wap to find the element from the tupple using loop.
#     else :
#         print("finding...")

#     i += 1

# i = 0
# while i <= 5 :
#     print(i)
#     if (i == 3): # using a break statement in the loop.
#         break
#     i += 1

# print("end of loop")

# i = 0
# while i <= 19 :
#     print(i)

#     if (i == 15) :
#         break
#     i += 1

# print("end the loop")

# i = 0
# while i <= 10:
#     if(i % 3 == 0):
#         i += 1
#         continue  # continue statment used to skip the current iteration and move to the next iteration in loop.
#     print(i)
#     i += 1

# i = 0
# while i <= 10:
#     if (i % 2 == 0):
#          i += 1
#          continue  #continue statment is used to skip the current iteration and move to the next iteration in the loop.
#     print(i)
#     i += 1

# print("end of loop")


# count = 0
# while count <= 5: # while loop condition is used to print no. from 0 to 5 , according to the condition. 
#     print(count)
#     count += 1

# i = 1
# while i <= 1000:
#     print("hello", i) #
#     i += 1

# i = 1
# while i <= 10: # print no. from 1 to 10. 
#     print(i)
#     i += 1

# print("loop ended")

# count = [1, 2, 45, 15, 46, 77, 89, 91, 100]

# idx = 0
# while idx < len(count):
#     print(count[idx])
#     idx += 1

# nums = (1, 23, 45, 56, 67, 87, 99, 100)

# x = 87

# i = 0
# while i < len(nums) :
#     if(nums[i] == x) :
#         print("element found at i :", i)

#     else :
#         print("finding...")
#     i += 1

# i = 1
# while i <= 10:
#     print(i)
#     i += 1

# nums = [1, 3, 13, 45, 65, 77, 89, 98, 100]

# idx = 0
# while idx < len(nums) : # wap to print element from list using loop.
#     print (nums[idx])
#     idx += 1

# i = 0
# while i <= 10 :
#     print(i)
#     if(i == 5) :
#         break
#     i += 1
# print("end of loop")

# i = 0
# while i <= 10 :
#     if(i == 5) :
#         i += 1
#         continue # skip statment is used to skip the current iteration and move to the next iteration.

#     print(i)
#     i += 1

# veggies = ["onion", "tomato", "garlic", "capsicum"]

# for item in veggies : # for loop is used for sequencial traversal.
#     print(item) # we can print the value of any data type without going in while loop.

# nums = [1, 3, 6, 8, 0]

# for el in nums :  # print element using for loop.
#     print(el)


# list = [12, 37, 46, 89, 98]

# for item in list :
#     print(item)    # print element using for loop with else statement.

# else:
#     print("end")


# list = [1, 34, 45, 67, 78, 90]

# for el in list :
#     print(el)


# tuple = (1, 12, 23, 24, 56, 67, 78, 68, 89, 99)
# x = 68

# idx = 0
# for el in tuple :
#     if (el == x) :
#         print("element found at idx :", idx)
#         break

#     idx += 1


# wap to create a simple calculator using conditional statement and input function.
# a = (input("enter the first value :"))
# b = (input("enter the second value :"))
# op = (input("enter the operator (+ , - , * , % , /) :"))

# if(op == "+") :
#     print(a + b)
# elif(op == "-") :
#     print(a-b)
# elif(op == "*") :
#     print(a*b)
# elif(op == "%") :
#     print(a%b)
# elif(op == "/") :
#     print(a/b)
# else :
#     print("invalid operator")

# for el in range(0, 10, 2): #rrange function is used to print the even number which start from 0 to 10 and incremented by 2.
#     print(el)

# for i in range (10):
#     print(i)

# for i in range (2, 10):
#     print(i)

# nums = [1, 2, 4, 6, 8, 9, 10]

# for el in nums :
#     print(el)

# val = (12, 34, 45, 56, 67, 68, 79, 89, 92, 98, 100)
# x =89

# idx = 0
# for el in val :
#     if(el == x) :
#         print("element found at idx :", idx)
#     else :
#         print("finding...")
#         idx += 1

# for el in range(1, 101): # print no. from 1 to 100 using for loop and range function.
#     print(el)

# for el in range(2, 22, 2): #print the multiplication of 2 by using for loop and range function.
#     print(el)

# nums = (int(input("enter the number :")))

# for i in range (1, 11) :
#     print (nums * i)

# for i in range(10) :
#     pass             # pass statement is used to skip the current block as a null for future use.

# print("some useful work")


# wap to print the sum of natural number using for loop and range function.
# num = 5

# sum = 0
# for i in range (1, num + 1) :
#     sum += i

# print("total sum =", sum)

# num =  5

# sum = 0
# i = 1
# while i <= num :
#     sum += i
#     i += 1

# print("total sum =", sum)

# # function definition
# def cal_sum(a, b): # define function and a and b are the parameters of the function.
#     sum = 1034 + 1283
#     return(sum) #return value

# print(cal_sum(1034, 1283))  #function calling.

# def cal_avg(a, b):
#     avg = (a + b) / 2
#     return(avg)


# print(cal_avg(139, 13487))

# def val_sum(a, b, c, d):  # define function and add a, b, c, d and return the average of the parameters.
#     sum = a + b + c + d
#     avg = sum / 4
#     print(avg)
#     return avg

# print(val_sum(1348, 1944, 3485, 37945))

# def cal_sum(a, b, c):
#     sum = a + b + c
#     return(sum)

#     if(a > b and a > c):
#         print("a is grater :", a)
#     else:
#         print("b is greater :", b)

# print(cal_sum(1248, 3847, 3783))

# def cal_product(b, a = 28): #default argument used in this function definition.
#     product = a*b
#     print(a*b)
#     return(a*b)

# cal_product(2)


# name = ["ankit", "raju", "arvind", "ranjay", "rahul", "rohit"]

# def print_len(name):
#     print(len(name))

# print_len(name)

# #function definition
# def calsum(a, b, c): #define function and take a,b,c as parameter of function.
#     sum = a + b + c
#     return sum # return value to the function caller.

# print(calsum(1488, 1933, 4593)) #function call.

# waf to print the average of three numbers.
# def cal_avg(a, b, c):
#     sum = a + b + c
#     avg = sum / 3
#     return avg

# print(cal_avg(1237642, 34762385, 8762381))


# WaF to print the length of the list and (list is the parameter)

# cities = ["bihar", "goa", "delhi", "mumbai"]
# subject = ["dbms", "os", "oops", "dsa", "python", "java", "apti", "reasoning"]

# def print_len(list):
#     return(len(list))

# print(len(cities))
# print(len(subject))

# subject = ["python", "django", "flask", "dsa", "fastapi"]

# def print_list(list):
#     for item in list:
#         print(list)

# print(subject)

# WAF to find the factorial of n number and (n is the parameter).
# def cal_fact(n):
#     fact = 1
#     for i in range(1, n + 1):
#         fact *= i
#     print(fact)

# cal_fact(7)

# WAF to convert usd into inr using function. 
# def converter(usd_value):
#     inr_value = usd_value * 95.63
#     print(usd_value, "USD =", inr_value,"INR")

# converter(5)
    
# def show(n):
#     if(n == 0):
#         return
#     print(n)
#     show(n-1)

# show(5)

# WAF to print number and check whether it is even or odd.
# num = int(input("enter the number :"))

# def print_number(num):
#     return num
# if(num % 2 == 0):
#     print(num, "is EVEN")

# else:
#     print(num, "is ODD")

# print_number(10)

# RECURSIVE FUNCTION.
# def show(n):
#     if(n == -1):
#         return
#     print(n)
#     show(n-1)

# show(5)
# recursive function in which we print from 10 to 0.
# def show(m):
#     if(m == -1): # condition used in function is known as base case.
#         return
#     print(m)
#     show(m-1)

# show(10) # function call
# write the recursive function to print the factorial of 10.
# def factorial(m):
#     if(m == 0 or m == 1):
#         return 1
#     return factorial(m-1) * m

# print(factorial(5))

# def print_sum(n):
#     if(n == 0):
#         return 0
#     return print_sum(n-1) + n
# sum = print_sum(10)
# print(sum)

# def print_len(list):
#     print(list)
#     return list

# print(len("ankitkumar"))

# course = ["python", "java", "html", "css"]
# subject = ["cs", "ece", "civil", "mech"]

# def print_list(list):
#     for item in list:
#         print(item, end=" ")

# print_list(course)

# FILE I/O how to open the file before write and read.

# f = open("Demo.txt", "rt")
# data = f.read() # this function read data and return the data which stored in our file.
# print(data)
# print(type(data))
# f.close() # how to close file.

# f = open("Demo.txt", "r")
# data = f.read()

# line1 = f.readline(8)
# print(line1)

# line2 = f.readline(4)
# print(line2)

# line3 = f.readline(5)
# print(line3)

# print(data)

# f.close()

# f = open("sample.txt", "r") # IF we try to read or write on the file which not exist, then it will created automatically.
# data = f.read()
# f.close()

# f = open("Demo.txt", "r+") # if we use r+ character it will positioned at the beginning of the data and update the data with new one.
# data = f.write("abc")
# f.close()

# f = open("Demo.txt", "a+")
# data = f.write("abxorf")
# print(data)
# print(type(data))
# f.close()

# f = open("practice.txt", "w")
# data = f.write("hi everyone\nwe are learning file I/O\nusing java.\ni like rprogramming in java.")

# f = open("practice.txt", "r")
# movies = []
# movie1 = input("enter the first movie :")
# movies.append(movie1)
# movie2 = input("enter the second movie :")
# movies.append(movie2)
# movie3 = input("enter the third movie :")
# movies.append(movie3)

# print(movies)

# list1 =
# list2 = 

# copy_list1 = list1.copy()
# copy_list1.reverse()

# if(copy_list1 == list1):
#     print("palindrome")
# else:
#     print("not palindrome")

# grade = ("a", "c", "a", "d", "a", "e", "a")
# print(grade.count("a"))

# grade = ["a", "c", "d", "a", "e", "a"]
# grade.sort()
# print(grade)

# student = {
#     "name" : "ankit kumar",
#     "age" : 19,
#     "subject" : {
#         "maths" : 91, 
#         "english" : 88,
#         "hindi" : 89,
#     }
# }
# print(student)

# collection = set()
# #empty set syntax.

# collection = {12, 235, "name", "rahul"}
# print(type(collection))
# dict = {
#     "table" : "a piece of furniture",
#     "cat" : "a small animal"
# }
# print(dict)

subject = {"python", "java", "c++", "python", "javascript", "python", "c++", "c"}
print(type(subject))
print(len(subject))
