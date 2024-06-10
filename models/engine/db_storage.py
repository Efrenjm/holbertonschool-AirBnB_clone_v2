#!/usr/bin/python3
"""Storage engine for the database"""
from os import getenv

from models.city import City
from models.user import User
from models.state import State
from models.place import Place
from models.review import Review
from models.amenity import Amenity
from models.base_model import Base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

USER = getenv('HBNB_MYSQL_USER')
PWD = getenv('HBNB_MYSQL_PWD')
HOST = getenv('HBNB_MYSQL_HOST')
DB = getenv('HBNB_MYSQL_DB')

classes = {'User': User, 'Place': Place, 'State': State,
           'City': City, 'Amenity': Amenity, 'Review': Review}


class DBStorage:
    """Storage engine for the database"""
    __engine = None
    __session = None

    def __init__(self):
        """Create a new instance of DBStorage"""
        self.__engine = create_engine(
            f"mysql+mysqldb://{USER}:{PWD}@{HOST}/{DB}", pool_pre_ping=True)
        if getenv('HBNB_ENV') == 'test':
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """Querie the current database session"""
        dictio = {}
        if cls:
            for item in self.__session.query(cls):
                key = f"{item.__class__.__name__}.{item.id}"
                dictio[key] = item
        else:
            for key, value in classes.items():
                for item in self.__session.query(value):
                    key = f"{item.__class__.__name__}.{item.id}"
                    dictio[key] = item
        return dictio

    def new(self, obj):
        """Add the object to the current database session"""
        self.__session.add(obj)

    def save(self):
        """Commit all changes of the current database session"""
        self.__session.commit()

    def delete(self, obj=None):
        """Delete from the current database session"""
        if obj:
            self.__session.delete(obj)

    def reload(self):
        """Create all tables in the database"""
        Base.metadata.create_all(self.__engine)
        Session = sessionmaker(bind=self.__engine, expire_on_commit=False)
        self.__session = Session()

    def close(self):
        """Close the database session"""
        self.__session.close()
