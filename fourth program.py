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


# s1.name = "raju"
# s1.get_avg()

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

class Student:
    def __init__(self, name, marks, subject):
        self.name = name
        self.marks = marks
        self.subject = subject

    def get_avg(self):
        sum = 0
        for val in self.marks:
            val += sum
        print("welcome", self.name, "your avg score is :", sum/3, "in", self.subject)

s1 = Student("ankit", [89, 90, 99], "maths")
s1.get_avg()




 




     


















