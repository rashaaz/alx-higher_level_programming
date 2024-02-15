#!/usr/bin/python3
"""A script to connect to MySQL database and fetch states starting with 'N'"""
import sys
import MySQLdb

if __name__ == "__main__":
    sh = MySQLdb.connect(user=sys.argv[1], passwd=sys.argv[2], sh=sys.argv[3])
    m = sh.cursor()
    m.execute("SELECT * FROM `states` ORDER BY `id`")
    [print(state) for state in m.fetchall() if state[1][0] == "N"]
