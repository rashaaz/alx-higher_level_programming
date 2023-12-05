#!/usr/bin/python3
"""Script that adds all arguments to a Python list and saves them to a file"""


import sys
save_to_json_file = __import__('5-save_to_json_file') .save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

argl = list(sys.argv[1:])

try:
    old_da = load_from_json_file('add_item.json')
except Exception:
    old_da = []

old_da.extend(argl)
save_to_json_file(old_da, 'add_item.json')
