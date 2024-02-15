#!/usr/bin/python3
"""A simple script to connect to a MySQL database and fetch 'states' table."""
import sys
import MySQLdb

if __name__ == "__main__":
    sh = MySQLdb.connect(user=sys.argv[1], passwd=sys.argv[2], sh=sys.argv[3])
    s = sh.cursor()
    s.execute("SELECT * FROM `states`")
    [print(state) for state in s.fetchall()]
