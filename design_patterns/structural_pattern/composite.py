# Composite pattern

# The problem is has a tree structure
# Examples: File System, Delivery Box, Organizational Hierarchy

# Component Interface: Base interface for all the objects in the composition.
# Leaf: It should be either an interface or an abstract class with the common methods to manage the child composites.
# Composite: Acts as a container that can hold both Leaf and other Composite instances, forming the structure.
# client: Has access to the composition elements by using the base component object.

from abc import ABC, abstractmethod


# Define the Component Interface
class Component(ABC):
    """The Component interface sets the common method for all components."""

    def add(self, component):
        """Method interface to add elements to the Composite."""
        pass

    def remove(self, component):
        """Method interface to remove elements to the Composite."""
        pass

    @abstractmethod
    def operation(self):
        """The operation method needs to be implemented by Leaf and Composite classes."""
        pass


# Create Leaf Class
class Leaf(Component):
    """Leaf represents individual objects that don’t contain other elements."""

    def __init__(self, name):
        self.name = name

    def operation(self):
        """Operation method for Leaf."""
        return f"Leaf: {self.name}"


# Create Composite Class
class Composite(Component):
    """Composite acts as a container that can hold both Leaf and other Composite instances."""

    def __init__(self, name):
        self.name = name
        self.children = []

    def add(self, component):
        """Method to add elements to the Composite."""
        self.children.append(component)
        component.parent = self

    def remove(self, component):
        """Method to remove elements from the Composite."""
        self.children.remove(component)
        component.parent = None

    def is_composite(self) -> bool:
        return True

    def operation(self):
        """Operation method for Composite."""
        results = [f"Composite: {self.name}"]
        for child in self.children:
            results.append(child.operation())
        return "\n".join(results)


def client_code(component):
    print(component.operation())


# Step 3: Demonstrate the Usage in Main
if __name__ == "__main__":

    # Creating Leaf objects
    leaf1 = Leaf("Leaf 1")
    leaf2 = Leaf("Leaf 2")
    leaf3 = Leaf("Leaf 3")

    # Creating Composite objects
    composite1 = Composite("Composite 1")
    composite2 = Composite("Composite 2")
    composite3 = Composite("Composite 3")

    composite1.add(leaf1)
    composite1.add(leaf2)

    composite2.add(leaf3)

    composite1.add(composite2)

    composite2.add(composite3)

    client_code(composite1)

# Assignment problem : Implement a composite pattern for a file system