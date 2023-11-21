# Project 0x06. Python - Classes and Objects

## Background Context
Object-Oriented Programming (OOP) is a fundamental concept in Python. This project aims to familiarize you with key OOP concepts, including classes, objects, attributes, methods, and encapsulation.

## Resources
Make sure to read or watch the following resources in the specified order:

1. [Object Oriented Programming](https://python.swaroopch.com/oop.html) (Read everything until the paragraph "Inheritance" excluded. You do NOT have to learn about class attributes, classmethod, and staticmethod yet.)
2. [Object-Oriented Programming](https://realpython.com/python3-object-oriented-programming/) (Please be careful: in most of the following paragraphs, the author shows things the way you should not use or write a class to help you better understand some concepts and how everything works in Python 3. Make sure you read everything in the following paragraphs: General Introduction, First-class Everything, A Minimal Class in Python, Attributes (You DON’T have to learn about class attributes), Methods, The __init__ Method, “Data Abstraction, Data Encapsulation, and Information Hiding,” “Public, Protected, and Private Attributes”)
3. [Properties vs. Getters and Setters](https://www.python-course.eu/python3_properties.php)
4. [Learn to Program 9: Object-Oriented Programming](https://www.youtube.com/watch?v=JeznW_7DlB0)
5. [Python Classes and Objects](https://www.programiz.com/python-programming/class)

## Learning Objectives
By the end of this project, you should be able to explain to anyone, without the help of Google:

### General
- Why Python programming is awesome
- What is OOP
- "First-class everything"
- What is a class
- What is an object and an instance
- What is the difference between a class and an object or instance
- What is an attribute
- What are and how to use public, protected, and private attributes
- What is `self`
- What is a method
- What is the special `__init__` method and how to use it
- What is Data Abstraction, Data Encapsulation, and Information Hiding
- What is a property
- What is the difference between an attribute and a property in Python
- What is the Pythonic way to write getters and setters in Python
- How to dynamically create arbitrary new attributes for existing instances of a class
- How to bind attributes to object and classes
- What is the `__dict__` of a class and/or instance of a class and what does it contain
- How does Python find the attributes of an object or class
- How to use the `getattr` function

## Copyright - Plagiarism
- You are tasked to come up with solutions for the tasks below yourself to meet the above learning objectives.
- You will not be able to meet the objectives of this or any following project by copying and pasting someone else’s work.
- You are not allowed to publish any content of this project.
- Any form of plagiarism is strictly forbidden and will result in removal from the program.

## Requirements
### General
- Allowed editors: `vi`, `vim`, `emacs`
- All your files will be interpreted/compiled on Ubuntu 20.04 LTS using `python3` (version 3.8.5)
- All your files should end with a new line
- The first line of all your files should be exactly `#!/usr/bin/python3`
- A `README.md` file, at the root of the folder of the project, is mandatory
- Your code should use the `pycodestyle` (version 2.8.*)
- All your files must be executable
- The length of your files will be tested using `wc`
- All your modules should have documentation (`python3 -c 'print(__import__("my_module").__doc__)'`)
- All your classes should have documentation (`python3 -c 'print(__import__("my_module").MyClass.__doc__)'`)
- All your functions (inside and outside a class) should have documentation (`python3 -c 'print(__import__("my_module").my_function.__doc__)' and `python3 -c 'print(__import__("my_module").MyClass.my_function.__doc__)'`)
- A documentation is not a simple word; it’s a real sentence explaining what’s the purpose of the module, class, or method (the length of it will be verified)

### More Info
- Documentation is now mandatory! Each module, class, and method must contain docstring as comments. Example [Google Style Python Docstrings](http://sphinxcontrib-napoleon.readthedocs.io/en/latest/example_google.html)

## Quiz questions
- Great! You've completed the quiz successfully! Keep going! (Show quiz)

## Tasks
### 0. My first square
Write an empty class `Square` that defines a square.

You are not allowed to import any module.

```python
#!/usr/bin/python3
Square = __import__('0-square').Square

my_square = Square()
print(type(my_square))
print(my_square.__dict__)
and more 6 tasks
and 4 advanced
