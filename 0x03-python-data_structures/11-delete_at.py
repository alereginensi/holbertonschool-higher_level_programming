#!/usr/bin/python3
def delete_at(my_list=[], idx=0):
    if idx < 0:
        return(my_list)
    elif idx not in range(len(my_list)):
        return(my_list)
    else:
        for idx in my_list:
            del my_list[3]
            return(my_list)
