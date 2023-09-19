#!/usr/bin/python3
""" Review module for the HBNB project """
from sqlalchemy import Column, String, ForeignKey
from models.base_model import BaseModel, Base
from sqlalchemy.orm import relationship
from models import storage_type

if storage_type == "db":
    class Review(BaseModel, Base):
        """ Review classto store review information """
        __tablename__ = "reviews"

        text = Column(String(1024), nullable=False)
        place_id = Column(String(60), ForeignKey('places.id'), nullable=False)
        user_id = Column(String(60), nullable=False)
else:
    class Review(BaseModel):
        """ Review classto store review information """
        text = ""
        place_id = ""
        user_id = ""
