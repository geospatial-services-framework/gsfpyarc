"""

"""

import unittest
import arcpy
from gsfarc.test import config


class TestDatatypeUInt(unittest.TestCase):
    """Tests the uint task datatype"""

    @classmethod
    def setUpClass(cls):
        """Class setup creates a toolbox file wrapper to GSF."""
        config.setup_idl_toolbox('test_datatype_uint', 'qa_idltaskengine_datatype_uint')

    @classmethod
    def tearDownClass(cls):
        pass

    def test_datatype_uint_max(self):
        """Tests the uint datatype."""
        input = 65535
        result = arcpy.QA_IDLTaskEngine_DataType_UInt_GSF(input)

        self.assertEqual(int(result.getOutput(0)), input)

    def test_datatype_uint_min(self):
        """Tests the uint datatype."""
        input = 0
        result = arcpy.QA_IDLTaskEngine_DataType_UInt_GSF(input)

        self.assertEqual(int(result.getOutput(0)), int(input))

if __name__ == '__main__':
    unittest.main()