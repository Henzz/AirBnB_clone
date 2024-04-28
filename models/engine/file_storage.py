#!/usr/bin/env python3
# file_storage.py
"""This module contains the `FileStorage` class."""
import json


class FileStorage:
    """
    FileStorage class represents the file storage for storing
    and retrieving model instances.

    Attributes:
        __file_path (str): The file storage to JSON file.
        __objects (dict): Stores <class name>.id.

    Methods:
        all(self)
        new(self, obj)
        save(self)
        reload(self)
    """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """
        Retrieves all model instances.

        Returns:
            dict: A dictionart containing all model instances."""
        return self.__objects.copy()

    def new(self, obj):
        """
        Adds a new model instance to the file storage.

        Args:
            obj (BaseModel): The model instance to be added.
        """
        # Format key to: <obj class name>.id
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        self.__objects[key] = obj

    def save(self):
        """
        Serializes and saves the model instance to the file storage.
        """
        serialized_data = {}
        for key, obj in self.__objects.items():
            serialized_data[key] = obj.to_dict()

        with open(self.__file_path, 'w') as file:
            json.dump(serialized_data, file)

    def reload(self):
        """
        Deserializes and reloads the models instances from the file storage.
        """
        try:
            if not os.path.isfile(FileStorage.__file_path):
                self.save()
            from models.base_model import BaseModel
            class_dict = {
                    'BaseModel': BaseModel,
            }
            with open(self.__file_path, 'r') as file:
                serialized_objs = json.load(file)
                for key, obj_dict in serialized_objs.items():
                    class_name, obj_id = key.split('.')
                    obj = class_dict.get(class_name)(**obj_dict)
                    self.__objects[key] = obj
        except FileNotFoundError:
            pass
