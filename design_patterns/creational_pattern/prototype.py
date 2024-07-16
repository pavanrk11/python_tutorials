##


import copy

li1 = [[1, 2, 3, 4], [5, 6], [7, 8, 9]]

li2 = copy.copy(li1)

li2[2][0] = 25

print("li1 after shallow copy and update", li1)

li3 = copy.deepcopy(li1)

li3[2][0] = 100

print("li1 after deep copy and update", li1)


##

class A:
    def __init__(self):
        self.x = 10
        self.y = 20


a = A()
print(a.x)

print(a.__dict__)

dict1 = {'x': 100, 'y': 200}

a.__dict__.update(dict1)

print(a.__dict__)

##


##

import copy


class Prototype:
    def __init__(self):
        self.data = []

    def clone(self):
        return copy.deepcopy(self)


prototype_instance = Prototype()

clone_instance = prototype_instance.clone()

##

import copy


class Prototype:
    def clone(self):
        return copy.deepcopy(self)


class ConcretePrototypeA(Prototype):
    def __init__(self, data):
        self.data = data


class ConcretePrototypeB(Prototype):
    def __init__(self, data):
        self.data = data


class PrototypeRegistry:
    def __init__(self):
        self.prototypes = {}

    def add_prototype(self, name, prototype):
        self.prototypes[name] = prototype

    def get_prototype(self, name):
        if name in self.prototypes:
            return self.prototypes[name].clone()
        else:
            raise ValueError(f"Prototype '{name}' not found.")


# Create prototype instances
prototype_a = ConcretePrototypeA("Prototype A Data")
prototype_b = ConcretePrototypeB("Prototype B Data")
#
# # Create and populate the Prototype Registry
# registry = PrototypeRegistry()
# registry.add_prototype("PrototypeA", prototype_a)
# registry.add_prototype("PrototypeB", prototype_b)
#
# # Clone prototypes from the registry
# cloned_prototype_a = registry.get_prototype("PrototypeA")
# cloned_prototype_b = registry.get_prototype("PrototypeB")
#
# # Verify cloned data
# print(cloned_prototype_a.data)  # Output: Prototype A Data
# print(cloned_prototype_b.data)  # Output: Prototype B Data

cloned_prototype_a = prototype_a.clone()
print(cloned_prototype_a.data)


