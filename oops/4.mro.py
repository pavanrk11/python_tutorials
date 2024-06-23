Method Resolution Order
# In case of mixed/hybrid inheritance rule to be followed
# DLR - Depth first left right
# Child will get more priority than the parent, left parent will have more priority than the right

class A:
    pass

class B(A):
    pass

class C(A):
    pass

class D(B, C):
    pass

print(A.__mro__)
print(B.__mro__)
print(C.__mro__)
print(D.__mro__)

##

class A:
    def m1(self):
        print("A class method")


class B(A):
    def m1(self):
        print("B class method")


class C(A):
    def m1(self):
        print("C class method")


class D(C, B):
    def m1(self):
        print("C class method")
        #A.m1(self)


d = D()
d.m1()

print(A.__mro__)
print(B.__mro__)
print(C.__mro__)
print(D.__mro__)

##

IS-A(Inheritance) and HAS-A(Composition) Relationship

##

# Passing members of one class to another class(without inheritance)

class Employee:
    def __init__(self,eno,ename,esal):
        self.eno=eno
        self.ename=ename
        self.esal=esal
    def display(self):
        print('Employee Number:',self.eno)
        print('Employee Name:',self.ename)
        print('Employee Salary:',self.esal)

class Test:
    def modify(emp):
        emp.esal=emp.esal+10000
        emp.display()

e=Employee(100,'Pavan',10000)
e.display()
Test.modify(e)