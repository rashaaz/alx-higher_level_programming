#!/usr/bin/python3
if __name__ == "__main__":
    import sys

    num_ar = len(sys.argv) - 1
    if num_ar == 0:
        print("0 arguments.")
    elif num_ar == 1:
        print("1 argument:")
    else:
        print("{} arguments:".format(num_ar))
    for i in range(num_ar):
        print("{}: {}".format(i + 1, sys.argv[i + 1]))
