#!/usr/bin/python3
"""This is the place class"""
from models.base_model import BaseModel, Base
from models.review import Review
from sqlalchemy import Column, String, Float, Integer, ForeignKey, Table
from sqlalchemy.orm import relationship
from os import getenv
import models

metadata = Base.metadata


class Place(BaseModel, Base):
    """This is the class for Place
    Attributes:
        city_id: city id
        user_id: user id
        name: name input
        description: string of description
        number_rooms: number of room in int
        number_bathrooms: number of bathrooms in int
        max_guest: maximum guest in int
        price_by_night:: pice for a staying in int
        latitude: latitude in flaot
        longitude: longitude in float
        amenity_ids: list of Amenity ids
    """
    __tablename__ = 'places'
    city_id = Column(String(60), ForeignKey('cities.id'), nullable=False)
    user_id = Column(String(60), ForeignKey('users.id'), nullable=False)
    name = Column(String(128), nullable=False)
    description = Column(String(1024))
    number_rooms = Column(Integer, default=0, nullable=False)
    number_bathrooms = Column(Integer, default=0, nullable=False)
    max_guest = Column(Integer, default=0, nullable=False)
    price_by_night = Column(Integer, default=0, nullable=False)
    latitude = Column(Float, nullable=True)
    longitude = Column(Float, nullable=True)
    amenity_ids = []

    place_amenity = Table(
        'place_amenity',
        metadata,
        Column(
            'place_id',
            String(60),
            ForeignKey('places.id'),
            primary_key=True
        ),
        Column('amenity_id',
               String(60),
               ForeignKey('amenities.id'),
               primary_key=True
               )
    )

    if getenv('HBNB_TYPE_STORAGE') == 'db':
        reviews = relationship(
            'Review',
            backref='place',
            cascade='all, delete'
        )

        amenities = relationship(
            'Amenity',
            secondary=place_amenity,
            viewonly=False
        )
    else:
        @property
        def reviews(self):
            objs = models.storage.all(Review)
            return [v for k, v in obj.items() if v.place_id == self.id]
