# Open/Closed Principle

# Problem : Modifying existing code to add new features

class Discount:
    def __init__(self, customer, price):
        self.customer = customer
        self.price = price

    def give_discount(self):
            if self.customer == 'Normal':
                return self.price * 0.2
            if self.customer == 'VIP':
                return self.price * 0.4

# Solution: Use inheritance and polymorphism


class Discount:
    def __init__(self, customer, price):
        self.customer = customer
        self.price = price

    def get_discount(self):
            return self.price * 0.2


class VIPDiscount(Discount):
    def get_discount(self):
        return super().get_discount() * 2


class SuperVIPDiscount(VIPDiscount):
    def get_discount(self):
        return super().get_discount() * 2