#!/usr/bin/python3
print(", ".join([
    "{:d}{:d}".format(i, j)
    for i in range(0, 10)
    for j in range(i + 1, 10)
]))
