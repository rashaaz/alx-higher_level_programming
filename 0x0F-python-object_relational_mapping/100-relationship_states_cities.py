#!/usr/bin/python3
"""Script to add a city and its corresponding state to the database"""
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from relationship_state import State
from relationship_city import Base, City

if __name__ == "__main__":
    sscctt = create_engine("mysql+mysqldb://{}:{}@localhost/{}"
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)
    Base.metadata.create_all(sscctt)
    Session = sessionmaker(bind=sscctt)
    session = Session()

    session.add(City(name="San Francisco", state=State(name="California")))
    session.commit()
