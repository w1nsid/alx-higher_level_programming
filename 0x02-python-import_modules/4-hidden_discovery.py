#!/usr/bin/python3
import hidden_4
if __name__ == "__main__":
    if len(dir(hidden_4)) > 0:
        print("\n".join([i for i in dir(hidden_4) if i[:2] != "__"]))
