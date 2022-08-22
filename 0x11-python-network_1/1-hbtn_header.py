#!/usr/bin/python3
'''takes in a URL, sends a request to the URL and displays the value'''
import urllib.request
from sys import argv

if __name__ == "__main__":
    if argv[1] is not None:
        with urllib.request.urlopen(argv[1]) as response:
            print(response.headers.get('X-Request-Id'))
