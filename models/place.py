#!/usr/bin/python3
""" Place Module for HBNB project """
from models import storage_type, storage
from models.base_model import BaseModel, Base, Column
from models.base_model import String, Integer, ForeignKey, Float
from sqlalchemy.orm import relationship
from models.amenity import Amenity
from models.review import Review
from sqlalchemy import Table

if storage_type == "db":
    association_table = Table('place_amenity', Base.metadata,
                              Column('place_id', String(60),
                                     ForeignKey('places.id'),
                                     primary_key=True,
                                     nullable=False),
                              Column('amenity_id', String(60),
                                     ForeignKey('amenities.id'),
                                     primary_key=True,
                                     nullable=False))


class Place(BaseModel, Base):
    """ A place to stay """

    if storage_type == "db":
        __tablename__ = "places"
        city_id = Column(String(60), ForeignKey("cities.id"), nullable=False)
        user_id = Column(String(60), ForeignKey("users.id"), nullable=False)
        name = Column(String(128), nullable=False)
        description = Column(String(1024))
        number_rooms = Column(Integer, default=0)
        number_bathrooms = Column(Integer, default=0)
        max_guest = Column(Integer, default=0)
        price_by_night = Column(Integer, default=0)
        latitude = Column(Float)
        longitude = Column(Float)
        reviews = relationship("Review", backref="place")
        amenities = relationship("Amenity", secondary="place_amenity",
                                 viewonly=False)

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
                """if k.split('.')[0] == "Review":"""
                if isinstance(v, Review):
                    if v.place_id == self.id:
                        listReview.append(v)
            return listReview

        @property
        def amenities(self):
            listAmenity = []
            for obj in storage.all().values():
                if obj.id in self.amenity_ids:
                    listAmenity.append(obj)
            return listAmenity

        @amenities.setter
        def amenities(self, value):
            if isinstance(value, Amenity):
                self.amenity_ids.append(value.id)

    def __init__(self, *args, **kwargs):
        '''place constructor'''
        super().__init__(*args, **kwargs)
