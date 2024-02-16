#!/usr/bin/python3
"""A script to connect to MySQL database and fetch states starting with 'N'"""
import sys
import MySQLdb

if __name__ == "__main__":
    db = MySQLdb.connect(user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])
    m = db.cursor()
    m.execute("SELECT * FROM `states` ORDER BY `id`")
    [print(state) for state in m.fetchall() if state[1][0] == "N"]
