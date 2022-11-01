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
        """Instatntiates a new model"""
        if args:
            pass
        if not kwargs:
            self.id = str(uuid.uuid4())
            self.created_at = _date
            self.updated_at = _date
        else:
            kwargs['updated_at'] = datetime.datetime.strptime(kwargs['updated_at'],
                                                     '%Y-%m-%dT%H:%M:%S.%f')
            kwargs['created_at'] = datetime.datetime.strptime(kwargs['created_at'],
                                                     '%Y-%m-%dT%H:%M:%S.%f')
            del kwargs['__class__']
            self.__dict__.update(kwargs)

    def __str__(self):
        """prints the string representation of a class"""
        _sn = self.__class__.__name__
        return ("[{}] ({}) {}".format(_sn, self.id, self.__dict__))

    def save(self):
        """updates the update_at time to the current time"""
        self.update_at = _date

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
