#!/usr/bin/python3
"""
Script that lists 10 commits (from the most recent to oldest)
of a repository by a specific user using the GitHub API.
"""
import sys
import requests


if __name__ == "__main__":
    url = "https://api.github.com/repos/{}/{}/commits".format(
        sys.argv[2], sys.argv[1])

    m = requests.get(url)
    co = m.json()
    try:
        for ii in range(10):
            print("{}: {}".format(
                co[ii].get("sha"),
                co[ii].get("commit").get("author").get("name")))
    except IndexError:
        pass
