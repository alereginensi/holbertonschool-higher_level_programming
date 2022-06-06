#!/usr/bin/python3

'''This class will be the “base” of all other classes in this project.'''


import json


class Base:
    '''creating the Base class'''
    __nb_objects = 0

    def __init__(self, id=None):
        '''defining init'''
        self.__nb_objects = 0
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    def to_json_string(list_dictionaries):
        '''defining to_json_string'''
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        else:
            return json.dumps(list_dictionaries)

    def from_json_string(json_string):
        '''returns the list of the JSON string representation json_string'''
        if json_string is None or len(json_string) == 0:
            json_string = "[]"
        return json.loads(json_string)
