from abc import ABC, abstractmethod

# Abstract Product A
class Car(ABC):

    @abstractmethod
    def drive(self) -> str:
        pass

# Abstract Product B
class Bike(ABC):

    @abstractmethod
    def ride(self) -> str:
        pass

# Concrete Products for Honda
class HondaCar(Car):

    def drive(self) -> str:
        return "Driving a Honda car."

class HondaBike(Bike):

    def ride(self) -> str:
        return "Riding a Honda Bike."

# Concrete Products for BMW
class BMWCar(Car):

    def drive(self) -> str:
        return "Driving a BMW car."

class BMWBike(Bike):

    def ride(self) -> str:
        return "Riding a BMW Bike."

# Abstract Factory
class VehicleFactory(ABC):

    @abstractmethod
    def create_car(self) -> Car:
        pass

    @abstractmethod
    def create_bike(self) -> Bike:
        pass

# Concrete Factory for Honda
class HondaFactory(VehicleFactory):

    def create_car(self) -> Car:
        return HondaCar()

    def create_bike(self) -> Bike:
        return HondaBike()

# Concrete Factory for BMW
class BMWFactory(VehicleFactory):

    def create_car(self) -> Car:
        return BMWCar()

    def create_bike(self) -> Bike:
        return BMWBike()


# Client Code
def client_code(factory: VehicleFactory):
    car = factory.create_car()
    bike = factory.create_bike()
    print(car.drive())
    print(bike.ride())


while True:
    factory = input("Enter your factory: ")
    if factory == "Honda":
        client_code(HondaFactory())
    elif factory == "BMW":
        client_code(BMWFactory())
    else:
        print("Invalid Input!")
        break