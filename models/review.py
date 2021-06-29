#!/usr/bin/python3
''' Review '''


from models.base_model import BaseModel
import models


class Review(BaseModel):
    ''' Class Review that inherit from BaseModel '''
    place_id = ""
    user_id = ""
    text = ""
