# if statement
x = 10
if x > 5:
    print("x is greater than 5")
# Output: x is greater than 5

#else statement
x = 4
if x > 5:
    print("x is greater than 5")
else:
    print("x is less than 5")
# Output: x is less than 5

#elif statement
x = 5
if x > 5:
    print("x is greater than 5")
elif x == 5:
    print("x is equal to 5")
else:
    print("x is less than 5")
# Output: x is equal to 5

#nested if statement
x = 10
if x > 5:
    print("x is greater than 5")
    if x > 7:
        print("x is greater than 7")
# Output: x is greater than 5
#         x is greater than 7


# Logical operators in if statement
x = 10
if x > 5 and x < 15:
    print("x is greater than 5 and less than 15")

x = 3
if x < 5 or x > 10:
    print("x is less than 5 or greater than 10")

x = 8
if not x > 10:
    print("x is not greater than 10")

# Comarision operators
x = 10
if x == 10:
    print("x is equal to 10")
if x != 5:
    print("x is not equal to 5")
if x > 5:
    print("x is greater than 5")



