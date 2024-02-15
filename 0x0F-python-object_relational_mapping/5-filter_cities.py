#!/usr/bin/python3
"""
A script to connect to a MySQL database, retrieve
data about cities and their corresponding states,
and print the names of cities based on a specific
state ID provided as a command-line argument
"""
import sys
import MySQLdb

if __name__ == "__main__":
    sh = MySQLdb.connect(user=sys.argv[1], passwd=sys.argv[2], sh=sys.argv[3])
    m = sh.cursor()
    m.execute("SELECT * FROM `cities` as `c` \
                INNER JOIN `states` as `s` \
                   ON `c`.`state_id` = `s`.`id` \
                ORDER BY `c`.`id`")
    print(", ".join([tt[2] for tt in m.fetchall() if tt[4] == sys.argv[4]]))
