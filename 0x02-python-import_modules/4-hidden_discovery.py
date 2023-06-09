#!/usr/bin/python3
import hidden_4
names = [i for i in dir(hidden_4) if i[:2] != "__"]
msg = "\n".join(names) if names else ""
if __name__ == "__main__":
    print("\n".join(names) if names else ""
