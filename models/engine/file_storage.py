#!/usr/bin/python3
''' FileStorage Module'''

import json


class FileStorage(self):
    ''' FileStorage '''
    __file_path
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

    ''' reload '''

    def reload(self):
        ''' reload '''


