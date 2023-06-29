#!/usr/bin/python3
"""
Displays the value of the X-Request-Id variable
found in the header of the response
"""
import requests
from sys import argv


def main(argv):
    """
    Method that takes in a URL, sends a request to the URL
    and displays the value of the X-Request-Id variable
    found in the header of the response
    """
    url = argv[1]
    r = requests.get(url)
    headers = r.headers.get('X-Request-Id')
    print(headers)

if __name__ == "__main__":
    main(argv)
