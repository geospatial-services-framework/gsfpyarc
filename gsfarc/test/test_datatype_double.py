"""

"""
import unittest
import arcpy
from numpy import pi
from gsfarc.test import config

class TestDatatypeDouble(unittest.TestCase):
    """Tests the double task datatype"""

    @classmethod
    def setUpClass(cls):
        """Class setup creates a toolbox file wrapper to GSF."""
        config.setup_idl_toolbox('test_datatype_double', 'qa_idltaskengine_datatype_double')

    @classmethod
    def tearDownClass(cls):
        pass

    def test_datatype_double_positive(self):
        """Tests the double datatype with a positive value."""
        input = pi
        result = arcpy.QA_IDLTaskEngine_DataType_Double_GSF(input)

        self.assertAlmostEqual(float(result.getOutput(0)), input, places=14)

    def test_datatype_double_negative(self):
        """Tests the double datatype with a negative value."""
        input = -pi
        result = arcpy.QA_IDLTaskEngine_DataType_Double_GSF(input)

        self.assertAlmostEqual(float(result.getOutput(0)), input, places=14)


if __name__ == '__main__':
    unittest.main()