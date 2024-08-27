result = 5 + 3  # 8
result = 10 - 4  # 6
result = 7 * 3  # 21
result = 8 / 2  # 4.0 (always returns a float)
result = 8 // 3  # 2
result = 10 % 3  # 1
result = 2 ** 3  # 8

#Assignment Operators:
x = 5  # Assigns the value 5 to x
x += 3  # Equivalent to x = x + 3
x -= 2  # Equivalent to x = x - 2
x *= 4  # Equivalent to x = x * 4
x /= 2  # Equivalent to x = x / 2
x //= 3  # Equivalent to x = x // 3
x %= 2  # Equivalent to x = x % 2
x **= 3  # Equivalent to x = x ** 3

"""
Order of Precedence:

Parentheses (()) – Highest precedence, evaluate first.
Exponentiation (**)
Multiplication, Division, Floor Division, Modulus (*, /, //, %)
Addition, Subtraction (+, -)
Assignment (=, +=, -=, etc.) – Lowest precedence.
"""
result = 2 + 3 * 4  # 14, because multiplication has higher precedence than addition
result = (2 + 3) * 4  # 20, parentheses change the order of operations


# Practice 
x = 10
x += x # 20
x -= x # 0
x *= x # 0
#x /= x # zero division error


#  3 + 4 * 2 / (1 - 5) ** 2
print(3 + 4 * 2 / (1 - 5) ** 2)  # 3.5