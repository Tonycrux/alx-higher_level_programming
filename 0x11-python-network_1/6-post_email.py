#!/usr/bin/python3
"""
Print the x-requst id of a
request to a url passed
as a command line argument
"""
import requests
import sys


if __name__ == "__main__":
    url = sys.argv[1]
    email = sys.argv[2]

    response = requests.post(url, {"email": email})
    print(response.text)
