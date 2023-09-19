#!/usr/bin/python3
"""This module defines a class User"""

from models.base_model import BaseModel, Base
from models import which_storage
from sqlalchemy.orm import relationship
from sqlalchemy import Column, String


class User(BaseModel):
    """This class defines a user by various attributes"""
    __tablename__'users'

    if which_storage == 'db':
        email = Column(String(128), nullable=False)
        password = Column(String(128), nullable=False)
        first_name = Column(String(128), nullable=True))
        last_name = Column(String(128), delete='delete-orphan')
        places = reltionship('Place', cascade='all, delete-orphan', backref='user')
        reviews = relationship('Review', backref'user', cascade='all, delete-orphan')
    else:

        email = ''
        password = ''
        first_name = ''
        last_name = ''
