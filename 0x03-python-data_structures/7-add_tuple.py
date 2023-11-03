#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    r1 = tuple_a[0] if len(tuple_a) > 0 else 0
    r2 = tuple_a[1] if len(tuple_a) > 1 else 0
    s1 = tuple_b[0] if len(tuple_b) > 0 else 0
    s2 = tuple_b[1] if len(tuple_b) > 1 else 0
    return (r1 + s1, r2 + s2)
