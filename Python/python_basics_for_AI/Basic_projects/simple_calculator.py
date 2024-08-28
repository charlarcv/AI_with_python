def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Division by zero is not allowed"
    else:
        return a / b

def calculate(a, b, operation):
    if operation == "+":
        return add(a, b)
    elif operation == "-":
        return subtract(a, b)
    elif operation == "*":
        return multiply(a, b)
    elif operation == "/":
        return divide(a, b)
    else:
        return "Invalid operation"
a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))
operation = input("Enter the operation: ")

result = calculate(a, b, operation)
print(result)

