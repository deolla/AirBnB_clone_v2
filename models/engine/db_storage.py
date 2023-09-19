#!/usr/bin/python3
"""This is a module that defines a db storage"""
import os
from sqlalchemy import create_engine, MetaData
from sqlalchemy.orm import scoped_session, sessionmaker
from models.base_model import Base
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.review import Review

metadata_obj = MetaData()


class DBStorage:
    """Private class Attribute for db storage

        Attributes:
            engine: None
            session: None
    """
    __engine = None
    __session = None

    classes = [State, City, Place, User, Review]

    def __init__(self):
        user = os.getenv("HBNB_MYSQL_USER")
        passwd = os.getenv("HBNB_MYSQL_PWD")
        host = os.getenv("HBNB_MYSQL_HOST")
        db = os.getenv("HBNB_MYSQL_DB")
        env = os.getenv("HBNB_ENV")

        self.__engine = create_engine("mysql" + "+" + "mysqldb" + "://" +
                                      user + ":" + passwd + "@" +
                                      host + "/" + db,
                                      pool_pre_ping=True)

        if env == "test":
            metadata_obj.drop_all(bind=self.__engine)

    def all(self, cls=None):
        """Query objects from the database based on class name (cls)"""
        dic = {}
        target = list(self.classes)

        if isinstance(cls, str):
            return dic

        if (cls is not None and cls in self.classes) or cls is None:
            if cls is not None:
              target = [cls]
            for i in target:
                instances = self.__session.query(i)
                for k in instances:
                    dic[k.__class__.__name__ + "." + k.id] = k
            return dic

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
            session.query(type(obj)).filter(type(obj).id == obj.id).delete()

    def close(self):
        """This is a close method"""
        self.__session.remove()

    def reload(self):
        """create all tables in the database"""
        Base.metadata.create_all(self.__engine)
        session_factory = sessionmaker(bind=self.__engine,
                                       expire_on_commit=False)
        self.__session = scoped_session(session_factory)
