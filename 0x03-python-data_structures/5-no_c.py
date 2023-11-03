#!/usr/bin/python3
def no_c(my_string):
    fil_str = ""
    for char in range(len(my_string)):
        if (my_string[char] != 'c' and my_string[char] != 'C'):
            fil_str += my_string[char]
    return fil_str
