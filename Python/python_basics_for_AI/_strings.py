# create strings
# string is a sequence of characters
# strings are immutable
# strings are ordered
# strings can be indexed and sliced
# strings can be concatenated and multiplied
# strings can be repeated
# strings can be compared
# strings can be formatted
# strings can be searched
# strings can be replaced
# strings can be splitted
# strings can be joined

# create strings
# single quote string
single_quote_str = 'Hello, World!'
double_quote_str = "Hello, World!"
# triple quote string
triple_quote_str = """Hello, World!"""

# indexing
print(single_quote_str[0]) # H
print(single_quote_str[-1]) # !
print(single_quote_str[-2]) # d
text = "Python"
sub_str = text[1:4]  # 'yth'
sub_str = text[:4]  # 'Pyth'
sub_str = text[4:]  # 'on'
sub_str = text[1:6:2]  # 'yh'
"""
# slicing
# [start:stop:step]
# start: starting index
# stop: ending index
# step: step size

"""
start_to_third = text[:3]  # 'Pyt'
third_to_end = text[2:]    # 'thon'



# String methods
text = "Python"
print(text.lower())  # 'python'
print(text.upper())  # 'PYTHON'

text = "  Hello, World!  "
print(text.strip())  # 'Hello, World!'

text = "Hello World"
words = text.split()  # ['Hello', 'World']

text = "Hello, World!"
new_text = text.replace("World", "Python")  # 'Hello, Python!'

index = text.find("World")  # 7

# String formatting
name = "Alice"
age = 30
greeting = f"My name is {name} and I am {age} years old."
# 'My name is Alice and I am 30 years old.'
greeting = "My name is {} and I am {} years old.".format(name, age)
greeting = "My name is %s and I am %d years old." % (name, age)


# escape sequences
text = "Hello\nWorld"  # 'Hello' and 'World' on separate lines
text = 'It\'s a beautiful day!'
text = "She said, \"Hello!\""
path = "C:\\Users\\Name"
