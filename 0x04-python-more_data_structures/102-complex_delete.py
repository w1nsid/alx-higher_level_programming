#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    li = list(a_dictionary.keys())
    [a_dictionary.pop(k) for k in li if a_dictionary[k] == value]
    return a_dictionary
