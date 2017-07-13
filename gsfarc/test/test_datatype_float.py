"""

"""
import unittest
import arcpy
from numpy import pi
from gsfarc.test import config


class TestDatatypeFloat(unittest.TestCase):
    """Tests the float task datatype"""

    @classmethod
    def setUpClass(cls):
        """Class setup creates a toolbox file wrapper to GSF."""
        config.setup_idl_toolbox('test_datatype_float', 'qa_idltaskengine_datatype_float')

    @classmethod
    def tearDownClass(cls):
        pass

    def test_datatype_float_positive(self):
        """Tests the float datatype with a positive value."""
        input = pi
        result = arcpy.QA_IDLTaskEngine_DataType_Float_GSF(input)

        self.assertAlmostEqual(float(result.getOutput(0)), input, places=6)

    def test_datatype_float_negative(self):
        """Tests the float datatype with a negative value."""
        input = -pi
        result = arcpy.QA_IDLTaskEngine_DataType_Float_GSF(input)

        self.assertAlmostEqual(float(result.getOutput(0)), input, places=6)


if __name__ == '__main__':
    unittest.main()