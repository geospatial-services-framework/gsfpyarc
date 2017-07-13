"""

"""
import unittest

import arcpy
from gsfarc.test import config


class TestDataTypeBoolArray(unittest.TestCase):
    """Tests the bool array task datatype"""

    @classmethod
    def setUpClass(cls):
        config.setup_envi_toolbox('test_datatype_boolarray', 'qa_envitaskengine_datatype_boolarray')

    @classmethod
    def tearDownClass(cls):
        pass

    def test_boolarray_one_dimension(self):
        """Verify a one dimensional array of bools returns a semicolon separated string list."""
        input = [True, True, False, True]
        expect_dims = [len(input)]
        result = arcpy.QA_ENVITaskEngine_DataType_BoolArray_GSF(input, expect_dims)
        self.assertEqual(str(result.getOutput(0)), 'true;true;false;true')

if __name__ == '__main__':
    unittest.main()
