#!/usr/bin/python3
"""A script to compute metrics based on input data from stdin"""


from sys import stdin

sta_co = {
    '200': 0,
    '301': 0,
    '400': 0,
    '401': 0,
    '403': 0,
    '404': 0,
    '405': 0,
    '500': 0,
    }

tot_si = i = 0


def p_me():
    """Print metrics based on the given parameters"""
    print(f'File size: {tot_si}')
    for key, value in sorted(sta_co.items()):
        if value > 0:
            print('{:s}: {:d}'.format(key, value))


try:
    for line in stdin:
        s_li = line.split()
        if len(s_li) >= 2:
            sta = s_li[-2]
            tot_si += int(s_li[-1])
            if sta in sta_co:
                sta_co[sta] += 1
        i += 1

        if i % 10 == 0:
            p_me()
    p_me()
except KeyboardInterrupt as e:
    p_me()
