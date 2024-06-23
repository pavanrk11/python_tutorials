# Recursive functions

def factorial(n):
    print(f"factorial() called with n = {n}")
    return_value = 1 if n <= 1 else n * factorial(n - 1)
    print(f"-> factorial({n}) returns {return_value}")
    return return_value

num = int(input("Please enter a positive number. "))

if num < 0:
    print("Invalid input!")
elif num == 0:
    print("Factorial of number 0 is 1")
else:
    print("Factorial of number", num, "=", factorial(num))


from sys import getrecursionlimit
getrecursionlimit()
setrecursionlimit(2000)


# Nested functions

def outerFunction(msg):
    text = msg

    def innerFunction():
        print(text)

    innerFunction()

outerFunction('Hello !')


##

def f1():
    s = 'I love python coding'

    def f2():
        print(s)

    f2()

f1()

##

def f1():
    s = 'I love python coding'

    def f2():
        s = 'Me too'
        print(s)

    f2()
    print(s)

f1()

##

def f1():
    s = ['I love python coding']

    def f2():
        s[0] = 'Me too'
        print(s)

    f2()
    print(s)

f1()

##

def f1():
    s = 'I love python coding'

    def f2():
        nonlocal s
        s = 'Me too'
        print(s)

    f2()
    print(s)

f1()


def f1():
    f1.s = 'I love python coding'

    def f2():
        f1.s = 'Me too'
        print(f1.s)

    f2()
    print(f1.s)

f1()

##

def outerFunction(msg):
    text = msg

    def innerFunction():
        print(text)

    def innerFunction2(a, b):
        print(a, b)

    def innerFunction3(a, b=[]):
        print(b.append(a))

    innerFunction()
    innerFunction2(10, 20)
    innerFunction3(10)

outerFunction('Hello !')


# first class functions

def shout(text):
    return text.upper()

print (shout('Hello'))

tell = shout

print (tell('Hello'))


###

def shout(text):
    return text.upper()

def whisper(text):
    return text.upper()

def greet(func):
    # storing the function in a variable
    greeting = func("""Hi, I am created by a function
                    passed as an argument.""")
    print (greeting)

greet(shout)
greet(whisper)
