# Q1. Ask the user to enter a number that is under 50. If they enter greater than the number, display the message “Too high”, otherwise display “Thank you”.

user_input = int(input("Please enter a number: "))
if user_input > 50:
    print("Too high")
else:
    print("Thank you")

# Q2. Write a program to find a minimum of three numbers.
a = 15
b = 20
c = 10

# 1
smallest = 0
if a < b and a < c:
    smallest = a
if b < a and b < c:
    smallest = b
if c < a and c < b:
    smallest = c

# 2
# smallest = 0
# if a < b and a < c:
#     smallest = a
# elif b < c:
#     smallest = b
# else:
#     smallest = c

# 3
# my_list = [a, b, c]
# smallest = min(my_list)

print(smallest, "is the smallest of three numbers.")

# Q3. Ask the user to enter their favourite colour. If they enter “blue”, “BLUE” or “Blue” display the message “This is my favourite colour”, otherwise display the message “I don’t like [colour], I prefer black”.

# 1
favorite_color = input("Enter your favorite color: ")

if favorite_color == "blue" or favorite_color == "BLUE" or favorite_color == "Blue":
    print("This is my favorite color.")
else:
    print(f"I don't like {favorite_color}, I prefer black.")

# 2
# favorite_color = input("Enter your favorite color: ").lower()
#
# if favorite_color == "blue":
#     print("This is my favorite color.")
# else:
#     print(f"I don't like {favorite_color}, I prefer black.")

# Q4.

first_name = input("Enter your first name: ")
last_name = input("Enter your last name: ")

first_name_upper = first_name.upper()
last_name_upper = last_name.upper()

# Join the names together
full_name = first_name_upper + " " + last_name_upper

print("Your full name in uppercase:", full_name)

#Q5.

items = []

binary_sequence = input(
    "Enter a sequence of 4-digit binary numbers separated by comma: "
)
binary_numbers = binary_sequence.split(",")

divisible_by_2 = []
divisible_by_2_base_10 = []
for binary_num in binary_numbers:
    decimal_num = int(binary_num, 2)  # Convert binary to decimal
    if decimal_num % 2 == 0:
        divisible_by_2.append(binary_num)
        divisible_by_2_base_10.append(decimal_num)

if divisible_by_2:
    print("Numbers divisible by 2:", ", ".join(divisible_by_2))
else:
    print("No numbers in the sequence are divisible by 2.")

print("my divisible by 2 items are: ", divisible_by_2_base_10)
print("my divisible by 2 items are: ", ", ".join(divisible_by_2))


# Q6.

Phrase = "My name is Pavan and I am checking for Vowels"
count = 0
vowels = {'a', 'e', 'i', 'o', 'u'}

for char in Phrase:
    if char.lower() in vowels:
        count += 1

print("Number of vowels in the given string: ", count)

# Q7.

# 1
radius = float(input("Enter the radius of the circle: "))
area = 3.142 * radius ** 2
print(f"Area of the circle: {area:.2f}")

# 2
import math
radius = float(input("Enter the radius of the circle: "))
area = math.pi * radius ** 2
print(f"Area of the circle: {area:.2f}")

num = 123456.789
print(f"{num:E}")

#Q8.

# 1

print("Choose an option:")
print("1. Circle")
print("2. Square")

choice = int(input("Enter your choice (1 or 2): "))

if choice == 1:
    radius = float(input("Enter the radius of the circle: "))
    area = 3.142 * radius ** 2
    print(f"Area of the circle: {area:.2f}")
elif choice == 2:
    side_length = float(input("Enter the length of a side of the square: "))
    area = side_length ** 2
    print(f"Area of the square: {area:.2f}")
else:
    print("Invalid option. Please choose 1 or 2.")

# 2
# def calculate_circle_area(radius):
#     return 3.142 * radius ** 2
#
#
# def calculate_square_area(side_length):
#     return side_length ** 2
#
#
# def main():
#
#     print("Choose an option:")
#     print("1. Circle")
#     print("2. Square")
#
#     choice = int(input("Enter your choice (1 or 2): "))
#
#     if choice == 1:
#         radius = float(input("Enter the radius of the circle: "))
#         area = calculate_circle_area(radius)
#         print(f"Area of the circle: {area:.2f}")
#     elif choice == 2:
#         side_length = float(input("Enter the length of a side of the square: "))
#         area = calculate_square_area(side_length)
#         print(f"Area of the square: {area:.2f}")
#     else:
#         print("Invalid option. Please choose 1 or 2.")
#
# if __name__ == "__main__":
#     main()

# Q9.

choice = input("Enter your choice (A or B): ")

