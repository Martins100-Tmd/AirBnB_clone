#!/usr/bin/python3
"""
Contains FileStorage class
"""


import json
from models.amenity import Amenity
from models.base_model import BaseModel
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User

classes = {"Amenity": Amenity, "BaseModel": BaseModel, "City": City,
           "Place": Place, "Review": Review, "State": State, "User": User}


class FileStorage:
    """
    serializes instances to a JSON file
    and deserializes them back to instances
    """
    # path to the JSON file
    __file_path = "file.json"
    # dictionary to store all objects by <class name>.id
    __objects = {}

    def all(self):
        """returns the dictionary __objects"""
        return FileStorage.__objects

    def new(self, obj):
        """
        sets in __objects the obj with
        key <obj class name>.id
        """
        if obj is not None:
            key = obj.__class__.__name__ + "." + obj.id
            FileStorage.__objects[key] = obj

    def save(self):
        """
        serializes __objects to the JSON file path
        """
        jsonObject = {}
        for key in FileStorage.__objects:
            jsonObject[key] = FileStorage.__objects[key].to_dict()
        with open(FileStorage.__file_path, "w") as f:
            json.dump(jsonObject, f)

    def reload(self):
        """deserializes the JSON file to __objects"""
        load = {}
        try:
            with open(FileStorage.__file_path, "r") as f:
                load = json.load(f)
            print(load)
            for key, value in load.items():
                FileStorage.__objects[key] = eval(value["__class__"])(**value)
        except Exception:
            pass

