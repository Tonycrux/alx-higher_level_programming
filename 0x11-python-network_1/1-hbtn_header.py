#!/usr/bin/python3
"""
Print the x-requst id of a
request to a url passed
as a command line argument
"""
import urllib.request
import sys


if __name__ == "__main__":
    url = sys.argv[1]
    with urllib.request.urlopen(url) as response:
        print(response.info().get("X-Request-Id"))
