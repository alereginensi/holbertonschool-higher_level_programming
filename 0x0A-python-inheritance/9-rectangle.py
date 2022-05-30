#!/usr/bin/python3

'''class BaseGeometry (based on 8-base_geometry.py).'''


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    '''class Rectangle that inherits from BaseGeometry'''
    def __init__(self, width, height):
        '''defining init'''
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height

    def area(self):
        '''defining area method'''
        if self.__height == 0 or self.__width == 0:
            return 0
        else:
            return self.__height*self.__width

    def __str__(self):
        '''defining string'''
        if self.__height == 0 or self.__width == 0:
            return 0
        else:
            return f"[Rectangle] {self.__width}/{self.__height}"


    def integer_validator(self, name, value):
        if type(value) is not int:
            raise TypeError(f"{name} must be an integer")
        elif value <= 0:
            raise ValueError(f"{name} must be greater than 0")
