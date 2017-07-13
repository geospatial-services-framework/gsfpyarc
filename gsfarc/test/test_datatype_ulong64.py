"""

"""

import unittest
import arcpy
from gsfarc.test import config


class TestDatatypeULong64(unittest.TestCase):
    """Tests the ulong64 task datatype"""

    @classmethod
    def setUpClass(cls):
        """Class setup creates a toolbox file wrapper to GSF."""
        config.setup_idl_toolbox('test_datatype_ulong64', 'qa_idltaskengine_datatype_ulong64')

    @classmethod
    def tearDownClass(cls):
        pass

    def test_datatype_ulong64_max(self):
        """Tests the ulong64 datatype maximum value."""
        # Since we have to use gplong, we are limited to the 32 bit signed long integer range.
        input = 2147483647

        result = arcpy.QA_IDLTaskEngine_DataType_ULong64_GSF(input)
        # int and long were consolidated to int only in Python 3
        self.assertEqual(int(result.getOutput(0)), input)

    def test_datatype_ulong64_min(self):
        """Tests the ulong64 datatype minimum value."""
        input = 0
        result = arcpy.QA_IDLTaskEngine_DataType_ULong64_GSF(input)
        # int and long were consolidated to int only in Python 3
        self.assertEqual(int(result.getOutput(0)), int(input))

if __name__ == '__main__':
    unittest.main()