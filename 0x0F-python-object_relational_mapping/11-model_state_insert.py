#!/usr/bin/python3
"""
module to add a State object to db
"""
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

# Pass the MySQL username, password, and database name as command-line args
u_name = sys.argv[1]
passw = sys.argv[2]
db_name = sys.argv[3]

# Create the connection string
connection_string = f'mysql://{u_name}:{passw}@localhost:3306/{db_name}'

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

    # Create a new State object
    louisiana = State(name='Louisiana')

    # Add the State object to the session
    session.add(louisiana)

    # Commit the session to persist the changes to the database
    session.commit()

    # Print the new states.id after creation
    print(louisiana.id)

    # Close the session
    session.close()
