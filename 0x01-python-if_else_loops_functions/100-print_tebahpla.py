#!/usr/bin/python3
for i in range(25, -1, -1):
    s = i + ord('A')
    if i % 2 == 1:
        s += 32
    print("{:c}".format(s), end="")
