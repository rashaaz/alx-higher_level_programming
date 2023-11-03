#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    if my_list is None:
        return None
    lisdiv = []
    for i in my_list:
        if (i % 2) == 0:
            lisdiv.append(True)
        else:
            lisdiv.append(False)
    return lisdiv
