#!/usr/bin/python3
''' City '''


from models.base_model import BaseModel
import models


class City(BaseModel):
    ''' Class City that inherit from BaseModel '''
    state_id = ""
    name = ""
