# functions

# def function_name(function parameters):

	function block
	
	return statement
	
# Different function signatures

# function with no parameters

def hello_function():
    print("Hello from hello_function ")
	
hello_function()
	
# function with 1 parameters

def hello_function(arg1):
    print(f"Hello {arg1} from hello_function ")
	
hello_function("Pavan")

# function with 2 parameters

def hello_function(arg1, arg2):
    print(f"Hello {arg1} {arg2} from hello_function ")
	
hello_function("Pavan", "Kulkarni")
	
# function with 2 parameters, positional and default/optional

def hello_function(arg1, arg2="Kulkarni"):
    print(f"Hello {arg1} {arg2} from hello_function ")
	
hello_function("Pavan")

def hello_function(arg1, arg2=None):
	if arg2 is not None:
		print(f"Hello {arg1} {arg2} from hello_function ")
	else:
		print(f"Hello {arg1} from hello_function ")
		
hello_function("Pavan")

# *args arguments or variable length arguments

def hello_function(*args):
    print(args)

hello_function('Hello', 'pavan', 'vcollab', 'types')

# **kwargs arguments or variable length keywordarguments

def hello_function(**kwargs):
    print(kwargs)

dictionary_characters = dict(greeting="Hello", name="pavan", company="vcollab")

hello_function(greeting="Hello", name="pavan", compny="vcollab")
# hello_function(**dictionary_characters)

# *args arguments and **kwargs arguments combined

def hello_function(*args, **kwargs):
    print("args =",args)
    print("kwargs =",kwargs)

numbers = [1, 2, 3, 4, 5]
characters = dict(greeting="Hello", name="pavan", company="vcollab")

hello_function(*numbers, **characters)

# function parameter rules

def f(pos1, pos2, /, pos_or_kwd, *, kwd1, kwd2):
    #return None

def standard_arg(arg):
    print(arg)

def pos_only_arg(arg, /):
    print(arg)

def kwd_only_arg(*, arg):
    print(arg)

def combined_example(pos_only, /, standard, *, kwd_only):
    print(pos_only, standard, kwd_only)


standard_arg(2)
standard_arg(arg=2)
pos_only_arg(1)
pos_only_arg(arg=1)
kwd_only_arg(3)
kwd_only_arg(arg=3)
combined_example(1, 2, 3)
combined_example(1, 2, kwd_only=3)
combined_example(1, standard=2, kwd_only=3)
combined_example(pos_only=1, standard=2, kwd_only=3)

# function optional parameter mutable type
#####

i = 5
def f(arg=i):
    print(arg)
i = 6
f()

# function optional parameter immutable type
#####

def f(a, L=[]):
    L.append(a)
    return L

print(f(1))
print(f(2))
print(f(3))

def f(a, L=None):
    if L is None:
        L = []
    L.append(a)
    return L
	
# global variables
 
intc = 10
def hello_function(intb):
    global intc
    intc = 60

def main():
    inta = [10]
    hello_function(inta)

main()
print(intc)