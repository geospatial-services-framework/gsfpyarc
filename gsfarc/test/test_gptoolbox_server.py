"""
Run gsf tasks tests as GPServices.
"""
import os
import filecmp
import time
import unittest
import arcpy

from gsf import Server
from gsfarc.gptoolbox import GPToolbox
from gsfarc.test.arcgisserver import ArcGISServer
from gsfarc.test import config


class TestGPToolboxServer(unittest.TestCase):
    """Tests gsf tasks as an ArcGIS GPService."""

    @classmethod
    def setUpClass(cls):
        config.setup_workspace()

        # Setup ArcGIS Server Connection
        cls.arcgis_server = ArcGISServer('/'.join((config.ARC_SERVER['url'], 'arcgis')),
                                         config.ARC_SERVER['username'], config.ARC_SERVER['password'])

        # Setup GSF Task Connections
        server = Server(config.GSF_SERVER['server'], config.GSF_SERVER['port'])
        service = server.service(config.ENVI_SERVICE)
        tasks = []
        for task_name in config.GSF_TASKS:
            tasks.append(service.task(task_name))
        server_toolbox = GPToolbox(tasks)

        # Setup GSF gptoolbox
        cls.tbx_file = server_toolbox.create_toolbox('test_gptoolbox_server',
                                                     output_toolbox_dir=arcpy.env.scratchFolder
                                                     )
        arcpy.ImportToolbox(cls.tbx_file)

    @classmethod
    def tearDownClass(cls):
        pass

    def dont_test_spectral_index_server(self):
        """Tests Spectral Index using input raster URI and runs from ArcServer"""
        input_raster_uri = '/'.join((config.GSF_SERVER['data_url'], 'qb_boulder_msi.dat'))
        index = 'Normalized Difference Vegetation Index'
        result = arcpy.SpectralIndex_GSF(None, index, None, input_raster_uri)
        self.assertTrue(result[0], 'Output Raster URI not set')

        service_name = 'spectralIndex'
        config.publish_service(service_name, result)
        service_name = '/'.join((config.ARC_SERVER['serviceFolder'], service_name))

        service_url = '/'.join((config.ARC_SERVER['url'],
                                'arcgis',
                                'services'
                                ))
        connection_string = ';'.join((service_url, service_name))
        arcpy.ImportToolbox(connection_string)

        #Run the GPService Task
        result = arcpy.SpectralIndex_spectralIndex(None, index, input_raster_uri)
        while result.status < 4:
            time.sleep(0.2)

        self.assertEqual(result.status, 4, result.getMessages(2))
        self.assertTrue(result.getOutput(0), 'Output Raster URI not set')

        # Compare result against the test file on disk
        expected_file = os.path.join(config.TEST_DATA_DIR, 'qb_boulder_ndvi.tif')
        self.assertTrue(filecmp.cmp(result.getOutput(0), expected_file),
                        'Output does not match expected raster.')

        # TODO: Needs to be called in the case of exceptions
        self.arcgis_server.delete_service(service_name, 'GPServer')