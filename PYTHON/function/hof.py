# 🔥 Built-in Higher Order Functions in Python

# These are functions that take another function as argument.

# 1️⃣ map()
# ✅ Purpose

# Applies a function to every element in an iterable.

# 🧠 Real-Time Use

# Data transformation (convert, scale, format, etc.)

nums = [1, 2, 3, 4]
result = list(map(lambda x: x * 10, nums))
print(result)


# Output: [10, 20, 30, 40]

# 🔄 Alternative
result = []
for n in nums:
    result.append(n * 10)

# 2️⃣ filter()
# ✅ Purpose

# Filters elements based on a condition function.

# 🧠 Real-Time Use

# Removing unwanted data (invalid users, odd numbers, empty values)

nums = [1, 2, 3, 4, 5]
evens = list(filter(lambda x: x % 2 == 0, nums))
print(evens)


# Output: [2, 4]

# 🔄 Alternative
evens = []
for n in nums:
    if n % 2 == 0:
        evens.append(n)

# 3️⃣ reduce() (from functools)
# ✅ Purpose

# Reduces an iterable to a single value.

# 🧠 Real-Time Use

# Sum, product, cumulative operations

from functools import reduce

nums = [1, 2, 3, 4]
total = reduce(lambda a, b: a + b, nums)
print(total)


# Output: 10

# 🔄 Alternative
total = 0
for n in nums:
    total += n

# 4️⃣ sorted()
# ✅ Purpose

# Sorts using a custom function.

# 🧠 Real-Time Use

# Sorting by length, salary, marks, dates, etc.

words = ["apple", "kiwi", "banana"]
print(sorted(words, key=len))


# Output: ['kiwi', 'apple', 'banana']

# 5️⃣ min() / max()
# ✅ Purpose

# Find smallest/largest using a function.

words = ["apple", "kiwi", "banana"]
print(max(words, key=len))


# Output: banana

# 6️⃣ any()
# ✅ Purpose

# Returns True if any element satisfies condition.

nums = [0, 0, 5]   # ->[false,false,true]
print(any(nums))


# Output: True

# 7️⃣ all()
# ✅ Purpose

# Returns True if all elements satisfy condition.

nums = [1, 2, 3]  # -> [true,true,true]
print(all(nums))


# Output: True

# 8️⃣ zip()
# ✅ Purpose

# Combines iterables element-wise (used with functions often).

names = ["A", "B"]
marks = [90, 80]
print(list(zip(names, marks)))


# Output:[('A', 90), ('B', 80)]

# 🧠 Interview Cheat Line

# “Common built-in higher order functions in Python are map(), filter(), reduce(), sorted(), min(), max(), any(), and all() — they accept functions as arguments to perform dynamic operations.”