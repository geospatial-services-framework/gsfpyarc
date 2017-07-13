'''
Created on Jan 19, 2016

@author: elefebvre
'''
import os.path
import arcpy


def sys_toolbox_dir():
    """
    Returns this site-package esri toolbox directory.
    """
    return os.path.join(os.path.dirname(os.path.abspath(__file__)), 'esri','toolboxes')

def my_toolbox_dir():
    """Helper method for returning the ArcGIS toolbox directory. """
    return os.path.join(appdata_roaming_dir(), 'ArcToolbox', 'My Toolboxes')

def appdata_roaming_dir():
    """Returns the roaming AppData directory for the installed ArcGIS Desktop."""
    install = arcpy.GetInstallInfo('desktop')
    app_data = arcpy.GetSystemEnvironment("APPDATA")
    product_dir = ''.join((install['ProductName'], major_version()))
    return os.path.join(app_data, 'ESRI', product_dir)

def major_version():
    """Returns the first two version numbers from the current ArcGIS install version"""
    install = arcpy.GetInstallInfo('desktop')
    return '.'.join(install['Version'].split('.')[0:2])
