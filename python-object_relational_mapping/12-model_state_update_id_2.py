#!/usr/bin/python3
"""
Script that updates the name of the State where id = 2
to "New Mexico" in the database hbtn_0e_6_usa.
"""
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

if __name__ == "__main__":
    # Get MySQL credentials from command-line arguments
    mysql_username = sys.argv[1]
    mysql_password = sys.argv[2]
    database_name = sys.argv[3]

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

    # Query the state with id = 2
    state = (
        session.query(State)
        .filter(State.id == 2)
        .first()
    )

    # If the state exists, update its name
    if state:
        state.name = "New Mexico"
        session.commit()

    # Close the session
    session.close()
