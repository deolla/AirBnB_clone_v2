#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from models import storage_type
from models.place import place_amenity


if storage_type == "db":
    class Amenity(BaseModel, Base):
        """ This class defines Amenity"""
        __tablename__ = "amenities"
        name = Column(String(128), nullable=False)

        place_amenities = relationship("Place", secondary=place_amenity)
else:
    class Amenity(BaseModel):
        """ This is a class that defines Amenity"""
        name = ""
