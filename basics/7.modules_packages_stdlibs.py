# modules and packages

# module search hierachy and paths
1. The directory containing the input script (or the current directory when no file is specified).
2. PYTHONPATH (a list of directory names, with the same syntax as the shell variable PATH).
3. The installation-dependent default (by convention including a site-packages directory, handled by the site module).

# Modules

# module1

print("printing from new module..")

name = "Pavan"
comp = "vcollab"

def match_string(fruits, targets="apple"):
    filter_fruits = []
    for i, value in enumerate(fruits):
        for target in targets:
            if target == value: filter_fruits.append(target)
    return filter_fruits
    

# main module

import module_directory.module1 as msd

fruits = ['apple', 'banana', 'grapes', 'pear', 'apricot', 'guava', 'apple']
filtered_fruits = msd.match_string(fruits, targets=["apple", 'pear'])
print(filtered_fruits)

# import module_same_dir as msd

name = "Preetham"

print(msd.name)

print(name)

msd.name = name
print(msd.name)

##

# using * to import all public objects in the current namespace, but using global for the object with same name get new value
# in the current space

from module_same_dir import *

print(name)

def foo():

    global name
    name = "preetham"

foo()

print(name)

##

import module_same_dir

import module_directory.module_inside_dir

import sys
sys.path.append(r"C:\Users\pavan\Desktop\external_modules_dir")

import module1

import sub_module.module2

print(sys.path)

import module3

###

encrypted files *.pyc

cached files

# Will have more priority in packages while indexing of modules 

##

Packages

###


# standard libraries

import os
cwd = os.getcwd()

def current_path():
    print(os.getcwd())
current_path()
os.chdir('../')
current_path()

directory = "new_directory"
parent_dir = "C:/Users/pavan/PycharmProjects"
path = os.path.join(parent_dir, directory)
mode = 0o666
os.mkdir(path, mode)
print("Directory '% s' created" % directory)

dir_list = os.listdir(path)

#

import random
fruits = ['apple', 'banana', 'grapes', 'pear', 'apricot', 'guava', 'apple']
print(random.choice(fruits))

import math

angle1 = 90
angle2 = 0
radians1 = math.radians(angle1)
print(math.sin(radians1))
radians2 = math.radians(angle2)
print(math.sin(radians2))

import datetime
print(datetime.date.today())
print(datetime.datetime.now())


from time import gmtime, strftime
print(strftime("%d-%m-%Y %H:%M:%S", gmtime()))

import calender
print(calender.isleap())
