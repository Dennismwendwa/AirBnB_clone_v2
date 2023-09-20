#!/usr/bin/python3
""" Review module for the HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy.sql.schema import ForeignKey
from models import which_storage


class Review(BaseModel, Base):
    """ Review classto store review information """
    __tablename__ = 'reviews'
    if which_storage == 'db':
        text = Column(String(1024), nullable=False)
        place_id = Column(String(60), ForeignKey('place.id'), nullable=False)
        user_id = Column(String(60), ForeignKey('place.id'), nullable=False)
    else:
        
        place_id = ""
        user_id = ""
        text = ""
