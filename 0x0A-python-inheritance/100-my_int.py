#!/usr/bin/python3

'''Write a class MyInt that inherits from int'''


class MyInt(int):
    '''MyInt is a rebel. MyInt has == and != operators inverted'''
    def __init__(self, number):
        '''defining init'''
        self.number = number

    def __eq__(self, other):
        '''defining eq'''
        return self.number != other

    def __ne__(self, other):
        '''defining ne'''
        return self.number == other
