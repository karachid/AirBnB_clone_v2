#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base, Column, String, ForeignKey
from sqlalchemy.orm import relationship
from models import storage_type


class Amenity(BaseModel, Base):
    """amenity Class"""
    if storage_type == db:
        __tablename__ = "amenities"
        name = Column(String(128), nullable=False)
        place_amenities = relationship("Place", secondary="place_amenity",
                                       viewonly=False)
    else:
        name = ""

    def __init__(self, *args, **kwargs):
        '''amenity constructor'''
        super().__init__(*args, **kwargs)
