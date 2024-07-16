# Standard/Classic implementation
class Singleton:
    _instance = None

    def __new__(cls):
        if not cls._instance:
            cls._instance = super(Singleton, cls).__new__(cls)
        return cls._instance

    def set_data(self, item):
        self.data = item

    def get_data(self):
        return self.data

if __name__ == "__main__":
    s1 = Singleton()
    s2 = Singleton()

    print(s1 is s2)  # Output: True

# Decorator implementation

def singleton(cls):
    instances = {}

    def wrapper(*args, **kwargs):
        if cls not in instances:
            instances[cls] = cls(*args, **kwargs)
        return instances[cls]

    return wrapper


@singleton
class Singleton:
    pass

@singleton
class Singleton:
    def __init__(self, data=None):
        self.data = data

    def set_data(self, item):
        self.data = item

    def get_data(self):
        return self.data

if __name__ == "__main__":
    s1 = Singleton()
    s2 = Singleton()

    print(s1 is s2)  # Output: True

# Base class implementation

class SingletonBase:
    _instances = {}

    def __new__(cls, *args, **kwargs):
        if cls not in cls._instances:
            instance = super().__new__(cls)
            cls._instances[cls] = instance
        return cls._instances[cls]


class Singleton(SingletonBase):
    pass

if __name__ == "__main__":
    s1 = Singleton()
    s2 = Singleton()

    print(s1 is s2)  # Output: True
    
# Meta class implementation

class SingletonMeta(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            instance = super().__call__(*args, **kwargs)
            cls._instances[cls] = instance
        return cls._instances[cls]

class Singleton(metaclass=SingletonMeta):
    """
    Singleton class using the Metaclass Approach.
    """
    def __init__(self, data=None):
        self.data = data

    def add_data(self, item):
        self.data = item

    def get_data(self):
        return self.data

if __name__ == "__main__":
    s1 = Singleton()
    s2 = Singleton()

    print(s1 is s2)  # Output: True

# Example Singleton class creation for Logging

class Logger(object):
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            print('Creating the object')
            cls._instance = super(Logger, cls).__new__(cls)
            # Put any initialization here.
        return cls._instance

log1 = Logger()
