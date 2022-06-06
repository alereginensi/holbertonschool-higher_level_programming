#!/usr/bin/python3

'''Write the class Square that inherits from Rectangle'''


from models.rectangle import Rectangle


class Square(Rectangle):
    '''class Square'''
    def __init__(self, size, x=0, y=0, id=None):
        '''defining init'''
        super().__init__(size, size, x, y, id)

    def __str__(self):
        '''returns Rectangle properties'''
        return f"[Square] ({self.id}) \
{self.x}/{self.y} - {self.width}"

    @property
    def size(self):
        '''defining size'''
        return self.width

    @size.setter
    def size(self, value):
        '''defining value size'''
        if type(value) is not int:
            raise TypeError("width must be an integer")
        elif value <= 0:
            raise ValueError("width must be > 0")
        else:
            self.width = value
            self.height = value

    def update(self, *args, **kwargs):
        '''defining update'''
        if args and kwargs is not None:
            arg_num = 0
            for j in args:
                if arg_num == 0:
                    self.id = j
                if arg_num == 1:
                    self.size = j
                if arg_num == 2:
                    self.x = j
                if arg_num == 3:
                    self.y = j
                arg_num += 1
        else:
            for key, value in kwargs.items():
                if key == "id":
                    self.id = value
                if key == "size":
                    self.size = value
                if key == "x":
                    self.x = value
                if key == "y":
                    self.y = value
