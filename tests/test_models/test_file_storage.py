#!/usr/bin/env python3
# test_file_storage.py
"""Unit test for FileStorage class."""
import unittest
import os
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel


class FileStorageTestCase(unittest.TestCase):
    """
    TestFileStorage class contains unit test for the FileStorage class.
    """
    def setUp(self):
        """
        Set up test fixtures and instantiation objects needed for each test case.
        """
        # Create an instance of FileStorage
        self.storage = FileStorage()
        self.base_model = BaseModel()
        self.base_model.save()
        # Clear any existing objects
        # self.storage._FileStorage__objects = {}

    def tearDown(self):
        """
        Clean up afer each test case.
        """
        self.storage.__objects = {}
        # Delete the test file if it exists
        if os.path.exists(self.storage._FileStorage__file_path):
            os.remove(self.storage._FileStorage__file_path)

    def test_all(self):
        """
        Test the all method of the FileStorage class.
        """
        objs = self.storage.all()
        self.assertEqual(type(objs), dict)

    def test_new(self):
        """
        Test the new method of the FileStorage class.
        """
        obj_id = self.base_model.id
        self.assertIn("BaseModel.{}".format(obj_id), self.storage.all())

    def test_save(self):
        """
        Test the save method of the FileStorage class.
        """
        obj_id = self.base_model.id
        self.storage.save()
        self.assertTrue(os.path.exists(self.storage._FileStorage__file_path))

        with open(self.storage._FileStorage__file_path, 'r') as file:
            file_data = file.read()

        self.assertIn("BaseModel.{}".format(obj_id), file_data)

    def test_reload(self):
        """
        Test the reload method of the FileStorage class.
        """
        obj_id = self.base_model.id
        self.storage.save()

        # Modify the file to simulate changes
        with open(self.storage._FileStorage__file_path, 'w') as file:
            file.write('{"BaseModel.123": {"__class__": "BaseModel", "id": "123"}}')

        self.storage.reload()
        objs = self.storage.all()
        self.assertIn("BaseModel.{}".format(obj_id), objs)
        self.assertNotIn("BaseModel.123", objs)


if __name__ == '__main__':
    unittest.main()
