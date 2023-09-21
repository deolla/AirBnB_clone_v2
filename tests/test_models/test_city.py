#!/usr/bin/python3o
""" """
from models.city import City
from datetime import datetime
import models
import inspect
from models import city
from models.base_model import BaseModel
import pycodestyle
from os import getenv
import unittest
City = city.City


class TestCityDocs(unittest.TestCase):
    """Tests documentation and style of City"""
    @classmethod
    def setUpClass(cls):
        """Set doc tests"""
        cls.pop = inspect.getmembers(City, inspect.isfunction)

    def test_pep8_conformance_city(self):
        """Test models/city.py"""
        pep = pycodestyle.StyleGuide(quiet=True)
        result = pep.check_files(['models/city.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")

    def test_pep8_conformance_test_city(self):
        """Test tests/test_models/test_city.py"""
        pep = pycodestyle.StyleGuide(quiet=True)
        result = pep.check_files(['tests/test_models/test_city.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")

    def test_city_module_docstring(self):
        """Test for the city.py module docstring"""
        self.assertIsNot(city.__doc__, None,
                         "city.py needs a docstring")
        self.assertTrue(len(city.__doc__) >= 1,
                        "city.py needs a docstring")

    def test_city_class_doc(self):
        """Test City class docstring"""
        self.assertIsNot(City.__doc__, None,
                         "City class needs a docstring")
        self.assertTrue(len(City.__doc__) >= 1,
                        "City class needs a docstring")

    def test_city_func_doc(self):
        """Test fuction docstrings in City"""
        for i in self.pop:
            self.assertIsNot(i[1].__doc__, None,
                             "{:s} method needs a docstring".format(i[0]))
            self.assertTrue(len(i[1].__doc__) >= 1,
                            "{:s} method needs a docstring".format(i[0]))


class TestCity(unittest.TestCase):
    """Test the City class"""
    def test_is_subclass(self):
        """Test City as subclass of BaseModel"""
        lop = City()
        self.assertIsInstance(lop, BaseModel)
        self.assertTrue(hasattr(lop, "id"))
        self.assertTrue(hasattr(lop, "created_at"))
        self.assertTrue(hasattr(lop, "updated_at"))

    def test_state_id_attr(self):
        """Test City has attribute and empty string"""
        city = City()
        self.assertTrue(hasattr(city, "state_id"))
        if models.storage_type == 'db':
            self.assertEqual(city.state_id, None)
        else:
            self.assertEqual(city.state_id, "")

    def test_to_dict_creates(self):
        """test to_dict method"""
        lop = City()
        n = lop.to_dict()
        self.assertEqual(type(n), dict)
        self.assertFalse("_sa_instance_state" in n)
        for attr in lop.__dict__:
            if attr != "_sa_instance_state":
                self.assertTrue(attr in n)
        self.assertTrue("__class__" in n)

    def test_to_dict_values(self):
        """test values in dict """
        date = "%Y-%m-%dT%H:%M:%S.%f"
        lop = City()
        n = lop.to_dict()
        self.assertEqual(n["__class__"], "City")
        self.assertEqual(type(n["created_at"]), str)
        self.assertEqual(type(n["updated_at"]), str)
        self.assertEqual(n["created_at"], lop.created_at.strftime(date))
        self.assertEqual(n["updated_at"], lop.updated_at.strftime(date))

    def test_str(self):
        """test str method"""
        i = City()
        string = "[City] ({}) {}".format(i.id, i.__dict__)
        self.assertEqual(string, str(i))
