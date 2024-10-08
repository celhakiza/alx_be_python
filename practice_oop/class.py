import pandas as pd

'''
Exercise 1: Creating a Student Class

Instructions:

Define a Student class with attributes like name and age. Include a method to display student information.
'''

class Student:

    def __init__(self, name,age):
        self.name = name
        self.age = age

    def student_inf(self):
        print(f"Student Name: {self.name}")
        print(f"Student Age: {self.age}")


stu = Student("celestin",20)
#stu.student_inf()
'''
Exercise 2: Creating a Product Catalog

Instruction:

Define a Product class with attributes like name, price, and quantity. 
Implement a method to calculate the total value of products in stock.
'''

class product:

    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

    def value_product(self):
        return self.price * self.quantity


pro = product("Laptop",20,30)
print(pro.value_product())

'''
Practice Exercises
Exercise 1: Handling ZeroDivisionError

Instructions:

Write a program that takes two numbers as input from the user and divides the first number by the second number.
Handle the ZeroDivisionError exception to inform the user if they attempt to divide by zero.
Exercise 2: File Handling with FileNotFoundError

Instructions:

Write a program that attempts to open and read data from a file specified by the user.
Handle the FileNotFoundError exception to provide a meaningful message if the file does not exist.
Exercise 3: Custom Exception

Instructions:

Create a custom exception class called ValueTooHighError that inherits from the Exception class.
Write a program that takes a number as input and raises a ValueTooHighError exception if the number is greater than 100.

'''
