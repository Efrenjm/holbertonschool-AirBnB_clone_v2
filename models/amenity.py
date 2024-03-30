#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, Table, ForeignKey
from sqlalchemy.orm import relationship


# association_table = Table('place_amenity', Base.metadata,
#                           Column('place_id', String(60), ForeignKey('places.id')),
#                           Column('amenity_id', String(60), ForeignKey('amenities.id'))
#                           )
class Amenity(BaseModel, Base):
    """ The Amenity class, contain name and place amenities table """
    __tablename__ = "amenities"
    name = Column(String(128), nullable=False)
    place_amenities = relationship("Place", secondary="place_amenity", viewonly=True)