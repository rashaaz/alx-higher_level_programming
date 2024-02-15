#!/usr/bin/python3
"""
A script to connect to a MySQL database using SQLAlchemy,
add a new state, and print its ID
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

    lou = State(name="Louisiana")
    session.add(lou)
    session.commit()
    print(lou.id)
