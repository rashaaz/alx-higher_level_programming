#!/usr/bin/python3
"""
A script to connect to a MySQL database and retrieve
data about cities and their corresponding states.
"""
import sys
import MySQLdb

if __name__ == "__main__":
    sh = MySQLdb.connect(user=sys.argv[1], passwd=sys.argv[2], sh=sys.argv[3])
    m = sh.cursor()
    m.execute("SELECT `c`.`id`, `c`.`name`, `s`.`name` \
                 FROM `cities` as `c` \
                INNER JOIN `states` as `s` \
                   ON `c`.`state_id` = `s`.`id` \
                ORDER BY `c`.`id`")
    [print(cit) for cit in m.fetchall()]
