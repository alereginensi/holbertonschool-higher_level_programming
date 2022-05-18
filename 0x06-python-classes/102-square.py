#!/usr/bin/python3

'''Write a class Square that defines a square by: (based on 4-square.py)'''


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

    def my_print(self):
        '''defining print square'''
        if self.__size != 0:
            for num in range(self.__size):
                for space in range(self.__size):
                    print('#', end="")
                print()
        else:
            print()

    def __lt__(self, other):
        '''defining x<y'''
        if not isinstance(other, Square):
            pass
        if self.area() < other.area():
            return True
        else:
            return False

    def __le__(self, other):
        '''defining  x<=y'''
        if not isinstance(other, Square):
            pass
        if self.area() <= other.area():
            return True
        else:
            return False

    def __eq__(self, other):
        '''defining x==y'''
        if not isinstance(other, Square):
            pass
        if self.area() == other.area():
            return True
        else:
            return False

    def __ne__(self, other):
        '''defining  x!=y'''
        if not isinstance(other, Square):
            pass
        if self.area() != other.area():
            return True
        else:
            return False

    def __gt__(self, other):
        '''defining x>y'''
        if not isinstance(other, Square):
            pass
        if self.area() > other.area():
            return True
        else:
            return False

    def __ge__(self, other):
        '''defining x>=y'''
        if not isinstance(other, Square):
            pass
        if self.area() >= other.area():
            return True
        else:
            return False
