#!/usr/bin/python3
"""create a unique FileStorage instance for your application"""
from models.engine.file_storage import FileStorage
from models.engine.db_storage import DBStorage
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from os import getenv

if getenv('HBNB_TYPE_STORAGE') == 'db':
    print('running in DB mode')
    storage = DBStorage()
else:
    print('running in FILE mode')
    storage = FileStorage()
storage.reload()
