#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    re_lt = []

    for ii in range(list_length):
        try:
            re_lt.append(my_list_1[ii] / my_list_2[ii])
        except ZeroDivisionError:
            re_lt.append(0)
            print('division by 0')
            continue
        except TypeError:
            re_lt.append(0)
            print('wrong type')
            continue
        except IndexError:
            re_lt.append(0)
            print('out of range')
            continue
        finally:
            pass
    return re_lt
