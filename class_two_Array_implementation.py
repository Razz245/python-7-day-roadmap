"""
Python Array Implementation using list
File: Class_two_Array_implementation.py
"""

class Array:
    def __init__(self, size):
        """Initialize array with fixed size and default None values"""
        self.size = size
        self.data = [None] * size
        self.length = 0  # Number of elements added

    def insert(self, index, value):
        """Insert value at specific index"""
        if self.length >= self.size:
            print("Error: Array is full")
            return
        if index < 0 or index > self.length:
            print("Error: Index out of bounds")
            return
        # Shift elements to right
        for i in range(self.length, index, -1):
            self.data[i] = self.data[i-1]
        self.data[index] = value
        self.length += 1

    def append(self, value):
        """Append value at the end"""
        self.insert(self.length, value)

    def delete(self, index):
        """Delete value at specific index"""
        if index < 0 or index >= self.length:
            print("Error: Index out of bounds")
            return
        for i in range(index, self.length-1):
            self.data[i] = self.data[i+1]
        self.data[self.length-1] = None
        self.length -= 1

    def display(self):
        """Display current array elements"""
        print([self.data[i] for i in range(self.length)])

    def get(self, index):
        """Get value at index"""
        if index < 0 or index >= self.length:
            print("Error: Index out of bounds")
            return None
        return self.data[index]

    def set(self, index, value):
        """Set value at index"""
        if index < 0 or index >= self.length:
            print("Error: Index out of bounds")
            return
        self.data[index] = value


# ===== Example Usage =====
if __name__ == "__main__":
    arr = Array(5)  # Array of size 5
    arr.append(10)
    arr.append(20)
    arr.append(30)
    arr.display()  # Output: [10, 20, 30]

    arr.insert(1, 15)
    arr.display()  # Output: [10, 15, 20, 30]

    arr.delete(2)
    arr.display()  # Output: [10, 15, 30]

    print("Value at index 1:", arr.get(1))  # Output: 15
    arr.set(1, 25)
    arr.display()  # Output: [10, 25, 30]


"""Topic: Besic"""
#Defining and declaring and array
arr = [10, 20, 30, 40, 50]
print(arr)

#Accessing Array Elements
print(arr[0])
print(arr[1])
print(arr[2])
print(arr[-1]) #Negative Indexing
print(arr[-2]) #Negative Indexing

brands = ["Coke", "Apple", "Google", "Microsoft", "Toyota"]
print(brands)

#Finding the length og the array
num_brands = len(brands)

#Findind the length of the array
num_brands = len(brands)
print(num_brands)

#Adding om elements to an array using append
brands.append("Intel")
print(brands)

#Remobing Elenents from an array
colors = ["violet", "indigo", "blue", "green", "yellow", "orange", "red"]
del colors[4]
colors.remove("blue")
colors.pop(3)
print(colors)

#Modifying elements of an array using indexing
fruits = ["Apple", "Banana", "Mango", "Grapes", "Orange"]
fruits[1] = "Pineapple"
fruits[-1] = "Guava"
print(fruits)

# Concatebting two arrays using the + operator
concat = [1, 2, 3]
concat + [4, 5, 6]
print(concat)
concat = concat + [4, 5, 6]
print(concat)

#Repeating elements im an array
repeat = ["a"]
repeat = repeat * 5
print(repeat)

#Slicing an array
fruits = ["Apple", "Banana", "Mango", "Grapes", "Orange"]
print(fruits)
print(fruits[1:4])
print(fruits[:3])
print(fruits[-4:])
print(fruits[-3:-1])

# Declearing and defininf=g multdimentional array
multd = [[1,2], [3,4],[5,6], [7,8]]
print(multd)
print(multd[0])
print(multd[3])
print(multd[2][1])
print(multd[3][0])

