"""

"""

import unittest

import arcpy
from gsfarc.test import config

class TestDataTypeLongArray(unittest.TestCase):
    """Tests the long array task datatype"""

    @classmethod
    def setUpClass(cls):
        config.setup_idl_toolbox('test_datatype_longarray', 'qa_idltaskengine_datatype_longarray')

    @classmethod
    def tearDownClass(cls):
        pass

    def test_datatype_longarray_one_dimension(self):
        """Verify a one dimensional array of longs returns a semicolon separated string list."""
        input = [0, 2147483647, -2147483647]
        expect_dims = [len(input)]
        result = arcpy.QA_IDLTaskEngine_DataType_LongArray_GSF(input, expect_dims)
        self.assertEqual(result[0], ';'.join(str(i) for i in input))

if __name__ == '__main__':
    unittest.main()
