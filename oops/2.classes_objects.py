# class template/signature 

class ClassName:
    """ Help Documentation for the Class"""

    # Variables :
        # Instance Variables
        # Class Variables
        # Local Variables

    # Methods
        # Instance Methods
        # Class Methods
        # Static Methods

# Instance Variables

# how to Create, access, delete the instance variables

class Employee:
    def __init__(self):
        self.enumber=17
        self.ename='Pavan'
        self.esal=100

    def m1(self):
        self.edept="RandD"

    def del_m1(self):
        del self.edept

e=Employee()
print(e.__dict__)

e.m1()
print(e.__dict__)

e.level="Sr"
print(e.__dict__)

e.del_m1()
print(e.__dict__)

del e.level
print(e.__dict__)


# Class Variables
# how to Create, access, delete the Class variables

class Test:
    x=10
    def __init__(self):
        self.y=20
    def instance_m1(self):
        self.x=30
    @classmethod
    def class_m2(cls):
        cls.x=40
        #del cls.x


t1=Test()
t2=Test()
print('t1:',t1.x,t1.y)
print('t2:',t2.x,t2.y)
Test.x=888
t1.y=999
print('t1:',t1.x,t1.y)
print('t2:',t2.x,t2.y)

# note deleting cls variable by instance variable is not possible

# local variables

class Test:
    def m1(self):
        a=1000
        print(a)
    def m2(self):
        b=2000
        #print(a)
        print(b)

t=Test()
t.m1()
#t.a
t.m2()

#####

# Instance methods

class Student:
    def __init__(self,name,marks):
        self.name=name
        self.marks=marks

    def display(self):
        print('Hi',self.name)
        print('Your Marks are:',self.marks)

s= Student("Pavan","100")
s.display()


# Class methods

class Animal:

    legs=4
    count = 0

    def __init__(self):
        Animal.count += 1

    @classmethod
    def walk(cls,name):
        print('{} walks with {} legs...'.format(name,cls.legs))

    @classmethod
    def noOfObjects(cls):
        print('The number of objects created for test class:',cls.count)

Animal.walk('Dog')

a = Animal()
a.walk('Cat')

print(Animal.noOfObjects())

# Static methods

class MathOperate:

    @staticmethod
    def add(x,y): print('The Sum:',x+y)

    @staticmethod
    def product(x,y): print('The Product:',x*y)

    @staticmethod
    def average(x,y): print('The average:',(x+y)/2)


MathOperate.add(10,20)
MathOperate.product(10,20)
MathOperate.average(10,20)