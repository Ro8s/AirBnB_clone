#!/usr/bin/python3
''' Unittest for BaseModel '''

import models
import unittest
from models.base_model import BaseModel
from datetime import datetime


class TestBaseModel(unittest.TestCase):
    ''' Test for BaseModel Ex 3'''

    def test_basemodel(self):
        '''  Test for BaseModel '''
        b1 = BaseModel()
        up = b1.updated_at
        self.assertIn(b1, models.storage.all().values())
        self.assertEqual(datetime, type(b1.created_at))
        self.assertEqual(datetime, type(b1.updated_at))
        self.assertEqual(dict, type(b1.to_dict()))
        self.assertEqual(str, type(b1.id))
        prin = "[{}] ({}) {}".format(
            b1.__class__.__name__,
            b1.id,
            b1.__dict__
        )
        self.assertEqual(prin, str(b1))
        b1.save()
        self.assertNotEqual(up, b1.updated_at)

    ''' Test for BaseModel Ex 3'''

    def test_basemodels(self):
        ''' Test for 2 classes BaseModel '''
        b1 = BaseModel()
        b2 = BaseModel()
        self.assertNotEqual(b1.id, b2.id)
        self.assertNotEqual(b1.created_at, b2.created_at)
        self.assertNotEqual(b1.updated_at, b2.updated_at)

    ''' Test for BaseModel Ex 4 '''

    def test_basemodelkwargs(self):
        ''' Test for the class with/out kwargs '''
        

if __name__ == '__main__':
    unittest.main()
