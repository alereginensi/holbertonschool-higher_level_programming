#!/usr/bin/python3

'''Write the class Rectangle that inherits from Base'''


from models.base import Base


class Rectangle(Base):
    '''class Rectangle'''
    def __init__(self, width, height, x=0, y=0, id=None):
        '''defining init'''
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        '''defining width'''
        return self.__width

    @width.setter
    def width(self, value):
        '''defining value width'''
        if type(value) is not int:
            raise TypeError("width must be an integer")
        elif value <= 0:
            raise ValueError("width must be > 0")
        else:
            self.__width = value

    @property
    def height(self):
        '''defining height'''
        return self.__height

    @height.setter
    def height(self, value):
        '''defining value height'''
        if type(value) is not int:
            raise TypeError("height must be an integer")
        elif value <= 0:
            raise ValueError("height must be > 0")
        else:
            self.__height = value

    @property
    def x(self):
        '''defining x'''
        return self.__x

    @x.setter
    def x(self, value):
        '''defining x'''
        if type(value) is not int:
            raise TypeError("x must be an integer")
        elif value < 0:
            raise ValueError("x must be >= 0")
        else:
            self.__x = value

    @property
    def y(self):
        '''defining y'''
        return self.__y

    @y.setter
    def y(self, value):
        '''defining y'''
        if type(value) is not int:
            raise TypeError("y must be an integer")
        elif value < 0:
            raise ValueError("y must be >= 0")
        else:
            self.__y = value

    def area(self):
        '''returns the rectangle's area'''
        if self.__height == 0 or self.__width == 0:
            return 0
        else:
            return self.__height*self.__width

    def display(self):
        '''defining print square'''
        if self.__width != 0 and self.__height != 0:
            for y_space in range(self.__y):
                z = ' '
                print(z)
            for num in range(self.__height):
                for x_space in range(self.__x):
                    z = ' '
                    print((z), end="")
                for space in range(self.__width):
                    print('#', end="")
                print()

    def __str__(self):
        '''returns Rectangle properties'''
        return f"[Rectangle] ({self.id}) \
{self.__x}/{self.__y} - {self.__width}/{self.__height}"

    def update(self, *args, **kwargs):
        '''defining update'''
        if args and kwargs is not None:
            arg_num = 0
            for j in args:
                if arg_num == 0:
                    self.id = j
                if arg_num == 1:
                    self.width = j
                if arg_num == 2:
                    self.height = j
                if arg_num == 3:
                    self.x = j
                if arg_num == 4:
                    self.y = j
                arg_num += 1
        else:
            for key, value in kwargs.items():
                if key == "id":
                    self.id = value
                if key == "width":
                    self.width = value
                if key == "height":
                    self.height = value
                if key == "x":
                    self.x = value
                if key == "y":
                    self.y = value
