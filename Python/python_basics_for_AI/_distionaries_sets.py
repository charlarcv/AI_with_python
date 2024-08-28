# Distionaries and Sets

#key concepts of dictionaries and sets
# dictionaries are used to store data values in key:value pairs.
# A dictionary is a collection which is ordered*, changeable and does not allow duplicates.
# Dictionaries are written with curly brackets, and have keys and values:

# creating a dictionary
empty_dict = {}
person = {
    "name": "Alice",
    "age": 30,
    "city": "New York"
}
# accessing dictionary items
name = person["name"]
age = person.get("age")
#adding and updating
person["city"] = "San Francisco"
person["capital"] = "Sacramento"
print(person)
del person["city"]
print(person)
# methods
keys = person.keys()
values = person.values()
items = person.items()
# looping through a dictionary
for key in person:
    print(key, person[key])
for key, value in person.items():
    print(key, value)

# Sets are used to store multiple items in a single variable.
# A set is a collection which is both unordered and unindexed.
# Sets are written with curly brackets.
# creating a set
empty_set = set()
numbers = {1, 2, 3, 4, 5}
# adding and removing
numbers.add(6)
numbers.remove(3)
numbers.discard(3)
numbers.pop()
# methods 
numbers.clear()
# set operations
a = {1, 2, 3}
b = {3, 4, 5}
union = a | b
intersection = a & b
difference = a - b
symmetric_difference = a ^ b

# looping through a set
for number in numbers:
    print(number)

#frozen set
# A frozenset is an immutable version of a set.
# A frozenset is a collection which is both unordered and unindexed.
# Frozensets are written with round brackets.
numbers = frozenset({1, 2, 3, 4, 5})
# numbers.add(6)  # AttributeError: 'frozenset' object has no attribute 'add'
# numbers.remove(3)  # AttributeError: 'frozenset' object has no attribute 'remove'

# Practice dist
book = {
    "title": "The Catcher in the Rye",
    "author": "J.D. Salinger",
    "year": 1951
}
book.update({"year": 1953})
book["publiser"] = "Little, Brown and Company"
print(book)

# Practice Set
numbers = {1,2,3,4,5,6}
numbers.add(7)
numbers.remove(3)
print(numbers)

# set operations
set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}

print(set1 & set2)  # Intersection: {3, 4}
print(set1 | set2)  # Union: {1, 2, 3, 4, 5, 6}
print(set1 - set2)  # Difference: {1, 2}
print(set1 ^ set2)  # Symmetric Difference: {1, 2, 5, 6}
