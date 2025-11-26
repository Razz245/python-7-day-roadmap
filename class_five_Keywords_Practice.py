# Python Keywords & Identifiers Practice Sheet
# -----------------------------------------
# This file contains all examples explained.

# 1. True / False
print(True)
print(False)
print(5 > 2)
print(5 < 1)

# 2. None
x = None
print(x)

# 3. and
age = 20
id_card = True
print(age >= 18 and id_card)

# 4. or
rain = False
umbrella = True
print(rain or umbrella)

# 5. not
logged_in = False
print(not logged_in)

# 6. if / elif / else
marks = 55
if marks >= 80:
    print("A+")
elif marks >= 60:
    print("A")
elif marks >= 50:
    print("B")
else:
    print("F")

# 7. for
for i in range(5):
    print(i)

# 8. while
x = 1
while x <= 3:
    print(x)
    x += 1

# 9. break
for i in range(10):
    if i == 5:
        break
    print(i)

# 10. class / def / return
class Person:
    def __init__(self, name):
        self.name = name

    def hello(self):
        return f"Hello {self.name}"

p = Person("Razz")
print(p.hello())

# 11. try / except / finally
try:
    y = 10 / 0
except:
    print("Error occurred!")
finally:
    print("Finished")

# 12. import / from / as
import math
print(math.sqrt(16))

from math import sqrt as s
print(s(25))

# 13. is
x = None
print(x is None)

# 14. in
print("a" in "kat")

# 15. pass
def todo():
    pass

# 16. global
value = 10

def modify():
    global value
    value = 20

modify()
print(value)

# 17. nonlocal
def outer():
    a = 10
    def inner():
        nonlocal a
        a = 20
    inner()
    print(a)

outer()

# 18. lambda
add = lambda x, y: x + y
print(add(5, 7))

# 19. yield
def numbers():
    yield 1
    yield 2
    yield 3

for n in numbers():
    print(n)
