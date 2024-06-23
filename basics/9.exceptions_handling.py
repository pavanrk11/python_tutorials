syntax errors and exceptions

syntax errors : parser detects and displays the info before it gets completely executed
while True print('Hello world')

exceptions : Errors detected during execution - Runtime
10 * (1/0)
4 + spam*3
'2' + 2

Builtin exceptions
user defined exceptions

Handling the exceptions

try:
    statement for execution check
except "the exception type" as "name for the exception":
    action to perform on the exception
-optional-
else:
    statement for execution - without execution check
finally: (cleanup action)
    no matter what execute this block before raising the exception

##

try:
    x = int(input("Please enter a number: "))
except ValueError:
    print("Oops!  That was no valid number.  Try again...")

##
while True:
    try:
        x = int(input("Please enter a number: "))
    except (ValueError, KeyboardInterrupt) as e:
        print("Oops!  That was no valid number.  Try again...")
        print(e.args)
        break
    else:
        print("the input was", x)
        a = x + 10
        print("increment 10", a)
    finally:
        print("Hi Pavan")


exception order

import sys

try:
    f = open('myfile.txt')
    s = f.readline()
    i = int(s.strip())

except OSError as err:
    print("OS error:", err)
except ValueError:
    print("Could not convert data to an integer.")
except Exception as err:
    print(f"Unexpected {err=}, {type(err)=}")
    raise NameError("Error1")
else:
    print(f.read())
    f.close()
finally:
    print("Executing Finally...")
print('End of program')



while True:
    try:
        x = int(input("Please enter a number: "))
    except (ValueError, KeyboardInterrupt) as e:
        print("Oops!  That was no valid number.  Try again...")
        print(type(e))
        # e.add_note("Something Happened in Iteration')
        # raise
        raise NameError("vcollab")
    except NameError as ne:
        print(ne.args)

# exception chaining

1.
try:
    open("database.sqlite")
except OSError:
    raise RuntimeError("unable to handle error")

2.

def func():
    raise ConnectionError
try:
    func()
except ConnectionError as exc:
    raise RuntimeError('Failed to open database') from exc

####

def func():
    raise ConnectionError

try:
    func()
except ConnectionError as exc:
    raise RuntimeError from None


# examples

import random

TARGET_NUMBER = random.randint(1, 10)


def guess_simulator(user_guess):
    try:
        if 1 <= user_guess <= 10:
            if user_guess == TARGET_NUMBER:
                print("Congratulations! Your guess is correct.")
                return True
            else:
                print(f"Oops! The correct number was {TARGET_NUMBER}.")
                return False
        else:
            print("Please enter a valid integer between 1 and 10.")
            return False
    except ValueError as e:
        print("Invalid input. Please enter a valid integer.")
        return False


if __name__ == "__main__":
    user_guess = int(input("Guess the number (between 1 and 10): "))
    result = guess_simulator(user_guess)
 

##
 
def f():
    raise ExceptionGroup(
        "group1",
        [
            OSError(1),
            SystemError(2),
            ExceptionGroup(
                "group2",
                [
                    OSError(3),
                    RecursionError(4)
                ]
            )
        ]
    )

try:
    f()
except* OSError as e:
    print("There were OSErrors")
except* SystemError as e:
    print("There were SystemErrors")