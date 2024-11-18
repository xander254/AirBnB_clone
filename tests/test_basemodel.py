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

    def test_init_with_kwargs(self):
        """test init with dict"""
        data = {
            "id": "1234-5678",
            "created_at": "2024-11-17T10:00:00.000000",
            "updated_at": "2024-11-17T10:10:00.000000",
            "name": "MyBaseModel"
        }
        instance = BaseModel(**data)

        self.assertEqual(instance.id, "1234-5678")
        self.assertEqual(instance.name, "MyBaseModel")
        self.assertIsInstance(instance.created_at, datetime)
        self.assertIsInstance(instance.updated_at, datetime)

    def test_ignore_class_key_in_kwargs(self):
        """test ingonre __class__ key"""
        data = {
            "__class__": "BaseModel",
            "id": "9876-5432",
            "created_at": "2024-11-17T10:00:00.000000",
            "updated_at": "2024-11-17T10:10:00.000000"
        }
        instance = BaseModel(**data)

        self.assertEqual(instance.id, "9876-5432")
        #self.assertFalse(hasattr(instance, "__class__"))

    def test_default_init(self):
        """test default init"""
        instance = BaseModel()
        
        self.assertIsNotNone(instance.id)
        self.assertIsInstance(instance.created_at, datetime)
        self.assertIsInstance(instance.updated_at, datetime)

    def test_creatd_at_coversion(self):
        """test conversion of created_at to iso formating"""
        data = {"created_at": "2024-11-18T04:35:15.253643"}

        instance = BaseModel(**data)

        self.assertIsInstance(instance.created_at, datetime)
        self.assertEqual(instance.created_at.isoformat(), "2024-11-18T04:35:15.253643")



if __name__ == '__main__':
    unittest.main()
