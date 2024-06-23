print("printing from new module..")

name = "Pavan"
comp = "vcollab"

def match_string(fruits, targets="apple"):
    filter_fruits = []
    for i, value in enumerate(fruits):
        for target in targets:
            if target == value: filter_fruits.append(target)
    return filter_fruits