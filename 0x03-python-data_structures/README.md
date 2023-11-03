# 0x03. Python - Data Structures: Lists, Tuples

## Description
This project is part of the ALX Software Engineering program curriculum and focuses on teaching students about Python data structures, specifically lists and tuples. It covers a range of topics, including the basics of lists, their common methods, using lists as stacks and queues, list comprehensions, tuples, and more.

## Learning Objectives
At the end of this project, you are expected to be able to explain to anyone, without the help of Google:

- Why Python programming is awesome
- What are lists and how to use them
- What are the differences and similarities between strings and lists
- What are the most common methods of lists and how to use them
- How to use lists as stacks and queues
- What are list comprehensions and how to use them
- What are tuples and how to use them
- When to use tuples versus lists
- What is a sequence
- What is tuple packing
- What is sequence unpacking
- What is the del statement and how to use it

## Requirements
### Python Scripts
- Allowed editors: vi, vim, emacs
- All your files will be interpreted/compiled on Ubuntu 20.04 LTS using python3 (version 3.8.5)
- All your files should end with a new line
- The first line of all your files should be exactly `#!/usr/bin/python3`
- A `README.md` file, at the root of the folder of the project, is mandatory
- Your code should use the pycodestyle (version 2.8.*)
- All your files must be executable
- The length of your files will be tested using wc

### C
- Allowed editors: vi, vim, emacs
- All your files will be interpreted/compiled on Ubuntu 20.04 LTS using python3 (version 3.8.5)
- All your files should end with a new line
- Your code should use the Betty style. It will be checked using betty-style.pl and betty-doc.pl
- You are not allowed to use global variables
- No more than 5 functions per file
- The prototypes of all your functions should be included in your header file called lists.h
- Don't forget to push your header file
- All your header files should be include guarded

## Tasks
1. [Print a list of integers](./0-print_list_integer.py)
   - Write a function that prints all integers of a list.
   - Prototype: `def print_list_integer(my_list=[]):`
   - Format: one integer per line.

2. [Secure access to an element in a list](./1-element_at.py)
   - Write a function that retrieves an element from a list like in C.
   - Prototype: `def element_at(my_list, idx):`
   - If `idx` is negative, the function should return None.
   - If `idx` is out of range (> number of elements in `my_list`), the function should return None.

3. [Replace element](./2-replace_in_list.py)
   - Write a function that replaces an element of a list at a specific position (like in C).
   - Prototype: `def replace_in_list(my_list, idx, element):`
   - If `idx` is negative, the function should not modify anything and return the original list.
   - If `idx` is out of range (> number of elements in `my_list`), the function should not modify anything and return the original list.

4. [Print a list of integers... in reverse!](./3-print_reversed_list_integer.py)
   - Write a function that prints all integers of a list, in reverse order.
   - Prototype: `def print_reversed_list_integer(my_list=[]):`
   - Format: one integer per line.

5. [Replace in a copy](./4-new_in_list.py)
   - Write a function that replaces an element in a list at a specific position without modifying the original list (like in C).
   - Prototype: `def new_in_list(my_list, idx, element):`
   - If `idx` is negative, the function should return a copy of the original list.
   - If `idx` is out of range (> number of elements in `my_list`), the function should return a copy of the original list.

6. [Lists of lists = Matrix](./6-print_matrix_integer.py)
   - Write a function that prints a matrix of integers.
   - Prototype: `def print_matrix_integer(matrix=[[]]):`
   - Format: see example.

7. [Tuples addition](./7-add_tuple.py)
   - Write a function that adds 2 tuples.
   - Prototype: `def add_tuple(tuple_a=(), tuple_b=()):`
   - Returns a tuple with 2 integers.

8. [More returns!](./8-multiple_returns.py)
   - Write a function that returns a tuple with the length of a string and its first character.
   - Prototype: `def multiple_returns(sentence):`
   - If the sentence is empty, the first character should be equal to None.

9. [Find the max](./9-max_integer.py)
   - Write a function that finds the biggest integer of a list.
   - Prototype: `def max_integer(my_list=[]):`
   - If the list is empty, return None.

10. [Only by 2](./10-divisible_by_2.py)
    - Write a function that finds all multiples of 2 in a list.
    - Prototype: `def divisible_by_2(my_list=[]):`
    - Return a new list with True or False, depending on whether the integer at the same position in the original list is a multiple of 2.

11. [Delete at](./11-delete_at.py)
    - Write a function that deletes the item at a specific position in a list.
    - Prototype: `def delete_at(my_list=[], idx=0):`
    - If `idx` is negative or out of range, nothing changes (returns the same list).

12. [Switch](./12-switch.py)
    - Complete the source code to switch the values of `a` and `b`.

13. [Linked list palindrome](./13-is_palindrome.c)
    - Write a function in C that checks if a singly linked list is a palindrome.
    - Prototype: `int is_palindrome(listint_t **head);`
    - Return: 0 if it is not a palindrome, 1 if it is a palindrome.
    - An empty list is considered a palindrome.
 and Other advanced taske

## Author
- Guillaume, [GitHub](https://github.com/Guillaume28)

