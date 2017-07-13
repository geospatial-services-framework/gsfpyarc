"""
Defines the base template for simple array data types.
"""
from __future__ import absolute_import
from string import Template
from .basic import BASIC


class BASICARRAY(BASIC):

    def default_value(self):
        return Template('''
        ${name}.values = $defaultValue
''')

    def pre_execute(self):
        return Template('''
        input_params['${name}'] = parameters[self.i${name}].values
''')

    def post_execute(self):
        return Template('''
        parameters[self.i${name}].values = task_results['${name}']
''')

def template():
    return BASICARRAY('GPType')