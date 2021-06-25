#!/usr/bin/python3
''' FileStorage Module'''

import json
import os


class FileStorage(self):
    ''' FileStorage '''
    __file_path = os.path.abspath("file.json")
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
        __objects[clac + i] = obj


    ''' save '''

    def save(self):
        ''' save '''
        if os.path.isfile(FileStorage.__file_path):
            with open(FileStorage.__file_path, "w") as f:
                f.write(json.dumps(FileStorage.__objects))

    ''' reload '''

    def reload(self):
        ''' reload '''
        if os.path.isfile(FileStorage.__file_path):
            with open(FileStorage.__file_path, "r") as f:
                s = f.read()
            a = json.loads(s)
            for key in a:
                FileStorage.__objects[key] = a[key]
