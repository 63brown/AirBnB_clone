#!usr/bin/python3
import uuid
from datetime import datetime
from sqlalchemy import Column, String, DATETIME
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class BaseModel:
    """Base model for airbnb models"""

    id = Column(String(60),
                nullable= False,
                primary_key=True)
    created_at = Column(DATETIME,
                        nullable=False,
                        default=datetime.utcnow())
    updated_at = Column(DATETIME,
                        nullable=False,
                        default=datetime.utcnow())

    def __init__(self, *args,**kwargs):
        """Instantiates a new model"""
        if not kwargs:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
        else:
            for k in kwargs:
                if k in ['created_at','updated_at']:
                    setattr(self,k,datetime.fromisoformat(kwargs[k]))
                elif k!= '__class__':
                    setattr(self,k,kwargs[k])

    def __str__(self):
        """Returns a string representation of the instance"""
        return '[{}] ({}) {}'.format(
            self.__class__.__name__, self.id, self.__dict__)

    def save(self):
        """updates the public instance attribute updated_at with the current datetime"""
        from models import storage
        self.updated_at = datetime.now()
        storage.new(self)
        storage.save()

    def to_dict(self):
        """returns a dictionary containing all keys/values of __dict__ of the instance"""
        dict = self.__dict__.copy()
        dict['__class__'] = self.__class__.__name__
        dict["created_at"] = self.created_at.isoformat()
        dict["updated_at"] = self.updated_at.isoformat()
        return dict
