"""

"""

import unittest

import arcpy
from gsfarc.test import config


class TestDataTypeULongArray(unittest.TestCase):
    """Tests the unsigned long array task datatype"""

    @classmethod
    def setUpClass(cls):
        config.setup_idl_toolbox('test_datatype_ulongarray', 'qa_idltaskengine_datatype_ulongarray')

    @classmethod
    def tearDownClass(cls):
        pass

    def test_datatype_ulongarray_one_dimension(self):
        """Verify a one dimensional array of unsigned longs returns a semicolon separated string list."""
        input = [0, 2147483647, 42]
        expect_dims = [len(input)]
        result = arcpy.QA_IDLTaskEngine_DataType_UlongArray_GSF(input, expect_dims)
        self.assertEqual(result[0], ';'.join(str(i) for i in input))

if __name__ == '__main__':
    unittest.main()
