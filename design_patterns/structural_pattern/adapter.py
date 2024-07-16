### Inheritance (Is-A Relationship)

class Parent:
    def __init__(self):
        print('Parent Class object created...')
    def m1(self):
        print('Parent Class Method called...')

class Child(Parent):

    def __init__(self):
        print('Child Class object created...')

    def m2(self):
        print('Child Class Method called...')

obj = Child()
obj.m1()
obj.m2()

### Composition (Has-A Relationship)

class Component:

    def __init__(self):
        print('Component class object created...')

    def m1(self):
        print('Component class m1() method executed...')


class Composite:

    def __init__(self):
        self.comp_obj = Component()
        print('Composite class object also created...')

    def m2(self):
        print('Composite class m2() method executed...')
        self.comp_obj.m1()


obj2 = Composite()
obj2.m2()

###

# The Adapter pattern is a structural design pattern that facilitates the interaction between two interfaces that are incompatible or cannot work together directly.
# It acts as a bridge, allowing objects with different interfaces to collaborate.
# The primary goal of the Adapter pattern is to ensure that client code can work with classes it was not initially designed to support.

# Real world example : A laptop's charger may have a 3-pin plug at the end, but the wall socket may only be a 2-pin socket. To plug a 3-pin charger into this socket, 
# we'd need an adapter, that accepts a 3-pin plug, and adapts the interface into the 2-pin socket.

### Inheritance way of implementing Adapter design pattern (Class Adapter)

class OldSystem:
    def legacy_operation(self):
        return "Legacy operation"

class Adapter(OldSystem):
    def new_operation(self):
        return f"Adapter: {self.legacy_operation()}"

# Client code
def client_code(adapter):
    result = adapter.new_operation()
    print(result)

if __name__ == "__main__":
    adapter = Adapter()
    client_code(adapter)

### Composition way of implementing Adapter design pattern (Object Adapter)

class OldSystem:
    def legacy_operation(self):
        return "Legacy operation"

class Adapter:
    def __init__(self, old_system):
        self.old_system = old_system

    def new_operation(self):
        return f"Adapter: {self.old_system.legacy_operation()}"

# Client code
def client_code(adapter):
    result = adapter.new_operation()
    print(result)

if __name__ == "__main__":
    old_system = OldSystem()
    adapter = Adapter(old_system)
    client_code(adapter)

###

Target Interface
Adaptee
Adapter
client_code

###

# Adaptee class
class LegacyClass:
    def legacy_method(self):
        print("Legacy method called")

# Target interface
class Target:
    def new_method(self):
        pass

# Adapter class
class Adapter(Target):
    def __init__(self):
        self.legacy_object = LegacyClass()

    def new_method(self):
        self.legacy_object.legacy_method()

# Client
def client_code(adapter):
    print(adapter.new_method())

if __name__ == "__main__":
    adapter = Adapter()
    client_code(adapter)

### Example 2

class LegacyWeatherSystem:
    def get_temperature_fahrenheit(self):
        return 77.0

class TemperatureAdapter:
    def __init__(self):
        self.legacy_system = LegacyWeatherSystem()

    def get_temperature_celsius(self):
        temp_fahrenheit = self.legacy_system.get_temperature_fahrenheit()
        temp_celsius = (temp_fahrenheit - 32) * 5.0 / 9.0
        return temp_celsius

class ModernWeatherSystem:
    def __init__(self, adapter):
        self.adapter = adapter

    def display_temperature(self):
        temp_celsius = self.adapter.get_temperature_celsius()
        print(f"The current temperature is {temp_celsius:.2f}°C")


# client
def client_code(adapter):
    modern_system = ModernWeatherSystem(adapter)
    modern_system.display_temperature()

if __name__ == "__main__":
    adapter = TemperatureAdapter(legacy_system)
    client_code(adapter)