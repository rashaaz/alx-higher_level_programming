#!/usr/bin/python3
"""Unit tests for the Square class."""
import unittest
from models.base import Base
from models.square import Square
from random import randrange
from contextlib import redirect_stdout
import io


class TestSquaremethod(unittest.TestCase):
    """Test cases for the Square class."""

    def setUp(self):
        """Set up test fixtures"""
        Base._Base__nb_objects = 0

    def tearDown(self):
        """Tear down test fixtures."""
        pass

    def test_r_class_name_me(self):
        """Test that the Square class is defined correctly"""
        self.assertEqual(str(Square),
                         "<class 'models.square.Square'>")

    def test_r_inher_me(self):
        """Test inheritance of Square from Base."""
        self.assertTrue(issubclass(Square, Base))

    def test_r_con_emty_args_me(self):
        """Test Square constructor with no arguments."""
        with self.assertRaises(TypeError) as s:
            h = Square()
        ss = "__init__() missing 1 required positional argument: 'size'"
        self.assertEqual(str(s.exception), ss)

    def test_r_con_more_args_me(self):
        """Test Square constructor with too many arguments."""
        with self.assertRaises(TypeError) as s:
            h = Square(2, 3, 4, 5, 6)
        ss = "__init__() takes from 2 to 5 positional arguments but 6 \
were given"
        self.assertEqual(str(s.exception), ss)

    def test_r_inst_me(self):
        """Test Square instantiation and validation."""
        h = Square(11)
        self.assertEqual(str(type(h)), "<class 'models.square.Square'>")
        self.assertTrue(isinstance(h, Base))
        c = {'_Rectangle__height': 11, '_Rectangle__width': 11,
             '_Rectangle__x': 0, '_Rectangle__y': 0, 'id': 1}
        self.assertDictEqual(h.__dict__, c)

        with self.assertRaises(TypeError) as s:
            h = Square("1")
        me = "width must be an integer"
        self.assertEqual(str(s.exception), me)

        with self.assertRaises(TypeError) as s:
            h = Square(2, "3")
        me = "x must be an integer"
        self.assertEqual(str(s.exception), me)

        with self.assertRaises(TypeError) as s:
            h = Square(2, 3, "4")
        me = "y must be an integer"
        self.assertEqual(str(s.exception), me)

        with self.assertRaises(ValueError) as s:
            h = Square(-1)
        me = "width must be > 0"
        self.assertEqual(str(s.exception), me)

        with self.assertRaises(ValueError) as s:
            h = Square(1, -2)
        me = "x must be >= 0"
        self.assertEqual(str(s.exception), me)

        with self.assertRaises(ValueError) as s:
            h = Square(2, 3, -4)
        me = "y must be >= 0"
        self.assertEqual(str(s.exception), me)

        with self.assertRaises(ValueError) as s:
            h = Square(0)
        me = "width must be > 0"
        self.assertEqual(str(s.exception), me)

    def test_r_inst_posit_me(self):
        """Test Square instantiation with positional arguments."""
        h = Square(6, 11, 16)
        c = {'_Rectangle__height': 6, '_Rectangle__width': 6,
             '_Rectangle__x': 11, '_Rectangle__y': 16, 'id': 1}
        self.assertEqual(h.__dict__, c)

        h = Square(6, 11, 16, 21)
        c = {'_Rectangle__height': 6, '_Rectangle__width': 6,
             '_Rectangle__x': 11, '_Rectangle__y': 16, 'id': 21}
        self.assertEqual(h.__dict__, c)

    def test_r_inst_keywo_me(self):
        """Test Square instantiation with keyword arguments."""
        h = Square(101, id=422, y=100, x=102)
        c = {'_Rectangle__height': 101, '_Rectangle__width': 101,
             '_Rectangle__x': 102, '_Rectangle__y': 100, 'id': 422}
        self.assertEqual(h.__dict__, c)

    def test_r_id_inher_me(self):
        """Test inheritance of id attribute in Square."""
        Base._Base__nb_objects = 98
        h = Square(2)
        self.assertEqual(h.id, 99)

    def test_r_prop_me(self):
        """Test Square properties."""
        h = Square(4, 8)
        h.size = 97
        h.x = 101
        h.y = 102
        c = {'_Rectangle__height': 97, '_Rectangle__width': 97,
             '_Rectangle__x': 101, '_Rectangle__y': 102, 'id': 1}
        self.assertEqual(h.__dict__, c)
        self.assertEqual(h.size, 97)
        self.assertEqual(h.x, 101)
        self.assertEqual(h.y, 102)

    def invalid_types(self):
        """Helper function to return a tuple of invalid types"""
        m = (4.15, -2.2, float('inf'), float('-inf'), True, "str", (3,),
             [5], {6}, {7: 8}, None)
        return m

    def test_r_vali_ty_me(self):
        """Test validation of attribute types in Square."""
        h = Square(1)
        att = ["x", "y"]
        for at in att:
            ss = "{} must be an integer".format(at)
            for invalid_type in self.invalid_types():
                with self.assertRaises(TypeError) as s:
                    setattr(h, at, invalid_type)
                self.assertEqual(str(s.exception), ss)
        ss = "width must be an integer"
        for invalid_type in self.invalid_types():
            with self.assertRaises(TypeError) as s:
                setattr(h, "width", invalid_type)
            self.assertEqual(str(s.exception), ss)

    def test_r_vali_val_nege_gt_me(self):
        """Test validation of negative values greater than zero"""
        h = Square(2, 3)
        att = ["size"]
        for at in att:
            ss = "width must be > 0".format(at)
            with self.assertRaises(ValueError) as s:
                setattr(h, at, -(randrange(11) + 2))
            self.assertEqual(str(s.exception), ss)

    def test_r_val_val_neg_ge_me(self):
        """Test validation of negative values greater than or equal to zero"""
        h = Square(2, 3)
        att = ["x", "y"]
        for at in att:
            ss = "{} must be >= 0".format(at)
            with self.assertRaises(ValueError) as s:
                setattr(h, at, -(randrange(11) + 2))
            self.assertEqual(str(s.exception), ss)

    def test_r_vali_val_0_me(self):
        """Test validation of values equal to zero"""
        h = Square(2, 3)
        att = ["size"]
        for at in att:
            ss = "width must be > 0".format(at)
            with self.assertRaises(ValueError) as s:
                setattr(h, at, 0)
            self.assertEqual(str(s.exception), ss)

    def test_h_prop_me(self):
        """Test validation of properties in Square."""
        h = Square(2, 3)
        att = ["x", "y", "width", "height"]
        for at in att:
            m = randrange(11) + 2
            setattr(h, at, m)
            self.assertEqual(getattr(h, at), m)

    def test_r_prop_ra_0_me(self):
        """Test validation of properties with zero values."""
        h = Square(1, 2)
        h.x = 0
        h.y = 0
        self.assertEqual(h.x, 0)
        self.assertEqual(h.y, 0)

    def test_r_ar_emty_args_me(self):
        """Test area method in Square with no arguments."""
        h = Square(6)
        with self.assertRaises(TypeError) as s:
            Square.area()
        ss = "area() missing 1 required positional argument: 'self'"
        self.assertEqual(str(s.exception), ss)

    def test_r_ar_me(self):
        """Test area method in Square."""
        h = Square(6)
        self.assertEqual(h.area(), 36)
        m = randrange(10) + 1
        h.size = m
        self.assertEqual(h.area(), m * m)
        m = randrange(10) + 1
        h = Square(m, 7, 8, 9)
        self.assertEqual(h.area(), m * m)
        m = randrange(10) + 1
        h = Square(m, y=7, x=8, id=9)
        self.assertEqual(h.area(), m * m)

        Base._Base__nb_objects = 0
        v1 = Square(5)
        self.assertEqual(str(v1), "[Square] (1) 0/0 - 5")
        self.assertEqual(v1.size, 5)
        v1.size = 10
        self.assertEqual(str(v1), "[Square] (1) 0/0 - 10")
        self.assertEqual(v1.size, 10)

        with self.assertRaises(TypeError) as s:
            v1.size = "9"
        self.assertEqual(str(s.exception), "width must be an integer")

        with self.assertRaises(ValueError) as s:
            v1.size = 0
        self.assertEqual(str(s.exception), "width must be > 0")

    def test_r_dis_emty_args_me(self):
        """Test display method in Square with no arguments."""
        h = Square(9)
        with self.assertRaises(TypeError) as s:
            Square.display()
        ss = "display() missing 1 required positional argument: 'self'"
        self.assertEqual(str(s.exception), ss)

    def test_r_dis_sim_me(self):
        """Test simple display method in Square."""
        h = Square(1)
        a = io.StringIO()
        with redirect_stdout(a):
            h.display()
        ss = "#\n"
        self.assertEqual(a.getvalue(), ss)
        h.size = 3
        a = io.StringIO()
        with redirect_stdout(a):
            h.display()
        ss = "\
###\n\
###\n\
###\n\
"
        self.assertEqual(a.getvalue(), ss)
        h = Square(5, 6, 7)
        a = io.StringIO()
        with redirect_stdout(a):
            h.display()
        ss = """\







      #####
      #####
      #####
      #####
      #####
"""
        self.assertEqual(a.getvalue(), ss)
        h = Square(9, 8)
        a = io.StringIO()
        with redirect_stdout(a):
            h.display()
        ss = """\
        #########
        #########
        #########
        #########
        #########
        #########
        #########
        #########
        #########
"""
        self.assertEqual(a.getvalue(), ss)
        h = Square(1, 1, 10)
        a = io.StringIO()
        with redirect_stdout(a):
            h.display()
        ss = """\










 #
"""
        self.assertEqual(a.getvalue(), ss)

        h = Square(5)
        a = io.StringIO()
        with redirect_stdout(a):
            h.display()
        ss = """\
#####
#####
#####
#####
#####
"""
        self.assertEqual(a.getvalue(), ss)

        h = Square(5, 5)
        a = io.StringIO()
        with redirect_stdout(a):
            h.display()
        ss = """\
     #####
     #####
     #####
     #####
     #####
"""
        self.assertEqual(a.getvalue(), ss)

        h = Square(5, 3)
        a = io.StringIO()
        with redirect_stdout(a):
            h.display()
        ss = """\
   #####
   #####
   #####
   #####
   #####
"""
        self.assertEqual(a.getvalue(), ss)

        h = Square(5, 0, 4)
        a = io.StringIO()
        with redirect_stdout(a):
            h.display()
        ss = """\




#####
#####
#####
#####
#####
"""
        self.assertEqual(a.getvalue(), ss)

        Base._Base__nb_objects = 0
        v1 = Square(5)
        self.assertEqual(str(v1), "[Square] (1) 0/0 - 5")
        self.assertEqual(v1.area(), 25)
        a = io.StringIO()
        with redirect_stdout(a):
            v1.display()
        ss = """\
#####
#####
#####
#####
#####
"""
        self.assertEqual(a.getvalue(), ss)

        v2 = Square(2, 2)
        self.assertEqual(str(v2), "[Square] (2) 2/0 - 2")
        self.assertEqual(v2.area(), 4)
        a = io.StringIO()
        with redirect_stdout(a):
            v2.display()
        ss = """\
  ##
  ##
"""
        self.assertEqual(a.getvalue(), ss)

        v3 = Square(3, 1, 3)
        self.assertEqual(str(v3), "[Square] (3) 1/3 - 3")
        self.assertEqual(v3.area(), 9)
        a = io.StringIO()
        with redirect_stdout(a):
            v3.display()
        ss = """\



 ###
 ###
 ###
"""
        self.assertEqual(a.getvalue(), ss)

    def test_r_str_emty_args_me(self):
        """Test str method in Square with no arguments."""
        h = Square(6, 3)
        with self.assertRaises(TypeError) as s:
            Square.__str__()
        ss = "__str__() missing 1 required positional argument: 'self'"
        self.assertEqual(str(s.exception), ss)

    def test_r_str_me(self):
        """Test str method in Square."""
        h = Square(5)
        ss = '[Square] (1) 0/0 - 5'
        self.assertEqual(str(h), ss)
        h = Square(1, 1)
        ss = '[Square] (2) 1/0 - 1'
        self.assertEqual(str(h), ss)
        h = Square(3, 4, 5)
        ss = '[Square] (3) 4/5 - 3'
        self.assertEqual(str(h), ss)
        h = Square(10, 20, 30, 40)
        ss = '[Square] (40) 20/30 - 10'
        self.assertEqual(str(h), ss)

    def test_r_up_empty_args_me(self):
        """Test update method in Square with no arguments"""
        h = Square(6, 3)
        with self.assertRaises(TypeError) as s:
            Square.update()
        ss = "update() missing 1 required positional argument: 'self'"
        self.assertEqual(str(s.exception), ss)

        c = h.__dict__.copy()
        h.update()
        self.assertEqual(h.__dict__, c)

    def test_r_upd_args_me(self):
        """Test update method in Square with arguments"""
        h = Square(6, 3)
        c = h.__dict__.copy()

        h.update(11)
        c["id"] = 11
        self.assertEqual(h.__dict__, c)

        h.update(11, 6)
        c["_Rectangle__height"] = 6
        c["_Rectangle__width"] = 6
        self.assertEqual(h.__dict__, c)

        h.update(11, 6, 21)
        c["_Rectangle__x"] = 21
        self.assertEqual(h.__dict__, c)

        h.update(11, 6, 21, 26)
        c["_Rectangle__y"] = 26
        self.assertEqual(h.__dict__, c)

    def test_r_upd_args_BAD_me(self):
        """Test update method in Square with invalid arguments"""
        h = Square(6, 3)
        c = h.__dict__.copy()

        h.update(11)
        c["id"] = 11
        self.assertEqual(h.__dict__, c)

        with self.assertRaises(ValueError) as s:
            h.update(11, -6)
        ss = "width must be > 0"
        self.assertEqual(str(s.exception), ss)

        with self.assertRaises(ValueError) as s:
            h.update(11, 6, -18)
        ss = "x must be >= 0"
        self.assertEqual(str(s.exception), ss)

        with self.assertRaises(ValueError) as s:
            h.update(11, 6, 18, -26)
        ss = "y must be >= 0"
        self.assertEqual(str(s.exception), ss)

    def test_r_up_kwar_me(self):
        """Test update method in Square with keyword arguments."""
        h = Square(6, 3)
        c = h.__dict__.copy()

        h.update(id=11)
        c["id"] = 11
        self.assertEqual(h.__dict__, c)

        h.update(size=18)
        c["_Rectangle__height"] = 18
        c["_Rectangle__width"] = 18
        self.assertEqual(h.__dict__, c)

        h.update(x=21)
        c["_Rectangle__x"] = 21
        self.assertEqual(h.__dict__, c)

        h.update(y=26)
        c["_Rectangle__y"] = 26
        self.assertEqual(h.__dict__, c)

    def test_r_upd_kwa_two_me(self):
        """Test update method in Square with multiple keyword arguments"""
        h = Square(6, 3)
        c = h.__dict__.copy()

        h.update(id=11)
        c["id"] = 11
        self.assertEqual(h.__dict__, c)

        h.update(id=11, size=6)
        c["_Rectangle__height"] = 6
        c["_Rectangle__width"] = 6
        self.assertEqual(h.__dict__, c)

        h.update(id=11, size=6, x=21)
        c["_Rectangle__x"] = 21
        self.assertEqual(h.__dict__, c)

        h.update(id=11, size=6, x=21, y=26)
        c["_Rectangle__y"] = 26
        self.assertEqual(h.__dict__, c)

        h.update(y=26, id=11, x=21, size=6)
        self.assertEqual(h.__dict__, c)

        Base._Base__nb_objects = 0
        v1 = Square(5)
        self.assertEqual(str(v1), "[Square] (1) 0/0 - 5")

        v1.update(10)
        self.assertEqual(str(v1), "[Square] (10) 0/0 - 5")

        v1.update(1, 2)
        self.assertEqual(str(v1), "[Square] (1) 0/0 - 2")

        v1.update(1, 2, 3)
        self.assertEqual(str(v1), "[Square] (1) 3/0 - 2")

        v1.update(1, 2, 3, 4)
        self.assertEqual(str(v1), "[Square] (1) 3/4 - 2")

        v1.update(x=12)
        self.assertEqual(str(v1), "[Square] (1) 12/4 - 2")

        v1.update(size=7, y=1)
        self.assertEqual(str(v1), "[Square] (1) 12/1 - 7")

        v1.update(size=7, id=89, y=1)
        self.assertEqual(str(v1), "[Square] (89) 12/1 - 7")

    def test_r_to_dict_me(self):
        """Test to_dictionary method in Square"""
        with self.assertRaises(TypeError) as s:
            Square.to_dictionary()
        ss = "to_dictionary() missing 1 required positional argument: 'self'"
        self.assertEqual(str(s.exception), ss)

        h = Square(1)
        c = {'x': 0, 'y': 0, 'size': 1, 'id': 1}
        self.assertEqual(h.to_dictionary(), c)

        h = Square(10, 3, 4, 5)
        c = {'x': 3, 'y': 4, 'size': 10, 'id': 5}
        self.assertEqual(h.to_dictionary(), c)

        h.x = 11
        h.y = 21
        h.size = 31
        c = {'x': 11, 'y': 21, 'size': 31, 'id': 5}
        self.assertEqual(h.to_dictionary(), c)

        v1 = Square(11, 3, 2)
        v1_dictionary = v1.to_dictionary()
        v2 = Square(2, 2)
        v2.update(**v1_dictionary)
        self.assertEqual(str(v1), str(v2))
        self.assertNotEqual(v1, v2)


if __name__ == "__main__":
    unittest.main()
