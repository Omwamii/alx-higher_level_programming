#!/usr/bin/python3
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
from model_city import City

if __name__ == "__main__":
    engine = create_engine(
        'mysql+mysqldb://{}:{}@localhost:3306/{}'
        .format(sys.argv[1], sys.argv[2],
                sys.argv[3]), pool_pre_ping=True)

    # Bind the engine to the base metadata
    Base.metadata.bind = engine

    # Create session
    Session = sessionmaker(bind=engine)
    session = Session()

    # Query all cities with their associated state
    results = session.query(City, State).\
        filter(City.state_id == State.id).all()

    # Print results
    for city, state in results:
        print("{}: ({}) {}".format(state.name, city.id, city.name))
    session.close()
