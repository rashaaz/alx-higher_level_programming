#!/usr/bin/python3
def magic_calculation(a, b):
    res = 0
    for ii in range(1, 3):
        try:
            if ii > a:
                raise Exception('Too far')
            res += a ** b / ii
        except Exception:
            res = b + a
            break
    return res
