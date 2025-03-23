from abc import ABC, abstractmethod

# Vehicle Interface
class Vehicle(ABC):

    @abstractmethod
    def drive(self) -> str:
        pass

# Concrete Vehicles
class Car(Vehicle):

    def drive(self) -> str:
        return "Driving a car"

class Bike(Vehicle):

    def drive(self) -> str:
        return "Riding a bike"

# Vehicle Factory Interface
class VehicleFactory(ABC):

    @abstractmethod
    def create_vehicle(self) -> Vehicle:
        pass

# Concrete Factories
class CarFactory(VehicleFactory):

    def create_vehicle(self) -> Vehicle:
        return Car()

class BikeFactory(VehicleFactory):

    def create_vehicle(self) -> Vehicle:
        return Bike()

# Client Code
def client_code(factory: VehicleFactory) -> None:
    vehicle = factory.create_vehicle()
    print(f"Client: {vehicle.drive()}")


while True:
    factory = input("Enter your factory: ")
    if factory == "bike":
        client_code(BikeFactory())
    elif factory == "car":
        client_code(CarFactory())
    else:
        print("Invalid Input!")
        break