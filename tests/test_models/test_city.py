#!/usr/bin/python3
''' Unittest for City '''

import models
import unittest
from models.base_model import BaseModel
from datetime import datetime
from models.city import City


class TestCity(unittest.TestCase):
    ''' Test for City '''

    def test_city(self):
        '''  Test for City '''
        c = City()
        self.assertEqual(str, type(c.state_id))
        self.assertEqual(str, type(c.name))

if __name__ == '__main__':
    unittest.main()
