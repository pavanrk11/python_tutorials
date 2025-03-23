# Visitor Design Pattern

# Add new operations to existing objects without modifying their structure

from abc import ABC, abstractmethod


# Visitor Interface
class RoomVisitor(ABC):
    @abstractmethod
    def visit_standard_room(self, room):
        pass

    @abstractmethod
    def visit_deluxe_room(self, room):
        pass

    @abstractmethod
    def visit_suite_room(self, room):
        pass


# Concrete visitor
class CleaningCostVisitor(RoomVisitor):
    def visit_standard_room(self, room):
        return 200

    def visit_deluxe_room(self, room):
        return 300

    def visit_suite_room(self, room):
        return 400

    # Concrete visitor


class PriceVisitor(RoomVisitor):
    def visit_standard_room(self, room):
        return 2000

    def visit_deluxe_room(self, room):
        return 5000

    def visit_suite_room(self, room):
        return 8000

    # Concrete visitor


class FacilitiesVisitor(RoomVisitor):
    def visit_standard_room(self, room):
        return ["Standard cot", "Table", "TV", "Bathroom"]

    def visit_deluxe_room(self, room):
        return ["King size cot", "Table", "TV", "Bathroom", "Sofa", "Wardrobe"]

    def visit_suite_room(self, room):
        return ["Double size cot", "Table", "TV", "Bathroom", "Sofa", "Wardrobe", "Oven", "Kettle", "Balcony"]

    # Visitable/Component/Element Interface


class Room(ABC):
    @abstractmethod
    def accept(self, visitor: RoomVisitor):
        pass



class Villa(Room):

    def accept(self, visitor: RoomVisitor):
        return visitor.visit_deluxe_room(self)

# Concrete component
class StandardRoom(Room):
    def accept(self, visitor: RoomVisitor):
        return visitor.visit_standard_room(self)


# Concrete component
class DeluxeRoom(Room):
    def accept(self, visitor: RoomVisitor):
        return visitor.visit_deluxe_room(self)


# Concrete component
class SuiteRoom(Room):
    def accept(self, visitor: RoomVisitor):
        return visitor.visit_suite_room(self)


# # Client code
# def client_code(components, visitor):
#
#     for component in components:
#         component.accept(visitor)

# Client code
def client_code(component, visitor):
    print(component.accept(visitor))


if __name__ == "__main__":
    # Create instances of rooms/components
    standard_room = StandardRoom()
    deluxe_room = DeluxeRoom()
    suite_room = SuiteRoom()

    components = [standard_room, deluxe_room, suite_room]

    # Create a visitor for calculating cleaning costs
    cleaning_cost_visitor = CleaningCostVisitor()
    # client_code(components, cleaning_cost_visitor)
    client_code(deluxe_room, cleaning_cost_visitor)

    # Create a visitor for price
    price_visitor = PriceVisitor()
    client_code(standard_room, price_visitor)

    # Create a visitor for checking facilities
    facilities_visitor = FacilitiesVisitor()
    client_code(standard_room, facilities_visitor)
    client_code(suite_room, facilities_visitor)

