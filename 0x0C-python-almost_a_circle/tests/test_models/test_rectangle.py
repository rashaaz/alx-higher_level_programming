#!/usr/bin/python3
"""Unittests for Rectangle class"""
import unittest
from models.base import Base
from models.rectangle import Rectangle
from random import randrange
from contextlib import redirect_stdout
import io


class TestRectanglemeyhod(unittest.TestCase):
    """Test cases for Rectangle class"""

    def setUp(self):
        """Set up for each test case"""
        Base._Base__nb_objects = 0

    def tearDown(self):
        """Clean up after each test case"""
        pass

    def test_name_class(self):
        """Test class name"""
        self.assertEqual(str(Rectangle),
                         "<class 'models.rectangle.Rectangle'>")

    def test_a_inher_me(self):
        """Test inheritance"""
        self.assertTrue(issubclass(Rectangle, Base))

    def test_r_cons_non_args(self):
        """Test constructor with no arguments"""
        with self.assertRaises(TypeError) as s:
            h = Rectangle()
        m = "__init__() missing 2 required positional arguments: 'width' \
and 'height'"
        self.assertEqual(str(s.exception), m)

    def test_r_cons_more_args(self):
        """Test constructor with too many arguments"""
        with self.assertRaises(TypeError) as s:
            h = Rectangle(2, 3, 4, 5, 6, 7)
        m = "__init__() takes from 3 to 6 positional arguments but 7 were \
given"
        self.assertEqual(str(s.exception), m)

    def test_r_cons_1_args(self):
        """Test constructor with only one argument"""
        with self.assertRaises(TypeError) as s:
            h = Rectangle(1)
        m = "__init__() missing 1 required positional argument: 'height'"
        self.assertEqual(str(s.exception), m)

    def test_m_inst(self):
        """Test instantiation of Rectangle class"""
        h = Rectangle(11, 21)
        self.assertEqual(str(type(h)), "<class 'models.rectangle.Rectangle'>")
        self.assertTrue(isinstance(h, Base))
        c = {'_Rectangle__height': 21, '_Rectangle__width': 11,
             '_Rectangle__x': 0, '_Rectangle__y': 0, 'id': 1}
        self.assertDictEqual(h.__dict__, c)

        with self.assertRaises(TypeError) as s:
            h = Rectangle("2", 3)
        me = "width must be an integer"
        self.assertEqual(str(s.exception), me)

        with self.assertRaises(TypeError) as s:
            h = Rectangle(2, "3")
        me = "height must be an integer"
        self.assertEqual(str(s.exception), me)

        with self.assertRaises(TypeError) as s:
            h = Rectangle(2, 3, "4")
        me = "x must be an integer"
        self.assertEqual(str(s.exception), me)

        with self.assertRaises(TypeError) as s:
            h = Rectangle(2, 3, 4, "5")
        me = "y must be an integer"
        self.assertEqual(str(s.exception), me)

        with self.assertRaises(ValueError) as s:
            h = Rectangle(-2, 3)
        me = "width must be > 0"
        self.assertEqual(str(s.exception), me)

        with self.assertRaises(ValueError) as s:
            h = Rectangle(2, -3)
        me = "height must be > 0"
        self.assertEqual(str(s.exception), me)

        with self.assertRaises(ValueError) as s:
            h = Rectangle(0, 3)
        me = "width must be > 0"
        self.assertEqual(str(s.exception), me)

        with self.assertRaises(ValueError) as s:
            h = Rectangle(2, 0)
        me = "height must be > 0"
        self.assertEqual(str(s.exception), me)

        with self.assertRaises(ValueError) as s:
            h = Rectangle(2, 3, -4)
        me = "x must be >= 0"
        self.assertEqual(str(s.exception), me)

        with self.assertRaises(ValueError) as s:
            h = Rectangle(2, 3, 4, -5)
        me = "y must be >= 0"
        self.assertEqual(str(s.exception), me)

    def test_m_inst_posit(self):
        """Test instantiation with positional arguments"""
        h = Rectangle(6, 11, 16, 21)
        c = {'_Rectangle__height': 11, '_Rectangle__width': 6,
             '_Rectangle__x': 16, '_Rectangle__y': 21, 'id': 1}
        self.assertEqual(h.__dict__, c)

        h = Rectangle(6, 11, 16, 21, 99)
        c = {'_Rectangle__height': 11, '_Rectangle__width': 6,
             '_Rectangle__x': 16, '_Rectangle__y': 21, 'id': 99}
        self.assertEqual(h.__dict__, c)

    def test_m_insta_keyword(self):
        """Test instantiation with keyword arguments"""
        h = Rectangle(101, 201, id=422, y=100, x=102)
        c = {'_Rectangle__height': 201, '_Rectangle__width': 101,
             '_Rectangle__x': 102, '_Rectangle__y': 100, 'id': 422}
        self.assertEqual(h.__dict__, c)

    def test_r_id_inher_me(self):
        """Test inheritance of id attribute"""
        Base._Base__nb_objects = 99
        h = Rectangle(3, 5)
        self.assertEqual(h.id, 100)

    def test_r_proper_me(self):
        """Test properties and attribute values"""
        h = Rectangle(4, 8)
        h.width = 99
        h.height = 100
        h.x = 101
        h.y = 102
        c = {'_Rectangle__height': 100, '_Rectangle__width': 99,
             '_Rectangle__x': 101, '_Rectangle__y': 102, 'id': 1}
        self.assertEqual(h.__dict__, c)
        self.assertEqual(h.width, 99)
        self.assertEqual(h.height, 100)
        self.assertEqual(h.x, 101)
        self.assertEqual(h.y, 102)

    def invalid_types(self):
        """Helper function to provide a list of invalid types"""
        g = (4.15, -2.2, float('inf'), float('-inf'), True, "str", (3,),
             [5], {6}, {7: 8}, None)
        return g

    def test_r_val_typ_me(self):
        """Test validation of attribute types"""
        h = Rectangle(2, 3)
        att = ["x", "y", "width", "height"]
        for at in att:
            ss = "{} must be an integer".format(at)
            for invalid_type in self.invalid_types():
                with self.assertRaises(TypeError) as s:
                    setattr(h, at, invalid_type)
                self.assertEqual(str(s.exception), ss)

    def test_m_val_val_n_gt_me(self):
        """ Test validation of attribute values (negative and zero)"""
        h = Rectangle(2, 3)
        att = ["width", "height"]
        for at in att:
            ss = "{} must be > 0".format(at)
            with self.assertRaises(ValueError) as s:
                setattr(h, at, -(randrange(11) + 2))
            self.assertEqual(str(s.exception), ss)

    def test_r_val_val_n_ge_me(self):
        """Test validation of attribute values (negative)"""
        h = Rectangle(2, 3)
        att = ["x", "y"]
        for at in att:
            ss = "{} must be >= 0".format(at)
            with self.assertRaises(ValueError) as s:
                setattr(h, at, -(randrange(11) + 2))
            self.assertEqual(str(s.exception), ss)

    def test_r_val_val_0_me(self):
        """Test validation of attribute values (zero)"""
        h = Rectangle(2, 3)
        att = ["width", "height"]
        for at in att:
            ss = "{} must be > 0".format(at)
            with self.assertRaises(ValueError) as s:
                setattr(h, at, 0)
            self.assertEqual(str(s.exception), ss)

    def test_r_prop_me(self):
        """Test property values and range"""
        h = Rectangle(2, 3)
        att = ["x", "y", "width", "height"]
        for at in att:
            m = randrange(11) + 2
            setattr(h, at, m)
            self.assertEqual(getattr(h, at), m)

    def test_r_prop_ra_0_me(self):
        """Test property values with zero"""
        h = Rectangle(2, 3)
        h.x = 0
        h.y = 0
        self.assertEqual(h.x, 0)
        self.assertEqual(h.y, 0)

    def test_r_ar_enyy_args_me(self):
        """Test area method with no arguments"""
        h = Rectangle(6, 7)
        with self.assertRaises(TypeError) as s:
            Rectangle.area()
        ss = "area() missing 1 required positional argument: 'self'"
        self.assertEqual(str(s.exception), ss)

    def test_r_ar_me(self):
        """Test area method with various cases"""
        h = Rectangle(6, 7)
        self.assertEqual(h.area(), 42)
        m = randrange(11) + 2
        k = randrange(11) + 2
        h.width = m
        h.height = k
        self.assertEqual(h.area(), m * k)
        m = randrange(11) + 2
        k = randrange(11) + 2
        h = Rectangle(m, k, 8, 8, 10)
        self.assertEqual(h.area(), m * k)
        m = randrange(11) + 2
        k = randrange(11) + 2
        h = Rectangle(m, k, y=8, x=9, id=10)
        self.assertEqual(h.area(), m * k)

        h1 = Rectangle(4, 3)
        self.assertEqual(h1.area(), 12)

        h2 = Rectangle(3, 11)
        self.assertEqual(h2.area(), 33)

        h3 = Rectangle(9, 8, 0, 0, 13)
        self.assertEqual(h3.area(), 72)

    def test_r_dis_eny_args_me(self):
        """Test display method with no arguments"""
        h = Rectangle(10, 9)
        with self.assertRaises(TypeError) as s:
            Rectangle.display()
        ss = "display() missing 1 required positional argument: 'self'"
        self.assertEqual(str(s.exception), ss)

    def test_r_dis_simp(self):
        """Test simple cases for display method"""
        h = Rectangle(1, 1)
        a = io.StringIO()
        with redirect_stdout(a):
            h.display()
        ss = "#\n"
        self.assertEqual(a.getvalue(), ss)
        h.width = 4
        h.height = 5
        a = io.StringIO()
        with redirect_stdout(a):
            h.display()
        ss = "\
####\n\
####\n\
####\n\
####\n\
####\n\
"
        self.assertEqual(a.getvalue(), ss)
        h = Rectangle(5, 6, 7, 8)
        a = io.StringIO()
        with redirect_stdout(a):
            h.display()
        ss = """







       #####
       #####
       #####
       #####
       #####
       #####
"""
        self.assertEqual(a.getvalue(), ss)
        h = Rectangle(9, 8)
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
"""
        self.assertEqual(a.getvalue(), ss)
        h = Rectangle(1, 1, 10, 10)
        a = io.StringIO()
        with redirect_stdout(a):
            h.display()
        ss = """\










          #
