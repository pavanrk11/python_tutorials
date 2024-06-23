# Closures

# closures
def outerFunction():
    text = "hello"

    def innerFunction():
        print(text)

    return innerFunction

if __name__ == '__main__':
    myFunction = outerFunction()
    myFunction()

##

def outerFunction():
    text = "hello"

    def innerFunction(*args, **kwargs):
        if len(args) == 0 and len(kwargs) == 0: print(text)
        else: print(args, kwargs)

    return innerFunction


if __name__ == "__main__":
    myFunction = outerFunction()
    myFunction()
    myFunction("Pavan")
    myFunction(company="Vcollab")
	
##

def create_adder(x):
    def adder(y):
        return x+y
    return adder

add_15 = create_adder(15)

print(add_15(10))

## Decorators or Decorator functions

def hello_decorator(func):
    def inner1():
        print("Hello, this is before function execution")
        return func()
        print("This is after function execution")

    return inner1


def function_to_be_used():
    print("This is inside the function !!")


function_to_be_used = hello_decorator(function_to_be_used)

# calling the function
function_to_be_used()

##

def decorator_function(original_function):
    def wrapper_function():
        print("wrapper function executed before {}".format(original_function.__name__))
        return original_function()
    return wrapper_function


def display_msg():
    print("display msg ran from original function!!")


decorated_display = decorator_function(display_msg)

decorated_display()

## same as above

def decorator_function(original_function):
    def wrapper_function():
        print("wrapper function executed before {}".format(original_function.__name__))
        return original_function()
    return wrapper_function

@decorator_function
def display_msg():
    print("display msg ran from original function!!")

display_msg()

##

def decorator_function(original_function):
    def wrapper_function(*agrs, **kwargs):
        print("wrapper function executed before {}".format(original_function.__name__))
        return original_function(*agrs, **kwargs)
    return wrapper_function

@decorator_function
def display_msg(name, age):
    print("display msg ran from original function!!")

display_msg("Pavan", 10)

## decorator chaining

def decor1(func):
    def wrap():
        print(f"{decor1.__name__} called")
        return func()

    return wrap


def decor(func):
    def wrap():
        print(f"{decor.__name__} called")
        return func()

    return wrap


@decor1
@decor
def foo():
    print("Original function called")


foo()
