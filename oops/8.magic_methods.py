# Special methods in Python

# Basic customization or controlling object creation process
# __init__
# __new__
# __del__
# __str__
# __repr__
# __bytes__
# __format__
# __hash__

# controlling and Customizing attribute access
# __bool__
# __getattr__
# __getattribute__
# __setattr__
# __delattr__
# __dir__

# operator overloading
# __add__
# __sub__
# __mul__


# comparison operators
# __eq__
# __lt__
# __gt__


# introspecting objects instance and subclass checks
# __instancecheck__
# __subclasscheck__


# Emulating container types
# __len__
# __length_hint__
# __getitem__
# __setitem__
# __delitem__
# __missing__
# __iter__
# __reversed__
# __contains__

# Emulating numeric types
# __add__
# __sub__
# __mul__
# __matmul__
# __truediv__
# __floordiv__
# __mod__
# __divmod__
# __pow__
# __lshift__
# __rshift__
# __and__
# __xor__
# __or__

# __radd__
# __rsub__
# __rmul__
# __rmatmul__
# __rtruediv__
# __rfloordiv__
# __rmod__
# __rdivmod__
# __rpow__
# __rlshift__
# __rrshift__
# __rand__
# __rxor__
# __ror__

# __iadd__
# __isub__
# __imul__
# __imatmul__
# __itruediv__
# __ifloordiv__
# __imod__
# __ipow__
# __ilshift__
# __irshift__
# __iand__
# __ixor__
# __ior__

# unary operators
# __neg__
# __pos__ +
# __abs__
# __invert__

# Builtin
# __complex__
# __int__
# __float__

# __index__

# __round__
# __trunc__
# __floor__
# __ceil__

import math


class Shape:

    edge = 1

    def __init__(self, color="Black"):
        self.color = color

    @classmethod
    def shape_type(cls):
        return cls.__name__

    def describe(self):
        return f" This is a {self.shape_type()} shape"


class Circle(Shape):

    def __init__(self, radius, center, color="Black"):
        self.radius = radius        # 1 attr
        super().__init__(color)     # 2 attr
        self.center = center        # 3 attr

    @property
    def area(self):
        return math.pi * self.radius**2

    @area.setter
    def area(self, area):
        self.radius = math.sqrt(area / math.pi)

    def perimeter(self):
        return 2 * math.pi * self.radius

    # @classmethod
    # def shape_type(cls):
    #     return cls.__name__

    def __repr__(self):
        return (
            f"Circle(radius={self.radius},center={self.center}, color='{self.color}')"
        )

    def __str__(self):
        return f"Object of {self.shape_type()}"

    def __eq__(self, other):
        if isinstance(other, Circle):
            return (
                self.radius == other.radius
                and self.center == other.center
                and self.color == other.color
            )
        return False

    def __hash__(self):
        return hash((self.radius, self.center, self.color))

    # def __setattr__(self, item, value):
    #     if item not in ["color", "center", "radius"]:
    #         raise AttributeError("Attribute not presnt")
    #     super().__setattr__(item, 10)

    # method to set the attributes based on the order how it constructs
    # in the constructor #1 attr #2 attr #3 attr
    def __setattr__(self, name, value):
        if name == "radius":
            if not isinstance(value, int | float):
                raise TypeError("radius must be a number")
            if value <= 0:
                raise ValueError("radius must be positive")
        super().__setattr__(name, value)


if __name__ == "__main__":
    circle1 = Circle(color="Red", radius=4, center=(5, 5))
    circle2 = Circle(radius=4, center=(5, 5), color="Red")
    circle3 = Circle(radius=4, center=(5, 5), color="Blue")

    circles = [circle1, circle2, circle3]
    # using __repr__ method to show the contents are stored in a container
    print(circles)

    # use of __str__ method
    for circle in circles:
        print(circle)

    # using __eq__ method
    if circle1 == circle2:
        print("Circle1 and Circle2 are equal")
    elif circle1 == circle3:
        print("Circle1 and Circle3 are equal")
    elif circle2 == circle3:
        print("Circle2 and Circle3 are equal")
    else:
        print("None of the circles are equal")

    # use of __hash__ method
    circles = {circle1, circle2, circle3}
    print(circles)

    circle1.radius = 25
    #circle1.radius = "ppp"
    print(circle1.__dict__)


# python descriptors
# TODO :  Not covered yet


class PositiveNumber:
    def __set_name__(self, owner, name):
        self._name = name

    def __get__(self, instance, owner):
        return instance.__dict__[self._name]

    def __set__(self, instance, value):
        if not isinstance(value, int | float) or value <= 0:
            raise ValueError("positive number expected")
        instance.__dict__[self._name] = value


class Circle:
    radius = PositiveNumber()

    def __init__(self, radius, c):
        self.radius = radius

    def area(self):
        return round(math.pi * self.radius**2, 2)
