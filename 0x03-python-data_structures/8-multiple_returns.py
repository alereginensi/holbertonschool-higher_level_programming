#!/usr/bin/python3
def multiple_returns(sentence):
    if not sentence:
        return(0, None)
    else:
        leng = len(sentence)
        first = sentence[0]
        my_tuple = (leng, first)
        return(my_tuple)
