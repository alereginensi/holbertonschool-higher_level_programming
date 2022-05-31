#!/usr/bin/python3

'''function that creates an Object from a “JSON file”'''


import json


def load_from_json_file(filename):
    '''function load_from_json_file'''
    with open(filename, encoding="utf-8") as f:
        rep = json.load(f)
        return rep
