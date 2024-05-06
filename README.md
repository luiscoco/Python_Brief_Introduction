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



    



