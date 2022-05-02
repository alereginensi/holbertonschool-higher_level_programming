#!/usr/bin/python3
def no_c(my_string):
    for i in range(len(my_string)):
        my_string2 = my_string.translate({ord('c'): None})
        my_string3 = my_string2.translate({ord('C'): None})
        return(my_string3)
