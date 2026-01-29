# 📂 PYTHON FILE HANDLING — COMPLETE NOTES (WITH THEORY)
# 1️⃣ What is File Handling?

# Definition:
# File handling is the process of storing data permanently in files so it can be used later. Unlike variables (stored in RAM), file data remains even after the program stops.

# Theory:
# A file is a collection of data stored on secondary storage (HDD/SSD). Python provides built-in tools to interact with files using streams (flow of data).

# Used in:

# Logs

# Reports

# Config files

# Data processing

# CSV/JSON data

# Large datasets

# 2️⃣ Opening a File
file = open("data.txt", "mode")


# Definition:
# open() is a built-in function used to open a file and returns a file object.

# Theory:
# When a file is opened:

# OS allocates memory buffer

# File pointer is placed at start

# A connection is created between program and file

# Parameters:
# Parameter	Meaning
# "data.txt"	File name (or path)
# "mode"	How you want to open the file

# Output:
# No visible output. A file object is created in memory like:

# <io.TextIOWrapper name='data.txt' mode='r' encoding='UTF-8'>

# 3️⃣ File Modes (VERY IMPORTANT)
# Mode	Purpose	Real-time Use
# "r"	Read file (default)	Reading logs, configs
# "w"	Write (overwrites)	Creating reports
# "a"	Append	Adding new log entries
# "x"	Create new file	Prevent overwriting
# "b"	Binary mode	Images, videos
# "t"	Text mode (default)	Text files
# "r+"	Read + Write	Editing existing file

# Theory:
# Modes control:

# Permission (read/write)

# File existence behavior

# Data type (text/binary)

# 4️⃣ Closing a File
file.close()


# Definition: Releases system resources.

# Theory:
# Closing:

# Flushes buffer

# Saves data

# Prevents memory leaks

# Output: No visible output. file.closed becomes True.

# 5️⃣ Using with Statement (Best Practice ⭐)
with open("data.txt", "r") as file:
    content = file.read()


# Definition:
# with uses a context manager to manage resources.

# Theory:
# Even if an error happens, Python automatically calls file.close().

# Output Example:
# If data.txt contains:

# Hello
# Python


# Then:

# content = "Hello\nPython\n"

# 6️⃣ Reading Files
# 🔹 read()

# Reads entire file.

file.read()


# Theory: Loads full file into memory.

# Output:

# "Hello\nPython\nWelcome\n"

# 🔹 read(n)

# Reads first n characters.

# Output (read(5)):

# "Hello"

# 🔹 readline()
file.readline()


# Output:

# "Hello\n"

# 🔹 readlines()
lines = file.readlines()


# Output:

# ["Hello\n", "Python\n", "Welcome\n"]

# 7️⃣ Writing to File
# 🔹 write()
with open("data.txt", "w") as f:
    f.write("Hello\n")


# Theory: Overwrites file if exists.

# Output in file:

# Hello

# 🔹 writelines()
lines = ["A\n", "B\n"]
f.writelines(lines)


# Output in file:

# A
# B

# 8️⃣ Appending to File
with open("data.txt", "a") as f:
    f.write("New Line\n")


# Theory: Pointer at end.

# Output (if file had Hello):

# Hello
# New Line

# 9️⃣ File Pointer Methods
# Method	Purpose
# tell()	Current position
# seek(pos)	Move pointer
file.seek(0)


# Output: Pointer moves to start.
# tell() before = 10, after seek = 0.

# 🔟 Exception Handling with Files
try:
    with open("data.txt", "r") as f:
        print(f.read())
except FileNotFoundError:
    print("File not found!")
finally:
    print("Done")


# Output if file exists:

# Hello
# Python
# Done


# Output if file missing:

# File not found!
# Done

# 1️⃣1️⃣ Working with Binary Files
with open("image.jpg", "rb") as f:
    data = f.read()


# Theory: Reads raw bytes.

# Output (sample):

# b'\xff\xd8\xff\xe0\x00\x10JFIF...'

# 1️⃣2️⃣ File Attributes
file.name
file.mode
file.closed


# Output Example:

# 'data.txt'
# 'r'
# False

# 1️⃣3️⃣ Checking File Existence
import os
os.path.exists("data.txt")


# Output:

# True


# or

# False

# 1️⃣4️⃣ Deleting Files
import os
os.remove("data.txt")


# Output: File removed. No text output.

# 1️⃣5️⃣ File Handling with CSV
import csv

with open("data.csv") as f:
    reader = csv.reader(f)
    for row in reader:
        print(row)


# CSV File:

# Name,Age
# John,25


# Output:

# ['Name', 'Age']
# ['John', '25']

# 1️⃣6️⃣ File Handling with JSON
import json

with open("data.json", "r") as f:
    data = json.load(f)

with open("data.json", "w") as f:
    json.dump(data, f)


# JSON File:

# {"name": "John", "age": 25}


# Output in Python:

# {'name': 'John', 'age': 25}

# 1️⃣7️⃣ Large File Handling (Memory Efficient)
with open("bigfile.txt") as f:
    for line in f:
        print(line)


# Output: Prints line by line without memory overload.

# 1️⃣8️⃣ Decorator to Log File Operation Time
import time

def timer(func):
    def wrapper(*args):
        start = time.time()
        func(*args)
        print("Time:", time.time() - start)
    return wrapper


# Output Example:

# Time: 0.00234

# 1️⃣9️⃣ Common Interview Questions

# (unchanged — already theory-based)

# 2️⃣0️⃣ Best Practices ✅

# ✔ Always use with
# ✔ Handle exceptions
# ✔ Use line-by-line reading for large files
# ✔ Close files properly
# ✔ Use correct mode

# 🧠 One-Line Summary (Interview)

# Python file handling enables permanent data storage using file streams, access modes, and context managers for safe resource control.