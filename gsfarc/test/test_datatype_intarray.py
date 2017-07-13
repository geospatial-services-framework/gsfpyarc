"""

"""
import unittest

import arcpy
from gsfarc.test import config

class TestDataTypeIntArray(unittest.TestCase):
    """Tests the int array task datatype"""

    @classmethod
    def setUpClass(cls):
        config.setup_idl_toolbox('test_datatype_intarray', 'qa_idltaskengine_datatype_intarray')

    @classmethod
    def tearDownClass(cls):
        pass

    def test_one_dimension(self):
        """Verify A one dimensional array of ints returns a semicolon separated string list."""
        input = [1,2,3,4,5]
        expect_dims = [len(input)]
        result = arcpy.QA_IDLTaskEngine_DataType_IntArray_GSF(input, expect_dims)
        print(result)
        print(result.getOutput(0))

        self.assertEqual(result[0], ';'.join(str(i) for i in input))

if __name__ == '__main__':
    unittest.main()
