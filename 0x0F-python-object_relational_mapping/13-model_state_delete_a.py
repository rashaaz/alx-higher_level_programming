#!/usr/bin/python3
"""
A script to connect to a MySQL database using SQLAlchemy,
retrieve states with names containing the letter 'a', and delete them.
"""
import sys
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


if __name__ == '__main__':
    sscctt = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.
                           format(sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)
    Session = sessionmaker(bind=sscctt)
    session = Session()

    sta = session.query(State).filter(State.name.like('%a%')).all()

    for sr in sta:
        session.delete(sr)

    session.commit()
