#!/usr/bin/python3
import sys
c = len(sys.argv) - 1
ar = "argument"
s1 = "{} {}{}{}".format(c, ar, "" if c == 1 else "s", "." if c == 0 else ":")
ar_l = ["{}: {}".format(i + 1, sys.argv[i + 1]) for i in range(c)]
res = "\n".join([s1] + ar_l)
if __name__ == "__main__":
    print(res)
