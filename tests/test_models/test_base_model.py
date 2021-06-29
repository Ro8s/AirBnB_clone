#!/usr/bin/python3
''' Unittest for BaseModel '''

import models
import unittest
from models.base_model import BaseModel
from datetime import datetime


class TestBaseModel(unittest.TestCase):
    ''' Test for BaseModel '''

    def test_basemodel(self):
        '''  Test for BaseModel ''' 
        b1 = BaseModel()
        self.assertIn(b1, models.storage.all().values())
        self.assertEqual(datetime, type(b1.created_at))
        self.assertEqual(datetime, type(b1.updated_at))
        self.assertEqual(dict, type(b1.to_dict()))

    ''' Test for BaseModel '''

    def test_basemodels(self):
        ''' Test for 2 classes BaseModel '''
        b1 = BaseModel()
        b2 = BaseModel()
        self.assertNotEqual(b1.id, b2.id)
        self.assertNotEqual(b1.created_at, b2.created_at)
        self.assertNotEqual(b1.created_at, b2.created_at)

if __name__ == '__main__':
    unittest.main()
