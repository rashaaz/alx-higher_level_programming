# 0x02. Python - import & modules

This project explores the concepts of Python modules and imports. It covers various aspects of module usage, including how to import functions from other files, creating modules, working with command line arguments, and more.

## Project Details

- Author: Guillaume
- Weight: 1
- Project Start: Nov 2, 2023 6:00 AM
- Project Deadline: Nov 3, 2023 6:00 AM
- Checker Release: Nov 2, 2023 12:00 PM
- Auto Review: Will be launched at the deadline

## Resources

Before starting this project, it is recommended to read or watch the following resources:

- [Modules](https://docs.python.org/3/tutorial/modules.html)
- [Command line arguments](https://docs.python.org/3/tutorial/stdlib.html#command-line-arguments)
- [Pycodestyle – Style Guide for Python Code](https://www.python.org/dev/peps/pep-0008/)
- Man or Help: `python3`

## Learning Objectives

By the end of this project, you will be able to:

### General
- Understand why Python programming is awesome.
- Import functions from another file.
- Use imported functions.
- Create a module.
- Use the built-in function `dir()`.
- Prevent code in your script from being executed when imported.
- Use command line arguments with your Python programs.

## Copyright and Plagiarism

- You are expected to come up with solutions for the project tasks yourself.
- Copying and pasting someone else's work is not allowed.
- Publishing any content of this project is prohibited.
- Plagiarism is strictly forbidden and will result in removal from the program.

## Requirements

### General

- Allowed editors: `vi`, `vim`, `emacs`
- All your files will be interpreted/compiled on Ubuntu 20.04 LTS using `python3` (version 3.8.5)
- All your files should end with a new line
- The first line of all your files should be exactly `#!/usr/bin/python3`
- A `README.md` file at the root of the project folder is mandatory
- Your code should follow the Pycodestyle style guide (version 2.8.*)
- All your files must be executable
- The length of your files will be tested using `wc`

## Tasks

### 0. Import a simple function from a simple file

- Write a program that imports the function `def add(a, b):` from the file `add_0.py` and prints the result of the addition `1 + 2 = 3`.
- You have to use the `print` function with string formatting to display integers.
- You have to assign the value 1 to a variable called `a` and the value 2 to a variable called `b`, using two different lines: `a = 1` and `b = 2`.
- Your program should print: `<a value> + <b value> = <add(a, b) value>` followed by a new line.
- You can only use the word `add_0` once in your code.
- You are not allowed to use `*` for importing or `__import__`.
- Your code should not be executed when imported.
