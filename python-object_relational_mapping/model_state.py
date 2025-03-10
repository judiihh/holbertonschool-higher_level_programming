#!/usr/bin/python3
"""
Contains the class definition of a State and an instance of Base.
"""

from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

# Create an instance of the Base class
Base = declarative_base()


class State(Base):
    """State class linked to the 'states' table in MySQL database"""
    __tablename__ = 'states'

    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    name = Column(String(128), nullable=False)
