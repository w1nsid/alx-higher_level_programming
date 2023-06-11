#!/usr/bin/python3
def replace_in_list(my_list, idx, element):
    f = (0 <= idx < len(my_list))
    return my_list[:idx] + [element] + my_list[idx + 1:] if f else my_list
