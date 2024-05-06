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

## 3. Variable types and built-in objects

Python has a range of variable types and built-in objects that facilitate various kinds of operations and data management

Let's go through the primary types and provide some code samples for each

### 3.1. Basic Variable Types

These are the fundamental types that you will use very frequently in Python

**Integer**

Integers (int) are whole numbers without a fractional part

```python
x = 10
print(x, type(x))
```

**Float**

Floating point numbers (float) represent real numbers and are written with a decimal point dividing the integer and fractional parts

```python
y = 3.14
print(y, type(y))
```

**String**

Strings (str) are sequences of Unicode characters, used for storing text

```python
z = "Hello, Python!"
print(z, type(z))
```

**Boolean**

Booleans (bool) can have two values: True and False. They are often used in conditions to control the flow of the program

```python
a = True
b = False
print(a, type(a))
print(b, type(b))
```

### 3.2. Built-in Compound Types

Python also has several built-in types that can handle multiple items in a single variable

**List**

Lists are ordered and mutable collections that can contain mixed types

```python
my_list = [1, 2, 3, "Python", True]
print(my_list, type(my_list))
```

**Tuple**

Tuples are ordered and immutable collections

Once created, their content cannot be changed

```python
my_tuple = (1, 2, 3, "Python")
print(my_tuple, type(my_tuple))
```

**Dictionary**

Dictionaries store data as key-value pairs and are mutable

```python
my_dict = {'name': 'John', 'age': 30}
print(my_dict, type(my_dict))
```

**Set**

Sets are unordered collections of unique elements.

```python
my_set = {1, 2, 3, 2}
print(my_set, type(my_set))  # {1, 2, 3}
```

### 3.3. Other Built-in Types

There are other types like **NoneType**, used for the None object, which signifies the absence of a value

```python
nothing = None
print(nothing, type(nothing))
```

**Built-in Functions and Object Methods**

Python has numerous built-in functions that interact with these types, and each type has its own set of methods

For example:

len() to get the length of a list, tuple, string, dictionary, or set

.append() method to add an item to a list

.upper() method to convert a string to uppercase

Here's a quick demonstration of some of these functions and methods:

```python
# Built-in function
print(len(my_list))

# List method
my_list.append("new item")
print(my_list)

# String method
print(z.upper())
```

### 3.4. Dynamic Typing

You don't need to declare variable types explicitly; Python infers them dynamically

For example:

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

## 5. Extensive Standard Library

Python comes with a large standard library that provides modules and functions for many common tasks

For example, to work with dates:

```python
from datetime import datetime

now = datetime.now()
print("Current date and time:", now)
```

## 6. Object-Oriented

Object-Oriented Programming (OOP) is a programming paradigm that uses objects and classes in programming

It aims to implement real-world entities like inheritance, hiding, polymorphism etc. in programming

The main concepts of OOP in Python are:

**Class**: A blueprint for creating objects

**Object**: An instance of a class

**Attributes**: Characteristics shared by all instances of a class

**Methods**: Functions defined inside a class and can only be used with an instance of that class

**Inheritance**: Mechanism of basing an object or class upon another object (prototypical inheritance) or class (class-based inheritance), retaining similar implementation

**Encapsulation**: Hiding of private details of a class from other objects

**Polymorphism**: A concept of using common operation in different ways for different data input

Let's break down these concepts with code snippets.

### 6.1. Defining a Class with Attributes and Methods

Here's a simple example of a class in Python, which models a Dog with attributes like name and age, and methods to define its actions

```python
class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def bark(self):
        return f"{self.name} says woof!"

    def describe(self):
        return f"{self.name} is {self.age} years old."
```

### 6.2. Creating Objects

You can create an instance of a Dog class by calling it like a function and passing the initial values for the name and age

```python
my_dog = Dog("Buddy", 4)
print(my_dog.describe())
print(my_dog.bark())
```

### 6.3. Inheritance

Inheritance allows us to define a class that inherits all the methods and properties from another class

```python
class Labrador(Dog):
    def __init__(self, name, age, color):
        super().__init__(name, age)
        self.color = color

    def describe(self):
        return f"{self.name} is a {self.color} Labrador and is {self.age} years old."

my_lab = Labrador("Max", 3, "golden")
print(my_lab.describe())
```

### 6.4. Encapsulation

Encapsulation is used to restrict access to methods and variables

This can prevent the data from being modified by accident and is done using private attributes using underscores (_)

```python
class Account:
    def __init__(self, owner, balance):
        self.owner = owner
        self.__balance = balance  # private attribute

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print("Deposit successful")
        else:
            print("Invalid amount")

    def show_balance(self):
        return f"{self.owner}'s balance is: ${self.__balance}"

acc = Account("John", 200)
acc.deposit(100)
print(acc.show_balance())
```

### 6.5. Polymorphism

Polymorphism allows us to define methods in the child class that have the same name as the methods in the parent class

