
from abc import ABC, abstractmethod

# class Server(ABC):
#     @abstractmethod
#     def serve_food(self):
#         pass
#
#     @abstractmethod
#     def take_orders(self):
#         pass
#
# class Cleaner(ABC):
#     @abstractmethod
#     def clean_table(self):
#         pass
#
# class Chef(ABC):
#     @abstractmethod
#     def cook_food(self):
#         pass
#
# class Waiter(Server, Cleaner):
#     def serve_food(self):
#         print("Serving food to the customer.")
#
#     def clean_table(self):
#         print("Cleaning the table after customers leave.")
#
#     def take_orders(self):
#         print("Recieve orders from the customer.")
#
# class Cook(Chef):
#     def cook_food(self):
#         print("Cooking food for the customers.")
#
#     def develop_new_item(self):
#         print()


class RestaurantEmployee(ABC):
    @abstractmethod
    def cook_food(self):
        pass

    @abstractmethod
    def serve_food(self):
        pass

    @abstractmethod
    def clean_table(self):
        pass

    @abstractmethod
    def take_orders(self):
        pass


class Waiter(RestaurantEmployee):
    def cook_food(self):
        raise NotImplementedError("Waiter doesn't cook food!")

    def serve_food(self):
        print("Serving food to the customer.")

    def clean_table(self):
        print("Cleaning the table after customers leave.")

    def take_orders(self):
        print("Recieve orders from the customer.")

class Cleaner(RestaurantEmployee):
    def cook_food(self):
        raise NotImplementedError("Waiter doesn't cook food!")

    def serve_food(self):
        raise NotImplementedError("Waiter doesn't cook food!")

    def clean_table(self):
        print("Cleaning the table after customers leave.")

    def take_orders(self):
        raise NotImplementedError("Waiter doesn't cook food!")

def restaurant_work(employee):
    if isinstance(employee, Waiter):
        employee.serve_food()
        employee.take_orders()
    if isinstance(employee, Cleaner):
        employee.clean_table()


waiter = Waiter()
clen = Cleaner()

restaurant_work(waiter)
restaurant_work(clen)