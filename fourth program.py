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
#         print("total balance :", self.get_balance())

#     def credit(self, amount, account_no):
#         self.balance += amount
#         print("Rs", amount, "was credit in your account no :", account_no)
#         print("total balance :", self.get_balance())

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
# class car:    # base class with methods and attributes.
#     def __init__(self, name):
#           self.name = name

#     @staticmethod
#     def start():
#            print("car started...")

#     @staticmethod
#     def stop():
#            print("car stopped...")      

# class Landrover(car):    # child class which inherit attri. & methods of base class with super()method.
#         def __init__(self, name, model, version):
#             super().__init__(name)
#             self.model = model
#             self.version = version

#         def type_info(self):
#             print("type : SUV")

# class RangeRover(Landrover):  # another child class which inherit properties and attribute and methods from both base class and derived class which become base for this class.
#       def __init__(self, name, variant, segment, model, version):    # if we don't use @staticmethod to call function, we can access them by call self in the paranthesis.
#             super().__init__(name, model, version)
#             self.variant = variant
#             self.segment = segment

# car1 = RangeRover("scorpio", "petrol", "3.2 litre", 2024, "hybrid")

# print(car1.name)   # we can access all teh attributes and methods of base class by using super() method.
# car1.start()
# print(car1.variant)
# print(car1.segment)
# print(car1.model)
# print(car1.version)
# car1.type_info()
#Ex: using super() method to access attri. & methods of parent class.
# class car:
#     def __init__(self, name, color):
#         self.name = name
#         self.color = color

#     @classmethod
#     def start(cls):
#         print("car started...")

#     @classmethod
#     def stop(cls):
#         print("car stopped...")

# class toyota(car):
#     def __init__(self, name, color, model, version):
#         super().__init__(name, color)
#         self.model = model
#         self.version = version

#     @staticmethod
#     def type_info():
#         print("type : suv")    

# class fortuner(toyota):
#     def __init__(self, name, color, model, version, variant, segment):
#         super().__init__(name, color, model, version)
#         self.variant = variant
#         self.segment = segment
#         super().start()
#         super().type_info()

# car1 = fortuner("fortuner", "black", 2026, "variant : petrol", "3.2 litre", "suv")
# print(car1.name)
# print(car1.color)
# print(car1.model)
# print(car1.version)
# print(car1.variant)

# using class method to access, modify or perform operation on the paticular class attributes and methods.
# class car:  # we create a baseclass car with name attri. (fortuner) and try to change it with new one.
#      name = "fortuner"

#      def changename(self, new_name):  # so, we create a object method to change the name of class car.
#           self.name = new_name        # but it didn't change the name of base class, it create a new name attri. for that object and change name of that object not i base class.

# car1 = car()                          # we create object.
# car1.changename("scorpio")        # we try to change name of base class, but it create new name attri. for that object instead of changing name of base class car, which means we cannot change name of class attr. with the object method because it didn't access them.
# print(car.name)
# print(car1.name)          

#Ex: we can change it by using various technique like: using class name, using __class__ constructor.
# class car:   # we create base class with name atri.
#     name = "mahindra"

#     def changename(self, new_name):  # we create method to change name of class with new name by object method(self).
#         self.__class__.name = new_name         # 1st technique: we can change it by calling name of class in object method, and 2nd technique is we can call __class__ constructor in object methods with its refernce(self).
#         car.name = new_name

# car1 = car()
# car1.changename("toyota")
# print(car1.name)
# print(car.name)

#Ex: using @classmethod decorator to access, modify or perform operation on class attri. & methods.
# class car:    # base class with class attributes and methods.
#     name = "scorpio"     # we pass class attri. name and color to access and modify them by using class method.
#     color = "black"

#     def __init__(cls, name, color):  # we create constructor and 1st implicit argument is cls which is a refernce to class attri. & method just like (self) for object attri. & methods.
#         cls.name = name
#         cls.color = color

#     @classmethod     # we pass class method decorator to which convert function into class method and we used to access and modify them.
#     def start(cls):
#         print("engine started...")

#     @classmethod     
#     def stop(cls):
#         print("engine stopped...")

#     @classmethod     # we create a class method to change the name of car by using @classmethod decorator.
#     def change_name(cls, new_name):   # first implicit argument is cls then parameters
#         cls.name = new_name           # same like a self parameter which is used toa access and modify the object attri. and methods, cls is the refrence for class attri. & methods.
#         print("car name changed to :", cls.name)    # it will print the new name of base class car.

