#!/usr/bin/python3
"""
Script that prints the id of the State object with the given name
from the database hbtn_0e_6_usa.
"""
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

if __name__ == "__main__":
    # Get MySQL credentials and state name from command-line arguments
    mysql_username = sys.argv[1]
    mysql_password = sys.argv[2]
    database_name = sys.argv[3]
    state_name = sys.argv[4]

    # Create the database engine
    engine = create_engine(
        'mysql+mysqldb://{}:{}@localhost/{}'.format(
            mysql_username, mysql_password, database_name
        ),
        pool_pre_ping=True
    )

    # Create a session
    Session = sessionmaker(bind=engine)
    session = Session()

    # Query for the state (SQL Injection Safe) - Fixed line length
    state = (
        session.query(State)
        .filter(State.name == state_name)
        .first()
    )

    # Print the state's ID if found, else print "Not found"
    if state:
        print(state.id)
    else:
        print("Not found")

    # Close the session
    session.close()
