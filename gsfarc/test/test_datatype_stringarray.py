"""

"""

import unittest

import arcpy
from gsfarc.test import config

class TestDataTypeStringArray(unittest.TestCase):
    """Tests the string array task datatype"""

    @classmethod
    def setUpClass(cls):
        config.setup_idl_toolbox('test_datatype_stringarray','qa_idltaskengine_datatype_stringarray')

    @classmethod
    def tearDownClass(cls):
        pass

    def test_datatype_stringarray_one_dimension(self):
        """Verify a one dimensional array of strings returns a semicolon separated string list."""
        input = ['foo', 'bar', 'baz']
        expect_dims = [len(input)]
        result = arcpy.QA_IDLTaskEngine_DataType_StringArray_GSF(input, expect_dims)

        self.assertEqual(result[0], ';'.join(str(i) for i in input))

if __name__ == '__main__':
    unittest.main()