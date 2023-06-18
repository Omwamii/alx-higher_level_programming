#!/usr/bin/python3
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
from model_city import City

if __name__ == "__main__":
    u_name = sys.argv[1]
    passw = sys.argv[2]
    db_name = sys.argv[3]

    # Create engine
    engine = create_engine(f'mysql+mysqldb://{u_name}:{passw}@localhost/{db_name}')

    # Bind the engine to the base metadata
    Base.metadata.bind = engine

    # Create session
    Session = sessionmaker(bind=engine)
    session = Session()

    # Query all cities with their associated state
    cities = session.query(City).join(State).order_by(City.id)

    # Print results
    for city in cities:
        print(f'{city.state.name}: ({city.id}) {city.name}')
