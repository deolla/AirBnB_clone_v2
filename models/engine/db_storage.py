#!/usr/bin/python3
"""This is a db storage module"""
import os
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from models.base_model import Base
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review

class DBStorage:
    """Private class attributes for db storage"""
    __engine = None
    __session = None

    classes = [User, State, Place, City, Amenity, Review]

    def __init__(self):
        user = os.getenv("HBNB_MYSQL_USER")
        passwd = os.getenv("HBNB_MYSQL_PWD")
        host = os.getenv("HBNB_MYSQL_HOST")
        db = os.getenv("HBNB_MYSQL_DB")

        self.__engine = create_engine(
            'mysql+mysqldb://{}:{}@{}/{}'.format(
                user, passwd, host, db), pool_pre_ping=True)

        if os.getenv("HBNB_ENV") == "test":
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """Query objects from the database based on class name (cls)"""
        session = self.__session()
        obj_dict = {}
        pop = list(self.classes)

        if type(cls) is str:
            return obj_dict

        if (cls is not None and cls in self.classes) or cls is None:
            if cls is not None:
                pop = [cls]
            for m in pop:
                rop = session.query(m)
                for i in rop:
                    obj_dict[i.__class__.__name__ + "." + i.id] = i
            return obj_dict

    def new(self, obj):
        """Add the object to the current database session"""
        session = self.__session()
        session.add(obj)

    def save(self):
        """commit all changes of the current database session"""
        session = self.__session()
        session.commit()

    def delete(self, obj=None):
        """delete from the current database session"""
        if obj is not None and type(obj) in self.classes:
            session = self.__session()
            session.query(type(obj)).filter(type(obj).id == obj,id.delete()

    def reload(self):
        """create all tables in the database"""
        Base.metadata.create_all(self.__engine)
        session_pop = sessionmaker(bind=self.__engine, expire_on_commit=False)
        self.__session = scoped_session(session_pop)

    def close(self):
        """This is a close method"""
        self.__session.remove()