if choice.upper() == "A":
    end_limit = int(input("Enter the end limit: "))
    if end_limit >= 1:
        for i in range(1, end_limit + 1):
            print(i, end=" ")
        print()  # Print a newline
    else:
        print("Invalid end limit. Please enter a positive integer.")
elif choice.upper() == "B":
    low_limit = int(input("Enter the low limit: "))
    if low_limit <= 50:
        for i in range(50, low_limit - 1, -1):
            print(i, end=",")
        print()  # Print a newline
    else:
        print("Invalid low limit. Please enter an integer less than or equal to 50.")

# Q10.

target_number = 27
guess = int(input("Guess the number: "))

while guess != target_number:
    if guess < target_number:
        print("Too low! Try again.")
    else:
        print("Too high! Try again.")
    guess = int(input("Guess the number: "))

print("Congratulations! You guessed it correctly.")

# Q11.

# import random
#
# TARGET_NUMBER = random.randint(1, 10)
#
#
# def guess_simulator(user_guess):
#     try:
#         if 1 <= user_guess <= 10:
#             if user_guess == TARGET_NUMBER:
#                 print("Congratulations! Your guess is correct.")
#                 return True
#             else:
#                 print(f"Oops! The correct number was {TARGET_NUMBER}.")
#                 return False
#         else:
#             print("Please enter a valid integer between 1 and 10.")
#             return False
#     except ValueError:
#         print("Invalid input. Please enter a valid integer.")
#         return False
#
#
# if __name__ == "__main__":
#     user_guess = int(input("Guess the number (between 1 and 10): "))
#     result = guess_simulator(user_guess)


# Q12

# Define a list of 5 countries
countries = ['India', 'Germany', 'USA', 'UK', 'Austria']

print("List of countries:")
for i, country in enumerate(countries):
    print(f"{i + 1}. {country}")

user_choice = int(input("Enter the number corresponding to your choice (1-5): "))
if 1 <= user_choice <= len(countries):
    chosen_country = countries[user_choice - 1]
    print(f"You chose '{chosen_country}'. Its index in the list is {user_choice-1}.")
else:
    print("Invalid choice. Please enter a number between 1 and 5.")

# Q13.

string1 = input("Enter the first string: ")
string2 = input("Enter the second string: ")

# Compare the strings
if string1 == string2:
    print("Correct!")
else:
    print("Please try again")

# Q14

def create_alternating_string(s1, s2):
    # Initialize an empty string to store the result
    s3 = ""

    # Determine the length of the shorter string
    min_length = min(len(s1), len(s2))

    # Construct the alternating string
    for i in range(min_length):
        s3 += s1[i] + s2[-(i + 1)]

    # Append any remaining characters from the longer string
    if len(s1) > len(s2):
        s3 += s1[min_length:]
    elif len(s2) > len(s1):
        s3 += s2[min_length:]

    return s3

# Example usage
s1 = "PAVAN"
s2 = "VCOLLAB"
result = create_alternating_string(s1, s2)
print(f"Result: {result}")


# Q15

import random
random_list = random.sample(range(1, 101), 10)
print(random_list)

# Q16

# 1
l1 = [15, 6, 7, 10, 12, 20, 10, 28, 10]
x = 10
count = l1.count(x)
print(f"{x} appears {count} times in the list.")

# 2
def countX(lst, x):
    count = 0
    for ele in lst:
        if ele == x:
            count += 1
    return count

print(f"{x} appears {countX(l1, x)} times in the list.")

# 3

occurrences = [ele for ele in l1 if ele == x]
print(f"{x} appears {len(occurrences)} times in the list.")

# Q17

import random

original_list = list(range(1, 101))
odd_values_list = [x for x in original_list if x % 2 != 0]

start_index = int(input("Enter the start index for slicing: "))
end_index = int(input("Enter the end index for slicing: "))

sliced_list = odd_values_list[start_index:end_index]


random.seed(sliced_list)
generated_number = random.randint(1, 100)

user_input = int(input("Enter your lucky number (1-100): "))

if user_input == generated_number:
    print("I am lucky..!")
else:
    print("Please try again.")

# Q18

# 1
def squares(n):
    result = []
    for i in range(1, n+1):
        result.append(i**2)
    return result

result = squares(100)
print(result)

# 2
def squares(n):
    return [i**2 for i in range(1, n+1)]

result = squares(100)
print(result)

# Q19

# 1
original_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
reversed_list = []

i = len(original_list) - 1
while i >= 0:
    reversed_list.append(original_list[i])
    i -= 1

print(reversed_list)

# 2
original_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
reversed_list = original_list[::-1]

