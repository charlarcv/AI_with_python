# functions
# defnination
def greet():
    print("Hello, World!")

# calling a function
greet()

# arguments
def greet(name):
    print("Hello, " + name)

greet("Alice")

# default arguments
def greet(name = "Alice"):
    print("Hello, " + name)

greet()

# return values
def add(a, b):
    return a + b

result = add(2, 3)
print(result)

# multiple return values
def square_and_cube(x):
    return x ** 2, x ** 3

square, cube = square_and_cube(2)
print(square)

# lambda function
# A lambda function is a small anonymous function.
# A lambda function can take any number of arguments, but can only have one expression.
# syntax
# lambda arguments : expression
x = lambda a : a + 10
print(x(5))

#keywords arguments
def greet(name, msg):
    print("Hello", name + ", " + msg)

greet(name = "Alice", msg = "Good morning")

# arbitrary arguments
def greet(*names):
    for name in names:
        print("Hello", name)

greet("Alice", "Bob", "Charlie")

# arbitrary keyword arguments
def greet(**names):
    for key, value in names.items():
        print(key, value)

greet(name1 = "Alice", name2 = "Bob", name3 = "Charlie")

def describe_pet(animal_type, pet_name):
    print(f"I have a {animal_type} named {pet_name}.")

describe_pet(pet_name="Buddy", animal_type="dog")  # Order doesn't matter

def greet_all(*names):
    for name in names:
        print(f"Hello, {name}!")

greet_all("Alice", "Bob", "Charlie")  # Outputs greetings for all names

def print_info(**info):
    for key, value in info.items():
        print(f"{key}: {value}")

print_info(name="Alice", age=30, city="New York")

def add(a, b):
    """Returns the sum of two numbers."""
    return a + b

print(add.__doc__)  # Output: Returns the sum of two numbers.

x = 10  # Global variable

def func():
    x = 5  # Local variable
    print(x)  # Output: 5

func()
print(x)  # Output: 10 (global x is unchanged)

