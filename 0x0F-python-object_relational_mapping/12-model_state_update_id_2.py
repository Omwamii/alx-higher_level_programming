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
connection_string = f'mysql+mysqldb://{u_name}:{passw}@localhost/{db_name}'

# Connect to the MySQL server using the connection string
engine = create_engine(connection_string)

# Create a session factory
Session = sessionmaker(bind=engine)

if __name__ == '__main__':
    # Import State and Base from model_state
    from model_state import State, Base

    # Create all tables defined by the classes inheriting from Base
    Base.metadata.create_all(engine)

    # Create a session
    session = Session()

    # Get the State object with id = 2
    state = session.query(State).filter(State.id == 2).first()

    if state:
        # Change the name of the State to "New Mexico"
        state.name = "New Mexico"

        # Commit the session to persist the changes to the database
        session.commit()
    else:
        print("State not found")

    # Close the session
    session.close()
