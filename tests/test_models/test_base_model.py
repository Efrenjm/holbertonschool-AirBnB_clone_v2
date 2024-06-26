#!/usr/bin/python3
""" Unittest for the base_model class """
import os
import json
from unittest.mock import patch
import MySQLdb
import unittest
import datetime
from models import storage
from models.base_model import BaseModel


class test_basemodel(unittest.TestCase):
    """ Test class basemodel"""

    def __init__(self, *args, **kwargs):
        """ Test basemodel instantiation"""
        super().__init__(*args, **kwargs)
        self.name = 'BaseModel'
        self.value = BaseModel

    def setUp(self):
        """ Test set up """
        pass

    def tearDown(self):
        """Test removing json file or closing database connection"""
        pass

    def test_default(self):
        """ Test default value type """
        i = self.value()
        self.assertEqual(type(i), self.value)

    def test_kwargs(self):
        """ Test if different ids"""
        i = self.value()
        copy = i.to_dict()
        new = self.value(**copy)
        self.assertFalse(new is i)

    def test_kwargs_int(self):
        """ Test kwargs type"""
        i = self.value()
        copy = i.to_dict()
        copy.update({1: 2})
        with self.assertRaises(TypeError):
            new = self.value(**copy)

    def test_save(self):
        """ Testing save """
        i = self.value()
        key = self.name + "." + i.id
        if os.getenv('HBNB_TYPE_STORAGE') == 'db':
            with patch('models.storage') as mock:
                i.save()
                mock.new.assert_called()
                mock.save.assert_called()
        else:
            i.save()
            try:
                with open('file.json', 'r') as f:
                    j = json.load(f)
                    self.assertEqual(j[key], i.to_dict())
            except FileNotFoundError:
                pass

    def test_str(self):
        """ Test displaying of str """
        i = self.value()
        self.assertEqual(str(i), '[{}] ({}) {}'.format(self.name, i.id,
                         i.__dict__))

    def test_to_dict(self):
        """ Test if same when assigned to variable """
        i = self.value()
        n = i.to_dict()
        self.assertEqual(i.to_dict(), n)

    def test_to_dict_output(self):
        i = self.value()
        i.name = "Test Model"
        d = i.to_dict()
        self.assertIsInstance(d, dict)
        self.assertEqual(d["__class__"], self.name)
        self.assertEqual(d["name"], "Test Model")
        self.assertIsInstance(d["created_at"], str)
        self.assertIsInstance(d["updated_at"], str)

    def test_kwargs_none(self):
        """ Test with no arguments """
        n = {None: None}
        with self.assertRaises(TypeError):
            new = self.value(**n)

    def test_kwargs_one(self):
        """ Test with one key-value argument"""
        n = {'name': 'Test Object'}
        new = self.value(**n)
        self.assertIsInstance(new, self.value)
        self.assertEqual(new.name, 'Test Object')

    def test_id(self):
        """ Test id type """
        new = self.value()
        self.assertEqual(type(new.id), str)

    def test_created_at(self):
        """ Test date type"""
        new = self.value()
        self.assertEqual(type(new.created_at), datetime.datetime)

    def test_updated_at(self):
        """ Test date type """
        if os.getenv('HBNB_TYPE_STORAGE') != 'db':
            new = self.value()
            self.assertEqual(type(new.updated_at), datetime.datetime)
            n = new.to_dict()
            new = self.value(**n)


if __name__ == '__main__':
    unittest.main()
