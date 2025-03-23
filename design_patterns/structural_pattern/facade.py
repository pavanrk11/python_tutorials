# Facade design pattern

# A handle to a complicated system helps to hide the implementation details
# and expose only the necessary information to the end user or the client

# Facade : A wrapper class that connects the individual systems
# Subsystems : Individual systems that comprises the whole system
# Client : End user

class Subsystem1:
    def operation1(self):
        return "Subsystem1: Ready!"


class Subsystem2:
    def operation2(self):
        return "Subsystem2: Ready!"


class Facade:
    def __init__(self):
        self._subsystem1 = Subsystem1()
        self._subsystem2 = Subsystem2()

    def operation(self):
        result = []
        result.append(self._subsystem1.operation1())
        result.append(self._subsystem2.operation2())
        return '\n'.join(result)


def client_code(facade):
    print(facade.operation())


if __name__ == "__main__":
    facade = Facade()
    client_code(facade)


###

class Waiter:

    def write_order(self):
        print("Waiter writes client's order")

    def send_to_kitchen(self):
        print("Send order to kitchen")

    def serve_customer(self):
        print("Customer is served!!!")


class Kitchen:

    def prepare_food(self):
        print("Cook food")

    def call_waiter(self):
        print("Call Waiter")

    def wash_dishes(self):
        print("Wash the dishes")


class Facade:

    def __init__(self):
        self.waiter = Waiter()
        self.kitchen = Kitchen()

    def order_food(self):  # Operation
        print("A series of interdependent calls on various subsystems:")
        self.waiter.write_order()
        self.waiter.send_to_kitchen()
        self.kitchen.prepare_food()
        self.kitchen.call_waiter()
        self.waiter.serve_customer()
        self.kitchen.wash_dishes()


def client_code(facade):
    facade.order_food()


if __name__ == "__main__":
    facade = Facade()
    client_code(facade)
