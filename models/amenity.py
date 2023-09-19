#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from models.place import place_amenity
from models import storage_type
from sqlalchemy import Column, String, Table
from sqlalchemy.orm import relationship

if storage_type == "db":
    class Amenity(BaseModel, Base):
        """Inherits from BaseModel and Base
            
            Attribute:
                name: ""
        """
        __tablename__ = 'amenities'

        name = Column(String(128), nullable=False)

        place_amenities = relationship("Place", secondary=place_amenity)
else:
    class Amenity(BaseModel):
        """ Amenity class """
        name = ""
