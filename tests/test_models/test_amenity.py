#!/usr/bin/python3
""" """
from os import getenv
from models import amenity
from models.amenity import Amenity
import models
from models.base_model import BaseModel
from datetime import datetime
import pycodestyle
import inspect
import unittest
Amenity = amenity.Amenity

pop_star = getenv("HBNB_TYPE_STORAGE")


class TestPEP8Amenity(unittest.TestCase):
    """Test documentaion of amenity class """
    def test_pep8_conformance_amenity(self):
        """Test that models/amenity.py conforms to PEP8."""
        pep = pycodestyle.StyleGuide(quiet=True)
        result = pep.check_files(['models/amenity.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")

    def test_pep8_conformance_test_amenity(self):
        """Test for amenity path tests/test_models/test_amenity.py"""
        pep = pycodestyle.StyleGuide(quiet=True)
        result = pep.check_files(['tests/test_models/test_amenity.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")


class TestDocAmenity(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        """Set up for the doc tests"""
        cls.pop = inspect.getmembers(Amenity, inspect.isfunction)

    def test_amenity_module_docstring(self):
        """Test for amenity.py module docstring"""
        self.assertIsNot(amenity.__doc__, None,
                         "amenity.py needs a docstring")
        self.assertTrue(len(amenity.__doc__) >= 1,
                        "amenity.py needs a docstring")

    def test_amenity_class_docstring(self):
        """Test for Amenity class docstring"""
        self.assertIsNot(Amenity.__doc__, None,
                         "Amenity class needs a docstring")
        self.assertTrue(len(Amenity.__doc__) >= 1,
                        "Amenity class needs a docstring")

    def test_amenity_func_docstrings(self):
        """Test for the presence of docstrings in Amenity methods"""
        for func in self.pop:
            self.assertIsNot(func[1].__doc__, None,
                             "{:s} method needs a docstring".format(func[0]))
            self.assertTrue(len(func[1].__doc__) >= 1,
                            "{:s} method needs a docstring".format(func[0]))


class TestAmenity(unittest.TestCase):
    """Test for Amenity class"""
    def test_name_attr(self):
        """Test amenity as a subclass of basemodel"""
        i = Amenity()
        self.assertTrue(hasattr(i, "name"))
        if pop_star == 'db':
            self.assertEqual(i.name, None)
        else:
            self.assertEqual(i.name, "")

    def test_name_attr(self):
        """Test that Amenity has attribute name, and it's as an empty string"""
        amenity = Amenity()
        self.assertTrue(hasattr(amenity, "name"))
        if pop_star == 'db':
            self.assertEqual(amenity.name, None)
        else:
            self.assertEqual(amenity.name, "")

    def test_to_dict_creates_dict(self):
        """test to_dict method creates a dictionary with proper attrs"""
        am = Amenity()
        print(am.__dict__)
        new_d = am.to_dict()
        self.assertEqual(type(new_d), dict)
        self.assertFalse("_sa_instance_state" in new_d)
        for attr in am.__dict__:
            if attr is not "_sa_instance_state":
                self.assertTrue(attr in new_d)
        self.assertTrue("__class__" in new_d)

    def test_str(self):
        """test if method has the correct output"""
        amenity = Amenity()
        string = "[Amenity] ({}) {}".format(amenity.id, amenity.__dict__)
        self.assertEqual(string, str(amenity))
