#!/usr/bin/python3
"""
Handles errors duing message
requests using urllib
"""
import urllib.request
import urllib.parse
import urllib.error
import sys


if __name__ == "__main__":
    url = sys.argv[1]
    try:
        with urllib.request.urlopen(url) as response:
            print(response.read().decode('utf-8'))
    except urllib.error.URLError as e:
        print("Error code: {}".format(e.code))
