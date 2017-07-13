"""

"""
import unittest
from gsfarc.test import config
import arcpy


class TestDatatypeBool(unittest.TestCase):
    """Tests the server GPToolbox class"""

    @classmethod
    def setUpClass(cls):
        """Class setup creates a toolbox file wrapper to GSF."""
        cls.tbx_file = config.setup_envi_toolbox('test_datatype_bool', 'QA_ENVITaskEngine_DataType_Bool')

    @classmethod
    def tearDownClass(cls):
        pass

    def test_datatype_bool_true(self):
        """Tests the bool datatype."""
        inputBool = True
        result = arcpy.QA_ENVITaskEngine_DataType_Bool_GSF(inputBool)
        self.assertEqual(result.getOutput(0), 'true')

    def test_datatype_bool_false(self):
        """Tests the bool datatype."""
        inputBool = False
        result = arcpy.QA_ENVITaskEngine_DataType_Bool_GSF(inputBool)
        self.assertEqual(result.getOutput(0), 'false')

if __name__ == '__main__':
    unittest.main()