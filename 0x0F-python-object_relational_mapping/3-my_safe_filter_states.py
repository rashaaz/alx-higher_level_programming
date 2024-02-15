#!/usr/bin/python3
"""A script to connect MySQL database and retrieve states by given name"""
import MySQLdb
from sys import argv

if __name__ == "__main__":
    sh = MySQLdb.connect(host="localhost", port=3306, user=argv[1],
                         passwd=argv[2], sh=argv[3], charset="utf8")
    cursor = sh.cursor()
    cursor.execute("SELECT * FROM states WHERE name LIKE %s ORDER BY id ASC",
                   (argv[4],))
    rs = cursor.fetchall()
    for r in rs:
        print(r)
    cursor.close()
    sh.close()