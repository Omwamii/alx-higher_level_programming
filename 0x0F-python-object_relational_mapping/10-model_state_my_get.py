#!/usr/bin/python3
from model_state import Base, State
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker
import sys


if __name__ == "__main__":
    u_name = sys.argv[1]
    passw = sys.argv[2]
    db_name = sys.argv[3]
    state_name = sys.argv[4]
    connection_string = f'mysql+mysqldb://{u_name}:{passw}@localhost/{db_name}'
    engine = create_engine(connection_string, pool_pre_ping=True)

    Session = sessionmaker(bind=engine)

    # create all tables defined by classes inheriting Base
    Base.metadata.create_all(engine)

    session = Session()

    # fetch all States objects and sort them by id
    state = session.query(State).filter(State.name == state_name).first()

    # check if the state exists
    if state:
        print(state.id)
    else:
        print("Not found")

    # close session
    session.close()
