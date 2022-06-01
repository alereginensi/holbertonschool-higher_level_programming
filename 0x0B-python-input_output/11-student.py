#!/usr/bin/python3

'''
Write a class Student that defines a student by:
    first_name
    last_name
    age
'''


class Student:
    '''defining class student'''
    def __init__(self, first_name, last_name, age):
        '''defining init'''
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        '''function to_json'''
        if attrs is None:
            return self.__dict__
        else:
            dictio = {}
            for x in attrs:
                if x in self.__dict__.keys():
                    dictio[x] = self.__dict__[x]
            return dictio

    def reload_from_json(self, json):
        '''function reload_from_json'''
        for attr in json:
            self.__dict__[attr] = json[attr]
