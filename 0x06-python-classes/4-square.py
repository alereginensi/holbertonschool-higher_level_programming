#!/usr/bin/python3

'''Write a class Square that defines a square by: (based on 3-square.py)'''


class Square:
    '''creating class square'''
    def __init__(self, size=0):
        '''defining size'''
        self.__size = size

    @property
    def size(self):
        '''self size'''
        return self.__size

    @size.setter
    def size(self, value):
        '''defining value'''
        if type(value) is not int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def area(self):
        '''defining area operation'''
        return self.__size * self.__size
