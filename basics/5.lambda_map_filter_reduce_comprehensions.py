# lambda functions

# lambda arguments : expression


def add(a):
    return a + a


result = add(5)
print(result)

f = lambda a: a + a
print(f(5))

##

f = lambda a, b: a + b
print(f(5, 10))

##
f = lambda *args, **kwargs: [args, kwargs]

list_nos = [1, 2, 3]
dictionary_characters = dict(greeting="Hello", name="pavan", compny="vcollab")

print(f(*list_nos, **dictionary_characters))


##

# Lambda as return
def create_adder(x):

    def adder(y):
        return x + y

    return adder


add_15 = create_adder(15)

print(add_15(10))


def create_adder(x):
    return lambda a: a + x


f = create_adder(15)
print(f(10))
print(f(20))
print(f(30))

##

# Lambda as argument
pairs = [(1, "one"), (2, "two"), (3, "three"), (4, "four")]
print(pairs)
pairs.sort(key=lambda pair: pair[1][1])
print(pairs)

##

# map

# map(function_to_apply, list_of_inputs)

items = [1, 2, 3, 4, 5]
squared = []
for i in items:
    squared.append(i**2)

items = [1, 2, 3, 4, 5]
squared = list(map(lambda x: x**2, items))


###

def multiply(x):
    return x * x


def add(x):
    return x + x


funcs = [multiply, add]
for i in range(5):
    value = list(map(lambda x: x(i), funcs))
    print(value)

# filter

# filter(function_to_apply=true, list_of_inputs)

number_list = range(-5, 5)
less_than_zero = list(filter(lambda x: x < 0, number_list))
print(less_than_zero)

# reduce

# reduce(function_to_apply, list_of_inputs)

product = 1
list1 = [1, 2, 3, 4]
for num in list1:
    product = product * num

from functools import reduce

product = reduce((lambda x, y: x * y), [1, 2, 3, 4])

# Enumerate

my_list = ["apple", "banana", "grapes", "pear"]
for counter, value in enumerate(my_list):
    print(counter, value)

my_list = ["apple", "banana", "grapes", "pear"]
for counter, value in enumerate(my_list, 1):
    print(counter, value)

# Comprehensions

nums = list(range(1, 11))

my_list = []
for n in nums:
    my_list.append(n)

print(my_list)

print([n for n in nums])

##

items = [1, 2, 3, 4, 5]
# squared = list(map(lambda x: x**2, items))
# squared = [(lambda x: x*x)(x) for x in items]
squared = [n * n for n in items]
print(squared)

##

number_list = range(-5, 5)
less_than_zero = list(filter(lambda x: x < 0, number_list))
print(less_than_zero)

less_than_zero1 = []
for i in number_list:
    if i < 0:
        less_than_zero1.append(i)
print(less_than_zero)

print([i for i in number_list if i < 0])


##

my_list = []
for i in range(1, 5):
    for j in range(101, 105):
        my_list.append((i, j))
print(my_list)

print([(i, j) for i in range(1, 5) for j in range(101, 105)])

##

fruits = ["apple", "banana", "grapes", "pear", "apricot", "guava"]
filtered_fruits = []

for fruit in fruits:
    if len(fruit) <= 1:
        continue
    if fruit[0] != "a":
        continue

    filtered_fruits.append(fruit)

print(filtered_fruits)

list_comp_filtered_fruits = [
    fruit for fruit in fruits if len(fruit) >= 1 if fruit[0] == "a"
]
print(list_comp_filtered_fruits)

####

numbers = list(range(1, 11))
even_odds = []
for num in numbers:
    if num % 2 == 0:
        even_odds.append("even")
    else:
        even_odds.append("odd")
print(even_odds)

list_comp_even_odds = ["even" if num % 2 == 0 else "odd" for num in numbers]
print(list_comp_even_odds)

##

print([[number for number in range(101, 106)] for _ in range(6)])

##

# dictionary comprehensions

my_dict = {number: number * number for number in range(5)}
print(my_dict)


##

names = ["name1", "name2", "name3"]
heros = ["Pavan", "Preetham", "aakash"]
print(list(zip(names, heros)))

my_dict = {}
for name, hero in zip(names, heros):
    my_dict[name] = hero
print(my_dict)

dict_comp_names = {name: hero for name, hero in zip(names, heros) if hero == "Pavan"}
print(dict_comp_names)

##

# Set Comprehensions

nums = [1, 1, 2, 1, 3, 4, 3, 4, 5, 5, 6, 7, 8, 7, 9, 9]
set_comp = {x * x for x in nums}
print(set_comp)
