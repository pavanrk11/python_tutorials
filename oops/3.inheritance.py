# Inheritance
# Inheritance is the capability of one class to derive or inherit the properties from another class

# Types of Inheritance
    # Single Inheritance:
        Single-level inheritance enables a derived class to inherit characteristics from a single-parent class.
    # Multilevel Inheritance:
        Multi-level inheritance enables a derived class to inherit properties from an immediate parent class
        which in turn inherits properties from his parent class.
    # Hierarchical Inheritance:
        Hierarchical-level inheritance enables more than one derived class to inherit properties from a parent class.
    # Multiple Inheritance:
        Multiple-level inheritance enables one derived class to inherit properties from more than one base class.

# Single Inheritance
# inheriting from a single base class

class Parent1:
    def func_1(self):
        print ("function is defined inside the parent class.")

class Child1(Parent1):
    def func_2(self):
        print ("function is defined inside the child class.")

object = Child1()
object.func_1()
object.func_2()

# Multiple Inheritance
# class is able to be created from multiple base classes

class Mother:
    mothername = "Geetha"

    def mother_name(self):
        print(self.mothername)


class Father:
    fathername = "Ranganath"

    def father_name(self):
        print(self.fathername)


class Son(Mother, Father):
    def parents(self):
        print("Father name is :", self.fathername)
        print("Mother name is :", self.mothername)


s1 = Son()
s1.parents()
s1.fathername = "Pavan"
s1.mothername = "Komal"
s1.parents()

# Multilevel Inheritance
# features that are part of the original class, as well as the class that is derived from it, are passed on to the new class

class Grandfather:

    def __init__(self, grandfathername):
        self.grandfathername = grandfathername


class Father(Grandfather):
    def __init__(self, fathername, grandfathername):
        self.fathername = fathername
        Grandfather.__init__(self, grandfathername)
        # super().__init__(grandfathername)


class Son(Father):
    def __init__(self, sonname, fathername, grandfathername):
        self.sonname = sonname
        Father.__init__(self, fathername, grandfathername)
        # super().__init__(fathername, grandfathername)

    def print_name(self):
        print("Grandfather name is :", self.grandfathername)
        print("Father name is :", self.fathername)
        print("Son name is :", self.sonname)


s = Son("Pavan", "Ranaganatha", "Raghavendra")
print(s.grandfathername)
s.print_name()

# Hierarchical Inheritance
# multiple derived classes are created from the same base

class Parent:
    def func_1(self):
        print("This function is defined inside the parent class.")

class Child_1(Parent):
    def func_2(self):
        print("This function is defined inside the child 1.")

class Child_2(Parent):
    def func_3(self):
        print("This function is defined inside the child 2.")

object1 = Child_1()
object2 = Child_2()
object1.func_1()
object2.func_1()
object1.func_2()
object2.func_3()

# Hybrid inheritance
# combination of all

