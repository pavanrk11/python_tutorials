from abc import ABC, abstractmethod

# Interface for concrete implementations
class DataSource(ABC):
    @abstractmethod
    def get_data(self):
        pass

# Low-level modules
class Database(DataSource):
    def get_data(self):
        return "Data from the database"

class File(DataSource):
    def get_data(self):
        return "Data from the File"
class API(DataSource):
    def get_data(self):
        return "Data from the API"

# High-level Module
class FrontEnd:
    def __init__(self, data_source):
        self.data_source = data_source

    def display(self):
        data = self.data_source.get_data()
        print("Display data:", data)

db_front_end = FrontEnd(Database())
db_front_end.display()

api_front_end = FrontEnd(API())
api_front_end.display()

file_front_end = FrontEnd(File())
file_front_end.display()