#!/usr/bin/python3
"""
Amenity Class from Models Module
"""
import os
from models.base_model import BaseModel, Base # type: ignore
from sqlalchemy.orm import relationship # type: ignore
from sqlalchemy import Column, Integer, String, Float # type: ignore
from sqlalchemy.orm import backref # type: ignore
storage_type = os.environ.get('HBNB_TYPE_STORAGE')


class Amenity(BaseModel, Base):
    """Amenity class handles all application amenities"""
    if storage_type == "db":
        __tablename__ = 'amenities'
        name = Column(String(128), nullable=False)
        place_amenities = relationship("Place", secondary="place_amenity")
    else:
        name = ''