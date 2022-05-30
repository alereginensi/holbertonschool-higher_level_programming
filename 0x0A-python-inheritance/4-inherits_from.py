#!/usr/bin/python3
"""
Write a function that returns True if the object is an instance of a class
that inherited (directly or indirectly) from the specified
class ; otherwise False.
"""


def inherits_from(obj, a_class):
    '''defines inherits_from'''
    if type(obj) is not a_class and issubclass(type(obj), a_class):
        return True
    else:
        return False
