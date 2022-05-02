#!/usr/bin/python3
def max_integer(my_list=[]):
    list2 = []
    if my_list:
        highest = my_list[0]
        for num in my_list:
            if num > highest:
                highest = num
                return(highest)
    else:
        return(None)


