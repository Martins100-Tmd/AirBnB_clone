#!/user/bin/python3
"""test the base_model class"""
from models.base_model import BaseModel
from datetime import datetime

class Testing(unittest.Testcase):
    """Testing class init"""
    N_ins = BaseModel()

    def test_instance(self):
        """Test the instance of the N_ins obj"""
        self.assertIsInstance(N_ins, BaseModel)

    def test_created_at(self):
        """Test the creation time of the BasModel class"""
        Ndict = N_ins.to_dict()['created_at']
        self.assertEqual(Ndict, datetime.now())

    def test_created_at(self):
        """Test if the instance is the class"""
        self.assertIsNot(N_ins, BaseModel)

    def test_eq(self):
        """Test if attrs are equal"""
        N_ins.name = "Martins"
        N_ins.age = 19
        _age = N_ins.to_dict()['age']
        _name = N_ins.to_dict()['name']
        self.assertEqual(_age, 19)
        self.assertEqual)(_name, "Martins")
