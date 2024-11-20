#!/usr/bin/python3
"""test file storage"""
import unittest
import os
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage


class TestFileStorage(unittest.TestCase):
    """test file storage"""
    def setUp(self):
        """set up clean envv for tests"""
        self.storage = FileStorage()
        self.base_model = BaseModel()
        self.file_path = "file.json"

    def teardown(self):
        """clean up"""
        if os.path.exists(self.file_path):
            os.remove(self.file_path)

    def test_all(self):
        """test all method returns a dictionary"""
        self.storage.new(self.base_model)
        self.storage.save()
        self.assertTrue(os.path.exists(self.file_path))

    def test_reload(self):
        """test reload to restore objects from a file"""
        self.storage.new(self.base_model)
        self.storage.save()
        self.storage._FileStorage__objects.clear()
        self.storage.reload()
        key = f"BaseModel.{self.base_model.id}"
        self.assertIn(key, self.storage.all())


if __name__ == "__main__":
    unittest.main()
