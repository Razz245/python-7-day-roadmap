"""
Class Four:
Python Logical Operators (and, or, not)
"""

# -------------------------------------
# 1. Basic Logical Operator Examples
# -------------------------------------

print("=== Basic Logical Operations ===")
print("True and True  =", True and True)
print("True and False =", True and False)
print("True or False  =", True or False)
print("False or False =", False or False)
print("not True       =", not True)
print("not False      =", not False)
print("\n")

# -------------------------------------
# 2. Real Life Examples
# -------------------------------------

print("=== Real Life Examples ===")

age = 20
has_id = True

print("Age >= 18 and has_id :", age >= 18 and has_id)
print("Age < 18 or has_id   :", age < 18 or has_id)
print("not has_id           :", not has_id)
print("\n")

# -------------------------------------
# 3. Login System Example
# -------------------------------------

print("=== Login Check Example ===")

username = "admin"
password = "1234"

if username == "admin" and password == "1234":
    print("Login Successful!")
else:
    print("Invalid credentials!")
print("\n")

# -------------------------------------
# 4. Practice Tasks (Auto Examples)
# -------------------------------------

print("=== Practice Tasks Solutions ===")

# Task 1: Both positive check
a, b = 10, 5
if a > 0 and b > 0:
    print("Task-1: Both Positive")
else:
    print("Task-1: Not Positive")

# Task 2: Age restriction
age = 65
if age < 18 or age > 60:
    print("Task-2: Not Allowed (age restriction)")
else:
    print("Task-2: Allowed")
    
# Task 3: Empty string check
user_text = ""
if not user_text:
    print("Task-3: Input is Empty")
else:
    print("Task-3: Input Provided")

# Task 4: Weather condition
temperature = 32
humidity = 80

if temperature > 30 and humidity > 70:
    print("Task-4: Hot & Humid")
else:
    print("Task-4: Normal Weather")

# Task 5: Wrong password check
real_password = "admin123"
user_input = "admin12"

if not (user_input == real_password):
    print("Task-5: Wrong Password")
else:
    print("Task-5: Correct Password")

print("\nAll tasks completed successfully!")
    