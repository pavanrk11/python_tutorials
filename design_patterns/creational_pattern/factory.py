# Problem 

# Tight coupling for creating objects

from abc import ABC, abstractmethod

class Vehicle(ABC):

    @abstractmethod
    def display_info(self):
        pass

class Bike(Vehicle):

    def display_info(self):
        return "I am a Bike"

class Car(Vehicle):

    def display_info(self):
        return "I am a Car"

if __name__ == "__main__":

    bike = Bike()
    print(bike.display_info())

    car = Car()
    print(car.display_info())
	
### 

# Solution - Factory Design Pattern 

from abc import ABC, abstractmethod

# Abstract Vehicle Class (Product Class)
class Vehicle(ABC):

    @abstractmethod
    def display_info(self):
        pass


# Bike Subclass (Concrete Product Class)
class Bike(Vehicle):

    def display_info(self):
        return "I am a bike"


# Car Subclass (Concrete Product Class)
class Car(Vehicle):

    def display_info(self):
        return "I am a Car"


# Truck Subclass (Concrete Product Class)
class Truck(Vehicle):

    def display_info(self):
        return "I am a truck"


# Vehicle Factory (Factory/Creator Class)
class VehicleFactory:

    @staticmethod
    def create_vehicle(vehicle_type):
        if vehicle_type == 'bike':
            return Bike()
        elif vehicle_type == 'car':
            return Car()
        elif vehicle_type == 'truck':
            return Car()
        else:
            raise ValueError(f"Unknown vehicle type: {vehicle_type}")


def client_code(vehicle):

    print(veh_object.display_info())

    
if __name__ == "__main__":

    while True:
    
        vehicle_type = input("Enter your vehicle type: ")
        veh_object = VehicleFactory.create_vehicle(vehicle_type)
        
        client_code(veh_object)



    