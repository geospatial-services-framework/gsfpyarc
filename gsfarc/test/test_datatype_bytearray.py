"""

"""
import unittest


import arcpy
from gsfarc.test import config


class TestDataTypeByteArray(unittest.TestCase):
    """Tests the byte array task datatype"""

    @classmethod
    def setUpClass(cls):
        config.setup_idl_toolbox('test_datatype_bytearray', 'qa_idltaskengine_datatype_bytearray')

    @classmethod
    def tearDownClass(cls):
        pass

    def test_datatype_bytearray_one_dimension(self):
        """Verify a one dimensional array of bytes returns a semicolon separated string list."""
        input = [0, 50, 255]
        expect_dims = [len(input)]
        result = arcpy.QA_IDLTaskEngine_DataType_ByteArray_GSF(input, expect_dims)
        self.assertEqual(result[0], ';'.join(str(i) for i in input))

if __name__ == '__main__':
    unittest.main()
