# List
"""
A list is an ordered collection of items (elements) that can be of different types.
Lists are created by placing elements inside square brackets [], separated by commas.
"""
# Create a list
numbers = [1, 2, 3, 4, 5]
empty_list = []
mixed_list = [1, 2.0, 'string', True]
print(f"{numbers}, {empty_list}, {mixed_list}")  

# accessing lists
"""
Elements in a list can be accessed by their index, with the first element at index 0.
Negative indices can be used to access elements from the end of the list.
"""
numbers = [10, 20, 30, 40]
first = numbers[0]   # 10
last = numbers[-1]   # 40

# Modifing lists
"""
Lists are mutable, meaning their elements can be changed after the list is created.
"""
numbers[2] = 99  # Changes the third element to 99

# List methods
"""
Python has a set of built-in methods that you can use on lists.
"""
numbers.append(50)  # [10, 20, 99, 40, 50]
numbers.insert(1, 15)  # [10, 15, 20, 99, 40, 50]
numbers.remove(99)  # [10, 15, 20, 40, 50]
numbers.pop()  # [10, 15, 20, 40]
numbers.pop(1)  # [10, 20, 40]
numbers.sort()  # [10, 15, 20, 40]
numbers.reverse()  # [40, 20, 15, 10]
length = len(numbers)  # 4

# List slicing
"""
You can specify a range of indices by specifying where to start and where to end the range.
When specifying a range, the return value will be a new list with the specified elements.
"""
sub_list = numbers[1:3]  # [20, 15]

# tuples
"""
A tuple is a collection which is ordered and unchangeable.
In Python tuples are written with round brackets.
"""
#create a tuple
empty_tuple = ()
numbers = (1, 2, 3, 4, 5)
single_element_tuple = (1,)  # Note the trailing comma

# accessing tuples
"""
Elements in a tuple can be accessed by their index, with the first element at index 0.
Negative indices can be used to access elements from the end of the tuple.
"""
numbers = (10, 20, 30, 40)
first = numbers[0]   # 10
last = numbers[-1]   # 40

# Modifing tuples
"""
Tuples are immutable, meaning their elements cannot be changed after the tuple is created.
"""
# numbers[2] = 99  # This will raise an error

# Tuple methods
"""
Python has two built-in methods that you can use on tuples.
"""
numbers = (10, 20, 30, 40)
length = len(numbers)  # 4
index = numbers.index(30)  # 2
count = numbers.count(10)  # 1

# Tuple slicing
"""
You can specify a range of indices by specifying where to start and where to end the range.
When specifying a range, the return value will be a new tuple with the specified elements.
"""
sub_tuple = numbers[1:3]  # (20, 30)

# tuple packing and unpacking
"""
Packing and unpacking is a common operation in Python.
"""
# Packing
numbers = 1, 2, 3  # This is a tuple
# Unpacking
a, b, c = numbers  # a = 1, b = 2, c = 3
print(a, b, c)



# Practice  - List
# Create a list of 5 elements
fruit = ['apple', 'banana', 'cherry', 'date', 'elderberry']
# Access the third element
print(fruit[2])
# Modify the fourth element
fruit[3] = 'dragonfruit'
# Add a new element to the list
fruit.append('fig')
# Remove the second element
fruit.pop(1)
# Sort the list in ascending order
fruit.sort()
# Reverse the list
fruit.reverse()
# Find the length of the list
print(len(fruit))
# Create a sublist with the first three elements
sub_fruit = fruit[:3]
# Practice  - Tuple
# Create a tuple of 5 elements
cities = ('New York', 'Los Angeles', 'Chicago', 'Houston', 'Phoenix')
# Access the third element
print(cities[2])
# Find the length of the tuple
print(len(cities))
# Create a sublist with the first three elements
sub_cities = cities[:3]
# Pack and unpack the tuple
a, b, c, d, e = cities
# Compare the list and tuple
# Lists are mutable, while tuples are immutable
# Lists use square brackets [], while tuples use round brackets ()
# Lists have more built-in methods than tuples
# Lists are more flexible than tuples
# Tuples are faster than lists
# Tuples are used for fixed data, while lists are used for variable data
# Tuples are used for heterogeneous data, while lists are used for homogeneous data
# Tuples are used for smaller data, while lists are used for larger data
# Tuples are used for read-only data, while lists are used for read-write data
# Tuples are used for data integrity, while lists are used for data manipulation
# Tuples are used for data security, while lists are used for data sharing


