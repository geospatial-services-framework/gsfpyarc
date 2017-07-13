"""

"""
from __future__ import absolute_import
from .basic import BASIC
from string import Template


class STRING(BASIC):

    def default_value(self):
        return Template('''
        ${name}.value = "$defaultValue"
''')

def template():
    return STRING('GPString')