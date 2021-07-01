#!/usr/bin/python3
''' Unittest for FileStorage '''

import models
import unittest
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
from datetime import datetime
import pep8
from os import path


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
        f = path.exists('file.json')
        self.assertTrue(f)
        b2 = BaseModel("a")
        b2.save()
        self.assertNotEqual(b2, models.storage.all())
        my_model = FileStorage()
        self.assertIsInstance(my_model, FileStorage)

    ''' Test pep8 '''

    def test_pep8_conformance(self):
        ''' Test for pep8 '''
        pep8s = pep8.StyleGuide(quiet=True)
        result = pep8s.check_files(['models/engine/file_storage.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")

if __name__ == '__main__':
    unittest.main()
