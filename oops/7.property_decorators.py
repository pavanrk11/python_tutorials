# property decorator

import math


class Shape:
    def __init__(self, color):
        self.color = color


class Circle(Shape):

    def __init__(self, radius, center, color="Black"):
        super().__init__(color)
        self.radius = radius
        self.center = center

    @property
    def area(self):
        return math.pi * self.radius**2
    
    @property
    def perimeter(self):
        return 2 * math.pi * self.radius


circle1 = Circle(radius=5, center=(5, 5), color="Red")
print(circle1.area)
print(circle1.perimeter)

# Trying to set the area or perimeter directly will raise an AttributeError
# circle1.area = 100
# print(circle1.area)
# circle1.perimeter = 25
# print(circle1.perimeter)

####

# A note on private variables

class A:
    def __init__(self):
        self.var = 1
        self._var = 2
        self.__var = 3

    def print_var(self):
        return self.__var

a = A()

print(dir(a))

print(a.var)
print(a._var)
#print(a._A__var)

##

class A:

    def __init__(self, a):
        self._a = a

    @property
    def a(self):
        """Getter for '_a'"""
        return self._a
        
    @a.setter
    def a(self, a):
        """Setter for '_a'"""
        self._a = a
        
    @a.deleter
    def a(self):
        """Deleter for '_a'"""
        del self._a
        
        
        
obj = A("Pavan")
print(obj.a)

obj.a = 10
print(obj.a)

del obj.a
#print(obj.a)

##

class Circle:
    def __init__(self, radius):
        self._radius = radius

    @property
    def radius(self):
        return self._radius

    @radius.setter
    def radius(self, value):
        self._radius = value

    @radius.deleter
    def radius(self):
        del self._radius

# Example usage
circle = Circle(5)
print(circle.radius)

circle.radius = 10
print(circle.radius)

del circle.radius
# print(circle.radius)


##

class Mapping:

    def __init__(self):
        self.items_list = []
    def __update(self, iterable):
        for item in iterable:
            self.items_list.append(item)
        return self.items_list


class MappingSubclass(Mapping):

    def update(self, iterable):
        return self._update(iterable)

    # def update(self, keys, values):
    #     # provides new signature for update()
    #     # but does not break __init__()
    #     for item in zip(keys, values):
    #         self.items_list.append(item)


map_object = MappingSubclass()
print(map_object.update([1,2,3]))
