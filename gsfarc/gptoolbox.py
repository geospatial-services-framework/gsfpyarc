"""

"""

import os.path
import gsfarc.system
import gsfarc.gptool.parameter.builder as param_builder
import gsfarc.gptool.help as help_builder
from string import Template



class GPToolbox(object):
    """GPToolbox is used to create GPTool wrappers to GSF tasks"""

    _imports_template = Template('''
import os

try:
    from urllib.request import urlopen, pathname2url, urlretrieve
    from urllib.parse import urlparse, urljoin
except ImportError:
    from urllib2 import urlopen
    from urllib import pathname2url, urlretrieve
    from urlparse import urlparse, urljoin

import time
import arcpy
from gsf import Task

''')

    _class_template = Template('''
class Toolbox(object):
    def __init__(self):
        self.label = "$label"
        self.alias = "$alias"

        # List of tool classes associated with this toolbox
        self.tools = $toolList
''')

    def __init__(self, tasks):
        self.tasks = tasks
        self.toolbox_file = None
        self.alias = 'GSF'

    def create_toolbox(self, filename):
        """
        Creates a new Python toolbox where each task name is a GPTool in the toolbox.

        :param filename: the filename of the generated toolbox
        :param service_name: The name of the ESE service containing the tasks.  Only tasks from
                             one service may be used.
        :param tasks: The list of tasks from the service to build as GPTools.
        """
        filename = os.path.splitext(filename)[0]
        label = os.path.basename(filename)

        # Get task information first so we can build the tool list
        tool_list = []
        for task in self.tasks:
            tool_list.append(task.name)

        fd = os.open(filename + '.pyt', os.O_WRONLY | os.O_CREAT | os.O_EXCL)
        with os.fdopen(fd, 'w') as self.toolbox_file:
            self.toolbox_file.write(self._imports_template.substitute({}))
            toolbox_class = self._class_template.substitute({'label': label,
                                                             'alias': self.alias,
                                                             'toolList': param_builder.convert_list(tool_list)
                                                            })
            self.toolbox_file.write(toolbox_class)

            for task in self.tasks:
                gp_tool = self.create_tool(task)
                self.toolbox_file.write(gp_tool)
                toolbox_help_filename = '.'.join((filename, task.name, 'pyt', 'xml'))
                gp_tool_help = help_builder.create(toolbox_help_filename,task, self.alias)

        return filename

    _tool_template = Template('''
class $taskName(object):
    def __init__(self):
        self.label = "$taskDisplayName"
        self.description = "$taskDescription"
        self.canRunInBackground = $canRunInBackground
        self.task = Task("$taskUri")

    def getParameterInfo(self):

        $parameterInfo

    def isLicensed(self):
        return True

    def updateParameters(self, parameters):
        $updateParameter
        return

    def updateMessages(self, parameters):
        return

    def execute(self, parameters, messages):
        $preExecute
        
        #Make the request and wait for success/failure
        job = self.task.submit(input_params)
        messages.AddMessage('Submitted Job to: ' + self.task.uri)
        messages.AddMessage('Submit Job ID: ' + str(job.job_id))

        job.wait_for_done()
        
        if job.status == 'Failed':
            messages.addErrorMessage("Task failed to execute")
            messages.addErrorMessage(job.error_message)
            raise arcpy.ExecuteError

        messages.AddMessage('Job Finished')
        task_results = job.results
        $postExecute
        return

''')

    def create_tool(self, task):
        """
        Creates a new GPTool for the toolbox.


        """
        gp_tool = dict(taskName=task.name,
                       taskDisplayName=task.display_name,
                       taskDescription=task.description,
                       canRunInBackground=True,
                       taskUri=task.uri
                       )

        gp_tool['parameterInfo'] = param_builder.create_param_info(task.parameters)
        gp_tool['updateParameter'] = param_builder.create_update_parameter(task.parameters)
        gp_tool['preExecute'] = param_builder.create_pre_execute(task.parameters)
        gp_tool['postExecute'] = param_builder.create_post_execute(task.parameters)
        return self._tool_template.substitute(gp_tool)

    def import_script(self, script_name):
        """Finds the script file and copies it into the toolbox"""
        filename = os.path.abspath(script_name)
        with open(filename, 'r') as script_file:
            self.toolbox_file.write(script_file.read())
