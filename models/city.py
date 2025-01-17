#!/usr/bin/python3
""" City Module for HBNB project """
from models.base_model import BaseModel, Base, Column, String, ForeignKey
from sqlalchemy.orm import relationship
from models import storage_type


class City(BaseModel, Base):
    """ The city class, contains state ID and name """

    if storage_type == "db":
        __tablename__ = 'cities'
        name = Column(String(128), nullable=False)
        state_id = Column(String(60), ForeignKey('states.id'))
        places = relationship("Place", backref="cities")
    else:
        name = ""
        state_id = ""

    def __init__(self, *args, **kwargs):
        '''city constructor'''
        super().__init__(*args, **kwargs)
