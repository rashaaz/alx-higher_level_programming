#!/usr/bin/python3
def max_integer(my_list=[]):
    if len(my_list) < 1:
        return None
    max_value = my_list.copy()
    max_value.sort()
    return max_value[-1]
