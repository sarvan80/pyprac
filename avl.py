import pandas as pd
import numpy as np
import keras



class treenode:
    def __init__(self, key):
        self.key = key

class binarytree():

    def __init__(self):
        pass

class avltree(binarytree):

    def __init__(self):
        super().__init__()

####### references #######
# Reference examples: calling a parent class initializer with super()
# -------------------------------------------------------------------

# General pattern:

    class Parent:
        def __init__(self, name):
            self.name = name

    class Child(Parent):
        def __init__(self, name, age):
            super().__init__(name)  # Initialize the Parent part
            self.age = age

    person = Child("Sam", 20)
    print(person.name)  # Sam
    print(person.age)   # 20

# Vehicle and car:

    class Vehicle:
        def __init__(self, color):
            self.color = color

    class Car(Vehicle):
        def __init__(self, color, brand):
            super().__init__(color)
            self.brand = brand

    car = Car("blue", "Toyota")
    print(car.color)  # blue
    print(car.brand)  # Toyota

# User and admin:

    class User:
        def __init__(self, username):
            self.username = username

    class Admin(User):
        def __init__(self, username, permissions):
            super().__init__(username)
            self.permissions = permissions

    admin = Admin("alex", ["manage_users", "view_reports"])
    print(admin.username)     # alex
    print(admin.permissions)  # ['manage_users', 'view_reports']

# When the parent initializer takes no arguments:

    class Logger:
        def __init__(self):
            self.messages = []

    class FileLogger(Logger):
        def __init__(self, filename):
            super().__init__()
            self.filename = filename

    logger = FileLogger("app.log")
    print(logger.messages)  # []
    print(logger.filename)  # app.log

    # method inheritence

    class Parent:
        def __init__(self):
            self.value = 10

        def describe(self):
            return f"value is {self.value}"

    class Child(Parent):
        def __init__(self, name):
            super().__init__()
            self.name = name

    child = Child("Alex")
    print(child.describe())  # value is 10



####### references end #######
