#!/usr/bin/python3
def multiple_returns(sentence):
    leng = len(sentence)
    first = sentence[0]
    my_tuple = (leng, first)
    if not sentence:
        return(0, None)
    else:
        return(my_tuple)
