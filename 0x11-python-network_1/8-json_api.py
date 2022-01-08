#!/usr/bin/python3
"""
Print the x-requst id of a
request to a url passed
as a command line argument
"""
import requests
import sys


if __name__ == "__main__":
    url = "http://0.0.0.0:5000/search_user"
    args = sys.argv[1] if len(sys.argv) >= 2 else ""

    response = requests.post(url, {"q": args})
    try:
        json_r = response.json()
        if not json_r:
            print("No result")
        else:
            print("[{}] {}".format(json_r["id"], json_r["name"]))
    except Exception as e:
        print("Not a valid JSON")
