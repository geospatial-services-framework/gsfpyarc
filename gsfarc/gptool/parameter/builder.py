"""
The GPTool Parameter Builder is responsible for creating code blocks to be placed into the main GPTool template.
Each create method corresponds to a GPTool method that must be defined in order for it to be a valid tool.
These methods implement the GetParameterInfo, UpdateParameter, and Execute methods of the GPTool Python class.

For example, to define a GPTool in a Python toolbox, start out with a class definition and implement
the methods arcpy expects::

    class myTool(Object):
        def __init__(self):
            self.label = "My Tool"
            self.description = "Tool description"
            self.canRunInBackground = True

        def getParameterInfo(self):
            # builder.create_param_info() goes here

        def is Licensed(self):
            return True

        def updateParameters(self, parameters):
            # builder.create_update_parameter goes here

        def updateMessages(self, parameters):
            return

        def execute(self, parameters, messages):
            # builder.create_pre_execute goes here
            # submit job
            # builder.create_post_execute goes here

"""
from string import Template
import pkgutil
import importlib
from . import templates


def load_templates():
    parameter_map = {}
    for importer, modname, is_pkg in pkgutil.iter_modules(templates.__path__):
        parameter_module = importlib.import_module('gsfarc.gptool.parameter.templates.' + modname )
        parameter_template = parameter_module.template()
        parameter_map[parameter_template.__class__.__name__.upper()] = parameter_template

    return parameter_map

parameter_map = load_templates()


class UnknownDataTypeError(Exception):
    """Error class for raising unknown datatypes"""
    pass

_PARAM_RETURN_TEMPLATE = Template('''
        params = $paramList
        return params
''')

_CHOICELIST_TEMPLATE = Template('''
        ${name}.filter.type="ValueList"
        ${name}.filter.list = $choiceList
''')


_DIRECTION_MAP = {'input' : 'Input',
                  'output': 'Output'
                 }

_PARAM_INDEX_TEMPLATE = Template('''
    i${name} = $idx''')


def convert_list(in_list):
    """Converts a list of strings to a printable list of object names"""

    return ''.join(('[', ','.join(in_list), ']'))


def create_param_info(task_params):
    """
    Builds the code block for the GPTool GetParameterInfo method based on the input task_params.

    :param task_params: A list of task parameters to map to GPTool parameters.
    :return: A string representing the code block to the GPTool GetParameterInfo method.
    """
    gp_params = []
    gp_param_list = []
    gp_param_idx_list = []
    gp_param_idx = 0
    for task_param in task_params:
        # Setup to gp_param dictionary used to substitute against the parameter info template.
        gp_param = {}

        # Convert DataType
        data_type = task_param['type'].upper()
        if 'dimensions' in task_param:
            data_type += 'ARRAY'

        if data_type in parameter_map:
            gp_param['dataType'] = parameter_map[data_type].data_type
        else:
            # No Mapping exists for this data type!
            raise UnknownDataTypeError('Unable to map task datatype: ' + data_type + '.  A template must be created.')

        gp_param['name'] = task_param['name']
        gp_param['displayName'] = task_param['display_name']
        gp_param['direction'] = _DIRECTION_MAP[task_param['direction']]
        gp_param['paramType'] = 'Required' if task_param['required'] else 'Optional'
        # GSF output type translates to a derived output type in Arc
        if gp_param['direction'] is 'Output':
            gp_param['paramType'] = 'Derived'

        gp_param['multiValue'] = True if 'dimensions' in task_param else False

        # Substitute values into the template
        gp_params.append(parameter_map[data_type].get_parameter(task_param).substitute(gp_param))

        # Convert the default value
        if 'default_value' in task_param:
            gp_param['defaultValue'] = task_param['default_value']
            gp_params.append(parameter_map[data_type].default_value().substitute(gp_param))

        # Convert any choicelist
        if 'choice_list' in task_param:
            gp_param['choiceList'] = task_param['choice_list']
            gp_params.append(_CHOICELIST_TEMPLATE.substitute(gp_param))

        # Construct the parameter list and indicies for future reference
        for param_name in parameter_map[data_type].parameter_names(task_param):
            gp_param_list.append(param_name.substitute(gp_param))
            gp_param_idx_list.append(_PARAM_INDEX_TEMPLATE.substitute({'name' : param_name.substitute(gp_param),
                                                                       'idx': gp_param_idx}
                                                                      ))
            gp_param_idx += 1

    # Construct the final parameter string
    gp_params.append(_PARAM_RETURN_TEMPLATE.substitute({'paramList': convert_list(gp_param_list)}))
    return ''.join((''.join(gp_params), ''.join(gp_param_idx_list)))


def create_update_parameter(task_params):
    """
    Builds the code block for the GPTool UpdateParameter method based on the input task_params.

    :param task_params: A list of task parameters from the task info structure.
    :return: A string representing the code block to the GPTool UpdateParameter method.
    """
    gp_params = []
    for param in task_params:
        if param['direction'].upper() == 'OUTPUT':
            continue

        # Convert DataType
        data_type = param['type'].upper()
        if 'dimensions' in param:
            data_type += 'ARRAY'

        if data_type in parameter_map:
            gp_params.append(parameter_map[data_type].update_parameter().substitute(param))

    return ''.join(gp_params)


_PRE_EXECUTE_INIT_TEMPLATE = '''
        #Get all the user input parameters from the GPTool
        input_params = {}
'''


_PRE_EXECUTE_CLEANUP_TEMPLATE = '''
        # Remove any empty values from the input parameters
        for key, value in list(input_params.items()):
            if value is None:
                messages.AddMessage('Removing empty input: ' + key)
                input_params.pop(key)

        messages.AddMessage('Collected input: ' + str(input_params))
        
'''


def create_pre_execute(task_params):
    """
    Builds the code block for the GPTool Execute method before the GSF job is submitted based on
    the input task_params.

    :param task_params: A list of task parameters from the task info structure.
    :return: A string representing the code block to the GPTool Execute method.
    """
    gp_params = [_PRE_EXECUTE_INIT_TEMPLATE]
    for task_param in task_params:
        if task_param['direction'].upper() == 'OUTPUT':
            continue

        # Convert DataType
        data_type = task_param['type'].upper()
        if 'dimensions' in task_param:
            data_type += 'ARRAY'

        if data_type in parameter_map:
            gp_params.append(parameter_map[data_type].pre_execute().substitute(task_param))

    gp_params.append(_PRE_EXECUTE_CLEANUP_TEMPLATE)
    return ''.join(gp_params)


def create_post_execute(task_params):
    """
    Builds the code block for the GPTool Execute method after the GSF job is submitted based on
    the input task_params.

    :param task_params: A list of task parameters from the task info structure.
    :return: A string representing the code block to the GPTool Execute method.
    """

    gp_params = []
    for task_param in task_params:
        if task_param['direction'].upper() == 'INPUT':
            continue

        # Convert DataType
        data_type = task_param['type'].upper()
        if 'dimensions' in task_param:
            data_type += 'ARRAY'

        if data_type in parameter_map:
            gp_params.append(parameter_map[data_type].post_execute().substitute(task_param))

    return ''.join(gp_params)
