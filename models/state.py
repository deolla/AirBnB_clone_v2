#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from models import storage_type
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship


if storage_type == "db":
    class State(BaseModel):
        """ State class """
        __tablename__ = "states"

        name = Column(
            String(128),
            nullable=False)

        cities = relationship(
            "City",
            back_populates="state",
            cascade="all, delete"
        )
else:
    class State(BaseModel):
        """ State class"""
        name = ""
