#!/usr/bin/python3
"""
Script that takes GitHub credentials
(username and password)
and uses the GitHub API to display
the user's id.
"""
import sys
import requests
from requests.auth import HTTPBasicAuth


if __name__ == "__main__":
    auth = HTTPBasicAuth(sys.argv[1], sys.argv[2])
    m = requests.get("https://api.github.com/user", auth=auth)
    print(m.json().get("id"))
