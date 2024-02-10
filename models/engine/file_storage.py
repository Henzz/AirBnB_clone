#!/usr/bin/python3
""" File Storage Module """
import json

class FileStorage:
    """ FileStorage class """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """ Returns the dictionary __objects """
        return FileStorage.__objects

    def new(self, obj):
        """ Sets in __objects the obj with key <obj class name>.id """
        key = "{}.{}".format(type(obj).__name__, obj.id)
        FileStorage.__objects[key] = obj

    def save(self):
        """ Serializes __objects to the JSON file """
        new_dict = {}
        for key, value in FileStorage.__objects.items():
            new_dict[key] = value.to_dict()
        with open(FileStorage.__file_path, mode='w', encoding='utf-8') as file:
            json.dump(new_dict, file)

    def reload(self):
        """ Deserializes the JSON file to __objects """
        try:
            with open(FileStorage.__file_path, mode='r', encoding='utf-8') as file:
                FileStorage.__objects = json.load(file)
            for key, value in FileStorage.__objects.items():
                class_name = value['__class__']
                del value['__class__']
                FileStorage.__objects[key] = eval(class_name)(**value)
        except FileNotFoundError:
            pass
