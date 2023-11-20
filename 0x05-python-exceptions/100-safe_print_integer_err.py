#!/usr/bin/python3
import sys


def safe_print_integer_err(value):
    i_n = True
    try:
        print("{:d}".format(value))
    except Exception as x:
        print("Exception:", x, file=sys.stderr)
        i_n = False
    return i_n
