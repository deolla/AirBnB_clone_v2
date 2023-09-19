#!/usr/bin/python3
""" City Module for HBNB project """
from models import storage_type
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship


if storage_type == "db":
    class City(BaseModel, Base):
        """ City class
            
            ATTRIBUTE:
                state ID
                name
        """
        __tablename__ = "cities"
        name = Column(String(128), nullable=False)
        state_id = Column(String(60), ForeignKey("states.id"), nullable=False)
        places = relationship("Place", backref="cities", cascade="all, delete")

else:
    class City(BaseModel):
        """ The city class
            
            Attributes:
                state_id
                name
        """
        name = ""
        state_id = ""
