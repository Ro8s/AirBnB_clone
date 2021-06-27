#!/usr/bin/python3
''' BaseModel class '''

from datetime import datetime
import uuid
import models


class BaseModel():
    ''' BaseModel class '''

    def __init__(self, *args, **kwargs):
        ''' init method '''
        if not kwargs:
            self.id = str(uuid.uuid4())
            self.created_at = self.updated_at = datetime.now()
            models.storage.new(self)
        else:
            for key, value in kwargs.items():
                if key == "created_at" or key == "updated_at":
                    value = datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f")
                if key != "__class__":
                    setattr(self, key, value)

    ''' __str__ '''

    def __str__(self):
        ''' __str__ '''
        return "[{}] ({}) {}".format(self.__class__.__name__,
                                     self.id, self.__dict__)

    ''' save mehtod '''

    def save(self):
        ''' save '''
        self.updated_at = datetime.now()
        models.storage.save()

    ''' to_dict '''

    def to_dict(self):
        ''' to_dict '''
        d = self.__dict__.copy()
        d["__class__"] = self.__class__.__name__
        d["created_at"] = self.created_at.isoformat()
        d["updated_at"] = self.updated_at.isoformat()
        return d
