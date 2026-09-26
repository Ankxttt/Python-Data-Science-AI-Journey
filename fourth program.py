#object-orinted programming practice.
# class Student: #class name student.
#     name = "ankit kumar"

# s1 = Student()  #object of class student.
# print(s1.name)

# class BMW:
#     name = "m4"
#     color = "gamma-green"
#     brand = "BMW"

# car1= BMW()
# print(car1.color)
# print(car1.name)
# print(car1.brand)

# class Student:
#     def __init__(self, fullname, age):
#         self.name = fullname
#         self.age = age
#         print("adding new students detail in database")

# s1 = Student("ankitkumar", 19)
# print(s1.name, s1.age)

# s2 = Student("rahul", 21)
# print(s2.name, s2.age)

# s3 = Student("karan", 20)
# print(s3.name, s3.age)

#Ex:
# class Student:
#     #class attribute.
#     college_name = "xyz college"

#     def __init__(self, name, age, marks, branch): #object attribute.  (object attribute > class attribute)
#         self.name = name
#         self.age = age
#         self.marks = marks
#         self.branch = branch

#     def hello(self):            #method / function in class.
#         print("hello world")    

# s1 = Student("ankit", 19, 94, "computer")
# s2 = Student("karan", 20, 88, "electrical")
# s3 = Student("arjun", 21, 73, "civil")
# s1.hello()

# print(s1.name, s1.age, s1.marks, s1.branch)
# print(s2.name, s2.age, s2.marks, s2.branch)
# print(s3.name, s3.age, s3.marks, s3.branch)
# print(s1.college_name)

#Ex:
# class Student:
#     def __init__(self, name, marks, subject):
#         self.name = name
#         self.marks = marks
#         self.subject = subject

#     @staticmethod  #decorator
#     def hello():
#         print("hello")

#     def get_avg(self):
#         sum = 0
#         for val in self.marks:
#             sum += val
#         print("welcome", self.name, "your avg score :", sum /3, "in", self.subject)

# s1 = Student("ankit", [98, 88, 89], "maths")
# s1.get_avg()
# s1.hello()

# if we want to the data in my class, then we can easily changed it and it will print the new data.
# s1.name = "raju"
# s1.get_avg()
#Ex:
# class Account:
#     def __init__(self, balance, account_no):
#         self.balance = balance
#         self.account_no = account_no

#     def debit(self, amount, account_no):
#         self.balance -= amount
#         print("Rs", amount, "was debited from account no :", account_no)
#         print("total balance", self.get_balance())

#     def credit(self, amount, account_no):
#         self.balance += amount
#         print("Rs", amount, "was credit in your account no :", account_no)
#         print("total balance", self.get_balance())

#     def get_balance(self):
#         return self.balance
    
# account1 = Account(10000, 223422)
# account1.debit(1000, 223422)
# account1.credit(900, 223422)

# deleting the object properties & object itself using del keyword:
# class Student:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

# s1 = Student("ankit", 19)
# print(s1.name, s1.age)

# del s1.name    # del keyword is used to delete the object's attribute & whole object itself.
# print(s1.name)

# private attribute & methods of oops in python:
# class Account:   # we create an class acount with account no,password.
#     def __init__(self, acc_no, acc_pass):
#         self.acc_no = acc_no
#         self.acc_pass = acc_pass    # password,acc-no attribute are accessible within and outside the class which is called public attribute.

#     def password(self):
#         print(self.acc_pass)      # password method are accessible within and outside the class which is called a public method. 

    
# acc_1 = Account("1234", "ankit@234")
# print(acc_1.acc_no, acc_1.acc_pass) # public attribute & methods are accessible from outside the class.
# acc_1.password()

#Ex: private atttribute & methods are not accessbile from outside the class.
# class Student: # private attri.& methods are not directly accessible from outside the class but internal function can access them which is only available inside the class. 
#     def __init__(self, name, branch):
#         self.name = name
#         self.__branch = branch  # this attribute are not accessible from outside the class.

#     def __hello(self):
#         print("beella ceao")    # this is also not accessible from outside the class.

# s1 = Student("ankit", 19)
# print(s1.__branch)
# s1.__hello()

#Ex : we can access them by another internal function which call the private method and we call that public method outside the class.
# class Student:
#     def __init__(self, name, age):
#         self.name = name
#         self.__age = age   # this private attri. cannot be accessed from outside the class, but only, internal function of this class can access them because it always inside the class.

#     def __hello(self):
#         print(self.__age)  # this private method can access the private attri. but we cannot access them outside of the class directly but we can call that method into another internal function which is public and we can call that function to outside the class.

#     def welcome(self):
#         self.__hello()

# s1 = Student("ankit", 19)

# print(s1.welcome()) # this is how we can prevent the exposure of our instance attri. from outside the class.
            









