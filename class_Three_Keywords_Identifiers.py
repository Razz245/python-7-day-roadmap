"""
Class Three:
Python Keywords and Identifiers
"""

# -----------------------------
# 1. Python Keywords
# -----------------------------
import keyword

print("=== Python Keywords ===")
print(keyword.kwlist)
print("Total Keywords:", len(keyword.kwlist))
print("\n")

# -----------------------------
# 2. Identifiers Introduction
# -----------------------------
"""
Identifiers are names for:
- Variables
- Functions
- Classes
- Modules
- Objects

Rules:
1. Must start with a letter (A-Z / a-z) or underscore (_)
2. Can contain digits after the first character
3. No spaces allowed
4. Keywords cannot be used
5. Case-sensitive
"""

# Valid Identifiers
name = "Razz"
first_name = "Python"
age1 = 25
_price = 100
totalAmount = 500

print("=== Valid Identifiers Output ===")
print(name, first_name, age1, _price, totalAmount)
print("\n")

# Invalid Identifiers (Commented to avoid errors)
"""
1age = 10          # starts with number
first-name = "John"  # hyphen not allowed
total amount = 20    # space not allowed
class = "Hello"      # keyword not allowed
"""

# -----------------------------
# 3. Check If a Name Is Keyword
# -----------------------------
print("=== Check User Input: Keyword or Identifier ===")
user_input = input("Enter a name: ")

if keyword.iskeyword(user_input):
    print(f"{user_input} is a Python keyword.")
else:
    print(f"{user_input} is a valid identifier.")
print("\n")

# -----------------------------
# 4. Task One: Write Identifier Info
# -----------------------------
with open("identifiers.txt", "w") as f:
    f.write("Valid Identifiers:\n")
    f.write("name\nfirst_name\nage1\n_price\ntotalAmount\n\n")
    f.write("Invalid Identifiers:\n")
    f.write("1name\nfirst-name\ntotal amount\nfor (keyword)\n\n")
    f.write("Total Keywords: " + str(len(keyword.kwlist)) + "\n")
    f.write("Keywords List:\n" + ", ".join(keyword.kwlist) + "\n")

print("Identifiers and Keywords information written to identifiers.txt")
print("\n")

# -----------------------------
# 5. Task Two: Save Only Keywords
# -----------------------------
with open("keywords.txt", "w") as f:
    for kw in keyword.kwlist:
        f.write(kw + "\n")

print("Keywords written to keywords.txt")
print("\n")

# -----------------------------
# 6. Task Three: Keyword or Identifier Checker
# -----------------------------
var = input("Enter a name again to verify: ")

if keyword.iskeyword(var):
    print(f"{var} is a Python keyword.")
else:
    print(f"{var} is a valid identifier.")

print("\nAll tasks completed successfully!")
