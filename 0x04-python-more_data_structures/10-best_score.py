#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary is None:
        return None
    mval = 0
    mkey = None
    for k, v in a_dictionary.items():
        if v > mval:
            mval = v
            mkey = k
    return mkey
