#!/usr/bin/python3
""" File storage module """
import json
import models

class FileStorage:
    """ FileStorage class """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """ Returns the dictionary __objects """
        return FileStorage.__objects

    def new(self, obj):
        """ Sets in __objects the obj with key <obj class name>.id """
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        FileStorage.__objects[key] = obj

    def save(self):
        """ Serializes __objects to the JSON file """
        json_dict = {}
        for key, value in FileStorage.__objects.items():
            json_dict[key] = value.to_dict()
        with open(FileStorage.__file_path, mode="w", encoding="utf-8") as f:
            json.dump(json_dict, f)

    def reload(self):
        """ Deserializes the JSON file to __objects """
        try:
            with open(FileStorage.__file_path, mode="r", encoding="utf-8") as f:
                json_dict = json.load(f)
                for key, value in json_dict.items():
                    class_name = key.split('.')[0]
                    obj = getattr(models, class_name)(**value)
                    FileStorage.__objects[key] = obj
        except FileNotFoundError:
            pass
