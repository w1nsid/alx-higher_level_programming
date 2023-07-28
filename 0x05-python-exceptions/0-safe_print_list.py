#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    count = 0
    for i, item in enumerate(my_list):
        try:
            if i < x:
                print(item, end=" ")
                count += 1
            else:
                break
        except IndexError:
            break
    print()
    return count
