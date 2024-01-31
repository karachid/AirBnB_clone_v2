#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base, Column, String
from sqlalchemy.orm import relationship
from models import storage_type


class State(BaseModel, Base):
    """ State class """
    if storage_type == "db":
        __tablename__ = "states"
        name = Column(String(128), nullable=False)
        cities = relationship("City", backref="state", cascade="all,delete")
    else:
        name = ""

        @property
        def cities(self):
            listCity = []
            for obj in storage.all().values():
                if obj.__class__.__name__ == "City":
                    if obj.state_id == self.id:
                        listCity.append(obj)
            return listCit

    def __init__(self, *args, **kwargs):
        '''state constructor'''
        super().__init__(*args, **kwargs)
