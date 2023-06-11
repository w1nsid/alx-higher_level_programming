#!/usr/bin/python3
def delete_at(my_list=[], idx=0):
    c = (idx < 0 or idx >= len(my_list))
    my_list[idx:idx+1] = [] if c else my_list[idx+1:]
    return my_list
