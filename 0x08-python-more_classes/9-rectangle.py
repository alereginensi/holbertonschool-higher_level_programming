#!/usr/bin/python3

'''class Rectangle that defines a rectangle by: (based on 8-rectangle.py)'''


class Rectangle:
    '''creating class rectangle'''
    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        ''' init of height and width'''
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        '''defining width'''
        return self.__width

    @width.setter
    def width(self, value):
        '''value width'''
        if type(value) is not int:
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
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
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
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

    def __str__(self, height=0, width=0):
        '''print rectangle with the character #'''
        string = ""
        symbol = str(self.print_symbol)
        if self.__height == 0 or self.__width == 0:
            return str()
        else:
            for i in range(self.__height):
                for j in range(self.__width):
                    string = string + symbol
                string = string + '\n'
            string = string[:-1]
        return string

    def __repr__(self):
        '''return a string representation of the rectangle'''
        return f"Rectangle({self.__width},{self.__height})"

    def __del__(self):
        '''deletes triangle and print a message'''
        if Rectangle.number_of_instances > 0:
            Rectangle.number_of_instances -= 1
        print("Bye rectangle...")

    def bigger_or_equal(rect_1, rect_2):
        '''returns the biggest rectangle based on the area'''
        if type(rect_1) is not Rectangle:
            raise TypeError("rect_1 must be an instance of Rectangle")
        elif type(rect_2) is not Rectangle:
            raise TypeError("rect_2 must be an instance of Rectangle")
        elif rect_1.area() > rect_2.area():
            return rect_1
        elif rect_2.area() > rect_1.area():
            return rect_2
        elif rect_2.area() == rect_1.area():
            return rect_1

    @classmethod
    def square(cls, size=0):
        '''returns a new Rectangle instance with width == height == size'''
        return cls(size, size)
