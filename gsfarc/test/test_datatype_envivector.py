"""
Tests the Server GP Toolbox.

Tests the generated toolbox by running the tools through arcpy with test data.
"""
import os
import filecmp
import unittest
import arcpy

from gsfarc.test import config


class TestGPToolbox(unittest.TestCase):
    """Tests the server GPToolbox class"""

    @classmethod
    def setUpClass(cls):
        """Class setup creates a toolbox file wrapper to GSF."""
        config.setup_envi_toolbox('test_datatype_envivector', 'qa_envitaskengine_datatype_envivector')

    @classmethod
    def tearDownClass(cls):
        pass

    def test_datatype_envivector_basic(self):
        """Tests envivector datatype."""

        input_vector = os.path.join(config.TEST_DATA_DIR, 'qb_boulder_msi_vectors.shp')
        result = arcpy.qa_envitaskengine_datatype_ENVIVector_GSF(input_vector)

        # Verify result exists.
        self.assertTrue(result.getOutput(0), 'Output Raster URI not set')

        output_shp = result.getOutput(0)
        output_filename = os.path.splitext(os.path.basename(output_shp))[0]
        output_dir = os.path.dirname(output_shp)
        input_dir = os.path.dirname(input_vector)
        input_filename = os.path.splitext(os.path.basename(input_vector))[0]

        # Verify files
        exp_extensions = ['.shp', '.shx', '.dbf', '.prj', '.shp.qtr']
        for ext in exp_extensions:

            output_file = os.path.join(output_dir, output_filename + ext)
            input_file = os.path.join(input_dir, input_filename + ext)

            # Verify file exists.
            self.assertTrue(os.path.isfile(output_file), 'Output file does not exist: ' + output_file)

            # Compare output to input.
            self.assertTrue(filecmp.cmp(output_file, input_file),
                        'Output does not match expected: ' + output_file)


if __name__ == '__main__':
    unittest.main()