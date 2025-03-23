# Problem

class Vehicle:
    def move(self):
        return "Moving"

class MotorVehicle(Vehicle):
    def start_engine(self):
        return "Engine started"

class Car(MotorVehicle):
    def start_engine(self):
        return "Car engine started"

class ElectricCar(MotorVehicle):
    def start_engine(self):
        return "Silently starting electric motor"

class Bicycle(Vehicle):
    def move(self):
        return "Pedaling forward"

def move_vehicle(vehicle: Vehicle):
    return vehicle.move()



objects = [Car(), ElectricCar(), Bicycle()]
for obj in objects:
    print(move_vehicle(obj))