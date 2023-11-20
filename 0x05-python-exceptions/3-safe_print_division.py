#!/usr/bin/python3
def safe_print_division(a, b):
    rt = 0

    try:
        rt = a / b
    except ZeroDivisionError:
        rt = None
    finally:
        print("Inside result: {}".format(rt))
        return rt
