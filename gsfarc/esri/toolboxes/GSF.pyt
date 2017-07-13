"""
Toolbox for creating gptools from an ese task endpoint.
"""
import os.path
import arcpy
from gsf import Server
from gsfarc.gptoolbox import GPToolbox

# Python 3
try:
    from urllib.parse import urlparse
except ImportError:
    from urlparse import urlparse


class Toolbox(object):
    def __init__(self):
        """Define the toolbox (the name of the toolbox is the name of the
        .pyt file)."""
        self.label = "GSF"
        self.alias = "gsf"

        # List of tool classes associated with this toolbox
        self.tools = [CreateTool]


class CreateTool(object):
    def __init__(self):
        """Define the tool (tool name is the name of the class)."""
        self.label = "Create Tool"
        self.description = "Create a tool from an ESE task endpoint."
        self.canRunInBackground = False

    def getParameterInfo(self):
        """Define parameter definitions"""

        # Task Endpoint
        param0 = arcpy.Parameter(
            displayName="Task Endpoint",
            name="taskEndpoint",
            datatype="GPString",
            parameterType="required",
            direction="input")

        # Toolbox Name
        param1 = arcpy.Parameter(
            displayName="Output Toolbox",
            name="outputToolbox",
            datatype="DEToolbox",
            parameterType="required",
            direction="output")

        return [param0, param1]

    def isLicensed(self):
        """Set whether tool is licensed to execute."""
        return True

    def updateParameters(self, parameters):
        """Modify the values and properties of parameters before internal
        validation is performed.  This method is called whenever a parameter
        has been changed."""
        return

    def updateMessages(self, parameters):
        """Modify the messages created by internal validation for each tool
        parameter.  This method is called after internal validation."""
        return

    def execute(self, parameters, messages):
        """The source code of the tool."""

        # Get toolbox path.
        toolbox_path = os.path.abspath(parameters[1].valueAsText)
        # Get toolbox directory.
        toolbox_dir = os.path.dirname(os.path.realpath(toolbox_path))
        # Check writability.
        if not os.access(toolbox_dir, os.W_OK):
            messages.addErrorMessage("Toolbox directory is not writable.")
            raise arcpy.ExecuteError

        # Get task name, service name, etc.
        parsed_url = urlparse(parameters[0].valueAsText)
        parsed_netloc = parsed_url.netloc.split(':')
        host = parsed_netloc[0]
        port = parsed_netloc[1] if len(parsed_netloc) > 1 else '9191'

        split_path = parsed_url.path.split('/')
        if len(split_path) < 5:
            messages.addErrorMessage('Task name not found in url.')
            raise arcpy.ExecuteError

        task_name = split_path[4]
        service_name = split_path[3]

        #  Messaging.
        messages.AddMessage('toolbox path: ' + toolbox_path)
        messages.AddMessage('service name: ' + service_name)
        messages.AddMessage('task name: ' + task_name)

        # Create toolbox.
        server = Server(host, port)
        task = server.service(service_name).task(task_name)
        toolbox = GPToolbox([task])
        toolbox.create_toolbox(toolbox_path)

        return
