#!/usr/bin/python3
"""BaseModel class file"""
import uuid
import json
import os
import datetime
_date = datetime.datetime.now()


class BaseModel:
    """model class declared"""

    def __init__(self, *args, **kwargs):
        """define instance attributes"""
        if args:
            pass
        if kwargs:
            tmp = {}
            for k, v in kwargs.items():
                if k == 'created_at' or k == 'updated_at':
                    v = datetime.datetime.strptime(v, "%Y-%m-%dT%H:%M:%S.%f")
                if k != '__class__':
                    tmp[k] = v
                if 'id' not in kwargs.items():
                    self.id = str(uuid.uuid4())
                if 'created_at' not in kwargs.items():
                    self.created_at = _date
                if 'updated_at' not in kwargs.items():
                    self.updated_at = _date
        else:
            self.id = str(uuid.uuid4())
            self.created_at = self.updated_at = _date

    def __str__(self):
        """prints the string representation of a class"""
        _sn = self.__class__.__name__
        return ("[{}] ({}) {}".format(_sn, self.id, self.__dict__))

    def save(self):
        """updates the update_at time to the current time"""
        self.update_at = str(_date)

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
