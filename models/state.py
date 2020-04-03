#!/usr/bin/python3
"""This is the state class"""
import models
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from os import getenv


class State(BaseModel, Base):
    """This is the class for State
    Attributes:
        name: input name
    """
    __tablename__ = 'states'
    name = Column(String(128), nullable=False)
    if getenv("HBNB_TYPE_STORAGE") == 'db':
        cities = relationship('City', backref='state', cascade='all,
                              delete-orphan')
    else:
        @property
        def cities(self):
            list = []
            for x in models.storage.all().values():
                if self.id == x.state_id:
                    list.append(x)

            return (list)
