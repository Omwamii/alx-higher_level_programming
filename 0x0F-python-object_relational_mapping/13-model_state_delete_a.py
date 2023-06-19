#!/usr/bin/python3
"""
module to delete State objects with name with 'a'
"""
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State


engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                       .format(sys.argv[1], sys.argv[2], sys.argv[3]))

Session = sessionmaker(bind=engine)

if __name__ == '__main__':
    Base.metadata.create_all(engine)
    session = Session()

    # Query and delete all State objects with a name containing the letter "a"
    states_to_del = session.query(State).filter(State.name.ilike('%a%')).all()
    for state in states_to_del:
        session.delete(state)

    # Commit the session to persist the deletions to the database
    session.commit()
    session.close()
