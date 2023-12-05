#!/usr/bin/python3
"""Class Student that defines a student with public instanc"""


class Student:
    """Class representing a student."""

    def __init__(self, first_name, last_name, age):
        """
        Initializes a new instance of the Student class.

        Args:
            first_name (str): The first name of the student.
            last_name (str): The last name of the student.
            age (int): The age of the student.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        Retrieves a dictionary representation of a Student instance.

        Args:
            attrs (list): List of strings, only attribute names contained in
                          this list must be retrieved.

        Returns:
            dict: A dictionary containing the public attributes of the student.
        """
        try:
            for sh in attrs:
                if type(sh) is not str:
                    return self.__dict__
        except Exception:
            return self.__dict__
        new_dic = dict()
        for key, value in self.__dict__.items():
            if key in attrs:
                new_dic[key] = value
        return new_dic
