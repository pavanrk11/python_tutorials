from abc import ABC, abstractmethod

# Product Class (To be built)
class House:
    def __init__(self):
        self.windows = None
        self.doors = None
        self.roof = None
        self.garden = None
        self.swimming_pool = None

    def __str__(self):
        features = []
        if self.windows:
            features.append(f"Windows: {self.windows}")
        if self.doors:
            features.append(f"Doors: {self.doors}")
        if self.roof:
            features.append(f"Roof: {self.roof}")
        if self.garden:
            features.append(f"Garden: {self.garden}")
        if self.swimming_pool:
            features.append(f"Swimming Pool: {self.swimming_pool}")
        return "House with " + ", ".join(features)
	
# Abstract Builder Interface	
class HouseBuilder(ABC):

    @abstractmethod
    def build_windows(self): pass

    @abstractmethod
    def build_doors(self): pass

    @abstractmethod
    def build_roof(self): pass

    @abstractmethod
    def build_garden(self): pass

    @abstractmethod
    def build_swimming_pool(self): pass

    @abstractmethod
    def get_house(self): pass

# Concrete Builder Class 
class SimpleHouseBuilder(HouseBuilder):
    def __init__(self):
        self.house = House()

    def build_windows(self):
        self.house.windows = "Simple Windows"

    def build_doors(self):
        self.house.doors = "Simple Doors"

    def build_roof(self):
        self.house.roof = "Simple Roof"

    def build_garden(self):
        self.house.garden = "No Garden"

    def build_swimming_pool(self):
        self.house.swimming_pool = "No Swimming Pool"

    def get_house(self):
        return self.house

# Concrete Builder Class 
class LuxuryHouseBuilder(HouseBuilder):
    def __init__(self):
        self.house = House()

    def build_windows(self):
        self.house.windows = "Luxury Windows"

    def build_doors(self):
        self.house.doors = "Luxury Doors"

    def build_roof(self):
        self.house.roof = "Luxury Roof"

    def build_garden(self):
        self.house.garden = "Beautiful Garden"

    def build_swimming_pool(self):
        self.house.swimming_pool = "Luxury Swimming Pool"

    def get_house(self):
        return self.house

# Constructs the objects in sequence using Builder Interface
class Director:
    def __init__(self, builder):
        self._builder = builder

    def construct_house(self):
        self._builder.build_windows()
        self._builder.build_doors()
        self._builder.build_roof()
        self._builder.build_garden()
        self._builder.build_swimming_pool()
        return self._builder.get_house()

if __name__ == "__main__":

    # Construct a simple house
    simple_builder = SimpleHouseBuilder()
    director = Director(simple_builder)
    simple_house = director.construct_house()
    print(simple_house)

    # Construct a luxury house
    luxury_builder = LuxuryHouseBuilder()
    director = Director(luxury_builder)
    luxury_house = director.construct_house()
    print(luxury_house)