#!/usr/bin/python3
''' Unittest for FileStorage '''

import models
import unittest
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
from datetime import datetime


class TestFileStorage(unittest.TestCase):
    ''' Test for Storage Ex 5'''

    def test_filestorage(self):
        '''  Test for FileStorage '''
        b1 = BaseModel()
        f1 = FileStorage()
        di = {}
        b1.save()
        self.assertNotEqual(di, models.storage.all())
        self.assertEqual(str, type(f1._FileStorage__file_path))
        self.assertEqual(dict, type(f1._FileStorage__objects))

if __name__ == '__main__':
    unittest.main()
