"""

"""
import os
import unittest
import arcpy
from gsfarc.test import config


class TestDatatypeByte(unittest.TestCase):
    """Tests the byte task datatype"""

    @classmethod
    def setUpClass(cls):
        """Class setup creates a toolbox file wrapper to GSF."""
        config.setup_idl_toolbox('test_datatype_byte','qa_idltaskengine_datatype_byte')

    @classmethod
    def tearDownClass(cls):
        pass

    def test_datatype_byte_min(self):
        """Tests the byte datatype minimum value."""
        input = 0
        result = arcpy.QA_IDLTaskEngine_DataType_Byte_GSF(input)

        self.assertEqual(int(result.getOutput(0)), input)

    def test_datatype_byte_max(self):
        """Tests the byte datatype maximum value."""
        input = 255
        result = arcpy.QA_IDLTaskEngine_DataType_Byte_GSF(input)

        self.assertEqual(int(result.getOutput(0)), input)

    def test_datatype_byte_outofrange(self):
        """Tests error message when value is out of datatype range."""
        input = 256

        try:
            result = arcpy.QA_IDLTaskEngine_DataType_Byte_GSF(input)
            self.fail('Exception not thrown.')
        except arcpy.ExecuteError:
            isError = str(arcpy.GetMessages(2))
            expError = 'Task failed to execute'

            self.assertIn(expError, isError)

if __name__ == '__main__':
    unittest.main()