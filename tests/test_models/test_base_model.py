#!/usr/bin/env python3
# test_base_model.py
"""Unit test for BaseModel class."""
import unittest
from datetime import datetime
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage


class TestBaseModel(unittest.TestCase):
    """
    TestBaseModel class contains unit tests for the BaseModel class.
    """

    def setUp(self):
        """
        Set up test fixtures and instantiate objects needed for each test case.
        """
        self.base_model = BaseModel()
        self.file_path = "test_file.json"
        self.storage = FileStorage()
        self.storage._FileStorage__file_path = self.file_path

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

    def test_file_storage_integration(self):
        """
        Test the integration with FileStorage.
        """
        # Create a new object
        obj = self.base_model

        # Save the object
        obj.save()

        # Reload the storage
        self.storage.reload()

        # Check if the object is correctly stored and reloaded from
        # the FileStorage
        self.assertIn("BaseModel.{}".format(obj.id), self.storage.all())
        reloaded_obj = self.storage.all()["BaseModel.{}".format(obj.id)]
        self.assertEqual(obj.id, reloaded_obj.id)
        self.assertEqual(obj.created_at, reloaded_obj.created_at)
        self.assertEqual(obj.updated_at, reloaded_obj.updated_at)


if __name__ == '__main__':
    unittest.main()
