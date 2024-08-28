# file handling in python
# opening file in python
# file = open("file_name", "mode")
# modes: r, w, a, r+, w+, a+
# r: read, w: write, a: append, r+: read and write, w+: write and read, a+: append and read
# file handling in python
"""
Modes include:
'r' (read): Opens a file for reading (default mode).
'w' (write): Opens a file for writing (creates a new file or truncates an existing one).
'a' (append): Opens a file for appending (creates a new file if it doesn't exist).
'b' (binary): Opens a file in binary mode (useful for non-text files).
'x' (exclusive creation): Creates a new file and returns an error if it already exists.
't' (text): Text mode (default mode).
'+' (read and write): Opens a file for reading and writing.
"""

# opening a file
file = open("test.txt", "r")
file.close()

# reading a file in python
# read() method reads the entire file
file = open("example.txt", "r")
content = file.read()
print(content)
file.close()

# readlines() method reads the entire file line by line
file = open("example.txt", "r")
lines = file.readlines()
print(lines)
file.close()


# readLine() method reads a single line from the file
file = open("example.txt", "r")
line = file.readline()
print(line)
file.close()

# Writing to a file in python
# write() method writes to a file
file = open("example.txt", "w")
file.write("This is a new line")
file.close()

# writelines() method writes a list of lines to a file
file = open("example.txt", "w")
lines = ["This is a new line", "This is another line"]
file.writelines(lines)
file.close()

# Appending to a file in python
# append() method appends to a file
file = open("example.txt", "a")
file.write("\nThis is a new line")
file.close()

# with statement in python
# with statement closes the file automatically
with open("example.txt", "r") as file:
    content = file.read()
    print(content)

# File modes 
"""
The combination of modes allows various operations:
'rb', 'wb', 'ab' for reading, writing, or appending in binary mode.
'r+', 'w+', 'a+' for reading and writing (reading and updating).
"""

# Handling exceptions in file handling
try:
    with open("example.txt", "r") as file:
        content = file.read()
        print(content)
except FileNotFoundError:
    print("The file was not found.")


