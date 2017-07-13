"""

"""
import unittest

import arcpy
from gsfarc.test import config

class TestDataTypeFloatArray(unittest.TestCase):
    """Tests the float array task datatype"""

    @classmethod
    def setUpClass(cls):
        config.setup_idl_toolbox('test_datatype_floatarry', 'qa_idltaskengine_datatype_floatarray')

    @classmethod
    def tearDownClass(cls):
        pass

    def test_datatype_floatarray_one_dimension(self):
        """Verify a one dimensional array of floats returns a semicolon separated string list."""
        input = [0, 5.64777, -254.3]
        expect_dims = [len(input)]
        result = arcpy.QA_IDLTaskEngine_DataType_FloatArray_GSF(input, expect_dims)
        print(result)
        resultArr = result.getOutput(0).split(';')
        for index in range(len(input)):
            self.assertAlmostEqual(input[index],float(resultArr[index]),places=5)
if __name__ == '__main__':
    unittest.main()
