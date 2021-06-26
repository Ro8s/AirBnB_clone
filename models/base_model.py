#!/usr/bin/python3
''' BaseModel class '''

from datetime import datetime
import uuid
from models import storage


class BaseModel():
    ''' BaseModel class '''

    def __init__(self, *args, **kwargs):
        ''' init method '''
        if not kwargs:
            self.id = str(uuid.uuid4())
            self.created_at = self.updated_at = datetime.now()
            storage.new(self)
            storage.save()
        else:
            for key in kwargs:
                if key is "created_at" or key is "updated_at":
                    a = datetime.strptime(kwargs[key], "%Y-%m-%dT%H:%M:%S.%f")
                    setattr(self, key, a)
                elif key is not "__class__":
                    setattr(self, key, kwargs[key])

    ''' __str__ '''

    def __str__(self):
        ''' __str__ '''
        return "[{}] ({}) {}".format(self.__class__.__name__,
                                     self.id, self.__dict__)

    ''' save mehtod '''

    def save(self):
        ''' save '''
        self.updated_at = datetime.now()
        storage.save()

    ''' to_dict '''

    def to_dict(self):
        ''' to_dict '''
        d = self.__dict__.copy()
        d["__class__"] = self.__class__.__name__
        d["created_at"] = self.created_at.isoformat()
        d["updated_at"] = self.updated_at.isoformat()
        return d
