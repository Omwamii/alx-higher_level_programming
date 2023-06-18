#!/usr/bin/python3
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

# Pass the MySQL username, password, and database name as command-line args
u_name = sys.argv[1]
passw = sys.argv[2]
db_name = sys.argv[3]

# Create the connection string
conn_string = f'mysql+mysqldb://{u_name}:{passw}@localhost/{db_name}'

# Connect to the MySQL server using the connection string
engine = create_engine(conn_string)

# Create a session factory
Session = sessionmaker(bind=engine)

if __name__ == '__main__':
    # Import State and Base from model_state
    from model_state import State, Base

    # Create all tables defined by the classes inheriting from Base
    Base.metadata.create_all(engine)

    # Create a session
    session = Session()

    # Query and delete all State objects with a name containing the letter "a"
    states_to_del = session.query(State).filter(State.name.ilike('%a%')).all()
    for state in states_to_del:
        session.delete(state)

    # Commit the session to persist the deletions to the database
    session.commit()

    # Close the session
    session.close()
