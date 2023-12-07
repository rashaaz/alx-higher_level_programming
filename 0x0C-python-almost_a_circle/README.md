# Project Title: 0x0C. Python - Almost a Circle

## Author: Guillaume

## Project Details

- **Weight:** 1
- **Project Start:** Dec 7, 2023 6:00 AM
- **Project End:** Dec 12, 2023 6:00 AM
- **Checker Release:** Dec 11, 2023 6:00 PM
- **Manual QA Review Required**

## Background Context

The AirBnB project is a significant part of the Higher-Level curriculum. This project aims to prepare you for it. In this project, you will review various aspects of Python, including import, exceptions, class, private attribute, getter/setter, class method, static method, inheritance, unittest, and file read/write operations. You will also learn about args, kwargs, serialization/deserialization, and JSON.

### Resources

- [args/kwargs](https://docs.python.org/3.8/tutorial/controlflow.html#arbitrary-argument-lists)
- [JSON encoder and decoder](https://docs.python.org/3/library/json.html)
- [unittest module](https://docs.python.org/3/library/unittest.html)
- [Python test cheatsheet](https://www.pythonsheets.com/notes/python-tests.html)

## Learning Objectives

Upon completing this project, you should be able to explain the following concepts without relying on external sources:

### General

- What is unit testing and how to implement it in a large project
- How to serialize and deserialize a class
- How to write and read a JSON file
- What is `*args` and how to use it
- What is `**kwargs` and how to use it
- How to handle named arguments in a function

## Copyright - Plagiarism

- You are tasked with finding solutions to the tasks yourself to meet the learning objectives.
- Copying and pasting someone else’s work is not allowed.
- Publishing any content of this project is strictly forbidden and will result in removal from the program.

## Requirements

### Python Scripts

- Allowed editors: vi, vim, emacs
- Interpreted/compiled on Ubuntu 20.04 LTS using Python3 (version 3.8.5)
- All files should end with a new line
- The first line of all files should be `#!/usr/bin/python3`
- A README.md file at the root of the project folder is mandatory
- Code should use pycodestyle (version 2.8.*)
- All files must be executable
- The length of your files will be tested using `wc`
- All modules, classes, and functions should be documented
- Documentation should be a real sentence explaining the purpose of the module, class, or method
- Python Unit Tests allowed editors: vi, vim, emacs
- All test files should end with a new line
- All test files should be inside a folder

## Tasks

### 0. If it's not tested, it doesn't work

- All files, classes, and methods must be unit tested and be PEP 8 validated.

### 1. Base class

- Create a folder named `models` with an empty file `__init__.py` inside - with this file, the folder will become a Python package.
- Create a file named `models/base.py`.
- Implement a class `Base` with the following:
  - Private class attribute `__nb_objects` initialized to 0.
  - Class constructor `def __init__(self, id=None)`.
    - If `id` is not `None`, assign the public instance attribute `id` with this argument value.
    - Otherwise, increment `__nb_objects` and assign the new value to the public instance attribute `id`.
### more 20 tasks
- Example usage:

  ```python
  #!/usr/bin/python3
  """ 0-main """
  from models.base import Base

  if __name__ == "__main__":
      b1 = Base()
      print(b1.id)

      b2 = Base()
      print(b2.id)

      b3 = Base()
      print(b3.id)

      b4 = Base(12)
      print(b4.id)

      b5 = Base()
      print(b5.id)
