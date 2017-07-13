"""

"""

import unittest

import arcpy
from gsfarc.test import config

class TestDataTypeUIntArray(unittest.TestCase):
    """Tests the unsigned int array task datatype"""

    @classmethod
    def setUpClass(cls):
        config.setup_idl_toolbox('test_datatype_uintarray', 'qa_idltaskengine_datatype_uintarray')

    @classmethod
    def tearDownClass(cls):
        pass

    def test_datatype_uintarray_one_dimension(self):
        """Verify a one dimensional array of unsigned ints returns a semicolon separated string list."""
        input = [0, 65535, 255]
        expect_dims = [len(input)]
        result = arcpy.QA_IDLTaskEngine_DataType_UIntArray_GSF(input, expect_dims)
        self.assertEqual(result[0], ';'.join(str(i) for i in input))

if __name__ == '__main__':
    unittest.main()
