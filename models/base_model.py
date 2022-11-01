#!/usr/bin/python3
"""BaseModel class file"""
import uuid
import json
import os
from datetime import datetime
_format = "%Y-%m-%dT%H:%M:%S.%f"


class BaseModel:
    """model class declared"""

    def __init__(self, *args, **kwargs):
        """Instatntiates a new model"""
        if args:
            pass
        if kwargs:
            for k, v in kwargs.items():
                if k == "__class__":
                    continue
                if k == "updated_at" or k == "created_at":
                    v = datetime.strptime(v, _format)
                setattr(self, k, v)
        else:
            setattr(self, 'id', str(uuid.uuid4()))
            setattr(self, 'created_at', datetime.now())
            setattr(self, 'updated_at', datetime.now())

    def __str__(self):
        """prints the string representation of a class"""
        _sn = self.__class__.__name__
        return ("[{}] ({}) {}".format(_sn, self.id, self.__dict__))

    def save(self):
        """updates the update_at time to the current time"""
        self.update_at = datetime.now()

    def to_dict(self):
        """returns a dictionary containing key/value
        of __dict__ of the instance"""
        tmp = {}
        for k, v in self.__dict__.items():
            tmp.update({k: v})
        tmp['__class__'] = self.__class__.__name__
        tmp['created_at'] = str(self.created_at.strftime("%Y-%m-%dT%H:%M:%S.%f"))
        tmp['updated_at'] = str(self.updated_at.strftime("%Y-%m-%dT%H:%M:%S.%f"))
        return tmp
