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


# Abstract Factory Interface (Factory/Creator Interface Class)
class VehicleFactory(ABC):

    @abstractmethod
    def create_vehicle(self):
        pass

    def some_operation(self):
        product = self.create_vehicle()
        result = product.display_info()
        return result


# Bike Factory (Concrete Factory/Creator Class)
class BikeFactory(VehicleFactory):

    def __init__(self):
        print("Bike factory created")

    def create_vehicle(self):
        return Bike()


# Car Factory (Concrete Factory/Creator Class)
class CarFactory(VehicleFactory):

    def __init__(self):
        print("Car factory created")

    def create_vehicle(self):
        return Car()


# Truck Factory (Concrete Factory/Creator Class)
class TruckFactory(VehicleFactory):

    def __init__(self):
        print("Truck factory created")

    def create_vehicle(self):
        return Truck()


# # Factory Producer
# class FactoryProducer:
#     @staticmethod
#     def get_factory(vehicle_type):
#         if vehicle_type == 'bike':
#             return BikeFactory()
#         elif vehicle_type == 'car':
#             return CarFactory()
#         elif vehicle_type == 'Truck':
#             return TruckFactory()
#         else:
#             raise ValueError(f"Unknown vehicle type: {vehicle_type}")
#
#
# while True:
#     vehicle_factory_type = input("Enter your factory type: ")
#     fact_object = FactoryProducer.get_factory('bike')
#     veh_obj = fact_object.create_vehicle()
#     print(veh_obj.display_info())


# OR (instead of FactoryProducer class)
# Implement a function  "client_code"

def client_code(vehicle_factory):
    print(vehicle_factory.some_operation())


if __name__ == "__main__":

    factories = {
        "bike": BikeFactory,
        "car": CarFactory,
        "truck": TruckFactory
    }

    vehicle_factory_type = input("Enter your factory type(bike, car, truck): ")
    if vehicle_factory_type in factories:
        client_code(factories[vehicle_factory_type]())
    else:
        print("Invalid type!")
