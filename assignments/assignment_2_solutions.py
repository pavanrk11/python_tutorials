class String:
    def __init__(self, input_string):
        self.input_string = input_string

    def to_uppercase(self):
        return self.input_string.upper()

    def to_lowercase(self):
        return self.input_string.lower()

    def reverse_string(self):
        return self.input_string[::-1]

    def count_alphabets(self):
        return sum(char.isalpha() for char in self.input_string)

    def display_menu(self):
        menu = """
			Choose an option:
			1. Convert to Uppercase
			2. Convert to Lowercase
			3. Reverse the String
			4. Count Alphabets
			5. Exit
        """
        print(menu)

    def execute_option(self, option):
        if option == 1:
            print("Uppercase:", self.to_uppercase())
        elif option == 2:
            print("Lowercase:", self.to_lowercase())
        elif option == 3:
            print("Reversed String:", self.reverse_string())
        elif option == 4:
            print("Alphabet Count:", self.count_alphabets())
        elif option == 5:
            print("Exiting the program.")
        else:
            print("Invalid option. Please try again.")

def main():
    input_string = input("Enter a string: ")
    manipulator = String(input_string)

    while True:
        manipulator.display_menu()
        try:
            option = int(input("Enter your choice: "))
            if option == 5:
                manipulator.execute_option(option)
                break
            manipulator.execute_option(option)
        except ValueError:
            print("Please enter a valid number.")

if __name__ == "__main__":
    main()


####


import math

