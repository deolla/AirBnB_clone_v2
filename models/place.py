#!/usr/bin/python3
""" Place Module for HBNB project """
from models.base_model import BaseModel, Base
from models import storage_type
from sqlalchemy import Column, String, Integer, Float, ForeignKey, Table
from sqlalchemy.orm import relationship
import models

if storage_type == "db":
    class Place(BaseModel, Base):
        """ A place to stay

            Attributes:
                city_id = ""
                user_id = ""
                name = ""
                description = ""
                number_room = 0
                number_bathroom = 0
                max_guest = 0
                price_by_night = 0
                latitude = 0.0
                longitude = 0.0
        """
        __tablename__ = 'places'

        city_id = Column(String(60), ForeignKey("cities.id"), nullable=False)
        user_id = Column(String(60), ForeignKey("users.id"), nullable=False)
        name = Column(String(128), nullable=False)
        description = Column(String(1024), nullable=True)
        number_rooms = Column(Integer, nullable=False, default=0)
        number_bathrooms = Column(Integer, nullable=False, default=0)
        max_guest = Column(Integer, nullable=False, default=0)
        price_by_night = Column(Integer, nullable=False, default=0)
        latitude = Column(Float, nullable=True)
        longitude = Column(Float, nullable=True)

        reviews = relationship("Review", backref="place",
                               cascade="all, delete")
else:
    class Place(BaseModel):
        """ A place to stay
            Attributes:
                city_id = ""
                user_id = ""
                name = ""
                descriptiin = ""
                number_room = 0
                number_bathroom = 0
                max_guest = 0
                price_by_night = 0
                latitude = 0.0
                longitude = 0.0
        """
        city_id = ""
        user_id = ""
        name = ""
        description = ""
        number_rooms = 0
        number_bathrooms = 0
        max_guest = 0
        price_by_night = 0
        latitude = 0.0
        longitude = 0.0

        @property
        def reviews(self):
            """
            Getter attr reviews that returns
            the list of review instances
            """
            from models import storage
            review_list = []
            for review in storage.all("Review").values():
                if review.place_id == self.id:
                    review_list.append(review)
            return review_list
