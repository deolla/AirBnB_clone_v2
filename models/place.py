#!/usr/bin/python3
""" Place Module for HBNB project """
from models.base_model import BaseModel, Base
from models import storage_type
from sqlalchemy import Column, String, Integer, Float, ForeignKey, Table
from sqlalchemy.orm import relationship
import models

place_amenity = Table("place_amenity", Base.metadata,
                      Column("place_id", String(60), ForeignKey("places.id"),
                             primary_key=True, nullable=False),
                      Column("amenity_id", String(60), ForeignKey("amenities.id"),
                             primary_key=True, nullable=False))


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
        amenities = relationship("Amenity", back_populates="place_amenities",
                                 secondary=place_amenity, viewonly=False)
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

        @property
        def amenities(self):
            """ Getter attr for amenity """
            from models import storage
            lists = [m for m in storage.all().values()
                    if m.__class__.__name__ == "Amenity"
                    and m.id in self.amenity_ids]
            return lists

        @amenities.setter
        def amenities(self, lists):
            if type(lists) == Amenity:
                self.amenity_ids.append(lists.id)
