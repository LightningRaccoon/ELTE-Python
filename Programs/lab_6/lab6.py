'''
from abc import *

class Nothing(metaclass=ABCMeta):
    def print_star(self):
        pass

class Something(Nothing):
    def __init_subclass__(self):
        pass
    def print_star(self):
        print('star')

var1 = Nothing()
var1.print_star()

import os
print(os.getcwd())
os.chdir('D:\Feladats\python_demonstartor\lab_6\my_first_dir')
print(os.getcwd())
os.system('date')

import datetime

today = date.today()

'''

#inheritance/öröklődés

class Animal:
    def __init__(self, name):
        self.name = name

class Cat(Animal):
    def __init__(self, name, age):
        super().__init__(name)
        self.age = age

cat1 = Cat('Cirmi', 5)
print(cat1.name)
print(cat1.age)

#try/except
print('reciprok')

def reciprocal(n):
    try:
        n = 1 / n
    except ZeroDivisionError:
        print("Division failed")
        n = None
    else:
        print("Everything went fine")
    finally:
        print("It's time to say goodbye")
        return n
print(reciprocal(2))
print(reciprocal(0))

print("")

try:
    i = int("Hello!")
except Exception as e:
    print(e)
    print(e.__str__())

def print_exception_tree(thisclass, nest = 0):
    if nest > 1:
        print(" |" * (nest - 1), end="")
    if nest > 0:
        print(" +---", end="")
    print(thisclass.__name__)
    for subclass in thisclass.__subclasses__():
        print_exception_tree(subclass, nest + 1)



#my_exception


class MyZeroDivisionException(ZeroDivisionError):
    pass

def if_true(statement):
    if statement:
        raise MyZeroDivisionException("MyZeroDivisionException happened")
    else:
        raise ZeroDivisionError("ZeroDivisionError happened")

try:
    if_true(True)
except MyZeroDivisionException:
    print("There was MyZeroDivisionException")
print("everything else was fine")


import os

#os.mkdir("ujmappa")
print(os.listdir())
#os.makedirs("my_first_directory/my_second_directory")

print(os.getcwd())
os.chdir('D:\Feladats\python_demonstartor\lab_6\my_first_dir')
print(os.getcwd())

#os.rmdir('D:\Feladats\python_demonstartor\lab_6\my_first_dir')

#datetime
from datetime import date
today = date.today()
print("Today:", today)
print("Year:", today.year)
print("Month:", today.month)
print("Day:", today.day)
