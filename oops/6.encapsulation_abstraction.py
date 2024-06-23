# Encapsulation

class Base:
    def __init__(self):
        self.a = 10
        self._b = 20
        self.__c = 30

class Derived(Base):
    def __init__(self):
        super().__init__(self)
        print(self.a)
        print(self._b)
        print(self.__c)

obj1 = Base()
print(obj1.a)
print(obj1.b)
print(obj1.c)

obj2 = Derived()

##

class Base:
    def __init__(self):
        self.a = 10
        self._b = 20
        self.__c = 30

    def setc(self, c):
        self.__c = c

    def get_c(self):
        return self.__c

class Derived(Base):
    def __init__(self, a, b, c):
        #super().__init__()
        self.a = a
        self.b = b
        self.setc(c)

        print(self.a, self.b, self.setc(c))


obj1 = Base()
print(obj1.a)
print(obj1._b)

c = Derived(10, 20, 30)

##

class Account:
    def __init__(self, id, balance=0):
        self.id = id        # Private attribute
        self.__balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount

    def withdraw(self, amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount
            return amount
        return "Insufficient balance"

    def get_balance(self):
        return self.__balance

account = Account(1, 1000)
account.deposit(500)
print(account.get_balance())  # 1500
account.withdraw(200)
print(account.get_balance())  # 1300

# Abstraction

# Achieved through the use of abstract classes and methods
# classes prevent object instantiation
# Do not enforce type checks

from abc import ABC, abstractmethod

class BaseClass(ABC):
    @abstractmethod
    def method_1(self):
         #empty body
         pass

##

class Shape(ABC):
    def __init__(self, x, y):
        self.x = x
        self.y = y

    @abstractmethod
    def render(self):
        pass

class Circle(Shape):
    pass

c = Circle(1, 2)

##

class Shape(ABC):
    def __init__(self, x, y):
        self.x = x
        self.y = y

    @abstractmethod
    def render(self):
        pass

class Circle(Shape):
    def render(self):
        return f"Rendering circle at x:{self.x}, y:{self.y}."

class Rectangle(Shape):
    def render(self):
        return f"Rendering rectangle at x:{self.x}, y:{self.y}."

class Ellipse(Shape):
    def render(self):
        pass

shapes = [
    Circle(30, 40)
    Rectange(100, 20),
    #Shape(1, 1),
    Ellipse(100, 20),
]

for s in shapes:
    print(s.render())