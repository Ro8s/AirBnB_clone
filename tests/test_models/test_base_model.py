#!/usr/bin/python3
''' Unittest for BaseModel '''

import models
import unittest
from models.base_model import BaseModel


class TestBaseModel(unittest.TestCase):
    ''' Test for BaseModel '''

    def TestBaseModelex3(self):
        '''  Test for BaseModel ''' 
        b1 = BaseModel()
        self.assertIn(b1, models.storage.all().values())

        ''' DIEGOTE '''
    def TestBaseModelex31(self):
        ''' Test for BaseModel '''
        b1 = BaseModel() 
        self.assertEqual(datetime, type(b1.created_at))


if __name__ == '__main__':
    unittest.main()
