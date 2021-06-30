#!/usr/bin/python3
''' Unittest for State '''

import models
import unittest
from models.base_model import BaseModel
from datetime import datetime
from models.state import State


class TestState(unittest.TestCase):
    ''' Test for State'''

    def test_user(self):
        '''  Test for State '''
        s = State()
        self.assertEqual(str, type(s.name))

if __name__ == '__main__':
    unittest.main()
