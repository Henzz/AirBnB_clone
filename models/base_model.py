#!/usr/bin/python3
"""This module contains the `BaseModel` class."""
import uuid
from datetime import datetime


class BaseModel:
    """
    Base Model class for other classes.

    Attributes:
        id (string):
            Assign uuid when an instance is created.
        created_at (datetime):
            Assign with the current datetime when an instance is created
        updated_at (datetime):
            Assign with the current datetime when an instance is created and
            it will be updated every time there is a change

    Methods:
        __init__(self)
    """

    def __init__(self, *args, **kwargs):
        """
        Initializes a BaseModel instance.
        It will assign unique public instance attribute `id` and datetime to
        `created_at` and `updated_at`.
        """
        if kwargs:
            self.id = str(uuid.uuid4())
            for key, value in kwargs.items():
                if key == '__class__':
                    continue
                if key in ['created_at', 'updated_at']:
                    value = datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f")
                setattr(self, key, value)
            if 'created_at' not in kwargs.items():
                self.created_at = datetime.now()
                self.updated_at = self.created_at
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = self.created_at

    def save(self):
        """
        Updates the public instance attribute `updated_at`
        with the current datetime.
        """
        self.updated_at = datetime.now()

    def to_dict(self):
        """
        Returns a dictionary representation containing all
        keys/value of `__dict__` of the instance.
        """
        data = self.__dict__.copy()
        data['__class__'] = self.__class__.__name__
        data['created_at'] = self.created_at.isoformat()
        data['updated_at'] = self.updated_at.isoformat()
        return data

    def __str__(self):
        """
        Returns a string representation of the BaseModel instance in format:
            [<class name>] (<self.id>) <self.__dict__>
        """
        class_name = self.__class__.__name__
        return f"[{class_name}] ({self.id}) {self.__dict__}"
