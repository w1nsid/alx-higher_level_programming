#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    f = (0 <= idx < len(my_list))
    c = my_list.copy()
    return c[:idx] + [element] + c[idx + 1:] if f else c
