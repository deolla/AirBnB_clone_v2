#!/usr/bin/python3
"""This module defines a class User"""
from models.base_model import BaseModel, Base
import models
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from models import storage_type


if storage_type == "db":
    class User(BaseModel, Base):
        """This class defines a user by various attributes"""
        __tablename__ = 'users'

        email = Column(String(128), nullable=False)
        password = Column(String(128), nullable=False)
        first_name = Column(String(128), nullable=True)
        last_name = Column(String(128), nullable=True)

        places = relationship("Place", backref="user",
                              cascade="all, delete, delete-orphan")

        reviews = relationship("Review", backref="user",
                               cascade="all, delete, delete-orphan")
else:
    class User(BaseModel):
        """ This class defines a user by various attributes """
        email = ""
        password = ""
        first_name = ""
        last_name = ""
