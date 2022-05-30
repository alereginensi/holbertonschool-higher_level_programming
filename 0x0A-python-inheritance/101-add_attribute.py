#!/usr/bin/python3

'''function that adds a new attribute to an object if it’s possible'''


def add_attribute(obj, attr, value):
    '''functions that tries to add and attribute'''
    if ('__dict__' in dir(obj)):
        setattr(obj, attr, value)
    else:
        raise TypeError("can't add new attribute")
