"""

"""

import unittest
import os
import arcpy
from gsfarc.test import config


class TestDatatypeENVIURI(unittest.TestCase):
    """Tests the ENVIURI task datatype"""

    @classmethod
    def setUpClass(cls):
        """Class setup creates a toolbox file wrapper to GSF."""
        config.setup_envi_toolbox('test_datatype_enviuri', 'QA_ENVITaskEngine_DataType_ENVIURI')

    @classmethod
    def tearDownClass(cls):
        pass

    def test_datatype_enviuri_file_uri(self):
        """Tests the enviuri datatype with file uri."""
        inputENVIURI = os.path.join(config.TEST_DATA_DIR,'qb_boulder_msi.dat')
        result = arcpy.QA_ENVITaskEngine_DataType_ENVIURI_GSF(inputENVIURI)
        self.assertEqual(result[0], inputENVIURI)

    def test_datatype_enviuri_url(self):
        """Tests the enviuri datatype with http url."""
        inputENVIURI = '/'.join((config.GSF_SERVER['data_url'], 'qb_boulder_msi.dat'))
        result = arcpy.QA_ENVITaskEngine_DataType_ENVIURI_GSF(inputENVIURI)
        self.assertEqual(result[0], inputENVIURI)

    def test_datatype_enviuri_string(self):
        """Tests the enviuri datatype with arbitrary string."""
        inputENVIURI = 'foo'
        result = arcpy.QA_ENVITaskEngine_DataType_ENVIURI_GSF(inputENVIURI)
        self.assertEqual(result[0], inputENVIURI)

if __name__ == '__main__':
    unittest.main()