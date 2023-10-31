#!/usr/bin/python3
def remove_char_at(str, n):
    res = ""
    for i, s in enumerate(str):
        if i != n:
            res += s
    return res
