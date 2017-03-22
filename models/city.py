#!/usr/bin/python3
from models import *
from sqlalchemy import Column, Integer, String, ForeignKey
"""
This is the City class module. This module creates a City class that inherits
from BaseModel.
"""


class City(BaseModel, Base):
    """  This is the City class and it inherts from BaseModel """
    __tablename__ = "cities"
    state_id = Column(String(60), nullable=False, ForeignKey('states.id'))
    name = Column(String(128), nullable=False)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
