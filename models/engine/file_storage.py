#!/usr/bin/python3
""" Module contains Filestorage class """

import datetime
import json
import os

class FileStorage():
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Returns a dictionary containing all stored objects.

        Returns:
            dict: A dictionary containing all stored objects, where the keys are
                  composed of the class name concatenated with the object ID, and
                  the values are the objects themselves.
        """
        return FileStorage.__objects

    def new(self, obj):
        """
        Adds a new object to the Filestorage dictionary
        Args:
        obj: The object to be added
        Returns:
        None
        Description:
            This method assigns the object given to the class
            it assigns the class to the id and forms the unique
            key
        """
        key = "{}.{}".format(type(obj).__name__, obj.id)
        FileStorage.__objects[key] = obj

    def save(self):
        """ serializes __objectsto a JSON file
        Args:
            None
        Returns:
            None:
        Description:
            This method serializes the objects dictionary to a JSON_file.
            Each object in the dictionary is converted into a dictionar
            representation and later dumped using dumps to a JSON_file
        """
        with open(FileStorage.__file_path, "w", encoding="utf-8") as f:
            d = {key: val.to_dict() for key, val in FileStorage.__objects.items()}
            json.dump(d, f)

    def reload(self):
        """ This module deserializes JSON file to objects """
        if not os.path.isfile(FileStorage.__file_path):
            return
        with open(FileStorage.__file_path, "r", encoding="utf-8") as f:
            object_dict = json.load(f)
            object_dict = {key: self.classes()[v["__class__"]](**val)
                    for key, value in object_dict.items()}
            FileStorage.__objects = object_dict

    def attributes(self):
        """Returns the valid attributes and their types for classname."""
        """
           Returns:
               dict: A dictionary containing class names as keys and dictionaries
                     of attributes and their types as values.
                     Example:
                     {
                         "BaseModel": {
                         "id": str,
                         "created_at": datetime.datetime,
                         "updated_at": datetime.datetime
                     },
                     ...
                     }
        """
        attributes = {
            "BaseModel":
                     {"id": str,
                      "created_at": datetime.datetime,
                      "updated_at": datetime.datetime},
            "User":
                     {"email": str,
                      "password": str,
                      "first_name": str,
                      "last_name": str},
            "State":
                     {"name": str},
            "City":
                     {"state_id": str,
                      "name": str},
            "Amenity":
                     {"name": str},
            "Place":
                     {"city_id": str,
                      "user_id": str,
                      "name": str,
                      "description": str,
                      "number_rooms": int,
                      "number_bathrooms": int,
                      "max_guest": int,
                      "price_by_night": int,
                      "latitude": float,
                      "longitude": float,
                      "amenity_ids": list},
            "Review":
            {"place_id": str,
                         "user_id": str,
                         "text": str}
        }
        return attributes
    def classes(self):
        """Returns a dictionary of valid classes and their references."""
        from models.base_model import BaseModel
        #from models.user import User
        #from models.state import State
        #from models.city import City
        #from models.amenity import Amenity
        #from models.place import Place
        #from models.review import Review

        classes = {"BaseModel": BaseModel,
                   "User": User,
                   "State": State,
                   "City": City,
                   "Amenity": Amenity,
                   "Place": Place,
                   "Review": Review}
        return classes
