#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    try:
        for x in my_list:
            print(x, end="")
    except:
            print(x)
    print()
    return x
