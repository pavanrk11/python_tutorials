from abc import ABC, abstractmethod


class Payment(ABC):

    @abstractmethod
    def request(self, amount):
        pass


class RealPayment(Payment):

    def request(self, amount):
        print(f"RealPayment: Processing payment of {amount}.")


class Proxy(Payment):

    def __init__(self, real_payment, balance):
        self._real_payment = real_payment
        self._balance = balance

    def request(self, amount):

        if self.check_access(amount):
            self._real_payment.request(amount)
            self.log_access(amount)

    def check_access(self, amount):
        print("Proxy: Checking access prior to making a payment request.")
        if self._balance >= amount:
            print("Proxy: Access granted.")
            self._balance -= amount
            return True
        else:
            print("Proxy: Access denied. Insufficient funds.")
            return False

    def log_access(self, amount):
        print(f"Proxy: Logging the payment request of {amount}.")


def client_code(payment, amount):

    payment.request(amount)


if __name__ == "__main__":


    real_payment = RealPayment()
    client_code(real_payment, 50)
    print()

    proxy = Proxy(real_payment, balance=100)
    client_code(proxy, 50)  # Sufficient funds
    print()
    client_code(proxy, 60)  # Insufficient funds