"""

"""
import unittest
import arcpy
from numpy import pi
from gsfarc.test import config


class TestDatatypeInt(unittest.TestCase):
    """Tests the int task datatype"""

    @classmethod
    def setUpClass(cls):
        """Class setup creates a toolbox file wrapper to GSF."""
        config.setup_idl_toolbox('test_datatype_int', 'qa_idltaskengine_datatype_int')
        config.setup_envi_toolbox('test_datatype_int_choicelist', 'qa_envitaskengine_datatype_int')

    @classmethod
    def tearDownClass(cls):
        pass

    def test_datatype_int_max(self):
        """Tests the int datatype maximum value."""
        input = 32767
        result = arcpy.QA_IDLTaskEngine_DataType_Int_GSF(input)

        self.assertEqual(int(result.getOutput(0)), input)

    def test_datatype_int_default(self):
        """Tests the int datatype with a default."""
        result = arcpy.QA_IDLTaskEngine_DataType_Int_GSF()

        self.assertEqual(int(result.getOutput(0)), 42)

    def test_datatype_int_choicelist(self):
        """Tests the int datatype with a choicelist."""
        input = 5
        result = arcpy.QA_ENVITaskEngine_DataType_Int_GSF()

        self.assertEqual(int(result.getOutput(0)), input)

    def test_datatype_int_min(self):
        """Tests the int datatype minimum value."""
        input = -32768
        result = arcpy.QA_IDLTaskEngine_DataType_Int_GSF(input)

        self.assertEqual(int(result.getOutput(0)), int(input))

    def test_datatype_int_demote(self):
        """Tests the int datatype with a floating point value."""
        input = pi
        result = arcpy.QA_IDLTaskEngine_DataType_Int_GSF(input)

        self.assertAlmostEqual(int(result.getOutput(0)), int(input))

if __name__ == '__main__':
    unittest.main()