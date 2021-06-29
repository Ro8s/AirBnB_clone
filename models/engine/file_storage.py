#!/usr/bin/python3
''' FileStorage Module'''

import json
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


classes = {"BaseModel": BaseModel, "User": User, "State": State, "City": City, "Amenity": Amenity, "Place": Place, "Review": Review}


class FileStorage():
    ''' FileStorage '''
    __file_path = "file.json"
    __objects = {}

    ''' all '''
    def all(self):
        ''' all '''
        return FileStorage.__objects

    ''' new '''

    def new(self, obj):
        ''' new '''
        clac = str(obj.__class__.__name__)
        i = str(obj.id)
        key = clac + "." + i
        FileStorage.__objects[key] = obj

    ''' save '''

    def save(self):
        ''' save '''
        aux_dict = {}
        for key in FileStorage.__objects:
            aux_dict[key] = FileStorage.__objects[key].to_dict()
        with open(FileStorage.__file_path, "w") as f:
            json.dump(aux_dict, f)

    ''' reload '''

    def reload(self):
        ''' reload '''
        try:
            with open(FileStorage.__file_path, "r") as f:
                a = json.load(f)
            for key, value in a.items():
                aux = key.split('.')
                obj = classes[aux[0]](**value)
                self.new(obj)
        except:
            pass
