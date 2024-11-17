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

    def test_unique_id(self):
        """test  uuid uniques id"""
        model0 = BaseModel()
        model1 = BaseModel()
        self.assertNotEqual(model0.id, model1.id)

    def test_save_method(self):
        """test saving"""
        model = BaseModel()
        old_updated_at = model.updated_at
        model.save()
        self.assertNotEqual(model.updated_at, old_updated_at)
        self.assertGreater(model.updated_at, old_updated_at)

    def test_to_dict(self):
        """test the conversion to dict"""
        model = BaseModel()
        model_dict = model.to_dict()
        self.assertIsInstance(model_dict, dict)
        self.assertIn('id', model_dict)
        self.assertIn('created_at', model_dict)
        self.assertIn('updated_at', model_dict)
        self.assertIn('__class__', model_dict)
        self.assertEqual(model_dict['__class__'], 'BaseModel')
        self.assertEqual(model_dict['created_at'], model.created_at.isoformat())
        self.assertEqual(model_dict['updated_at'], model.created_at.isoformat())

    def test_str_method(self):
        """Test return of string representstion"""
        model = BaseModel()
        expected_output = f"[BaseModel] ({model.id}) {model.__dict__}"
        self.assertEqual(str(model), expected_output)




if __name__ == '__main__':
    unittest.main()
