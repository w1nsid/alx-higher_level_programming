#!/usr/bin/python3
def delete_at(my_list=[], idx=0):
    c = (0 <= idx < len(my_list))
    my_list[idx:idx+1] = [] if c else my_list
    return my_list
