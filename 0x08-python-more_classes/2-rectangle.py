#!/usr/bin/python3

'''class Rectangle that defines a rectangle by: (based on 1-rectangle.py)'''


class Rectangle:
    '''creating class rectangle'''
    def __init__(self, width=0, height=0):
        ''' init of height and width'''
        self.__width = width
        self.__height = height

    @property
    def width(self):
        '''defining width'''
        return self.__width

    @width.setter
    def width(self, value):
        '''value width'''
        if type(value) is not int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__width = value

    @property
    def height(self):
        '''defining height'''
        return self.__height

    @height.setter
    def height(self, value):
        '''value height'''
        if type(value) is not int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__height = value

    def area(self):
        '''returns the rectangle's area'''
        if self.__height == 0 or self.__width == 0:
            return 0
        else:
            return self.__height*self.__width

    def perimeter(self):
        '''returns the rectangle's perimeter'''
        if self.__height == 0 or self.__width == 0:
            return 0
        else:
            return ((self.__height + self.__width)*2)
