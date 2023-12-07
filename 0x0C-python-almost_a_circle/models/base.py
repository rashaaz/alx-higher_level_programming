#!/usr/bin/python3
"""Module for Base class."""
from json import dumps, loads
import csv


class Base:
    """Base class for managing id attribute in classes"""

    __nb_objects = 0

    def __init__(self, id=None):
        """Initialize Base instance with a unique id."""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """Convert a list of dictionaries to a JSON-formatted string"""
        if list_dictionaries is None or not list_dictionaries:
            return "[]"
        else:
            return dumps(list_dictionaries)

    @staticmethod
    def from_json_string(json_string):
        """Convert a JSON-formatted string to a list of dictionaries"""
        if json_string is None or not json_string:
            return []
        return loads(json_string)

    @classmethod
    def save_to_file(cls, list_objs):
        """Save a list of objects to a JSON file"""
        if list_objs is not None:
            list_objs = [s.to_dictionary() for s in list_objs]
        with open("{}.json".format(cls.__name__), "w", encoding="utf-8") as fa:
            fa.write(cls.to_json_string(list_objs))

    @classmethod
    def create(cls, **dictionary):
        """Create an instance of the class with attributes"""
        from models.rectangle import Rectangle
        from models.square import Square
        if cls is Rectangle:
            n = Rectangle(1, 1)
        elif cls is Square:
            n = Square(1)
        else:
            n = None
        n.update(**dictionary)
        return n

    @classmethod
    def load_from_file(cls):
        """Load a list of objects from a JSON file"""
        from os import path
        fi = "{}.json".format(cls.__name__)
        if not path.isfile(fi):
            return []
        with open(fi, "r", encoding="utf-8") as file:
            return [cls.create(**c) for c in cls.from_json_string(file.read())]

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """Save a list of objects to a CSV file"""
        from models.rectangle import Rectangle
        from models.square import Square
        if list_objs is not None:
            if cls is Rectangle:
                list_objs = [[s.id, s.width, s.height, s.x, s.y]
                             for s in list_objs]
            else:
                list_objs = [[s.id, s.size, s.x, s.y]
                             for s in list_objs]
        with open('{}.csv'.format(cls.__name__), 'w', newline='',
                  encoding='utf-8') as file:
            wr = csv.writer(file)
            wr.writerows(list_objs)

    @classmethod
    def load_from_file_csv(cls):
        """Load a list of objects from a CSV file"""
        from models.rectangle import Rectangle
        from models.square import Square
        rs = []
        with open('{}.csv'.format(cls.__name__), 'r', newline='',
                  encoding='utf-8') as file:
            re = csv.reader(file)
            for ro in re:
                ro = [int(f) for f in ro]
                if cls is Rectangle:
                    c = {"id": ro[0], "width": ro[1], "height": ro[2],
                         "x": ro[3], "y": ro[4]}
                else:
                    c = {"id": ro[0], "size": ro[1],
                         "x": ro[2], "y": ro[3]}
                rs.append(cls.create(**c))
        return rs

    @staticmethod
    def draw(list_rectangles, list_squares):
        import turtle
        import time
        from random import randrange
        turtle.Screen().colormode(255)
        for ii in list_rectangles + list_squares:
            m = turtle.Turtle()
            m.color((randrange(255), randrange(255), randrange(255)))
            m.pensize(1)
            m.penup()
            m.pendown()
            m.setpos((ii.x + m.pos()[0], ii.y - m.pos()[1]))
            m.pensize(10)
            m.forward(ii.width)
            m.left(90)
            m.forward(ii.height)
            m.left(90)
            m.forward(ii.width)
            m.left(90)
            m.forward(ii.height)
            m.left(90)
            m.end_fill()

        time.sleep(5)
