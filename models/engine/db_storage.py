#!/usr/bin/python3
from models.base_model import BaseModel, Base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session, relationship
from os import getenv
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class DBStorage:
    __engine = None
    __session = None

    def __init__(self):
        """Create the engine
        """
        user = getenv("HBNB_MYSQL_USER")
        passw = getenv("HBNB_MYSQL_PWD")
        host = getenv("HBNB_MYSQL_HOST")
        db = getenv("HBNB_MYSQL_DB")
        env = getenv("HBNB_ENV")
        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'
                                      .format(user, passw, host, db),
                                      pool_pre_ping=True)

        Base.metadata.create_all(self.__engine)
        if env == "test":
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """query on the current database session
        """
        object = []
        if cls is not None:
            object = self.__session.query(cls)
        else:
            classes = [State, City, User, Place, Review, Amenity]
            for x in classes:
                object += self.__session.query(x).all()

        obj_dict = {}
        for obj in object:
            key = '{}.{}'.format(type(obj).__name__, obj.id)
            obj_dict[key] = obj
        return (obj_dict)

    def new(self, obj):
        """add the object to the current database session
        """
        if obj is not None:
            self.__session.add(obj)

    def save(self):
        """commit all changes of the current database session
        """
        self.__session.commit()

    def delete(self, obj=None):
        """delete from the current database session
        """
        if obj is not None:
            self.__session.delete(obj)

    def reload(self):
        """creates all tables in the database
        """
        Base.metadata.create_all(self.__engine)
        self.__session = sessionmaker(expire_on_commit=False,
                                      bind=self.__engine)
        Session = scoped_session(self.__session)
        self.__session = Session()
