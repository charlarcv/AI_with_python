# error handling
# types of errors in python
# 1. syntax error
# 2. TypeError
# 3. IndexError
# 4. ValueError
# 5. KeyError
# 6. ZeroDivisionError

# try except
# try:
#     print(x)
# except:
#     print("An exception occurred")

# try except else
# try:
#     print("Hello")
# except:
#     print("Something went wrong")
# else:
#     print("Nothing went wrong")
#try and except block
try:
    x = 10 / 0
except ZeroDivisionError:
    print("Cannot divide by zero!")
# catching multiple exceptions
try:
    value = int(input("Enter a number: "))
    result = 10 / value
except ValueError:
    print("Invalid input! Please enter a number.")
except ZeroDivisionError:
    print("Cannot divide by zero!")

#else with try
try:
    value = int(input("Enter a number: "))
    result = 10 / value
except ZeroDivisionError:
    print("Cannot divide by zero!")
else:
    print("The result is:", result)

#finally
try:
    file = open("test.txt", "r")
    content = file.read()
except FileNotFoundError:
    print("File not found!")
finally:
    file.close()  # Ensures the file is closed whether or not an error occurred

# raising exceptions
def divide(x, y):
    if y == 0:
        raise ValueError("Cannot divide by zero!")
    return x / y

try:
    result = divide(10, 0)
except ValueError as e:
    print(e)

# custom exceptions
class NegativeNumberError(Exception):
    pass

def check_positive(number):
    if number < 0:
        raise NegativeNumberError("Negative number encountered!")

try:
    check_positive(-5)
except NegativeNumberError as e:
    print(e)
