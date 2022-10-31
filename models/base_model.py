#!/usr/bin/python
"""BaseModel class file"""
import uuid
import json
import os
import datetime
_date = datetime.datetime.now()


class BaseModel:
    """model class declared"""

    def __init__(self):
        """define instance attributes"""
        self.id = str(uuid.uuid4())
        self.created_at = _date
        self.updated_at = _date

    def __str__(self):
        """prints the string representation of a class"""
        _sn = self.__class__.__name__
        return ("[{}] ({}) {}".format(_sn, self.id, self.__dict__))

    def save(self):
        """updates the update_at time to the current time"""
        update_at = str(_date)

    def to_dict(self):
        """returns a dictionary containing key/value
        of __dict__ of the instance"""
        tmp = {}
        for k, v in self.__dict__.items():
            tmp.update({k: v})
        tmp['__class__'] = self.__class__.__name__
        tmp['created_at'] = str(_date.strftime("%Y-%m-%dT%H:%M:%S.%f"))
        tmp['updated_at'] = str(_date.strftime("%Y-%m-%dT%H:%M:%S.%f"))
        return tmp
