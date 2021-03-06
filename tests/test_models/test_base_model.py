"""Test cases for base_module class."""
import unittest
import pep8
from models.base_model import BaseModel
from datetime import datetime


class TestCodeFormat(unittest.TestCase):

    def test_pep8_conformance(self):
        """Test that we conform to PEP8."""
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(['models/base_model.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")

    @classmethod
    def setUpClass(cls):
        """Set up class before start testing."""
        cls.BM1 = BaseModel()
        cls.BM2 = BaseModel()

    def test_docstring(self):
        """tests class and method documentation."""
        self.assertIsNotNone(BaseModel.__doc__)
        self.assertIsNotNone(BaseModel.__init__.__doc__)
        self.assertIsNotNone(BaseModel.__str__.__doc__)
        self.assertIsNotNone(BaseModel.save.__doc__)
        self.assertIsNotNone(BaseModel.to_dict.__doc__)

    def test_BaseModelinit(self):
        """tests for __init__ of BaseModel."""
        cls = type(self)

        self.assertIsNot(cls.BM1, cls.BM2)
        self.assertIsInstance(cls.BM1, BaseModel)
        self.assertIsInstance(cls.BM2, BaseModel)

        self.assertTrue(hasattr(cls.BM1, 'id'))
        self.assertTrue(hasattr(cls.BM2, 'id'))
        self.assertTrue(hasattr(cls.BM1, 'created_at'))
        self.assertTrue(hasattr(cls.BM2, 'created_at'))
        self.assertTrue(hasattr(cls.BM1, 'updated_at'))
        self.assertTrue(hasattr(cls.BM2, 'updated_at'))

        self.assertIsInstance(cls.BM1.id, str)
        self.assertIsInstance(cls.BM2.id, str)
        self.assertIsInstance(cls.BM1.created_at, datetime)
        self.assertIsInstance(cls.BM2.created_at, datetime)
        self.assertIsInstance(cls.BM1.updated_at, datetime)
        self.assertIsInstance(cls.BM2.updated_at, datetime)

        self.assertNotEqual(cls.BM1.id, cls.BM2.id)
        self.assertNotEqual(cls.BM1.created_at, cls.BM2.created_at)
        self.assertNotEqual(cls.BM1.updated_at, cls.BM2.updated_at)

    def test_BaseMode_init_kwargs(self):
        """test kwargs argument from __init__ method."""
        cls = type(self)

        dict = {'id': '56d43177-cc5f-4d6c-a0c1-e167f8c27337',
                'created_at': '2017-09-28T21:03:54.052298',
                '__class__': 'BaseModel', 'my_number': 89,
                'updated_at': '2017-09-28T21:03:54.052302',
                'name': 'Holberton'}

        obj = BaseModel(**dict)
        self.assertTrue(hasattr(obj, 'id'))
        self.assertTrue(hasattr(obj, 'created_at'))
        self.assertTrue(hasattr(obj, 'updated_at'))
        self.assertTrue(hasattr(obj, 'my_number'))
        self.assertTrue(hasattr(obj, 'name'))

        self.assertIsInstance(obj.id, str)
        self.assertIsInstance(obj.created_at, datetime)
        self.assertIsInstance(obj.updated_at, datetime)
        self.assertIsInstance(obj.my_number, int)
        self.assertIsInstance(obj.name, str)

        self.assertEqual(obj.id,
                         '56d43177-cc5f-4d6c-a0c1-e167f8c27337')
        self.assertEqual(obj.created_at,
                         datetime(2017, 9, 28,
                                  21, 3, 54, 52298))
        self.assertEqual(obj.updated_at,
                         datetime(2017, 9, 28,
                                  21, 3, 54, 52302))
        self.assertEqual(obj.my_number, 89)
        self.assertEqual(obj.name, 'Holberton')
        self.assertNotEqual(obj.__class__, 'BaseModel')

    def test_str(self):
        """tests __str__ method of class."""
        cls = type(self)

        self.assertIsInstance(cls.BM1.__str__(), str)

    def test_save(self):
        """tests save method of BaseModel class."""
        cls = type(self)

        updated_at = cls.BM1.updated_at
        cls.BM1.save()
        self.assertNotEqual(updated_at, cls.BM1.updated_at)

    def test_to_dict(self):
        """tests to_dict method of BaseModel"""
        cls = type(self)

        dict = cls.BM1.to_dict()

        self.assertIsInstance(dict['updated_at'], str)
        self.assertIsInstance(dict['created_at'], str)

        self.assertEqual(dict['__class__'], 'BaseModel')
