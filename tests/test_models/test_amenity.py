#!/usr/bin/python3
''' Unittest for Amenity '''

import models
import unittest
from models.base_model import BaseModel
from datetime import datetime
from models.amenity import Amenity


class TestAmenity(unittest.TestCase):
    ''' Test for User'''

    def test_amenity(self):
        '''  Test for Amenity '''
        a = Amenity()
        self.assertEqual(str, type(a.name))

        
if __name__ == '__main__':
    unittest.main()
