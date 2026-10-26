#1. Create a class Person whose constructor takes age as an argument. Raise a ValueError if the age is less than 0.

# class Person:
#     def __init__(self,age):
#         if age<0:
#             raise ValueError("age cannot be negative")
#         self.age=age
# try:
#     a=int(input("enter age:"))
#     p=Person(a)
#     print("age:",p.age)
# except ValueError as e:
#     print(e)


#2. Write a function named find_length(obj) that uses a loop to calculate the length of the given object without using the built-in len() function. The function should return the calculated length if the object is iterable. If a non-iterable object such as an integer is passed, the function should raise and handle a TypeError, and print an appropriate error message explaining what happens when an integer is sent as input.
def find_length(obj):
    c = 0
    try:
        if isinstance(obj, (str, list, tuple, set, dict)):
            for i in obj:
                c += 1
            return c
        else:
            raise TypeError("Send only iterable objects")
    except TypeError as te:
        print(te)

print(find_length('12345'))
print(find_length(56))


# 3.Create a class Student with an attribute marks. Implement a method set_marks(marks) that raises a ValueError if marks are not in the range 0 to 100.

# class Student:
#     def set_marks(self, marks):
#         if marks < 0 or marks > 100:
#             raise ValueError("Marks must be between 0 and 100")
#         self.marks = marks
#
# try:
#     s = Student()
#     marks = int(input("Enter marks: "))
#     s.set_marks(marks)
#     print("Marks:", s.marks)
# except ValueError as e:
#     print(e)


# 4.Create a custom exception named InvalidAgeError. Create a class Voter with a method check_eligibility(age) that raises this exception if age is less than 18.

# class InvalidAgeError(Exception):
#     pass
# class Voter:
#     def check_eligibility(self,age):
#         if age<18:
#             raise InvalidAgeError("not eligible to vote")
#         print("eligible to vote")
# try:
#     age=int(input("enter age: "))
#     v=Voter()
#     v.check_eligibility(age)



# except InvalidAgeError as e:
#     print(e)
# except ValueError:
#     print("enter valid integer")


# 5.Create a class BankAccount with an attribute balance. Implement a method withdraw(amount) that raises an exception if the withdrawal amount is greater than the available balance.

# class BankAccount:
#     def __init__(self,balance):
#         self.balance=balance
#     def withdraw(self,amount):
#         if amount>self.balance:
#             raise ValueError("insufficient balance")
#         self.balance=self.balance-amount
#         print("remaining balance:",self.balance)
# try:
#     balance=int(input("enter balance:"))
#     amount=int(input("enter withdraw amount:"))
#     b=BankAccount(balance)
#     b.withdraw(amount)
# except ValueError as e:
#     print(e)


# 6.Create a class PasswordValidator with a method validate(password). Raise an exception if the password length is less than 8 characters.

# class PasswordValidator:
#     def validate(self,password):
#         if len(password)<8:
#             raise ValueError("password must consists of 8 characters")
#         print("valid")
# try:
#     a=(input("enter password:"))
#     p=PasswordValidator()
#     p.validate(a)
# except ValueError as e:
#     print(e)


# 7.Create a class UserInput with a method get_integer(value). Handle ValueError and TypeError using separate except blocks.

# class UserInput:
#     def get_integer(self, value):
#         try:
#             num = int(value)
#             print("Integer:", num)
#         except ValueError:
#             print("ValueError: Invalid value")
#         except TypeError:
#             print("TypeError: Invalid data type")
#
# try:
#     a = (input("Enter a value: "))
#     u = UserInput()
#     u.get_integer(a)
# except Exception as e:
#     print(e)


# 8.Create a base class Shape with a method area() that raises NotImplementedError. Create a child class Rectangle that overrides and implements the area method.

# class Shape:
#     def area(self):
#         raise NotImplementedError("Area method must be implemented")
#
# class Rectangle(Shape):
#     def __init__(self, length, breadth):
#         self.length = length
#         self.breadth = breadth
#     def area(self):
#         return self.length * self.breadth
# try:
#     length = int(input("Enter length: "))
#     breadth = int(input("Enter breadth: "))
#     r = Rectangle(length, breadth)
#     print("Area of rectangle:", r.area())
# except ValueError:
#     print("Please enter valid integers")


#9. Create a class Service with a method that calls another method which raises an exception. Catch and handle the exception in the Service class

class Service:
    def method1(self, num):
        if num < 0:
            raise ValueError("Negative numbers are not allowed")
        print("Number:", num)
    def method2(self, num):
        try:
            self.method1(num)
        except ValueError as e:
            print(e)
try:
    n = int(input("Enter a number: "))
    s = Service()
    s.method2(n)
except ValueError:
    print("Please enter a valid integer")


# 10. Create a class Transaction with a method process() that uses try, except, and finally blocks to ensure a cleanup message is always printed.

# class Transaction:
#     def process(self, amount):
#         try:
#             print("Processing transaction")
#             if amount < 0:
#                 raise ValueError("Amount cannot be negative")
#             print("Transaction successful")
#         except ValueError as e:
#             print(e)
#         finally:
#             print("Cleanup completed")
# try:
#     amount = int(input("Enter transaction amount: "))
#     t = Transaction()
#     t.process(amount)
# except ValueError:
#     print("Please enter a valid integer")


#11. Create a class LoginSystem with a method login(password) that raises an exception for an incorrect password and handles the exception outside the class.

class LoginSystem:
    def login(self, password):
        if password != "python123":
            raise ValueError("Incorrect password")
        print("Login successful")

try:
    password = input("Enter password: ")
    l = LoginSystem()
    l.login(password)
except ValueError as e:
    print(e)
