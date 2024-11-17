#!/usr/bin/python3
"""Test the base model class"""
import unittest
from models.base_model import BaseModel
from datetime import datetime



class TestBaseModel(unittest.TestCase):
    """Test methods"""
    def test_initialization(self):
        """test base model initialization"""
        model = BaseModel()
        self.assertIsInstance(model.id, str)
        self.assertIsInstance(model.created_at, datetime)
        self.assertIsInstance(model.updated_at, datetime)
        self.assertEqual(model.created_at, model.updated_at)



if __name__ == '__main__':
    unittest.main()
