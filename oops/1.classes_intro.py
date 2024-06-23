# Namespace is a mapping from names to objects
# module1.func1() is different from module2.func1()

# Scope is a textual region of a Python program where a namespace is "directly accessible"

1. The innermost scope, which is searched first, contains the local names
2. The scopes of any enclosing functions, which are searched starting with the nearest 
enclosing scope, contain non-local, but also non-global names
3. The next-to-last scope contains the current module’s global names
4. The outermost scope (searched last) is the namespace containing built-in names

# Python OOPS

# Class: A blueprint for creating objects.
# Object: An instance of a class. Has a state and behavior associated with it(Identity->Uniqueness, State->property, Behavior)

# Attributes: Characteristics of an object.
# Methods: Functions that operate on the object's data.

# Inheritance: Mechanism for creating a new class from an existing class.

# Polymorphism: Ability to define methods in a child class that have the
# same name as the methods in the parent class but behave differently.

# Encapsulation: Bundling of data and methods. Attribute visibility, name mangling, properties

# Abstraction: 

##

# Class

class ClassName:
    pass

obj = ClassName
print(obj)

##

from utils import ClassName1
obj1 = ClassName1
print(obj1)

##

class ClassName:

    class SubClassName:
        pass

    pass

obj = ClassName
print(obj)

innerObj = ClassName.SubClassName
print(innerObj)

##

class MyClass:

    i = 12345

    def f():
        return 'hello world'

x = MyClass
y = MyClass
print(x)
print(y)

x.i = 5
print(y.i)
print(x.i)

##

# Instance : Is an object that belongs to a class

class MyClass:

    name = ""
    age = None

# Instance creation using CLASSNAME and ()
obj1 = MyClass()
obj1.name = "Pavan"
obj1.age = 25

print(f"Object at location {obj1} have name {obj1.name} and age{obj1.age}")

obj2 = MyClass()
obj2.name = "Preetham"
obj2.age = 20

print(f"Object at location {obj2} have name {obj2.name} and age{obj2.age}")

##

class Employee:
    pass

e = Employee()
print(e)

emp_list = []
for i in range(10):
    emp_list.append(Employee())

##

class MyClass:

    def __init__(self):
        print(f"object was created {self}")
        pass

    i = 12345

    def f():
        return "hello world"


x = MyClass()
print(x.i)

##

class MyClass:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display(self):
        print(f"Object at location {self} have name {self.name} and age{self.age}")


obj1 = MyClass("Pavan", 25)
print(obj1.display())
obj2 = MyClass("Preetham", 20)
print(obj2.display())

##

def display_names(self):
    print(self.name)

class MyClass:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display(self):
        print(f"Object at location {self} have name {self.name} and age{self.age}")

    d = display

    d1 = display_names

obj1 = MyClass("Pavan", 25)
obj1.d1()
obj2 = MyClass("Preetham", 20)
obj2.d()

##

class MyClass:

    gender = ""
    weight = list()

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def set_gender(self, gender):
        self.gender = gender

    def set_weight(self, weight):
        self.weight.append(weight)

    def display(self):
        print(f"Object at location {self} have name {self.name} and age{self.age}")


obj1 = MyClass("Pavan", 25)
obj1.set_gender("Male")
obj1.set_weight(50)
print(obj1.gender)
print(obj1.weight)

obj2 = MyClass("Preetham", 10)
obj2.set_gender("Female")
obj2.set_weight(30)
print(obj2.gender)
print(obj2.weight)
