#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from models import which_storage
from sqlalchemy import String, column


class Amenity(BaseModel, Base):
    """Ammenty table"""
    __tablename__ = "amenities"

    if which_storage == 'db':
        name = Column(String(128), nullable=False)
    else:
        name = ""
