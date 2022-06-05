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
        return f"[Square] ({self.id}) {self.x}/{self.y} - {self.width}"

    @property
    def size(self):
        '''defining size'''
        return self.width

    @size.setter
    def size(self, value):
        '''defining value size'''
        self.width = value
        self.height = value
