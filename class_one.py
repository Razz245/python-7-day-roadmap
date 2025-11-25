print("Hello from class_one.py")
print("This is a sample Python file.")
a = 10
b = 20
c = a + b
print("The sum of a and b is:", c)

# Tutorial 3
"""Python Variables and Constants"""

# Declaring constants
PI = 3.14159
GRAVITY = 9.81

# Declaring and assigning values to variables
a = "Apple"
print("Fruit:", a)

# Changing value of variable
a = "Aeroplane"
print("Vehicle:", a)

a = 100
print("Number:", a)

# Assigning multiple values to multiple variables
b, c, d = 1, 2.5, "Hello"
print("Integer:", b, c, d)

# Assigning same value to multiple variables
b = c = d = 5
print("Values:", b, c, d)

# Tutorial 4
"""Python Classes and Objects"""

class MyComplexNumber:
    # Constructor Method
    def __init__(self, real=0, imag=0):
        print("MyComplexNumber Object is created")
        self.real_part = real
        self.imag_part = imag

    def displayComplex(self):
        print(f"{self.real_part} + {self.imag_part}j")

# Creating Object of MyComplexNumber class
complex1 = MyComplexNumber(30, 40)
complex1.displayComplex()

"""Creating another object using default constructor values"""
complex2 = MyComplexNumber(60, 70)
complex2.new_attr = 80

print((complex2.real_part, complex2.imag_part, complex2.new_attr))

# Deleting object attribute and object
print(complex1)
del complex1.real_part
del complex1
print("complex1 deleted successfully")

      