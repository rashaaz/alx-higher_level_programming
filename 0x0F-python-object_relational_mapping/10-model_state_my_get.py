#!/usr/bin/python3
"""
A script to connect to a MySQL database using SQLAlchemy
and find a specific state by name
"""
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import State

if __name__ == "__main__":
    sscctt = create_engine("mysql+mysqldb://{}:{}@localhost/{}"
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)
    Session = sessionmaker(bind=sscctt)
    session = Session()

    fo = False
    for sr in session.query(State):
        if sr.name == sys.argv[4]:
            print("{}".format(sr.id))
            fo = True
            break
    if fo is False:
        print("Not found")