```python
class Cat:
    def speak(self):
        return "Meow!"

class Dog:
    def speak(self):
        return "Woof!"

def pet_speak(pet):
    print(pet.speak())

my_cat = Cat()
my_dog = Dog()

# Using the function with a Cat instance.
pet_speak(my_cat)  # Output: Meow!

# Using the function with a Dog instance.
pet_speak(my_dog)  # Output: Woof!
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

Functional programming is a programming paradigm where you model computations as the evaluation of mathematical functions and avoid changing-state and mutable data

Python, being a multi-paradigm language, supports functional programming among other paradigms

Below, I'll explain some of the key concepts of functional programming and illustrate each with Python code examples

### 7.1. First-Class and Higher-Order Functions

In functional programming, functions are first-class citizens. This means that functions can be passed around as arguments, returned from other functions, and assigned to variables

Higher-order functions either take one or more functions as arguments or return a function

Example: **Higher-Order Functions**

```python
def greet(name):
    return "Hello, " + name

def loud(text_func, name):
    result = text_func(name)
    return result.upper()

print(loud(greet, "Alice"))
```

This loud function is a higher-order function because it takes a function text_func as an argument

### 7.2. Pure Functions

A pure function is a function where the output value is determined only by its input values, without observable side effects

This is a core concept in functional programming

Example: **Pure Function**

```python
def multiply(x, y):
    return x * y

result = multiply(2, 3)
print(result)  # Output: 6
```

This function is pure because it always returns the same output for the same inputs and does not modify any external state

### 7.3. Immutability

In functional programming, once data is created, it cannot be changed

This avoids side effects and makes the code more predictable

Example: **Using Tuples (Immutable) Over Lists (Mutable)**

```python
def process_data(data):
    return tuple(x * 2 for x in data)

data = (1, 2, 3)
new_data = process_data(data)
print(new_data)  # Output: (2, 4, 6)
```

Using tuples emphasizes immutability in functional programming

### 7.4. Function Composition

Function composition is the process of combining two or more functions to produce a new function

Composing functions together is a common practice in functional programming

Example: **Function Composition**

```python
def add_five(x):
    return x + 5

def multiply_by_three(x):
    return x * 3

def compose(f, g):
    return lambda x: f(g(x))

combined_function = compose(add_five, multiply_by_three)
print(combined_function(4))  # Output: 17
```

Here, combined_function first multiplies by three, then adds five

### 7.5. Map, Filter, and Reduce

These are staple functions in functional programming that operate on lists (or similar data structures) and return new lists

Map applies a function to all items in an input list

Filter creates a list of elements for which a function returns true

Reduce applies a function of two arguments cumulatively to the items of a list

Example: **Map, Filter, and Reduce**

```python
from functools import reduce

# Map example

numbers = [1, 2, 3, 4]
squared = list(map(lambda x: x ** 2, numbers))
print(squared)  # Output: [1, 4, 9, 16]

# Filter example

even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
print(even_numbers)  # Output: [2, 4]

# Reduce example

sum_of_numbers = reduce(lambda x, y: x + y, numbers)
print(sum_of_numbers)  # Output: 10
```

Functional programming can lead to code that's easier to test, debug, and understand, especially in scenarios involving concurrency or shared state

It is well-suited for processing pipelines, data analysis, and tasks requiring high reliability

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

## 14. Concurrency with Threading and Multiprocessing

Python supports concurrent programming using threads and processes

Here's an example using **threading**:

```python
import threading

def print_numbers():
    for i in range(5):
        print(i)

thread = threading.Thread(target=print_numbers)
thread.start()
```

And here's an example using **multiprocessing**:

```python
from multiprocessing import Process

def print_numbers():
    for i in range(5):
        print(i)

process = Process(target=print_numbers)
process.start()
```

## 15. Asynchronous Programming with Async/Await

Python supports asynchronous programming using the asyncio module

Here's an example using **async** and **await**:

```python
import asyncio

async def greet(name):
    await asyncio.sleep(1)
    print(f"Hello, {name}")

asyncio.run(greet("Alice"))
```

## 16. Context Managers

Python supports context managers using the with statement

Here's an example using a **custom context manager**:

```python
class MyContextManager:
    def __enter__(self):
        print("Entering the context")
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        print("Exiting the context")

with MyContextManager() as cm:
    print("Inside the context")
```

## 17. Metaprogramming with Decorators and Metaclasses

Python allows you to modify classes and functions dynamically using decorators and metaclasses

Here's an example using a class **decorator**:

```python
def add_property(cls):
    cls.new_property = property(lambda self: self._value * 2)
    return cls

@add_property
class MyClass:
    def __init__(self, value):
        self._value = value

obj = MyClass(5)
print(obj.new_property)  # Output: 10
```

## 18. Descriptors

Python descriptors allow you to define how attributes are accessed and modified

Here's an example using a **descriptor**:

```python
class ReversedString:
    def __get__(self, instance, owner):
        return instance._value[::-1]

    def __set__(self, instance, value):
        instance._value = value[::-1]

class MyClass:
    string = ReversedString()

    def __init__(self, value):
        self._value = value

obj = MyClass("hello")
print(obj.string)  # Output: olleh
obj.string = "world"
print(obj.string)  # Output: dlrow
```


