# Handling input and output (I/O)
# Python provides a number of built-in functions that can be used to read and write files.
# input
# The input() function allows for user input.
name = input("Enter your name: ")
print("Hello, " + name)

# type conversion
# By default, the input() function reads input as a string.
age = int(input("Enter your age: "))
print("You are " + str(age) + " years old.")

#prompt for input
name = input("Enter your name: ")

## OUTPUT
# print
# The print() function prints the specified message to the screen, or other standard output device.
print("Hello, World!")

# String Concatenation and Formatting
name = "Alice"
print("Hello, " + name)

name = "Alice"
print("Hello, {}".format(name))

# sep and end parameters
print("Hello", "World", sep = ", ", end = "!")
# OUTPUT
