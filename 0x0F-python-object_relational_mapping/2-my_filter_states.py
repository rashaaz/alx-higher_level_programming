#!/usr/bin/python3
"""A script to connect to a MySQL database and fetch states given name"""
import sys
import MySQLdb

if __name__ == "__main__":
    sh = MySQLdb.connect(user=sys.argv[1], port=3306, host="localhost",
                         passwd=sys.argv[2], sh=sys.argv[3])
    m = sh.cursor()
    m.execute("SELECT * FROM states WHERE name LIKE '{:s}' ORDER BY \
    id ASC".format(sys.argv[4]))
    sta = m.fetchall()
    for s in sta:
        if s[1] == sys.argv[4]:
            print(s)
    m.close()
    sh.close()
