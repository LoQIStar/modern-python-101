# Python Phase 1: Getting Started with Python

## 1. Basic Syntax and Rules

### Python Indentation
```python
# Indentation is crucial in Python - it defines code blocks
if True:
    print("This is indented")  # Standard is 4 spaces
    if True:
        print("Nested indentation")  # 8 spaces
```

### Comments
```python
# This is a single-line comment

"""
This is a multi-line comment
or docstring when used at the
beginning of a function/class
"""
```

### Variables and Data Types
```python
# Variable naming rules:
# - Must start with letter or underscore
# - Can contain letters, numbers, underscores
# - Case-sensitive
name = "John"           # str (string)
age = 25               # int (integer)
height = 1.75          # float (floating-point)
is_student = True      # bool (boolean)
numbers = [1, 2, 3]    # list
coordinates = (x, y)   # tuple
person = {"name": "John", "age": 25}  # dict (dictionary)
unique_items = {1, 2, 3}  # set
```

## 2. Basic Operations

### Arithmetic Operations
```python
# Basic math
addition = 5 + 3       # 8
subtraction = 5 - 3    # 2
multiplication = 5 * 3 # 15
division = 5 / 3       # 1.6666... (float division)
floor_division = 5 // 3 # 1 (integer division)
modulus = 5 % 3        # 2 (remainder)
power = 5 ** 3         # 125 (5 to the power of 3)

# Augmented assignment
x = 5
x += 3  # Same as: x = x + 3
x -= 2  # Same as: x = x - 2
x *= 4  # Same as: x = x * 4
```

### String Operations
```python
# String creation
single_quotes = 'Hello'
double_quotes = "World"
multi_line = """This is a
multi-line string"""

# String concatenation
full_greeting = single_quotes + " " + double_quotes  # "Hello World"

# String formatting
name = "John"
age = 25
# f-strings (Python 3.6+)
message = f"My name is {name} and I'm {age} years old"
# .format() method
message = "My name is {} and I'm {} years old".format(name, age)
# % operator (older style)
message = "My name is %s and I'm %d years old" % (name, age)

# String methods
text = "  Hello, World!  "
text.upper()          # "  HELLO, WORLD!  "
text.lower()          # "  hello, world!  "
text.strip()          # "Hello, World!"
text.replace("o", "0") # "  Hell0, W0rld!  "
text.split(",")       # ["  Hello", " World!  "]
```

## 3. Control Flow

### Conditional Statements
```python
# if, elif, else
age = 18
if age < 13:
    print("Child")
elif age < 20:
    print("Teenager")
else:
    print("Adult")

# Ternary operator
status = "Adult" if age >= 18 else "Minor"
```

### Loops
```python
# For loop
for i in range(5):
    print(i)  # Prints 0, 1, 2, 3, 4

# Loop through list
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)

# While loop
count = 0
while count < 5:
    print(count)
    count += 1

# Break and Continue
for i in range(10):
    if i == 3:
        continue  # Skip this iteration
    if i == 8:
        break    # Exit the loop
    print(i)
```

## 4. Basic Functions

### Function Definition and Usage
```python
# Basic function
def greet(name):
    return f"Hello, {name}!"

# Function with default parameter
def greet_with_title(name, title="Mr."):
    return f"Hello, {title} {name}!"

# Function with multiple parameters
def calculate_rectangle_area(length, width):
    return length * width

# Function with arbitrary arguments
def sum_all(*args):
    return sum(args)

# Function with keyword arguments
def print_info(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")
```

## 5. Basic Data Structures

### Lists
```python
# List creation and operations
fruits = ["apple", "banana", "cherry"]
fruits.append("date")        # Add to end
fruits.insert(1, "orange")   # Insert at index
fruits.remove("banana")      # Remove by value
popped = fruits.pop()        # Remove and return last item
fruits.sort()               # Sort in place
sorted_fruits = sorted(fruits)  # Return new sorted list
```

### Dictionaries
```python
# Dictionary creation and operations
person = {
    "name": "John",
    "age": 25,
    "city": "New York"
}

# Accessing values
name = person["name"]       # Using key
age = person.get("age")     # Using get method

# Modifying dictionary
person["email"] = "john@example.com"  # Add new key-value
person.update({"phone": "123-456-7890"})  # Update multiple

# Dictionary methods
keys = person.keys()        # Get all keys
values = person.values()    # Get all values
items = person.items()      # Get all key-value pairs
```

## 6. Error Handling

### Try-Except Blocks
```python
# Basic error handling
try:
    number = int(input("Enter a number: "))
    result = 10 / number
except ValueError:
    print("Please enter a valid number")
except ZeroDivisionError:
    print("Cannot divide by zero")
except Exception as e:
    print(f"An error occurred: {e}")
else:
    print(f"Result: {result}")  # Runs if no exception
finally:
    print("This always runs")   # Cleanup code
```

## 7. File Operations

### Basic File Handling
```python
# Reading a file
with open("file.txt", "r") as file:
    content = file.read()           # Read entire file
    lines = file.readlines()        # Read lines into list

# Writing to a file
with open("file.txt", "w") as file:
    file.write("Hello, World!")     # Write string
    file.writelines(["Line 1\n", "Line 2\n"])  # Write multiple lines

# Appending to a file
with open("file.txt", "a") as file:
    file.write("New content")
```

## 8. Built-in Functions

### Common Built-in Functions
```python
# Type conversion
str(123)               # Convert to string
int("123")            # Convert to integer
float("12.34")        # Convert to float
bool(1)               # Convert to boolean

# Sequence functions
len([1, 2, 3])        # Length of sequence
max([1, 2, 3])        # Maximum value
min([1, 2, 3])        # Minimum value
sum([1, 2, 3])        # Sum of sequence

# Other useful functions
abs(-5)               # Absolute value
round(3.14159, 2)     # Round to 2 decimal places
isinstance(5, int)    # Check type
type(5)               # Get type
help(str)             # Get help documentation
```

## 9. Best Practices

### Python Style Guide (PEP 8)
- Use 4 spaces for indentation
- Use snake_case for function and variable names
- Use CamelCase for class names
- Keep lines under 79 characters
- Add docstrings to functions and classes
- Use meaningful variable names
- Add comments to explain complex logic

### Code Organization
```python
# Import statements at top
import os
from datetime import datetime

# Constants in UPPERCASE
MAX_ATTEMPTS = 3
DEFAULT_TIMEOUT = 30

# Classes and functions
class User:
    def __init__(self, name):
        self.name = name

def main():
    # Main program logic here
    pass

if __name__ == "__main__":
    main() 