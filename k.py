#!/usr/bin/python3
from models.engine.file_storage import FileStorage

s = FileStorage()
s.reload()
print(s.all())
