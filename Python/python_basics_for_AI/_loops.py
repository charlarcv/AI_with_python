# Key Concepts
# 1. For loop
# 2. While loop
# 3. Loop control statements

# For loop
# A for loop is used for iterating over a sequence (that is either a list, a tuple, a dictionary, a set, or a string).
# This is less like the for keyword in other programming languages, and works more like an iterator method as found in other object-orientated programming languages.
# With the for loop we can execute a set of statements, once for each item in a list, tuple, set etc.

# for
num = [1, 2, 3, 4, 5]
for i in num:
    print(i)
# range
for i in range(5):
    print(i)

# loop in string
text = "Python"
for char in text:
    print(char)

#loop through dist
person = {
    "name": "Alice",
    "age": 30,
    "city": "New York"
}
for key in person:
    print(key, person[key])

# While loop
# With the while loop we can execute a set of statements as long as a condition is true.
# while
i = 1
while i < 6:
    print(i)
    i += 1


# loop control statements
# break
# With the break statement we can stop the loop before it has looped through all the items:
i = 1
while i < 6:
    print(i)
    if i == 3:
        break
    i += 1

# continue
# With the continue statement we can stop the current iteration of the loop, and continue with the next:
for i in range(5):
    if i == 2:
        continue
    print(i)
# else
# The else keyword in a for loop specifies a block of code to be executed when the loop is finished:
for i in range(5):
    print(i)
else:
    print("Loop completed without a break")

# Nested loop
# A nested loop is a loop inside a loop.
# The "inner loop" will be executed one time for each iteration of the "outer loop":
adj = ["red", "big", "tasty"]
fruits = ["apple", "banana", "cherry"]
for i in adj:
    for j in fruits:
        print(i, j)
        
