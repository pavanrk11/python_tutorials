# Decorator design pattern

# Add functionality to an object dynamically without altering its structure

class Notifier:
    def send(self, message):
        pass


class SimpleNotifier(Notifier):
    def send(self, message):
        print(f"Sending notification: {message}")


class NotifierDecorator(Notifier):
    def __init__(self, notifier):
        self._notifier = notifier

    def send(self, message):
        self._notifier.send(message)


class SMSNotifier(NotifierDecorator):
    def send(self, message):
        super().send(message)
        self.send_sms(message)

    def send_sms(self, message):
        print(f"Sending SMS: {message}")


class EmailNotifier(NotifierDecorator):
    def send(self, message):
        super().send(message)
        self.send_email(message)

    def send_email(self, message):
        print(f"Sending Email: {message}")


def client_code(component, msg):

    component.send(msg)


if __name__ == "__main__":

    # Create a simple notifier
    notifier = SimpleNotifier()
    client_code(notifier, "Hello, this is a test message!")

    # Wrap it with SMS functionality
    notifier1 = SMSNotifier(notifier)
    client_code(notifier1, "Hello, this is a test message!")

    # Wrap it with Email functionality
    notifier2 = EmailNotifier(notifier1)
    client_code(notifier2, "Hello, this is a test message!")

