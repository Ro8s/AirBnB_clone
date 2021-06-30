#!/usr/bin/python3
''' Unittest for Review '''

import models
import unittest
from models.base_model import BaseModel
from datetime import datetime
from models.review import Review


class TestReview(unittest.TestCase):
    ''' Test for Review'''

    def test_review(self):
        '''  Test for Review '''
        r = Review()
        self.assertEqual(str, type(r.place_id))
        self.assertEqual(str, type(r.user_id))
        self.assertEqual(str, type(r.text))

if __name__ == '__main__':
    unittest.main()
