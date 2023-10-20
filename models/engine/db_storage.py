#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import Base
from sqlalchemy.orm import sessionmaker, scoped_session
from sqlalchemy import create_engine
from os import getenv
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review

if getenv('HBNB_TYPE_STORAGE') == 'db':
    from models.place import place_amenity

classes = {
        "User": User,
        "State": State,
        "City": City,
        "Amenity": Amenity,
        "Place": Place,
        "Review": Review,
        }


class DBStorage:
    """ DBStorage class """
    __engine = None
    __session = None

    def __init__(self):
        """creates new dbstorage instances"""
        HBNB_MYSQL_USER = getenv('HBNB_MYSQL_USER')
        HBNB_MYSQL_PWD = getenv('HBNB_MYSQL_PWD')
        HBNB_MYSQL_HOST = getenv('HBNB_MYSQL_HOST')
        HBNB_MYSQL_DB = getenv('HBNB_MYSQL_DB')

        self.__engine = create_engine(
            'mysql+mysqldb://{}:{}@{}/{}'.format(
                                           HBNB_MYSQL_USER,
                                           HBNB_MYSQL_PWD,
                                           HBNB_MYSQL_HOST,
                                           HBNB_MYSQL_DB
                                        ), pool_pre_ping=True)

        if getenv('HBNB_ENV') == 'test':
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """making query sets from the current database instances"""
        my_dict = {}

        if cls is None:
            for k in classes.values():
                objects = self.__session.query(k).all()
                for f in objects:
                    key = f.__class__.__name__ + '.' + f.id
                    my_dict[key] = f
        else:
            objects = self.__session.query(cls).all()
            for t in objects:
                key = t.__class__.__name__ + '.' + t.id
                my_dict[key] = t
        return my_dict

    def new(self, obj):
        """adds new object to database"""
        if obj is not None:
            try:
                self.__session.add(obj)
                self.__session.flush()
                self.__session.refresh(obj)

            except Exception as e:
                self.__session.rollback()
                raise e

    def save(self):
        """commits chenges of current session"""
        self.__session.commit()

    def delete(self, obj=None):
        """deletes objects from the db"""
        if obj is not None:
            self.__session.query(type(obj)).filter(
                    type(obj).id == obj.id).delete()

    def reload(self):
        """creates table in db"""
        Base.metadata.create_all(self.__engine)
        session_fact = sessionmaker(
                    bind=self.__engine, expire_on_commit=False)

        self.__session = scoped_session(session_fact)()

    def close(self):
        """classes class session"""
        self.__session.close()
