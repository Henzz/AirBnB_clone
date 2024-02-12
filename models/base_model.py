#!/usr/bin/env python3
# base_model.py
"""This module contains the `BaseModel` class."""
import uuid
from datetime import datetime


class BaseModel:
    """
    Base Model class represents the base model for all other models.

    Attributes:
        id (str): The unique identifier.
        created_at (datetime.datetime): The creation date and time.
        updated_at (datetime.datetime): The last update date and time.

    Methods:
        __init__(self, *args, **kwargs)
        save(self)
        to_dict(self)
        __str__(self)
    """

    def __init__(self, *args, **kwargs):
        """
        Initializes a new instance of the BaseModel.

        Args:
            *args: Variable length argument list.
            **kwargs: Arbitrary keyword arguments.
        """
        if kwargs:
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
            from models import storage
            storage.new(self)

    def save(self):
        """
        Updates the attribute `updated_at`.
        Saves the current model instance.
        """
        self.updated_at = datetime.now()
        from models import storage
        storage.save()

    def to_dict(self):
        """
        Converts the model instance to a dictionary.

        Returns:
            data (dict): A dictionary representation containing all of the
            model instance.
        """
        data = self.__dict__.copy()
        data['__class__'] = self.__class__.__name__
        data['created_at'] = self.created_at.isoformat()
        data['updated_at'] = self.updated_at.isoformat()
        return data

    def __str__(self):
        """
        Returns:
            A string representation of the BaseModel instance in format:
                [<class name>] (<self.id>) <self.__dict__>
        """
        class_name = self.__class__.__name__
        return f"[{class_name}] ({self.id}) {self.__dict__}"
