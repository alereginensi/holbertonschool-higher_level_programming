#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    if idx < 0:
        return(my_list)
    elif idx not in range(len(my_list)):
        return(my_list)
    else:
        my_list1 = list(my_list)
        my_list1[idx] = element
        return(my_list1)
