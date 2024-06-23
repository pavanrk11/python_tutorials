# this is a single line comment
#

"""
 This is a multi line comment
"""

#
#
#

# Expressions/Operators

# Constant expression
a = 5
b = 5 + 10
c = 10 + 20

# Arithmatic expressions

x = b + c
y = b * c
z = b / c
r = b // c
s = b % c
t = b ** 2
# print(x, y, z, r, s, t)

# Integer expression
d = 5 + int(9.5)

# float express
f = 5.0 + float(9)

# relational expression

a = 5
b = 10
c = 20
p = a > b

# logical expressions
a = 5
b = 10
c = 20

p = (a >= b) and (b < c)
q = (a >= b) or (b < c)
r = not (a >= b)

# bitwise expressions
a = 10
b = a
print("a & b =", a & b)
print("a | b =", a | b)

# Combined expression

# BODMAS or PEDMAS
# Bracket Order Division Multiplication Addition Subtraction (BODMAS)
# Parenthesis Exponents Division Multiplication Addition Subtraction (PEMDAS)
# left to right evaluation

h = 2+2
j = 50 + 5*5
f = (5 + (2*5))/(6/3)
g = 4**2 + 5
# print(h, j, f, g)
# more complicate types containing lists/sets etc will be taught during subsequent lectures

# Data types

# Text type
# Numeric type
# Sequence type
# Map type
# Bool type
# Byte type
# None type

# Text type

string_example = "This is a demo session"
# print(len(string_example))

new_string = string_example
print(new_string + " hi " + new_string)

a = 15
b = 20
new_string = f"This is a demo session {a}"
print("This is a demo session {} {}".format(str(a), str(b)))


multiple_type = [1, None, True, "Pavan", (1, 2)]
multiple_type.clear()
print(multiple_type)


# special operators
# identity : is, is not
# membership : in, not in

# Numbers/ Numeric type

a = complex(10, -2)
print(a.real)
print(a.imag)

# Sequence types

# list

list1 = [1, 2, 3]
list2 = list1 + [4, 5, 6]
# list operations

# tuple

point = (1, 2, 3)
tuple1 = tuple(["Pavan"])
tuple2 = tuple(["vcollab"])
tuple1 += tuple2
# for x in point:
#     print(x)

# range

r = range(10, 20, 2)
# print(list(r))


# dictionary

dict1 = {"name": "Pavan", "id": 10, "age": 30, "color": ["Red", "blue"]}
print(dict1.keys())
print(dict1.values())
print(dict1.items())

childrens = {"child1": {"name": "P", "age": 2}, "child2": {"name": "P", "age": 3}}


# sets

set1 = {"apple", "apple", "banana", True, (1, 2, 3)}


# bytes
msg = "this is a bye object"

a = bytes(msg, "utf-8")
print(a)

# bool
y = True
z = False

# None
x = None

# False Values:
    # False
    # None
    # Zero of any numeric type
    # Any empty sequence. For example, '', (), [].
    # Any empty mapping. For example, {}.


# control flow statements

# conditional statements : if, elif, if-elif-else, if-else
# Transfer statements: break, continue, pass
# iterative statements: for, while

# conditional statements : if, elif, if-elif-else, if-else

x = int(input("Enter some random number"))
if x > 0 and x < 10:
    print(f"my number is {x}")
    if x < 5:
        print(f"{x}is printed from nested if block")
    elif x > 6:
        print(f"{x}is printed from nested elif block")
    else:
        print(f"{x}is printed from nested else block")
else:
    print(f"{x}is printed from else out block")


condition = False

if condition:
    print('Evaluated to True')
else:
    print('Evaluated to False')

# for loops

# traditional for loops
for i in range(5):
    print(i)

# Measure some strings:
animals = ['cat', 'dogs', 'lion']
for animal in animals:
    print(animal, len(animal))

vehicle = {
  "brand": "hyundai",
  "model": "i20",
  "type": "hatchback",
  "year": 2015
}

status = 'inactive'

# Strategy :  Create a new collection / Iterate over a copy

active_users = {}
for user, status in users.items():
    if status == 'active':
        active_users[vehicle] = status


# break, continue and pass statements

for i in range(20):
    if i == 10:
        # break at the 10th iteration
        break
    print(i)

for i in range(20):
    if i == 10:
        # skip the 10th iteration
        continue
    print(i)

# nested for loop

for i in range(5):
    for j in range(5):
        print('j', j)
    print('i', i)
    

def foo():
    pass
    
#class MyClass:
    #pass
    

# while loops

# difference between while and for loop
# for - Iterates over a definitive sequence
# while - Iterates until a condition is True
 
# endless while loop/infinite loop
while True:
    pass
    
x = 0
while True:
    if x == 10:
        break
    x+=1
    
x = 0
while x < 10:
    print(x)
    x += 1