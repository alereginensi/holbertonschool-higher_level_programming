#!/usr/bin/python3
'''displays the value of the variable X-Request-Id'''
import requests
from sys import argv


if __name__ == "__main__":
    if argv[1] is not None:
        response = requests.get(argv[1])
        print(response.headers.get('X-Request-Id'))
