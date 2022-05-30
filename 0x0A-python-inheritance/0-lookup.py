#!/usr/bin/python3

'''Returns the list of available attributes and methods of an object'''


def lookup(obj):
    '''defines lookup class'''
    o = obj()
    return dir(o)
