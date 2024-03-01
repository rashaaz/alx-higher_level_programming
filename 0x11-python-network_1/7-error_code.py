#!/usr/bin/python3
"""
Script that takes in a URL, sends a request to
the URL, and displays the body
of the response. If the HTTP status code
is greater than or equal to 400,
prints: Error code: followed by
the value of the HTTP status code.
"""
import sys
import requests


if __name__ == "__main__":
    url = sys.argv[1]

    m = requests.get(url)
    if m.status_code >= 400:
        print("Error code: {}".format(m.status_code))
    else:
        print(m.text)