"""
        self.assertEqual(a.getvalue(), ss)

        h = Rectangle(5, 5)
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

        h = Rectangle(5, 3, 5)
        a = io.StringIO()
        with redirect_stdout(a):
            h.display()
        ss = """\
     #####
     #####
     #####
"""
        self.assertEqual(a.getvalue(), ss)

        h = Rectangle(5, 3, 0, 4)
        a = io.StringIO()
        with redirect_stdout(a):
            h.display()
        ss = """\




#####
#####
#####
"""
        self.assertEqual(a.getvalue(), ss)

    def test_r_str_eny_args_me(self):
        """Test __str__ method with no arguments"""
        h = Rectangle(6, 3)
        with self.assertRaises(TypeError) as s:
            Rectangle.__str__()
        ss = "__str__() missing 1 required positional argument: 'self'"
        self.assertEqual(str(s.exception), ss)

    def test_r_str_me(self):
        """Test __str__ method"""
        h = Rectangle(6, 3)
        ss = '[Rectangle] (1) 0/0 - 6/3'
        self.assertEqual(str(h), ss)
        h = Rectangle(1, 1, 1)
        ss = '[Rectangle] (2) 1/0 - 1/1'
        self.assertEqual(str(h), ss)
        h = Rectangle(3, 4, 5, 6)
        ss = '[Rectangle] (3) 5/6 - 3/4'
        self.assertEqual(str(h), ss)

        Base._Base__nb_objects = 0
        h1 = Rectangle(4, 6, 2, 1, 12)
        self.assertEqual(str(h1), "[Rectangle] (12) 2/1 - 4/6")

        h2 = Rectangle(5, 5, 1)
        self.assertEqual(str(h2), "[Rectangle] (1) 1/0 - 5/5")

    def test_r_upd_eny_args_me(self):
        """Test update method with no arguments"""
        h = Rectangle(6, 3)
        with self.assertRaises(TypeError) as s:
            Rectangle.update()
        ss = "update() missing 1 required positional argument: 'self'"
        self.assertEqual(str(s.exception), ss)

        c = h.__dict__.copy()
        h.update()
        self.assertEqual(h.__dict__, c)

    def test_r_upd_args_me(self):
        """Test update method with positional arguments"""
        h = Rectangle(6, 3)
        c = h.__dict__.copy()

        h.update(11)
        c["id"] = 11
        self.assertEqual(h.__dict__, c)

        h.update(11, 6)
        c["_Rectangle__width"] = 6
        self.assertEqual(h.__dict__, c)

        h.update(11, 6, 18)
        c["_Rectangle__height"] = 18
        self.assertEqual(h.__dict__, c)

        h.update(11, 6, 18, 21)
        c["_Rectangle__x"] = 21
        self.assertEqual(h.__dict__, c)

        h.update(11, 6, 18, 21, 26)
        c["_Rectangle__y"] = 26
        self.assertEqual(h.__dict__, c)

    def test_r_upd_ar_bad_me(self):
        """Test update method with invalid positional arguments"""
        h = Rectangle(6, 3)
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
        ss = "height must be > 0"
        self.assertEqual(str(s.exception), ss)

        with self.assertRaises(ValueError) as s:
            h.update(11, 6, 18, -21)
        ss = "x must be >= 0"
        self.assertEqual(str(s.exception), ss)

        with self.assertRaises(ValueError) as s:
            h.update(11, 6, 18, 21, -26)
        ss = "y must be >= 0"
        self.assertEqual(str(s.exception), ss)

    def test_r_upd_kwar_me(self):
        """Test update method with keyword arguments"""
        h = Rectangle(6, 3)
        c = h.__dict__.copy()

        h.update(id=11)
        c["id"] = 11
        self.assertEqual(h.__dict__, c)

        h.update(width=6)
        c["_Rectangle__width"] = 6
        self.assertEqual(h.__dict__, c)

        h.update(height=18)
        c["_Rectangle__height"] = 18
        self.assertEqual(h.__dict__, c)

        h.update(x=21)
        c["_Rectangle__x"] = 21
        self.assertEqual(h.__dict__, c)

        h.update(y=26)
        c["_Rectangle__y"] = 26
        self.assertEqual(h.__dict__, c)

    def test_r_upd_kwar_two_me(self):
        """Test update method with combinations"""
        h = Rectangle(6, 3)
        c = h.__dict__.copy()

        h.update(id=11)
        c["id"] = 11
        self.assertEqual(h.__dict__, c)

        h.update(id=11, width=6)
        c["_Rectangle__width"] = 6
        self.assertEqual(h.__dict__, c)

        h.update(id=11, width=6, height=18)
        c["_Rectangle__height"] = 18
        self.assertEqual(h.__dict__, c)

        h.update(id=11, width=6, height=18, x=21)
        c["_Rectangle__x"] = 21
        self.assertEqual(h.__dict__, c)

        h.update(id=11, width=6, height=18, x=21, y=26)
        c["_Rectangle__y"] = 26
        self.assertEqual(h.__dict__, c)

        h.update(y=26, id=11, height=18, x=21, width=6)
        self.assertEqual(h.__dict__, c)

        Base._Base__nb_objects = 0
        h1 = Rectangle(10, 10, 10, 10)
        self.assertEqual(str(h1), "[Rectangle] (1) 10/10 - 10/10")

        h1.update(height=1)
        self.assertEqual(str(h1), "[Rectangle] (1) 10/10 - 10/1")

        h1.update(width=1, x=2)
        self.assertEqual(str(h1), "[Rectangle] (1) 2/10 - 1/1")

        h1.update(y=1, width=2, x=3, id=89)
        self.assertEqual(str(h1), "[Rectangle] (89) 3/1 - 2/1")

        h1.update(x=1, height=2, y=3, width=4)
        self.assertEqual(str(h1), "[Rectangle] (89) 1/3 - 4/2")

        Base._Base__nb_objects = 0
        h1 = Rectangle(10, 10, 10, 10)
        self.assertEqual(str(h1), "[Rectangle] (1) 10/10 - 10/10")

        h1.update(89)
        self.assertEqual(str(h1), "[Rectangle] (89) 10/10 - 10/10")

        h1.update(89, 2)
        self.assertEqual(str(h1), "[Rectangle] (89) 10/10 - 2/10")

        h1.update(89, 2, 3)
        self.assertEqual(str(h1), "[Rectangle] (89) 10/10 - 2/3")

        h1.update(89, 2, 3, 4)
        self.assertEqual(str(h1), "[Rectangle] (89) 4/10 - 2/3")

        h1.update(89, 2, 3, 4, 5)
        self.assertEqual(str(h1), "[Rectangle] (89) 4/5 - 2/3")

    def test_r_to_dic_me(self):
        """Test to_dictionary method"""
        with self.assertRaises(TypeError) as s:
            Rectangle.to_dictionary()
        ss = "to_dictionary() missing 1 required positional argument: 'self'"
        self.assertEqual(str(s.exception), ss)

        h = Rectangle(1, 2)
        c = {'x': 0, 'y': 0, 'width': 1, 'id': 1, 'height': 2}
        self.assertEqual(h.to_dictionary(), c)

        h = Rectangle(1, 2, 3, 4, 5)
        c = {'x': 3, 'y': 4, 'width': 1, 'id': 5, 'height': 2}
        self.assertEqual(h.to_dictionary(), c)

        h.x = 10
        h.y = 20
        h.width = 30
        h.height = 40
        c = {'x': 10, 'y': 20, 'width': 30, 'id': 5, 'height': 40}
        self.assertEqual(h.to_dictionary(), c)

        h1 = Rectangle(10, 2, 1, 9)
        h1_dic = h1.to_dictionary()
        h2 = Rectangle(1, 1)
        h2.update(**h1_dic)
        self.assertEqual(str(h1), str(h2))
        self.assertNotEqual(h1, h2)


if __name__ == "__main__":
    unittest.main()
