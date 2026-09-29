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

# ENCAPSULATION: whenever we create a class with various attri. and methods, we only show the esssential features to the user and hide the implementation details from the users.
# class car: # this car have many features and it has mechanism to start and stop the car.
#     def __init__(self, car_acc, car_brk):
#         self.car_acc = car_acc
#         self.car_brk = car_brk

#     def car_stop():  #car stop mechanism (function).
#         car_acc = False
#         car_brk = False
#         print("car stopped...")

#     def car_start():  #car start mechanism (function).
#         car_acc = True
#         car_brk = True
#         print("car started..,")

# print(car.car_start())  # this is how user access the essential feature of car and we hide the mechanism that how car start and stop.
# print(car.car_stop())   # so, this is how encapsulation works.

# Inheritance: when one class(derived, child) derived or inherit properties, attri. and methods from (base, parent)class.
# class bike:  # this is the base class with various methods like start, stop.
#     color = "black"  # if we define any object, base class can access them too.
#     @staticmethod
#     def start():
#         print("bike started..")

#     def stop():
#         print("bike stopped..")

# class yamaha(bike):  # this is the derived class and it can access the properties & attributes of the base class.
#     def __init__(self, brand):
#         self.brand = brand

# b1 = yamaha("R15")       # this is also known as single inheritance.

# print(b1.brand)
# print(b1.color)
# print(b1.start())

#types of inheritance :
#single inheritance:  in this, only one base class with 
# class car:    # base class

#     @staticmethod     # base class methods
#     def start():
#         print("car started..")

#     @staticmethod     # base class methods
#     def stop():
#         print("car stopped..")

# class mahindracar(car):    # derived class
#     def __init__(self, brand):
#         self.brand = brand

# car1 = mahindracar("scorpio")

# print(car1.brand)    # so, it can access all the properties and methods from base class by calling base class in derived class.
# car1.start()
         
# multi-level inheritance: # when one class inherit attri. & methods from from another class and third class inherit from that derived class, which become base for that class.
# class car:                  # base class with start, stop method.
#     def start(self):
#         print("car started...")

#     def stop(self):
#         print("car stopped...")

# class mahindra(car):           # child class with attribute,methods and inherit all the feature, methods from base class.
#     def __init__(self, brand, model):
#         self.brand = brand
#         self.model = model

# class scorpio(mahindra):         # another child class with own attribute and methods and inherit all attri.,methods from base and derived class both.
#     def __init__(self, type, version, brand, model):
#         super().__init__(brand, model)    # this is super() method, when we want to inherit all the attri. with constructor from parent class, we use super method which helps to inherit all the object -attri, methods from both parent and child class.
#         self.type = type
#         self.version = version

#     def type_info(self):
#         print("Suv")

# car1 = scorpio("scorpio", "2026", "3.2 litre", "petrol")

# print(car1.version)    # in multiple inherit. one class inherit attr., methods from one class and thir one inheit attri, method from the base and that derived class both.
# print(car1.type)
# print(car1.brand)
# print(car1.model)
# car1.start()
# car1.type_info()

#multiple inheritance: one child class inherit attri, methods from one or more parent class.
# class car:      # base class 1 with methods and attri.

#     @staticmethod
#     def car_info():
#         print("car is powerful...")

# class mahindra(car):    # base class 2 with methods and attr.

#     @staticmethod
#     def mahindra_info():
#         print("mahindra car is more powerful...")

# class scorpio(mahindra, car):   # child class which inherit attri., and methods of both parents class.

#     @staticmethod
#     def scorpio_info():
#         print("scorpio is top vehicle of mahindra company..")


# car1 = scorpio()    # it can inherit attrributes and method of both parent class.

# print(ar1.car_info()) 
# print(car1.mahindra_info())
# print(car1.scorpio_info())

#Ex: Multiple inheritance.
# class A:                            # parent class 1
#     VarA = "welcome in A..."

# class B:                            # parent class 2
#     VarB = "welcome in B..."

# class C(A,B):                       # child class which inherit attributes and method of both parent and child class.
#     VarC = "welcome in C..."

# c1 = C()
# print(c1.VarA, c1.VarB, c1.VarC)

# using super()method which helps to inherit all attributes and methods of parent class.
class car:
    def __init__(self, name):
          self.name = name

    @staticmethod
    def start():
           print("car started...")

    @staticmethod
    def stop():
           print("car stopped...")      

class Landrover(car):
        def __init__(self, name, model, version):
            super().__init__(name)
            self.model = model
            self.version = version

        def type_info(self):
            print("type : SUV")

class RangeRover(Landrover):
      def __init__(self, name, variant, segment, model, version):
            super().__init__(name, model, version)
            self.variant = variant
            self.segment = segment

car1 = RangeRover("autobiography", "petrol", "3.2 litre", 2024, "hybrid")

print(car1.name)
print(car1.variant)
print(car1.segment)
print(car1.model)
print(car1.version)
car1.start()
car1.type_info()












