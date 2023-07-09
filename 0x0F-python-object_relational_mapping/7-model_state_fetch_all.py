#!/usr/bin/python3
""" module that lists all State objects from db
"""
from model_state import Base, State
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker
import sys


if __name__ == "__main__":
    engine = create_engine(
            'mysql+mysqldb://{}:{}@localhost:3306/{}'
            .format(sys.argv[1], sys.argv[2],
                    sys.argv[3]), pool_pre_ping=True)
    Session = sessionmaker(bind=engine)

    # create all tables defined by classes inheriting Base
    Base.metadata.create_all(engine)

    session = Session()

    # fetch all States objects and sort them by id
    states = session.query(State).order_by(State.id).all()

    for state in states:
        print(f'{state.id}: {state.name}')

    # close session
    session.close()
