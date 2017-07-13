"""
Tests the GSF Toolbox.
"""

import unittest
import json
import arcpy
import os
import gsfarc.system


class TestToolboxGSF(unittest.TestCase):
    """Tests the server GPToolbox class"""

    # Load test configuration info.
    with open('input.json') as data_file:
        test_config = json.load(data_file)

    # URL to task endpoint from which to create a tool.
    task_url = '/'.join((test_config['url'], test_config['root'],
                        'services', test_config['serviceName'],
                        test_config['taskName']))

    # Build path to output toolbox file.
    output_toolbox_path = os.path.abspath(os.path.join(gsfarc.system.my_toolbox_dir(),
                                                     test_config['outputToolboxName']))
    output_toolbox_path_with_ext = output_toolbox_path + '.pyt'

    @classmethod
    def setUpClass(cls):
        """Class setup imports CreateESEToolbox."""
        # Import HGS toolbox.
        toolbox_path = os.path.abspath('../' + cls.test_config['toolboxName'] + '.pyt')
        arcpy.ImportToolbox(toolbox_path)

    @classmethod
    def tearDownClass(cls):
        """Class teardown removes the toolbox file."""

        # Remove pyt file.
        arcpy.RemoveToolbox(cls.output_toolbox_path_with_ext)
        if os.path.isfile(cls.output_toolbox_path_with_ext):
            os.remove(cls.output_toolbox_path_with_ext)

    def test_create_tool(self):
        """Verify Create Tool for ISODATAClassification task creates a valid toolbox file."""

        # Create tool.
        result = arcpy.CreateTool_gsf(self.task_url, self.output_toolbox_path)

        # Verify.
        self.assertEqual(result[0], self.output_toolbox_path)
        self.assertTrue(os.path.isfile(self.output_toolbox_path_with_ext))

        # Import toolbox and make sure it is available.
        arcpy.ImportToolbox(self.output_toolbox_path_with_ext)
        toolbox_list = arcpy.ListToolboxes()
        toolbox_name = self.test_config['outputToolboxName'] + '(' + self.test_config['alias'] + ')'
        self.assertTrue(toolbox_name in toolbox_list)

    def test_create_tool_extension(self):
        """
        Verify Create Tool for ISODATAClassification task
        creates a valid toolbox file when output toolbox is specified with
        .pyt extension.
        """

        # Remove pyt file.
        if os.path.isfile(self.output_toolbox_path_with_ext):
            os.remove(self.output_toolbox_path_with_ext)

        # Create tool.
        output_toolbox = self.output_toolbox_path_with_ext
        result = arcpy.CreateTool_gsf(self.task_url, output_toolbox)

        # Verify.
        self.assertEqual(result[0], self.output_toolbox_path_with_ext)
        self.assertTrue(os.path.isfile(self.output_toolbox_path_with_ext))

        # Import toolbox and make sure it is available.
        arcpy.ImportToolbox(self.output_toolbox_path_with_ext)
        toolbox_list = arcpy.ListToolboxes()
        toolbox_name = self.test_config['outputToolboxName'] + '(' + self.test_config['alias'] + ')'
        self.assertTrue(toolbox_name in toolbox_list)

if __name__ == '__main__':
    unittest.main()