class ScientificCalc:
    def __new__(cls, value):
        if isinstance(value, (int, float)):
            return super(ScientificCalc, cls).__new__(cls)
        else:
            raise ValueError("Value must be a real number")

    def __init__(self, value):
        self.value = value

    def __del__(self):
        print(f"Deleting {self}")

    def __repr__(self):
        return f"ScientificCalc({self.value})"

    def __str__(self):
        return str(self.value)

    def __bytes__(self):
        return bytes(str(self.value), 'utf-8')

    def __format__(self, format_spec):
        return format(self.value, format_spec)

    def __hash__(self):
        return hash(self.value)

    def __bool__(self):
        return bool(self.value)

    def __getattr__(self, name):
        return f"'ScientificCalc' object has no attribute '{name}'"

    def __getattribute__(self, name):
        return object.__getattribute__(self, name)

    def __setattr__(self, name, value):
        self.__dict__[name] = value

    def __delattr__(self, name):
        del self.__dict__[name]

    def __dir__(self):
        return dir(self.__class__)

    def __len__(self):
        return len(str(self.value))

    def __length_hint__(self):
        return len(str(self.value))

    def __getitem__(self, key):
        return str(self.value)[key]

    def __setitem__(self, key, value):
        temp = list(str(self.value))
        temp[key] = value
        self.value = float(''.join(temp))

    def __delitem__(self, key):
        temp = list(str(self.value))
        del temp[key]
        self.value = float(''.join(temp))

    def __missing__(self, key):
        return f"Missing key: {key}"

    def __iter__(self):
        return iter(str(self.value))

    def __reversed__(self):
        return reversed(str(self.value))

    def __contains__(self, item):
        return str(item) in str(self.value)

    def __add__(self, other):
        if isinstance(other, ScientificCalc):
            return ScientificCalc(self.value + other.value)
        return NotImplemented

    def __sub__(self, other):
        if isinstance(other, ScientificCalc):
            return ScientificCalc(self.value - other.value)
        return NotImplemented

    def __mul__(self, other):
        if isinstance(other, ScientificCalc):
            return ScientificCalc(self.value * other.value)
        return NotImplemented

    def __matmul__(self, other):
        raise NotImplementedError("Matrix multiplication not supported")

    def __truediv__(self, other):
        if isinstance(other, ScientificCalc):
            if other.value != 0:
                return ScientificCalc(self.value / other.value)
            else:
                raise ValueError("Cannot divide by zero")
        return NotImplemented

    def __floordiv__(self, other):
        if isinstance(other, ScientificCalc):
            if other.value != 0:
                return ScientificCalc(self.value // other.value)
            else:
                raise ValueError("Cannot divide by zero")
        return NotImplemented

    def __mod__(self, other):
        if isinstance(other, ScientificCalc):
            if other.value != 0:
                return ScientificCalc(self.value % other.value)
            else:
                raise ValueError("Cannot divide by zero")
        return NotImplemented

    def __divmod__(self, other):
        if isinstance(other, ScientificCalc):
            if other.value != 0:
                return divmod(self.value, other.value)
            else:
                raise ValueError("Cannot divide by zero")
        return NotImplemented

    def __pow__(self, other, modulo=None):
        if isinstance(other, ScientificCalc):
            return ScientificCalc(pow(self.value, other.value, modulo))
        return NotImplemented

    def __lshift__(self, other):
        raise NotImplementedError("Left shift not supported")

    def __rshift__(self, other):
        raise NotImplementedError("Right shift not supported")

    def __and__(self, other):
        raise NotImplementedError("Bitwise AND not supported")

    def __xor__(self, other):
        raise NotImplementedError("Bitwise XOR not supported")

    def __or__(self, other):
        raise NotImplementedError("Bitwise OR not supported")

    def __eq__(self, other):
        if isinstance(other, ScientificCalc):
            return self.value == other.value
        return NotImplemented

    def __lt__(self, other):
        if isinstance(other, ScientificCalc):
            return self.value < other.value
        return NotImplemented

    def __gt__(self, other):
        if isinstance(other, ScientificCalc):
            return self.value > other.value
        return NotImplemented

    def __neg__(self):
        return ScientificCalc(-self.value)

    def __pos__(self):
        return self

    def __abs__(self):
        return ScientificCalc(abs(self.value))

    def __invert__(self):
        raise NotImplementedError("Bitwise NOT not supported")

    def __complex__(self):
        return complex(self.value)

    def __int__(self):
        return int(self.value)

    def __float__(self):
        return float(self.value)

    def __index__(self):
        return int(self.value)

    def __round__(self, ndigits=None):
        return round(self.value, ndigits)

    def __trunc__(self):
        return math.trunc(self.value)

    def __floor__(self):
        return math.floor(self.value)

    def __ceil__(self):
        return math.ceil(self.value)

    @classmethod
    def __instancecheck__(cls, instance):
        return isinstance(instance, cls)

    @classmethod
    def __subclasscheck__(cls, subclass):
        return issubclass(subclass, cls)

    def sin(self):
        return math.sin(math.radians(self.value))

    def cos(self):
        return math.cos(math.radians(self.value))

    def tan(self):
        return math.tan(math.radians(self.value))

    def log(self, base=10):
        return math.log(self.value, base)

    def sqrt(self):
        return math.sqrt(self.value)

    def exp(self):
        return math.exp(self.value)

    def display_menu(self):
        menu = """
        Choose an operation:
        1. Addition
        2. Subtraction
        3. Multiplication
        4. Division
        5. Power
        6. Sine
        7. Cosine
        8. Tangent
        9. Logarithm
        10. Square Root
        11. Exponential
        12. Exit
        """
        print(menu)

    def execute_operation(self, choice, other=None):
        if choice == 1:
            return self + other
        elif choice == 2:
            return self - other
        elif choice == 3:
            return self * other
        elif choice == 4:
            return self / other
        elif choice == 5:
            return self ** other
        elif choice == 6:
            return self.sin()
        elif choice == 7:
            return self.cos()
        elif choice == 8:
            return self.tan()
        elif choice == 9:
            base = float(input("Enter the base for the logarithm: ") or 10)
            return self.log(base)
        elif choice == 10:
            return self.sqrt()
        elif choice == 11:
            return self.exp()
        elif choice == 12:
            print("Exiting the program.")
        else:
            print("Invalid choice. Please try again.")

def main():
    while True:
        try:
            value1 = float(input("Enter the first real number: "))
            calc1 = ScientificCalc(value1)
            calc1.display_menu()
            choice = int(input("Enter your choice: "))

            if choice in [1, 2, 3, 4, 5]:
                value2 = float(input("Enter the second real number: "))
                calc2 = ScientificCalc(value2)
                result = calc1.execute_operation(choice, calc2)
            else:
                result = calc1.execute_operation(choice)

            if result is not None:
                print("Result:", result)

            if choice == 12:
                break
        except ValueError:
            print("Invalid input. Please enter a valid real number.")

if __name__ == "__main__":
    main()

#####

import tkinter as tk
from tkinter import messagebox
import math

class CalculatorUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Scientific Calculator")

        self.entry = tk.Entry(root, width=40, borderwidth=5)
        self.entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

        self.create_buttons()

    def create_buttons(self):
        button_texts = [
            '7', '8', '9', '/',
            '4', '5', '6', '*',
            '1', '2', '3', '-',
            '0', '.', '+', '=',
            'sin', 'cos', 'tan', 'log',
            'sqrt', 'exp', 'C'
        ]

        row = 1
        col = 0

        for text in button_texts:
            button = tk.Button(self.root, text=text, padx=20, pady=20, command=lambda t=text: self.on_button_click(t))
            button.grid(row=row, column=col, sticky="nsew")

            col += 1
            if col > 3:
                col = 0
                row += 1

    def on_button_click(self, char):
        if char == 'C':
            self.entry.delete(0, tk.END)
        elif char == '=':
            try:
                expression = self.entry.get()
                self.entry.delete(0, tk.END)
                result = eval(expression, {"__builtins__": None}, {"ScientificCalc": ScientificCalc, "sin": math.sin, "cos": math.cos, "tan": math.tan, "log": math.log, "sqrt": math.sqrt, "exp": math.exp})
                self.entry.insert(0, str(result))
            except Exception as e:
                messagebox.showerror("Error", str(e))
        elif char in ('sin', 'cos', 'tan', 'log', 'sqrt', 'exp'):
            try:
                value = float(self.entry.get())
                calc = ScientificCalc(value)
                self.entry.delete(0, tk.END)
                if char == 'sin':
                    self.entry.insert(0, str(calc.sin()))
                elif char == 'cos':
                    self.entry.insert(0, str(calc.cos()))
                elif char == 'tan':
                    self.entry.insert(0, str(calc.tan()))
                elif char == 'log':
                    self.entry.insert(0, str(calc.log()))
                elif char == 'sqrt':
                    self.entry.insert(0, str(calc.sqrt()))
                elif char == 'exp':
                    self.entry.insert(0, str(calc.exp()))
            except Exception as e:
                messagebox.showerror("Error", str(e))
        else:
            current = self.entry.get()
            self.entry.delete(0, tk.END)
            self.entry.insert(0, current + char)


root = tk.Tk()
CalculatorUI(root)
root.mainloop()

#####

class StudentExam:
    def __init__(self, student_name):
        self.student_name = student_name
        self.semester1 = {}
        self.semester2 = {}

    def assign_marks(self, semester, subject_marks):
        if semester == 1:
            self.semester1.update(subject_marks)
        elif semester == 2:
            self.semester2.update(subject_marks)
        else:
            raise ValueError("Semester must be either 1 or 2")

    def final_score(self):
        total_marks = sum(self.semester1.values()) + sum(self.semester2.values())
        return total_marks

student = StudentExam("Pavan")
student.assign_marks(1, {"LinearFEA": 85, "Dynamics": 90})
student.assign_marks(2, {"NonLinearFEA": 90, "Topology Optimization": 90})
final_score = student.final_score()
print(f"Final score for {student.student_name}: {final_score}")

#####


from datetime import datetime

class ENoticeBoard:
    def __init__(self):
        self.notes = {}

    def post_note(self, user_id, post_id, content):
        if post_id in self.notes:
            print(f"Post ID {post_id} already exists. Use update or modify to change the content.")
            return

        self.notes[post_id] = {
            'user_id': user_id,
            'content': content,
            'last_updated': datetime.now(),
            'last_updated_by': user_id
        }
        print(f"Note {post_id} posted by {user_id}")

    def update_note(self, user_id, post_id, new_content):
        if post_id in self.notes:
            self.notes[post_id]['content'] = new_content
            self.notes[post_id]['last_updated'] = datetime.now()
            self.notes[post_id]['last_updated_by'] = user_id
            print(f"Note {post_id} updated by {user_id}")
        else:
            print(f"Note {post_id} does not exist")

    def modify_note(self, user_id, post_id, new_content):
        self.update_note(user_id, post_id, new_content)

    def delete_note(self, user_id, post_id):
        if post_id in self.notes:
            del self.notes[post_id]
            print(f"Note {post_id} deleted by {user_id}")
        else:
            print(f"Note {post_id} does not exist")

    def get_updates(self):
        for post_id, note in self.notes.items():
            print(f"Post ID: {post_id}")
            print(f"Posted By: {note['user_id']}")
            print(f"Content: {note['content']}")
            print(f"Last Updated: {note['last_updated']}")
            print(f"Last Updated By: {note['last_updated_by']}")
            print("----------")


board = ENoticeBoard()
board.post_note('user1', 1, 'This is the first note')
board.post_note('user2', 2, 'This is the second note')
board.update_note('user1', 1, 'This is the updated first note')
board.modify_note('user3', 2, 'This is the modified second note')
board.delete_note('user2', 1)
board.get_updates()

#####

class UnileverShampoo:
    def __init__(self, name: str) -> None:
        self.name = name
        self.inventory: dict[str, int] = {}

    def add_item(self, item: str, quantity: int) -> None:
        if item in self.inventory:
            self.inventory[item] += quantity
        else:
            self.inventory[item] = quantity

    def remove_item(self, item: str, quantity: int) -> None:
        if item in self.inventory:
            if self.inventory[item] >= quantity:
                self.inventory[item] -= quantity
                print(f"{quantity} {item}(s) removed from inventory.")
            else:
                print("Not enough quantity in inventory.")
        else:
            print("Item not found in inventory.")

    def display_inventory(self) -> None:
        print("Inventory:")
        for item, quantity in self.inventory.items():
            print(f"{item}: {quantity}")

class Employee:
    def __init__(self, name: str) -> None:
        self.name = name

    def take_order(self, customer: str, order: dict[str, int]) -> None:
        print(f"{self.name} takes order from {customer}: {order}")

class Customer:
    def __init__(self, name: str) -> None:
        self.name = name

    def place_order(self, shampoo: UnileverShampoo, order: dict[str, int]) -> None:
        print(f"{self.name} places order: {order}")
        for item, quantity in order.items():
            shampoo.remove_item(item, quantity)

shampoo = UnileverShampoo("Dove")
shampoo.add_item("Dove Men Care", 5)
shampoo.add_item("Dove Women Care", 10)
shampoo.display_inventory()

employee = Employee("Pavan")
customer = Customer("Varun")

order = {"Dove Intense Care": 2, "Dove Silk": 5}
customer.place_order(shampoo, order)
shampoo.display_inventory()

employee.take_order(customer.name, order)
