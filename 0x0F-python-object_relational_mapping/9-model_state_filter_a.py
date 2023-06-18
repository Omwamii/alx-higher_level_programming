#!/usr/bin/python3
from model_state import Base, State
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker
import sys


if __name__ == "__main__":
    engine = create_engine(
            'mysql+mysqldb://{}:{}@localhost:3306/{}'
            .format(argv[1], argv[2],
                    argv[3]), pool_pre_ping=True)

    Session = sessionmaker(bind=engine)

    # create all tables defined by classes inheriting Base
    Base.metadata.create_all(engine)

    session = Session()

    # fetch all States objects containing 'a' and sort them by id
    states = session.query(State).filter(State.name.like('%a%')).order_by(State.id).all()

    for state in states:
        print(f'{state.id}: {state.name}')

    # close session
    session.close()
