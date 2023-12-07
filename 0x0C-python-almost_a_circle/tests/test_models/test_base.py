#!/usr/bin/python3
"""Module for testing the Base class."""
import unittest
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class TestBaseMethods(unittest.TestCase):
    """Test cases for the Base class."""

    def setUp(self):
        """Set up method to initialize test cases."""
        Base._Base__nb_objects = 0
        pass

    def tearDown(self):
        """Tear down method to clean up after each test case."""
        pass

    def test_has_attr(self):
        """Test case for checking if __nb_objects is private in Base class."""
        self.assertTrue(hasattr(Base, "_Base__nb_objects"))

    def test_nb_objects_initialized(self):
        """Test case for checking if __nb_objects is initialized to 0"""
        self.assertEqual(getattr(Base, "_Base__nb_objects"), 0)

    def test_instantiation(self):
        """Test case for checking instantiation of Base class."""
        c = Base()
        self.assertEqual(str(type(c)), "<class 'models.base.Base'>")
        self.assertEqual(c.__dict__, {"id": 1})
        self.assertEqual(c.id, 1)

    def test_constructor_with_args(self):
        """Test case for checking constructor of Base class."""
        with self.assertRaises(TypeError) as s:
            Base.__init__()
        me = "__init__() missing 1 required positional argument: 'self'"
        self.assertEqual(str(s.exception), me)

    def test_constructor_with_two_args(self):
        """Test case for checking constructor with 2 arguments"""
        with self.assertRaises(TypeError) as s:
            Base.__init__(self, 1, 2)
        me = "__init__() takes from 1 to 2 positional arguments but 3 \
were given"
        self.assertEqual(str(s.exception), me)

    def test_consecutive_ids(self):
        """Test case for checking consecutive ids in Base class."""
        c1 = Base()
        c2 = Base()
        self.assertEqual(c1.id + 1, c2.id)

    def test_id_synchronization(self):
        """Test case for checking id synchronization in Base class."""
        c = Base()
        self.assertEqual(getattr(Base, "_Base__nb_objects"), c.id)

    def test_id_synchronization_with_more_instances(self):
        """Test case for checking id synchronization with more instances"""
        c = Base()
        c = Base("Foo")
        c = Base(98)
        c = Base()
        self.assertEqual(getattr(Base, "_Base__nb_objects"), c.id)

    def test_custom_id_with_int(self):
        """Test case for checking custom id with int in Base class."""
        ii = 98
        c = Base(ii)
        self.assertEqual(c.id, ii)

    def test_custom_id_with_str(self):
        """Test case for checking custom id with str in Base class"""
        ii = "FooBar"
        c = Base(ii)
        self.assertEqual(c.id, ii)

    def test_id_with_keyword_argument(self):
        """Test case for checking id with keyword argument"""
        ii = 421
        c = Base(id=ii)
        self.assertEqual(c.id, ii)

    def test_to_json_string_error(self):
        """Test case for checking to_json_string method in Base class."""
        with self.assertRaises(TypeError) as es:
            Base.to_json_string()
        m = "to_json_string() missing 1 required positional argument: \
'list_dictionaries'"
        self.assertEqual(str(es.exception), m)

        self.assertEqual(Base.to_json_string(None), "[]")
        self.assertEqual(Base.to_json_string([]), "[]")
        c = [{'x': 111, 'y': 20456, 'width': 321123, 'id': 533355,
             'height': 35350}]
        self.assertEqual(len(Base.to_json_string(c)),
                         len(str(c)))
        c = [{'x': 4, 'y': 5, 'width': 6, 'id': 7, 'height': 8}]
        self.assertEqual(len(Base.to_json_string(c)),
                         len(str(c)))
        c = [{"soosarrooo": 909090}]
        self.assertEqual(Base.to_json_string(c),
                         '[{"soosarrooo": 909090}]')

        c = [{"soosarrooo": 909090}, {"def": 456}, {"HI": 0}]
        self.assertEqual(Base.to_json_string(c),
                         '[{"soosarrooo": 909090}, {"def": 456}, {"HI": 0}]')

        c = [{'x': 1, 'y': 2, 'width': 3, 'id': 4, 'height': 5},
             {'x': 101, 'y': 20123, 'width': 312321, 'id': 522244,
             'height': 34340}]
        self.assertEqual(len(Base.to_json_string(c)),
                         len(str(c)))
        c = [{}]
        self.assertEqual(Base.to_json_string(c),
                         '[{}]')
        c = [{}, {}]
        self.assertEqual(Base.to_json_string(c),
                         '[{}, {}]')

        m1 = Rectangle(11, 8, 3, 9)
        dic = m1.to_dictionary()
        js_dic = Base.to_json_string([dic])
        dic = str([dic])
        dic = dic.replace("'", '"')
        self.assertEqual(dic, js_dic)

        m1 = Rectangle(10, 7, 2, 8)
        m2 = Rectangle(1, 2, 3, 4)
        m3 = Rectangle(2, 3, 4, 5)
        dic = [m1.to_dictionary(), m2.to_dictionary(),
               m3.to_dictionary()]
        js_dic = Base.to_json_string(dic)
        dic = str(dic)
        dic = dic.replace("'", '"')
        self.assertEqual(dic, js_dic)

        m1 = Square(11, 8, 3)
        dic = m1.to_dictionary()
        js_dic = Base.to_json_string([dic])
        dic = str([dic])
        dic = dic.replace("'", '"')
        self.assertEqual(dic, js_dic)

        m1 = Square(11, 8, 3)
        m2 = Square(5, 3, 4)
        m3 = Square(3, 4, 5)
        dic = [m1.to_dictionary(), m2.to_dictionary(),
               m3.to_dictionary()]
        js_dic = Base.to_json_string(dic)
        dic = str(dic)
        dic = dic.replace("'", '"')
        self.assertEqual(dic, js_dic)

    def test_from_json_string_error(self):
        """Test case for checking from_json_string"""
        with self.assertRaises(TypeError) as c:
            Base.from_json_string()
        t = "from_json_string() missing 1 required positional argument: \
'json_string'"
        self.assertEqual(str(c.exception), t)

        self.assertEqual(Base.from_json_string(None), [])
        self.assertEqual(Base.from_json_string(""), [])

        ss = '[{"x": 1, "y": 2, "width": 3, "id": 4, "height": 5}, \
{"x": 101, "y": 20123, "width": 312321, "id": 522244, "height": 34340}]'
        m = [{'x': 1, 'y': 2, 'width': 3, 'id': 4, 'height': 5},
             {'x': 101, 'y': 20123, 'width': 312321, 'id': 522244,
             'height': 34340}]
        self.assertEqual(Base.from_json_string(ss), m)

        m = [{}, {}]
        ss = '[{}, {}]'
        self.assertEqual(Base.from_json_string(ss), m)
        m = [{}]
        ss = '[{}]'
        self.assertEqual(Base.from_json_string(ss), m)

        m = [{"soosarrooo": 909090}, {"def": 456}, {"HI": 0}]
        ss = '[{"soosarrooo": 909090}, {"def": 456}, {"HI": 0}]'
        self.assertEqual(Base.from_json_string(ss), m)

        m = [{"soosarrooo": 909090}]
        ss = '[{"soosarrooo": 909090}]'
        self.assertEqual(Base.from_json_string(ss), m)

        m = [{'x': 1, 'y': 2, 'width': 3, 'id': 4, 'height': 5}]
        ss = '[{"x": 1, "y": 2, "width": 3, "id": 4, "height": 5}]'
        self.assertEqual(Base.from_json_string(ss), m)

        m = [{'x': 101, 'y': 20123, 'width': 312321, 'id': 522244,
             'height': 34340}]
        ss = '[{"x": 101, "y": 20123, "width": 312321, "id": 522244, \
"height": 34340}]'
        self.assertEqual(Base.from_json_string(ss), m)

        li_in = [
            {'id': 89, 'width': 10, 'height': 4},
            {'id': 7, 'width': 1, 'height': 7}
        ]
        li_out = Rectangle.from_json_string(
            Rectangle.to_json_string(li_in))
        self.assertEqual(li_in, li_out)

    def test_save_to_file(self):
        """Test case for checking save_to_file method in Base class."""
        import os
        m1 = Rectangle(11, 8, 3, 9)
        m2 = Rectangle(3, 5)
        Rectangle.save_to_file([m1, m2])

        with open("Rectangle.json", "r") as f:
            self.assertEqual(len(f.read()), 105)

        Rectangle.save_to_file(None)
        with open("Rectangle.json", "r") as f:
            self.assertEqual(f.read(), "[]")

        try:
            os.remove("Rectangle.json")
        except:
            pass
        Rectangle.save_to_file([])
        with open("Rectangle.json", "r") as f:
            self.assertEqual(f.read(), "[]")

        m2 = Rectangle(3, 5)
        Rectangle.save_to_file([m2])
        with open("Rectangle.json", "r") as f:
            self.assertEqual(len(f.read()), 52)

        Square.save_to_file(None)
        with open("Square.json", "r") as f:
            self.assertEqual(f.read(), "[]")

        try:
            os.remove("Square.json")
        except:
            pass
        Square.save_to_file([])
        with open("Square.json", "r") as f:
            self.assertEqual(f.read(), "[]")

        m2 = Square(1)
        Square.save_to_file([m2])
        with open("Square.json", "r") as f:
            self.assertEqual(len(f.read()), 38)

    def test_create_method(self):
        """Test case for checking create method in Base class."""
        m1 = Rectangle(4, 6, 2)
        m1_dic = m1.to_dictionary()
        m2 = Rectangle.create(**m1_dic)
        self.assertEqual(str(m1), str(m2))
        self.assertFalse(m1 is m2)
        self.assertFalse(m1 == m2)

    def test_load_from_file(self):
        """Test case for checking load_from_file method in Base class."""
        m1 = Rectangle(11, 8, 3, 9)
        m2 = Rectangle(3, 5)
        li_in = [m1, m2]
        Rectangle.save_to_file(li_in)
        li_out = Rectangle.load_from_file()
        self.assertNotEqual(id(li_in[0]), id(li_out[0]))
        self.assertEqual(str(li_in[0]), str(li_out[0]))
        self.assertNotEqual(id(li_in[1]), id(li_out[1]))
        self.assertEqual(str(li_in[1]), str(li_out[1]))

        c1 = Square(5)
        c2 = Square(7, 9, 1)
        li_in = [c1, c2]
        Square.save_to_file(li_in)
        li_out = Square.load_from_file()
        self.assertNotEqual(id(li_in[0]), id(li_out[0]))
        self.assertEqual(str(li_in[0]), str(li_out[0]))
        self.assertNotEqual(id(li_in[1]), id(li_out[1]))
        self.assertEqual(str(li_in[1]), str(li_out[1]))


if __name__ == "__main__":
    unittest.main()
