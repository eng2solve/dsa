# Create class User with constructor
# Answer constructor is a special method which is automatically called 
# when the object is created from the class The method __new__ is the constructor that creates a new instance of the class
#  while __init__ is the initializer that sets up the instance's attributes after creation.
class User:
    def __init__(self,userId,name,email,age,gender): #parametrized constructor
        self.user_id=userId
        self.name=name
        self.email=email
        self.age=age
        self.gender=gender
user=User(1,'durgesh','dg@gmail.com','26','m')
# print(user.name)
        
# Add method to display user info
class User:
    def __init__(self,userId,name,email,age,gender): #parametrized constructor
        self.user_id=userId
        self.name=name
        self.email=email
        self.age=age
        self.gender=gender
    
    def __str__(self):
        return f"ID: {self.user_id}\n  Name: {self.name}\n  Email: {self.email}\n Age:{self.age}\n Gender:{self.gender}"
    
print(User(1,'durgesh','dg@gmail.com','26','m'))

# Inheritance example
class Animal:
    def __init__(self,name,owner):
        self.name=name
        self.owner=owner
    
class Dog(Animal):
    def info(self):
        print("Animal info:",self.name ,"is owned by",self.owner, "is a dog")
d=Dog('rocky','tejas')
print(d.info())
# Override method
class Parent:
    def __init__(self):
        self.value="This is parent value which will be inherited in the child class"
class Child(Parent):
    def __init__(self):
        super().__init__()
        self.value="Overriting the value of parent"
    def display(self):
        print(self.value)
d=Child()
print(d.display())

# Use @classmethod
class MyClass:
    @classmethod
    def class_method(cls):
        return "This is a class method"
print(MyClass().class_method())
# Use @staticmethod

class Person:
    def __init__(self):
        self.name='Durgesh'
        self.age='26'
        self.gender="M"
    @staticmethod
    def check_gender(gender):
        if gender=='m' or gender=='M': return "Male" 
        elif gender=='f' or gender=='F': return "Female"
        else: return 'other'
person=Person()
print(person.check_gender('M'))

# Encapsulation using private variable
class Employee:
    def __init__(self):
        self.name="Durgesh"
        self.__salary=67000 ##private defined with __ and protected with _
    def show_salary(self):
        print(self.__salary)
detail=Employee()
# print(detail.__salary) #wrong way
print(detail.show_salary())

# Create custom exception
class CustomError(Exception):
   def __init__(self, message):
      self.message = message
      super().__init__(self.message)
def check_value(value):
   if value < 0:
      raise CustomError("Please enter positive number you dumb")
   else:
      return value
try:
   result = check_value(-5)
   print(result)
except CustomError as e:
   print(f"Exception {e.message}")

# Handle file exception
try:
    with open("files/demo1.txt",'r') as file:
        content=file.read()
except FileNotFoundError:
    print("File not fount at the destination")
except PermissionError:
    print("Don't have the permission to update file")
except IOError as e:
    print("something went wrong",e)

# Create mini BankAccount class
class Account:
    def __init__(self, account_number, name, balance=0.0):
        self.account_number = account_number
        self.name = name
        self.balance = balance
