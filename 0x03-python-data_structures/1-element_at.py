#!/usr/bin/python3
def element_at(my_list, idx):
    if idx not in my_list:
        return(None)
    elif idx < 0:
        return(None)
    else:
        return(my_list[idx])

