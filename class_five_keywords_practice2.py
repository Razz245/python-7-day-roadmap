"""
Class Five:
Python Keywords & Practical Examples
"""

# ===============================
# 1. Logical Operators: and, or, not
# ===============================

a = 10
b = 20
c = 5

print("=== Logical Operators ===")
print(a > b and a > c)   # False
print(a < b or b < c)    # True
print(not (a < b))       # False
print("\n")


# ===============================
# 2. Conditional Keywords: if / elif / else
# ===============================

x = 45

print("=== if / elif / else ===")
if x > 50:
    print("Greater than 50")
elif x == 50:
    print("Equal to 50")
else:
    print("Less than 50")
print("\n")


# ===============================
# 3. Loop Keywords: for, while, break
# ===============================

print("=== For Loop with Break ===")
for i in range(10):
    if i == 5:
        break
    print(i)
print("\n")


print("=== While Loop ===")
count = 1
while count <= 5:
    print(count)
    count += 1
print("\n")


# ===============================
# 4. Defining functions using def & return
# ===============================

print("=== Function Example ===")
def add_numbers(x, y):
    return x + y

print(add_numbers(3, 7))
print("\n")


# ===============================
# 5. Class keyword
# ===============================

print("=== Class Example ===")
class Person:
    def __init__(self, name):
        self.name = name

    def show(self):
        print("Name:", self.name)


p = Person("Razz")
p.show()
print("\n")


# ===============================
# 6. Exception handling: try / except / finally
# ===============================

print("=== Try / Except / Finally ===")
try:
    result = 10 / 0
except ZeroDivisionError:
    print("Cannot divide by zero!")
finally:
    print("Execution Completed.\n")


# ===============================
# 7. Import / from / as
# ===============================

print("=== Import Example ===")
import math
from math import sqrt as root

print("Pi value:", math.pi)
print("Square root of 16:", root(16))
print("\n")


# ===============================
# 8. Identity & Membership: is / in
# ===============================

print("=== is / in Example ===")
a = [1, 2, 3]
b = a

print(a is b)           # True
print(2 in a)           # True
print("\n")


# ===============================
# 9. pass keyword
# ===============================

print("=== pass Example ===")
for i in range(3):
    pass   # Placeholder, no action
print("Pass used successfully.\n")


# ===============================
# 10. global & nonlocal
# ===============================

print("=== global / nonlocal Example ===")
total = 0

def add():
    global total
    total += 10

add()
print("Global total:", total)


def outer():
    value = 5

    def inner():
        nonlocal value
        value += 5
        return value

    return inner()

print("Nonlocal value:", outer())
print("\n")


# ===============================
# 11. lambda
# ===============================

print("=== Lambda Example ===")
square = lambda x: x * x
print(square(6))
print("\n")


# ===============================
# 12. yield Example (Generator)
# ===============================

print("=== Yield Example (Generator) ===")
def my_generator():
    yield 1
    yield 2
    yield 3

for num in my_generator():
    print(num)
print("\n")

