#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    ii, co = 0, 0
    while ii < x:
        try:
            print("{:d}".format(my_list[ii]), end='')
            co += 1
        except (ValueError, TypeError):
            pass
        ii += 1
    print()
    return co
