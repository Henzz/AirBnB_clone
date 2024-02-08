#!/usr/bin/env python3
"""Unit test for BaseModel class."""
import unittest
import models.base_mode import BaseModel


class TestBaseModel(unittest.TestCase):
    def test_attributes(self):
        model = BaseModel()
        self.assertIsInstance(model.id, str)
        self.assertIsInstance(model.created_at, datetime)
        self.assertIsInstance(model.updated_at, datetime)

    def test_save(self):
        model = BaseModel()
        initial_updated_at = model.updated_at
        model.save()
        self.assertNotEqual(model.updated_at, initial_updated_at)

    def test_to_dict(self):
        model = BaseModel()
        data = model.to_dict()
        self.assertIsInstance(data, dict)
        self.assertEqual(data['__class__'], 'BaseModel')
        self.assertEqual(data['created_at'], model.created_at.isoformat())
        self.assertEqual(data['updated_at'], model.updated_at.isoformat())


if __name__ == '__main__':
    unittest.main()
