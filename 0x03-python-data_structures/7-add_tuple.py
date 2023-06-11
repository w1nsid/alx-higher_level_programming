#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    z = zip((tuple_a + (0, 0))[:2], (tuple_b + (0, 0))[:2])
    return tuple(sum(pair) for pair in z)
