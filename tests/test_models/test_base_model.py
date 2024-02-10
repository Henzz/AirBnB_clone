#!/usr/bin/env python3
# test_base_model.py
"""Unit test for BaseModel class."""
import unittest
import models.base_mode import BaseModel
import models.engine.file_storage import FileStorage


class TestBaseModel(unittest.TestCase):
    """
    TestBaseModel class contains unit tests for the BaseModel class.
    """

    def setUp(self):
        """
        Set up test fixtures and instantiate objects needed for each test case.
        """
        self.base_model = BaseModel()

    def tearDown(self):
        """
        Clean up after each test case.
        """
        FileStorage.__objects = {}

    def test_attributes(self):
        """
        Test the attributes of the BaseModel class.
        """
        self.assertTrue(hasattr(self.base_model, 'id'))
        self.assertIsInstance(self.base_model.id, str)
        self.assertTrue(hasattr(self.base_model, 'created_at'))
        self.assertIsInstance(self.base_model.created_at, datetime)
        self.assertTrue(hasattr(self.base_model, 'updated_at'))
        self.assertIsInstance(self.base_model.updated_at, datetime)

    def test_save(self):
        """
        Test the save method of the BaseModel class.
        """
        old_updated_at = self.base_model.updated_at
        self.base_model.save()
        self.assertNotEqual(old_updated_at, self.base_model.updated_at)

    def test_to_dict(self):
        """
        Test the to_dict method of the BaseModel class.
        """
        obj_dict = self.base_model.to_dict()
        self.assertIsInstance(obj_dict, dict)
        self.assertEqual(obj_dict['__class__'], 'BaseModel')
        self.assertEqual(type(obj_dict['created_at']), str)
        self.assertEqual(type(obj_dict['updated_at']), str)
        # self.assertEqual(data['created_at'], model.created_at.isoformat())
        # self.assertEqual(data['updated_at'], model.updated_at.isoformat())

    def test_file_storage(self):
        """
        Test the integration of the BaseModel class with the FileStorage class.
        """
        storage = FileStorage()
        storage.new(self.base_model)
        storage.save()
        storage.reload()
        all_objects = storage.all()
        self.assertEqual(len(all_objects), 1)
        loaded_model = all_objects['BaseModel.' + self.base_model.id]
        self.assertEqual(loaded_model.id, self.base_model.id)
        self.assertEqual(loaded_model.created_at, self.base_model.created_at)
        self.assertEqual(loaded_model.updated_at, self.base_model.updated_at)


if __name__ == '__main__':
    unittest.main()
