#!/usr/bin/python3
"""
Script that takes in a URL and an email,
sends a POST request to the passed URL
with the email as a parameter, and displays
the body of the response (decoded in utf-8)
"""
import sys
import urllib.parse
import urllib.request


if __name__ == "__main__":
    url = sys.argv[1]
    va = {"email": sys.argv[2]}
    da = urllib.parse.urlencode(va).encode("ascii")

    re = urllib.request.Request(url, da)
    with urllib.request.urlopen(re) as response:
        print(response.read().decode("utf-8"))
