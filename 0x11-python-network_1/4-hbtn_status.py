#!/usr/bin/python3
"""
Script that fetches https://alx-intranet.hbtn.io/status
"""
import requests


if __name__ == "__main__":
    s = requests.get('https://alx-intranet.hbtn.io/status')
    m = s.text
    print('Body response:\n\t- type: {}\n\t- content: {}'.format(type(m), m))
