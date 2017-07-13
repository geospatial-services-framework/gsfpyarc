"""

"""
from __future__ import absolute_import
from string import Template as StrTemplate
from abc import ABCMeta, abstractmethod


class Template(object):
    """
Interface class for mapping ESE parameters to ArcGIS GPTool parameters.
    """
    __metaclass__ = ABCMeta

    def __init__(self, data_type):
        self.data_type = data_type

    @abstractmethod
    def get_parameter(self, task_param):
        """
        Defines the code block for this parameter data type in the GPTool GetParameterInfo method.  All code returned must begin with 2 indents. The template is substituted against the GP parameter
        dictionary.

        :param task_param: The ESE task parameter information.
        :return: Returns the string.Template object.
        """
        return

    @abstractmethod
    def parameter_names(self, task_param):
        """
        Defines the code block for the parameter variable names in the GPTool GetParameterInfo method.

        :param task_param: The ESE task parameter
        :return: A list of string.Template objects representing the parameter variable names defined in get_parameter.

        """
        return

    @abstractmethod
    def default_value(self):
        """
        Defines the code block for this parameter data type in the GPTool GetParameterInfo if a default value exists.

        :return: Returns the string.Template object.
        """
        return

    def update_parameter(self):
        """
        Defines the code block for this parameter data type in the GPTool UpdateParameter method.

        :return: Returns the string.Template object.
        """
        return StrTemplate('')

    @abstractmethod
    def pre_execute(self):
        """
        Defines the code block for this parameter data type in the GPTool Execute method before the job is
        submitted to GSF

        :return: Returns the string.Template object
        """
        return

    @abstractmethod
    def post_execute(self):
        """
        Defines the code block for this parameter data type in the GPTool Execute method after the job is
        submitted to GSF

        :return: Returns the the string.Template object
        """
        return
