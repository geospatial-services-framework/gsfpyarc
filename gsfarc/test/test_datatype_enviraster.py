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
        config.setup_envi_toolbox('test_datatype_enviraster', 'qa_envitaskengine_datatype_enviraster')

    @classmethod
    def tearDownClass(cls):
        pass

    def test_datatype_enviraster_basic(self):
        """Tests enviraster datatype."""

        input_raster = os.path.join(config.TEST_DATA_DIR, 'qb_boulder_msi_enviraster.dat')
        result = arcpy.qa_envitaskengine_datatype_enviraster_GSF(input_raster)

        # Verify result exists.
        self.assertTrue(result.getOutput(0), 'Output Raster URI not set')

        output = result.getOutput(0)
        output_filename = os.path.splitext(os.path.basename(output))[0]
        output_dir = os.path.dirname(output)
        input_dir = os.path.dirname(input_raster)
        input_filename = os.path.splitext(os.path.basename(input_raster))[0]

        # Verify dat file.
        output_file = os.path.join(output_dir, output_filename + '.dat')
        input_file = os.path.join(input_dir, input_filename + '.dat')

        self.assertTrue(os.path.isfile(output_file), 'Output file does not exist: ' + output_file)
        self.assertTrue(filecmp.cmp(output_file, input_file),
                    'Output does not match expected: ' + output_file)

        # Verify hdr file
        output_hdr = os.path.join(output_dir, output_filename + '.hdr')
        input_hdr = os.path.join(input_dir, input_filename + '.hdr')

        self.assertTrue(os.path.isfile(output_file), 'Output file does not exist: ' + output_hdr)

        diff = config.compare_text_files(output_hdr, input_hdr)
        self.assertEqual(diff, '', 'Output does not match expected: ' + output_hdr)
if __name__ == '__main__':
    unittest.main()