# class mahindra(car):      # derived class which inherit base class attri. and methods.
#     def __init__(self, name, color):    # constructor created for the ojects attri. and methods by calling self.
#             super().__init__(name, color)
#             self.name = name
#             self.color = color
#             super().start()
#             super().stop()


# car1 = mahindra("fortuner", "black")
# print(car1.name)
# print(car.name)            # we print it didn't change the name of base class.
# car.change_name("bolero")  # we can change name of base class and then we will print, it will change the name permanently.
# print(car.name)

# without using an @property decorator to any method of class to use that method as a property(attribute).
# suppose we have an attributes which their value will change in future, it's value is not fixed, so it depend on another function and we use that function as a property.
# class subject:  # class of subject
#     def __init__(self, phy, chem, maths):  # we have 3 attri. of subject class
#         self.phy = phy
#         self.chem = chem
#         self.maths = maths
#         self.percentage = str((self.phy + self.chem + self.maths)/ 3) + "%"  # we perform operation get percentage from 3 subject. suppose one of the subject mark get change in future then we have to store new percentage. 

#     def cal_percentage(self): #we create a method get percentage
#         self.percentage = str((self.phy + self.chem + self.maths)/3) + "%"

# cgpa = subject(89, 82, 85)  # marks of 3 subject.

# print(cgpa.phy)
# print(cgpa.percentage)

# cgpa.phy = 99              # suppose marks get change from any subject in future then we have to get new percentage according to it, so we have to change it manually.
# print(cgpa.phy)            # which is very complex and take much line of codes.
# cgpa.cal_percentage()
# print(cgpa.percentage)

#using @property decorator to perform same task:
# class Student:                            #class of student
#     def __init__(self, phy, chem, maths):    # 3 attri. 
#         self.phy = phy
#         self.chem = chem
#         self.maths = maths

#     @property                           # now we use property decorator in class mehtod which make method as property/attr and their value change in future, then the method will change automatically,not need to perform manually.
#     def percentage(self):
#         return str((self.phy + self.chem + self.maths)/3) + "%"

# stu1 = Student(91, 90, 88)

# print(stu1.phy)
# print(stu1.percentage)

# stu1.phy = 80                # attri. value change then their percentage will automatically changed.
# print(stu1.percentage)       # that's why we use @property to any method of class and objects.   
# print(stu1.phy)

#Ex: using @property decorator
# class Employee:                         # employee have salary and bonus.
#     def __init__(self, salary, bonus):
#         self.salary = salary
#         self.bonus = bonus

#     @property                            # we use @property decorator to calculate total salary, if any one of attri. change, then total_salary will change automatically and we can print them without calling method and using ()parenthesis.
#     def total_salary(self):
#         return str(self.salary + self.bonus)
        
# emp1 = Employee(50000, 5000)       

# print(emp1.salary, emp1.bonus)
# print(emp1.total_salary)                 # we call that method as an attribute with using()parenthesis and no need call the method, it allow to controlled access to object's attributes.

# emp1.salary = 60000               #if salary change then total salary change automatically, no need to do it manually and we can call them without ()parenthesis.
# print(emp1.total_salary)

#Ex: using @property decorator with getter and setter to print marks by putting validation in the value:(condtion)
# class subject:                       # we create class subject.
#     def __init__(self, marks1, marks2):
#         self._marks1 = marks1        # we use _marks instead of marks because setter call it again & again which causes recursion. we use _marks as an private-convention storage where value stored and marks is used as an public controlled property.
#         self._marks2 = marks2     # simply marks is a public property and _marks is a private/backing attribute which store value in it and we can be access through the property because we don't want to access them directly outside the class which increase the chance of changes/modification to the store value in it.

#     @property
#     def marks1(self):           # suppose we don't want outside code to access/modify actual store value, so we keep it into the _value as private-convention-storage and expose the value through the property,so the value is public controlled interface and _value is where the data stored and when we call obj.value,it return value store in _value.
#         return self._marks1      # we don't use normal self.marks because when sel.value call the value property again and again which causes infinite recursion.

