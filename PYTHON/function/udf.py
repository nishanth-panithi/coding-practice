# 🧠 What is a Function in Python?

# A function is a block of reusable code that performs a specific task.

# Instead of writing the same code again and again, we define once and call many times.

# 👉 Syntax
# def function_name(parameters):
#     # block of code
#     return value

# 👉 Example
def greet(name):
    return "Hello " + name

# print(greet("Nishanth"))

# 🚀 Types of Functions in Python

# Python functions are mainly divided into two big categories:

# 1️⃣ Built-in Functions (Already provided by Python)

# These are functions Python gives us directly.

# 🔹 Purpose

# To perform common tasks quickly.

# 🔹 Real-time Use

# Used in almost every program.

# 🔹 Examples
# Function	Use
# print()	Displays output
# len()	Finds length
# type()	Checks datatype
# sum()	Adds numbers
# max()	Finds largest value
numbers = [10, 20, 30]
print(len(numbers))   # 3
print(max(numbers))   # 30

################################################
# ⭐ 1. Basic User-Defined Function
# ✅ Definition

# A function created using def to perform a specific task.

# 🧩 Syntax
# def function_name():
#     # code

# 💻 Example
def greet():
    print("Hello Nishanth!")

greet()

# Output: Hello Nishanth!

# 🌍 Real-time Use

# Used to avoid repeating code (e.g., greeting message, logging, printing reports).

# ⭐ 2. Function with Parameters
# ✅ Definition

# Function that takes input values.

# 🧩 Syntax
# def function_name(parameter1, parameter2):
#     # code

# 💻 Example
def add(a, b):
    print(a + b)

add(5, 3)

# Output: 8

# 🌍 Real-time Use

# Used in calculators, form inputs, API data processing.

# ⭐ 3. Function with Return Value
# ✅ Definition

# Function that sends result back using return.

# 🧩 Syntax
# def function_name():
#     return value

# 💻 Example
def square(n):
    return n * n

result = square(4)
print(result)

# Output: 16

# 🌍 Real-time Use

# Bank balance calculation, tax computation, scoring systems.

# ⭐ 4. Default Parameter Function
# ✅ Definition

# Parameter has a default value if user doesn't pass one.

# 🧩 Syntax
# def function_name(param=value):

# 💻 Example
def greet(name="Guest"):
    print("Hello", name)

greet()
greet("Nishanth")

# Output:   Hello Guest
            # Hello Nishanth

# 🌍 Real-time Use

# Forms where optional fields exist.

# ⭐ 5. Keyword Argument Function
# ✅ Definition

# Arguments passed using parameter names.

# 💻 Example
def student(name, age):
    print(name, age)

student(age=21, name="Nishanth")

# Output: Nishanth 21


# 🌍 Real-time Use

# APIs and configuration settings.

# ⭐ 6. Variable-Length Arguments
# (a) *args → multiple values
# 🧩 Syntax
# def function_name(*args):

# 💻 Example
def total_sum(*numbers):
    print(sum(numbers))

total_sum(1, 2, 3, 4)

# Output: 10


# 🌍 Real-time Use

# Shopping cart totals, dynamic inputs.

# (b) **kwargs → key-value inputs
# 🧩 Syntax
# def function_name(**kwargs):

# 💻 Example
def details(**data):
    print(data)

details(name="Nishanth", age=21)

# Output: {'name': 'Nishanth', 'age': 21}


# 🌍 Real-time Use

# User profiles, JSON data handling.

# ⭐ 7. Recursive Function
# ✅ Definition

# Function calling itself.

# 💻 Example
def factorial(n):
    if n == 1:
        return 1
    return n * factorial(n-1)

print(factorial(5))

# Output: 120


# 🌍 Real-time Use

# Tree structures, file system traversal.

# ⭐ 8. Lambda Function (Anonymous Function)
# ✅ Definition

# Short, single-line function without name.

# 🧩 Syntax
# lambda arguments: expression

# 💻 Example
square = lambda x: x * x
print(square(5))

# Output: 25


# 🌍 Real-time Use

# Sorting, filtering, quick operations.

# Alternative: Use normal def if logic is complex.

# ⭐ 9. Nested Function
# ✅ Definition

# Function inside another function.

# 💻 Example
def outer():
    def inner():
        print("Inside inner")
    inner()

outer()

# Output: Inside inner


# 🌍 Real-time Use

# Data hiding, helper functions.

# ⭐ 10. Closure Function
# ✅ Definition

# Inner function remembers outer function variables.

# 💻 Example
def outer(x):
    def inner(y):
        return x + y
    return inner

add_five = outer(5)
print(add_five(3))

# Output: 8


# 🌍 Real-time Use

# Configuration-based functions.

# ⭐ 11. Generator Function
# ✅ Definition

# Uses yield to return values one at a time.

# 💻 Example
def count_up_to(n):
    for i in range(n):
        yield i

for num in count_up_to(3):
    print(num)

# Output:   0
#           1
#           2


# 🌍 Real-time Use

# Large data processing, file reading.

# Alternative: Normal function returns full list (uses more memory).

# ⭐ 12. Decorator Function
# ✅ Definition

# Function that modifies another function.

# 💻 Example
def decorator(func):
    def wrapper():
        print("Before function")
        func()
        print("After function")
    return wrapper

@decorator
def say_hello():
    print("Hello!")

say_hello()

# Output:   Before function
#           Hello!
#           After function


# 🌍 Real-time Use

# Logging, authentication, timing execution.

# 🎯 Interview Tip

# If asked “What are user-defined functions?”

# 👉 "Functions created using def by the programmer to perform specific reusable tasks. They improve modularity, reduce repetition, and make code maintainable."