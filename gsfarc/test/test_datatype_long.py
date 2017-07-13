"""

"""

import unittest
import arcpy

from gsfarc.test import config


class TestDatatypeLong(unittest.TestCase):
    """Tests the long task datatype"""

    @classmethod
    def setUpClass(cls):
        """Class setup creates a toolbox file wrapper to GSF."""
        config.setup_idl_toolbox('test_datatype_long', 'qa_idltaskengine_datatype_long')

    @classmethod
    def tearDownClass(cls):
        pass

    def test_datatype_long_max(self):
        """Tests the long datatype maximum value."""
        input = 2147483647
        result = arcpy.QA_IDLTaskEngine_DataType_Long_GSF(input)

        self.assertEqual(int(result.getOutput(0)), input)

    def test_datatype_long_min(self):
        """Tests the long datatype minimum value."""
        input = -2147483648
        result = arcpy.QA_IDLTaskEngine_DataType_Long_GSF(input)

        self.assertEqual(int(result.getOutput(0)), int(input))

if __name__ == '__main__':
    unittest.main()