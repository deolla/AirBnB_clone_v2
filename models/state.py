#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from models import storage_type
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship


if storage_type == "db":
    class State(BaseModel, Base):
        """ State class

            Attributes:
                name: ""
        """
        __tablename__ = "states"
        name = Column(String(128), nullable=False)
        cities = relationship("City", backref="state",
                              cascade="all, delete")
else:
    class State(BaseModel):
        """ State class

            Attribute:
                name: "string"
        """
        name = ""

        @property
        def cities(self):
            """setter property"""
            from models import storage
            lista = [pop for pop in storage.all().values()
                     if pop.__class__.__name__ == "City" and
                     pop.state_id == self.id]
            return lista