print(reversed_list)

# 20

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

main_diagonal = [matrix[i][i] for i in range(len(matrix))]

# 21

import random

# Generate random student names
def generate_random_names(num_students):
    first_names = ["Pavan", "Preetham", "Anika", "Ajay", "Raj"]
    last_names = ["K", "H", "P", "J", "S"]
    student_names = []
    for _ in range(num_students):
        first_name = random.choice(first_names)
        last_name = random.choice(last_names)
        student_names.append(f"{first_name} {last_name}")
    return student_names

def create_class(num_students):
    class_dict = {}
    student_names = generate_random_names(num_students)
    for student in student_names:
        # Generate random marks for Maths, Science, and Social
        maths_marks = random.randint(50, 100)
        science_marks = random.randint(40, 95)
        social_marks = random.randint(30, 90)
        class_dict[student] = {"Maths": maths_marks, "Science": science_marks, "Social": social_marks}
    return class_dict

# Create two classes with 5 students each
class1 = create_class(5)
class2 = create_class(5)

# Print the dictionaries
print("Class 1:")
for student, marks in class1.items():
    print(f"{student}: {marks}")

print("\nClass 2:")
for student, marks in class2.items():
    print(f"{student}: {marks}")

# 22

food_prices = {
    "carrot": 25,
    "Beetrrot": 30,
    "onion": 50
}

# 23

def greet(name, age=18):
    print(f"Hello, {name}! You are {age} years old.")

greet("Pavan")

def greet(*, name, age=18):
    print(f"Hello, {name}! You are {age} years old.")

greet(name="Preetham")

def greet(name, age=18):
    print(f"Hello, {name}! You are {age} years old.")

greet("Komal", age=25)

def greet(name, age=18, *args):
    print(f"Hello, {name}! You are {age} years old.")
    print("Additional arguments:", args)

greet("Anika", 2, "extra1", "extra2")

def greet(name, age=18, **kwargs):
    print(f"Hello, {name}! You are {age} years old.")
    print("Additional keyword arguments:", kwargs)

greet("Raj", 25, city="Hubli", hobby="Biking")

# 24

def calculation(operation, arg1, arg2):
    if operation == 'addition':
        return arg1 + arg2
    elif operation == 'subtraction':
        return arg1 - arg2
    elif operation == 'multiplication':
        return arg1 * arg2
    elif operation == 'division':
        if arg2 != 0:
            return arg1 / arg2
        else:
            return "Error: Division by zero is not allowed."

# Example usage
arg1 = 10
arg2 = 5

# Addition
result_addition = calculation(operation='addition', arg1=arg1, arg2=arg2)
print(f"Addition result: {result_addition}")

# Subtraction
result_subtraction = calculation(operation='subtraction', arg1=arg1, arg2=arg2)
print(f"Subtraction result: {result_subtraction}")

# Multiplication
result_multiplication = calculation(operation='multiplication', arg1=arg1, arg2=arg2)
print(f"Multiplication result: {result_multiplication}")

# Division
result_division = calculation(operation='division', arg1=arg1, arg2=arg2)
print(f"Division result: {result_division}")


# 25

def show_employee(name, salary=5000):

    print(f"Employee Name: {name}")
    print(f"Salary: {salary}")

# Example usage:
show_employee("Pavan Kulkarni", 7500)
show_employee("Preetham G")

# 26

greet_user = lambda name: f"Hello {name}!"
user_name = input("Enter your name : ")
print(greet_user(user_name))

# 27

is_num = lambda q: q.replace('.', '', 1).isdigit()
is_num1 = lambda r: is_num(r[1:]) if r[0] == '-' else is_num(r)
print(is_num('265'))
print(is_num('4.23'))
print(is_num('A001'))
print(is_num1('-16.4'))
print(is_num1('+16.4'))

# 28
def maximum(a, b):
    return a if a >= b else b

# Minimum of two numbers using ternary operator
def minimum(a, b):
    return a if a < b else b

# Example usage
a = 10
b = 20
print(f"Largest number between {a} and {b} is {maximum(a, b)}")
print(f"Smallest number between {a} and {b} is {minimum(a, b)}")

#29

is_num = lambda q: q.replace('.', '', 1).isdigit()

print(is_num('265'))  # True
print(is_num('4.23'))  # True
print(is_num('-125'))  # False
print(is_num('00'))     # True
print(is_num('A00'))   # False
print(is_num('001'))    # True

is_num1 = lambda r: is_num(r[1:]) if r[0] == '-' else is_num(r)

print(is_num1('-16.445'))    # True
print(is_num1('+24587.11'))  # True