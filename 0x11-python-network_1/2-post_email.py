#!/usr/bin/python3
"""takes in a URL sends a request to the URL and displays the body"""

from urllib import request, parse
from sys import argv


if __name__ == "__main__":
    url = argv[1]
    email = {'email': argv[2]}

    data = parse.urlencode(email)
    data = data.encode('ascii')
    with request.urlopen(url, data) as response:
        print(response.read().decode('utf-8'))
