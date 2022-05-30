#!/usr/bin/python3

'''class BaseGeometry (based on 10-rectangle.py).'''


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    '''class Square that inherits from Rectangle'''
    def __init__(self, size):
        '''defining init'''
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def area(self):
        '''defining area method'''
        if self.__size == 0:
            return 0
        else:
            return self.__size*self.__size

    def __str__(self):
        '''defining string'''
        if self.__size == 0:
            return 0
        else:
            return f"[Square] {self.__size}/{self.__size}"
