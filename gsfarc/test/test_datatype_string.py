"""

"""

import unittest
import arcpy
from gsfarc.test import config


class TestDatatypeString(unittest.TestCase):
    """Tests the string datatype."""

    @classmethod
    def setUpClass(cls):
        """Class setup creates a toolbox file wrapper to GSF."""
        config.setup_idl_toolbox('test_datatype_string', 'qa_idltaskengine_datatype_string')
        config.setup_envi_toolbox('test_datatype_string_choicelist', 'qa_envitaskengine_datatype_string')

    @classmethod
    def tearDownClass(cls):
        pass

    def test_datatype_string_basic(self):
        """Tests the string datatype with a basic string."""
        inputString = 'th1sIsaTESTString!'
        result = arcpy.QA_IDLTaskEngine_DataType_String_GSF(inputString)

        self.assertEqual(result.getOutput(0), inputString)

    def test_datatype_string_default(self):
        """Tests the string datatype with a default value."""
        result = arcpy.QA_IDLTaskEngine_DataType_String_GSF()

        self.assertEqual(result.getOutput(0), "cat")

    def test_datatype_string_choicelist(self):
        """Tests the string datatype with a choicelist."""
        input = "fish"
        result = arcpy.QA_ENVITaskEngine_DataType_String_GSF(input)

        self.assertEqual(result.getOutput(0), input)

    def test_datatype_string_longstring(self):
        """Tests the string datatype with a long string."""
        inputString = "x" * 31846
        result = arcpy.QA_IDLTaskEngine_DataType_String_GSF(inputString)

        self.assertEqual(result.getOutput(0), inputString)

if __name__ == '__main__':
    unittest.main()