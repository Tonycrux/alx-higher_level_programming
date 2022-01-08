#!/usr/bin/python3
"""
Print the x-requst id of a
request to a url passed
as a command line argument
"""
import urllib.request
import urllib.parse
import sys


if __name__ == "__main__":
    url = sys.argv[1]
    email = sys.argv[2]
    msg = urllib.parse.urlencode({"email": email})
    msg = msg.encode('ascii')
    req_url = urllib.request.Request(url, msg)

    with urllib.request.urlopen(req_url) as response:
        print(response.read().decode('utf-8'))
