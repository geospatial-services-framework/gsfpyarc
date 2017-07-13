"""

"""
from __future__ import absolute_import
from ..template import Template as ParamTemplate
from string import Template


class ENVIURI(ParamTemplate):
    def get_parameter(self, task_param):
        # Input uses a composite data type of both defile and gpstring.
        # This allows for url strings while also providing file selection in the UI.
        if task_param['direction'].upper() == 'INPUT':
            return Template('''
        $name = arcpy.Parameter(
            displayName="$displayName",
            name="$name",
            datatype=["DEFile","GPString"],
            parameterType="$paramType",
            direction="$direction",
            multiValue=$multiValue
        )
''')
        # Return the output template
        else:
            return Template('''
        $name = arcpy.Parameter(
            displayName="$displayName",
            name="$name",
            datatype="GPString",
            parameterType="$paramType",
            direction="$direction",
            multiValue=$multiValue
        )
    ''')

    def parameter_names(self, task_param):
        return [Template('${name}')]

    def default_value(self):
        return Template('''
        ${name}.value = "$defaultValue"
''')

    def pre_execute(self):
        return Template('''
        input_params['${name}'] = parameters[self.i${name}].valueAsText
''')

    def post_execute(self):
        return Template('''
        parameters[self.i${name}].value = task_results['${name}']
''')

def template():
    return ENVIURI('DEFile')