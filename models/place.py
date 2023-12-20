#!/usr/bin/python3
""" Place Module for HBNB project """
from models import storage_type, storage
from models.base_model import BaseModel, Base, Column
from models.base_model import String, Integer, ForeignKey, Float
from sqlalchemy.orm import relationship


class Place(BaseModel, Base):
    """ A place to stay """

    if storage_type == "db":
        __tablename__ = "places"
        city_id = Column(String(60), ForeignKey("cities.id"), nullable=False)
        user_id = Column(String(60), ForeignKey("users.id"), nullable=False)
        name = Column(String(128), nullable=False)
        description = Column(String(1024), nullable=False)
        number_rooms = Column(Integer, nullable=False, default=0)
        number_bathrooms = Column(Integer, nullable=False, default=0)
        max_guest = Column(Integer, nullable=False, default=0)
        price_by_night = Column(Integer, nullable=False, default=0)
        latitude = Column(Float, nullable=False)
        longitude = Column(Float, nullable=False)
        reviews = relationship("Review", backref="place")

    else:
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
        amenity_ids = []

        @property
        def reviews(self):
            listReview = []
            for k, v in storage.all().items():
                if k.split('.')[0] == "Review":
                    if v.place_id == self.id:
                        listReview.append(v)
            return listReview

    def __init__(self, *args, **kwargs):
        '''place constructor'''
        super().__init__(*args, **kwargs)
