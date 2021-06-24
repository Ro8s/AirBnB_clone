#!/usr/bin/python3
''' BaseModel class '''

from datetime import datetime
import uuid


class BaseModel():
    ''' BaseModel class '''

    def __init__(self):
        ''' init method '''
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    ''' __str__ '''

    def __str__(self):
        ''' __str__ '''
        return "[{}] ({}) {}".format(self.__class__.__name__ , self.id, self.__dict__)

    ''' save mehtod '''

    def save(self):
        ''' save '''
        self.updated_at = datetime.now()

    ''' to_dict '''

    def to_dict(self):
        ''' to_dict '''
        self.__dict__["__class__"] = self.__class__.__name__
        self.__dict__["created_at"] = self.created_at.isoformat()
        self.__dict__["updated_at"] = self.updated_at.isoformat()
        return self.__dict__
