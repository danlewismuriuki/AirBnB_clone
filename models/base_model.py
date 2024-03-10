#!/usr/bin/python3
"""Base class
This is the base class for the console
"""

import uuid
# from models import storage
from datetime import datetime


class BaseModel():
    """ base model of objectivity """
    def __init__(self, *args, **kwargs):
        """ Initialization of a Base instance
        Args:
        - *args list of arguments
        - **kwargs: dict of key-value arguments
        """
        if kwargs:
            for key in kwargs:
                if key == "created_at":
                    self.__dict__["created_at"] = datetime.strptime(
                            kwargs["created_at"], "%Y-%m-%dT%H:%M:%S.%f")
                elif key == "updated_at":
                    self.__dict__["updated_at"] = datetime.strptime(
                            kwargs["updated_at"], "%Y-%m-%dT%H:%M:%S.%f")
                else:
                    self.__dict__[key] = kwargs[key]
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            #storage.new(self)

    def __str__(self):
        """ method prints human-readable string representantion
        of an instance of the class
        """
        return "[{}] ({}) {}".\
            format(type(self).__name__, self.id, self.__dict__)

    def save(self):
        """ saves the current time to the update_at attribute """
        self.updated_at = datetime.now()
        storage.save()

    def to_dict(self):
        """ Returns a dictionary representation of an instance
        Returns:
        dict: A dictionary containing the attributes of the instance along
        with additional metadata
        dictionary has the following key-value pairs
        - '__class__': The name of the class instance
        - 'created_at': timestamp representing when the instance was created
        - 'updated_at': timestamp repr.. when the instance was last update
        {
        '__class__': 'MyClass',
        'id': '12345',
        'name': 'example',
        'created_at': '2024-03-08T10:30:00',
        'updated_at': '2024-03-08T10:35:00'
        }
        """
        my_dict = self.__dict__.copy()
        my_dict["__class__"] = type(self).__name__
        my_dict["created_at"] = my_dict["created_at"].isoformat()
        my_dict["updated_at"] = my_dict["updated_at"].isoformat()
        return my_dict
