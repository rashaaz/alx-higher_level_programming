#!/usr/bin/python3
def roman_to_int(roman_string):
    if not isinstance(roman_string, str):
        return 0
    tl = 0
    numb = 0
    dg = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    for r in reversed(roman_string):
        numb = dg[r]
        tl += numb if tl < numb * 5 else -numb
    return tl