#     @marks1.setter          # it used to put validation to value and give control over changing of an attribute outside the class.
#     def marks1(self, value):  # it give control over(anyone can change the stored value outside the class) and it avoid to put any invalid data.
#         if 0 < value <= 100:
#             self._marks1 = value

#         else:
#             print("Invalid marks")

#     @property                 # Each attr. have its own property and each property has its own getter,setter,deleter.
#     def marks2(self):         
#         return self._marks2

#     @marks2.setter
#     def marks2(self, value):
#         if 0 < value <= 100:
#             self._marks2 = value

#         else:
#             print("Invalid marks")

#     @property         # it also represent calculated value which depends on other attributes, it didn't store it separately, it calculate it whenever we access them.
#     def total_marks(self):   # whenever attr. change then the new derived/calculated value print automatically, no need to store it manually everytime.
#         return str(self.marks1 + self.marks2)    
    
# result = subject(89, 90)
# print(result.total_marks)  # so, it tell other propgrammer we didn't directly access and call obj._value , we can acccess the value through the @property. 

# result.marks2 = 150
# print(result.total_marks)

#Ex2:
# class person:
#     def __init__(self, _age):
#         self.age = _age

#     @property
#     def age(self):
#         return self._age

#     @age.setter
#     def age(self, value):
#         if value >= 0:
#             self._age = value

#         else:
#             print("Age cannot be negative.")

# p = person(20)
# print(p._age)

# p.age = -100
# print(p.age)

#Ex: using @ property decorator with getter and setter and put validation inside the the value by using _value name convention which help to store value in private/backing attribute.
# class Mycls:
#     def __init__(self, value):
#         self._value = value

#     @property
#     def value(self):
#         return self._value

#     @value.setter
#     def value(self, value):
#         if 0 < value <= 100:
#             self._value = value

#         else:
#             print("Invalid value...")

# cls1 = Mycls(90)

# print(cls1.value)

# cls1.value = 100
# print(cls1.value)

#Ex: using @property decorator with @setter and @deleter decorators.
# class car:
#     def __init__(self, model, number):
#         self._model = model
#         self._number = number

#     @property
#     def model(self):
#         return self._model

#     @model.setter
#     def model(self, value):
#         if 2018 < value <= 2026:
#             self._model = value

#         else:
#             print("Model is not valid")                                                                                   

#     @property
#     def number(self):
#         return self._number

#     @number.setter
#     def number(self, value):
#         if 0000 < value <= 9999:
#             self._number = value

#         else:
#             print("Number is not available")

#     @number.deleter
#     def number(self):
#         del self._number       

# mahindra = car(2020, 8019)

# print(mahindra.model)
# print(mahindra.number)

# mahindra.model = 2021
# print(mahindra.model)

# del mahindra._number
# print(mahindra._number)

#Ex: using @property with @setter to put validation to the value and give control over changing the values of objects.
# class Subject:
#     def __init__(self, marks):
#         self._marks = marks

    
#     def show(self):
#         print(f"this is {self._marks}")

#     @property
#     def marks(self):
#         return 10*self._marks

#     @marks.setter
#     def marks(self, new_value):
#         self._marks = new_value/10

# s1 = Subject(40)

# print(s1.marks)

# s1.marks = 100
# print(s1.marks)
# s1.show()

#Ex: using @property and @setter to print email and change the email using split()function.
class Employee:                          # class Employee
    def __init__(self, fname, lname):
        self._fname = fname           #first parameter first name.
        self._lname = lname           #second parameter second name.

    def show(self):                 # we create a normal function show() to print attri.
        print (f"This is {self._fname} {self._lname}.")  
 
    @property                          # now, we use @propeerty decorator return email.
    def email(self):
        return (f"{self._fname}.{self._lname}@gmail.com")    # in this we use format() string method to print value in a single line of code which increase code readability.

    @email.setter            #then, we use @setter decorator to put validation on name values and give control over changing the email's first name and last name.
    def email(self, new):
        name = new.split("@")[0]    # we use split() function to change first and last name of the email and return to the user with new email.
        self._fname, self._lname  = name.split(".")

    @email.deleter
    def email(self):
        del sub.email
    

sub = Employee("Ankit", "Kumar")
print(sub.email)
sub.show()

sub.email = "raju.rajiv@gmail.com"
print(sub.email)      # we call them as an attribute not like a method with () parenthesis.
del sub.email
print(sub.email)
