# Iterators

nums = [1, 2, 3]

for num in nums:
    print(num)

print(dir(nums))
print(nums.__iter__)
# print(nums.__next__)

i_nums = nums.__iter__()
print(dir(i_nums))
print(next(i_nums))


# Generators

a = range(5)
print(a)
print(list(a))

def multi_yield():
    state1 = "first string"
    yield state1
    state2 = "second string"
    yield state2

multi_obj = multi_yield()
print(next(multi_obj))
print(next(multi_obj))
print(next(multi_obj))

def square_numbers(nums):
    result = []
    for i in nums:
        result.append(i * i)
    return result


my_nums = square_numbers(range(5))


def square_numbers(nums):
    for i in nums:
        yield i * i


my_nums = square_numbers(range(5))


my_nums = [x * x for x in range(5)]
my_nums = (x * x for x in range(5))

print(my_nums)

import sys

my_nums = [x * x for x in range(5)]
sys.getsizeof(my_nums)

my_nums = (x * x for x in range(5))
print(sys.getsizeof(my_nums))


# match statements

def http_error(status):
    match status:
        case 400:
            return "Bad request"
        case 404:
            return "Not found"
        case 418:
            return "I'm a teapot"
        case _:
            return "Something's wrong with the internet"

status  = 300
print(http_error(status))

####

def func1(point_2d):
    match point_2d:
        case (100, 300):  # Mismatch: 200 != 300
            print("Case 1")
        case (x, 400):
            print("Case 2")
        case (x, y) if x == y:  # Matches and binds y to 200
            print(f"Case 3, y: {y}")
        case _:  # Pattern not attempted
            print("Case 4, I match anything!")


point_2d = (100)
func1(point_2d)

# ternary conditionals
# a if condition else b or [on_true] if [expression] else [on_false]
a, b = 10, 20

c = (
    "Both a and b are equal"
    if a <= b
    else "a is greater than b" if a < b else "b is greater than a"
)
print(c)

###

def my_max(a, b):
    return a if a > b else b

a, b = 10, 20
my_max(a, b)


# namespace and scopes
LEGB: local, enclosing, global, builtin

# global
x = [10, 20]

def func1(a):

    x = 20  # local, if not defined use global
    y = [1, 2]
    print(x)
    print(y)

    def func2():

        # enclosing
        print(a)
        print(x)
        print(y)

    func2()


func1(100)
print(x)

# builtin
# def min():
#     return True


print(min(x))

##

name = "pavan"

def f1():
    print(name)

    s = 'I love python coding'

    def f2():
        print(s)

    f2()

f1("hello")

# nonlocal keyword

def f1():
    s = 'I love India'

    def f2():
        nonlocal s
        s = 'Me too'
        print(s)

    f2()
    print(s)

f1()

#

import builtins
dir(builtins)
