#!/usr/bin/python3
"""filestorage test"""
from models.engine.file_storage import Filestorage
import unittest


class Testing(unittest.Testcase):
    """Testing class init"""
    S = FileStorage()


    def test_all(self):
        """"Test the all method of the Filstorage class"""
        self.assertIsInstance(S.all(), dict)

    def test_instance(self):
        """Check if S is an instance of the FileSTorage class"""
        self.assertIsInstance(S, FileStorage)


