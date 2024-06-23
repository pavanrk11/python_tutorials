# Polymorphism -> Many Forms

#1. Duck Typing Philosophy of Python

# In Python we cannot specify the type explicitly. Based on provided value at runtime the type will
# be considered automatically. Hence Python is considered as Dynamically Typed Programming Language.

class Duck:
    def talk(self): print('Quack.. Quack..')

class Dog:
    def talk(self): print('Bow Bow..')

class Cat:
    def talk(self): print('Moew Moew ..')

class Goat:
    def talk(self): print('Myaah Myaah ..')


def f1(obj): obj.talk()

l=[Duck(),Cat(),Dog(),Goat()]
for obj in l:
    f1(obj)



#2. Overloading

#2.1. Operator Overloading

class Math:
    def __init__(self,a):
        self.a=a
    def __add__(self,other):
        return self.a+other.a
    def __sub__(self,other):
        return self.a-other.a
    def __mul__(self,other):
        return self.a*other.a

a1=Math(100)
a2=Math(200)
print(a1+a2)

a1=Math("Sum1")
a2=Math("Sum2")
print(a1+a2)

#2.2 Method Overloading

class Test:
    def m1(self): print('no-arg method')
    def m1(self,a): print('one-arg method')
    def m1(self,a,b): print('two-arg method')
    def m1(self,*args, **kwargs): print('multi-arg method', args, kwargs)

t=Test()
#t.m1()
#t.m1(10)
#t.m1(10,20)
#t.m1(10,20,30,operate="add")


class Math:
    def add(self, a, b=None, c=None):
        if b is not None and c is not None:
            return a + b + c
        elif b is not None:
            return a + b
        else:
            return a

# Example Usage
math_obj = Math()
result1 = math_obj.add(5)
result2 = math_obj.add(5, 10)
result3 = math_obj.add(5, 10, 15)

print(result1)
print(result2)
print(result3)

#2.3. Constructor Overloading

class Test:
    def __init__(self): print('No-Arg Constructor')
    def __init__(self,a): print('One-Arg constructor')
    def __init__(self,a,b): print('Two-Arg constructor')
    def __init__(self,*args, **kwargs): print('multi-Arg constructor')

t1=Test()
#t1=Test(10)
#t1=Test(10,20)

class Person:
    def __init__(self, name, age=None):
        self.name = name
        self.age = age

person1 = Person("Pavan")
person2 = Person("Kumar", 25)

print(person1.name, person1.age)
print(person2.name, person2.age)

#3. Overriding

#3.1. Method overriding

class A:
    def m1(self): print('method1 from A')
    def m2(self): print('method2 from A')

class B(A):
    def m2(self):
        super().m2()
        print('method1 from B')

b = B()
b.m1()
b.m2()

#3.2. constructor overriding

class P:
    def __init__(self): print('Parent Constructor')

class C(P):
    def __init__(self):
        #super().__init__()
        #P.__init__(self)
        print('Child Constructor')

p = P()

c = C()

# 2
class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age

class Employee(Person):
    def __init__(self,name,age,eno,esal):
        super().__init__(name,age)
        self.eno=eno
        self.esal=esal

    def display(self):
        print('Employee Name:',self.name)
        print('Employee Age:',self.age)
        print('Employee Number:',self.eno)
        print('Employee Salary:',self.esal)

e1=Employee('Pavan',20,1,1000)
e1.display()
e2=Employee('Kulkarni',30,2,2000)
e2.display()