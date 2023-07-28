#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    count = 0
    for count, item in enumerate(my_list[:x]):
        print(item, end=" ")
    print()
    return count + 1 if count else 0
