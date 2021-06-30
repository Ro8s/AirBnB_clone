#!/usr/bin/python3
''' Unittest for Place '''

import models
import unittest
from models.base_model import BaseModel
from datetime import datetime
from models.place import Place


class TestUser(unittest.TestCase):
    ''' Test for Place'''

    def test_user(self):
        '''  Test for User '''
        p = Place()
        self.assertEqual(str, type(p.city_id))
        self.assertEqual(str, type(p.user_id))
        self.assertEqual(str, type(p.name))
        self.assertEqual(int, type(p.number_rooms))
        self.assertEqual(int, type(p.number_bathrooms))
        self.assertEqual(int, type(p.max_guest))
        self.assertEqual(int, type(p.price_by_night))
        self.assertEqual(float, type(p.latitude))
        self.assertEqual(float, type(p.longitude))
        self.assertEqual(list, type(p.amenity_ids))

if __name__ == '__main__':
    unittest.main()
