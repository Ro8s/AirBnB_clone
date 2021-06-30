#!/usr/bin/python3
''' Unittest for User '''

import models
import unittest
from models.base_model import BaseModel
from datetime import datetime
from models.user import User


class TestUser(unittest.TestCase):
    ''' Test for User'''

    def test_user(self):
        '''  Test for User '''
        u = User()
        self.assertEqual(str, type(u.email))
        self.assertEqual(str, type(u.password))
        self.assertEqual(str, type(u.first_name))
        self.assertEqual(str, type(u.last_name))

if __name__ == '__main__':
    unittest.main()
