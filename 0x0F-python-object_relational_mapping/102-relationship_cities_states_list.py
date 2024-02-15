#!/usr/bin/python3
"""Script to query cities and their associated states from the database"""
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from relationship_state import State
from relationship_city import City

if __name__ == "__main__":
    sscctt = create_engine("mysql+mysqldb://{}:{}@localhost/{}"
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)
    Session = sessionmaker(bind=sscctt)
    session = Session()

    for ci in session.query(City).order_by(City.id):
        print("{}: {} -> {}".format(ci.id, ci.name, ci.state.name))
