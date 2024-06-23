print("I am printing from external module inside directory")

name = 'Pavan'
comp = 'vcollab'

def match_string(search_string, target="apple"):
    for i, value in enumerate(search_string):
        if value == target:
            return value