#!/usr/bin/python3
"""This module defines a class User"""
from models.base_model import BaseModel, Base, Column, String
from sqlalchemy.orm import relationship
from models import storage_type


class User(BaseModel, Base):
    """This class defines a user by various attributes"""

    if (storage_type == "db"):
        __tablename__ = "users"
        email = Column(String(128), nullable=False)
        password = Column(String(128), nullable=False)
        first_name = Column(String(128))
        last_name = Column(String(128))
        places = relationship("Place", backref="user")
        reviews = relationship("Review", backref="user")
    else:
        email = ''
        password = ''
        first_name = ''
        last_name = ''
