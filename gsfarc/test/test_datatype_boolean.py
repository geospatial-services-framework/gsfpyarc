"""

"""
import unittest

import arcpy
from gsfarc.test import config


class TestDatatypeBoolean(unittest.TestCase):
    """Tests the server GPToolbox class"""

    @classmethod
    def setUpClass(cls):
        """Class setup creates a toolbox file wrapper to GSF."""
        config.setup_idl_toolbox('test_datatype_boolean', 'QA_IDLTaskEngine_DataType_Boolean')

    @classmethod
    def tearDownClass(cls):
        pass

    def test_datatype_boolean_true(self):
        """Tests the bool datatype with a value of true."""
        inputBool = True
        result = arcpy.QA_IDLTaskEngine_DataType_Boolean_GSF(inputBool)
        self.assertEqual(result.getOutput(0), 'true')

    def test_datatype_boolean_default(self):
        """Tests the bool datatype with a default value."""
        result = arcpy.QA_IDLTaskEngine_DataType_Boolean_GSF()
        self.assertEqual(result.getOutput(0), 'false')

    def test_datatype_boolean_false(self):
        """Tests the bool datatype with a value of false."""
        inputBool = False
        result = arcpy.QA_IDLTaskEngine_DataType_Boolean_GSF(inputBool)
        self.assertEqual(result.getOutput(0), 'false')

if __name__ == '__main__':
    unittest.main()