"""

"""
import os
import arcpy
import shutil
import stat
import difflib
import glob

from gsf import Server
from gsfarc.gptoolbox import GPToolbox


GSF_SERVER = dict(server='localhost',
                  port='9191',
                  data_url='http://localhost:9191/ese/data')

ENVI_SERVICE = 'ENVI'
IDL_SERVICE = 'IDL'

EXELIS_DIR = os.path.join('C:\\', 'Program Files', 'Exelis')

IDL_TASK_DIR = os.path.join(EXELIS_DIR, 'IDL85', 'lib', 'tasks', 'templates')
ENVI_TASK_DIR = os.path.join(EXELIS_DIR, 'ENVI53', 'custom_code')
TEST_TASK_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'tasks')

ARC_SERVER = {
    'uri' : os.path.join(os.path.dirname(os.path.abspath(__file__)),
                         'arccatalog',
                         'engefase102vm_6080_publisher.ags'),
    'url' : 'http://engefase102vm:6080',
    'serviceFolder' : 'qa',
    'username' : 'admin',
    'password' : 'testlab'
}

WORKSPACE = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                         'workspace'
                         )
SCRATCH_WORKSPACE = os.path.join(WORKSPACE, 'scratch')

TEST_DATA_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                         'data'
                         )


def remove_toolbox(toolbox_file):
    toolbox_file = os.path.splitext(toolbox_file)[0]
    for f in glob.glob(toolbox_file + '*'):
        os.remove(f)


def install_task(task_name, directory):
    task_def_name = task_name + '.task'
    task_pro_name = task_name + '.pro'
    task_def_src = os.path.join(TEST_TASK_DIR, task_def_name)
    task_pro_src = os.path.join(TEST_TASK_DIR, task_pro_name)
    task_def_dst = os.path.join(directory, task_def_name)
    task_pro_dst = os.path.join(directory, task_pro_name)
    if os.path.exists(task_def_dst):
        os.chmod(task_def_dst, stat.S_IWRITE)
    if os.path.exists(task_pro_dst):
        os.chmod(task_pro_dst, stat.S_IWRITE)

    shutil.copyfile(task_def_src, task_def_dst)
    shutil.copyfile(task_pro_src, task_pro_dst)


def compare_text_files(file1, file2):
    # ***Removes whitespace, empty lines, and newline chars***
    # Empty string as return value means files are the same.

    # Open, read lines to string list, remove any newline chars, and filter out empty strings/lines.
    text1 = list(filter(None, map(str.rstrip, open(file1, 'U').readlines())))
    text2 = list(filter(None, map(str.rstrip, open(file2, 'U').readlines())))

    return ''.join(difflib.unified_diff(text1, text2))


def setup_workspace():
    # Setup arcgis workspaces
    if not os.path.isdir(WORKSPACE):
        os.mkdir(WORKSPACE)
    arcpy.env.workspace = WORKSPACE

    if not os.path.isdir(SCRATCH_WORKSPACE):
        os.mkdir(SCRATCH_WORKSPACE)
    arcpy.env.scratchWorkspace = SCRATCH_WORKSPACE


def publish_service(service_name, results):
    """Publishes the results list to an ArcGIS Server specified in the config module"""
    # Create Service draft.
    sddraft = arcpy.CreateUniqueName(service_name + '.sddraft')
    info = arcpy.CreateGPSDDraft(results,
                                 sddraft,
                                 service_name,
                                 folder_name=ARC_SERVER['serviceFolder'],
                                 showMessages='INFO'
                                 )

    sd = arcpy.CreateUniqueName(service_name + '.sd')
    info = arcpy.StageService_server(sddraft, sd)

    info = arcpy.UploadServiceDefinition_server(sd, ARC_SERVER['uri'])
    return sd


def setup_envi_toolbox(toolbox_name, task_name):
    setup_workspace()

    install_task(task_name, ENVI_TASK_DIR)
    server = Server(GSF_SERVER['server'], GSF_SERVER['port'])
    task = server.service(ENVI_SERVICE).task(task_name)
    server_toolbox = GPToolbox([task])

    #Create the toolbox
    remove_toolbox(os.path.join(arcpy.env.scratchFolder, toolbox_name))
    tbx_file = server_toolbox.create_toolbox(os.path.join(arcpy.env.scratchFolder, toolbox_name))
    arcpy.ImportToolbox(tbx_file)
    return tbx_file


def setup_idl_toolbox(toolbox_name, task_name):
    setup_workspace()

    # Setup GSF Task Connections
    install_task(task_name, IDL_TASK_DIR)
    server = Server(GSF_SERVER['server'], GSF_SERVER['port'])
    task = server.service(IDL_SERVICE).task(task_name)
    server_toolbox = GPToolbox([task])

    # Setup GSF gptoolbox
    remove_toolbox(os.path.join(arcpy.env.scratchFolder, toolbox_name))
    tbx_file = server_toolbox.create_toolbox(os.path.join(arcpy.env.scratchFolder, toolbox_name))
    arcpy.ImportToolbox(tbx_file)
    return tbx_file
