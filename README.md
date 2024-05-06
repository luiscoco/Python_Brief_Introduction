# Python: a brief introduction

## 1. How to install Python

https://www.python.org/downloads/

![image](https://github.com/luiscoco/Python_Brief_Introduction/assets/32194879/d8ba5ff6-7779-4255-aab6-2720b3e0d9b1)

We intall python latest version

We verify the installed version:

```
python --version
```

![image](https://github.com/luiscoco/Python_Brief_Introduction/assets/32194879/8e5061e5-897f-45eb-962b-f589cc755a9f)

## 2. How to create a python project in VSCode and how to run it

We first install the official Microsoft Pythoh extension in VSCode

![image](https://github.com/luiscoco/Python_Brief_Introduction/assets/32194879/d1432cbb-0faa-49f0-a46e-3a36c02c0ce1)

We create a new python file 

**hello_world.py**

```python
print("Hello, World!")
```

For running this first application we execute the command

```
python hello_world.py
```

![image](https://github.com/luiscoco/Python_Brief_Introduction/assets/32194879/d52ced43-6350-438e-ba8b-e2d3d27a0d81)

## 3. Dynamic Typing

You don't need to declare variable types explicitly; Python infers them dynamically. For example:

```python
x = 5
print(x)
```

```python
x = "Hello"
print(x)
```

## 4. Indentation-based Syntax

Python uses indentation to define blocks of code, rather than braces or keywords 

For example, in a loop:

```python
for i in range(5):
    print(i)
```

## 5. Extensive Standard Library:

Python comes with a large standard library that provides modules and functions for many common tasks

For example, to work with dates:

```python
from datetime import datetime

now = datetime.now()
print("Current date and time:", now)
```

## 6. Object-Oriented

Python supports object-oriented programming, allowing you to define classes and objects

For example:

```python
class Dog:
    def __init__(self, name):
        self.name = name

    def bark(self):
        print(f"{self.name} says Woof!")

my_dog = Dog("Buddy")
my_dog.bark()  # Output: Buddy says Woof!
```

## 7. Functional Programming

Python supports functional programming paradigms like lambda functions and map/filter/reduce

For example:

```python
# Lambda function
add = lambda x, y: x + y
print(add(3, 5))  # Output: 8

# Map function
numbers = [1, 2, 3, 4, 5]
squared = list(map(lambda x: x ** 2, numbers))
print(squared)  # Output: [1, 4, 9, 16, 25]
```

## 8. List Comprehensions:

Python supports concise syntax for creating lists based on existing lists

For example:

```python
# Create a list of squares of numbers from 1 to 5
squares = [x ** 2 for x in range(1, 6)]
print(squares)  # Output: [1, 4, 9, 16, 25]
```

## 9. Exception Handling:

Python allows you to handle exceptions gracefully using try, except, and finally blocks

For example:

```python
try:
    result = 10 / 0
except ZeroDivisionError:
    print("Cannot divide by zero!")
```

## 10. Modules and Packages:

Python code can be organized into modules and packages, making it easy to reuse code across projects

For example, you can **create a module** named my_module.py:

```python
# my_module.py
def greet(name):
    print("Hello, " + name)
```

Then you can **use this module** in another Python file:

```python
# main.py
import my_module

my_module.greet("Alice")
```

## 11. File Handling:

Python provides built-in functions for reading from and writing to files

For example:

```python
# Writing to a file
with open("example.txt", "w") as file:
    file.write("Hello, World!")

# Reading from a file
with open("example.txt", "r") as file:
    content = file.read()
    print(content)  # Output: Hello, World!
```

## 12. Generators:

Python supports generators, which are functions that can yield multiple values lazily

For example:

```python
def countdown(n):
    while n > 0:
        yield n
        n -= 1

for num in countdown(5):
    print(num)  # Output: 5, 4, 3, 2, 1
```

## 13. Decorators:

Python decorators allow you to modify the behavior of functions or methods

For example:

```python
def uppercase_decorator(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        return result.upper()
    return wrapper

@uppercase_decorator
def greet(name):
    return f"Hello, {name}"

print(greet("Alice"))  # Output: HELLO, ALICE
```



