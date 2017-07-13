"""

"""

from setuptools import setup
from distutils.core import Command as BaseCommand
from unittest import TestLoader, TextTestRunner


class TestCommand(BaseCommand):
    """Runs the package tests."""
    description = 'Runs all package tests.'

    user_options = [
        ('junit=', None,
         'outputs results to a results.xml file.')
    ]

    def initialize_options(self):
        self.junit = None

    def finalize_options(self):
        pass

    def run(self):
        # Import xmlrunner here so it's not a setup requirement
        import xmlrunner
        test_suite = TestLoader().discover('.')
        if self.junit:
            with open('report.xml', 'wb') as output:
                runner = xmlrunner.XMLTestRunner(output)
                runner.run(test_suite)
        else:
            runner = TextTestRunner(verbosity=2)
            runner.run(test_suite)

setup(name='gsfarc',
      version='1.0.4',
      description='GSF Py Client Utilities for ArcGIS',
      author='Exelis Visual Information Solutions, Inc.',
      packages=['gsfarc',
                'gsfarc.gptool',
                'gsfarc.gptool.parameter',
                'gsfarc.gptool.parameter.templates'],
      package_dir= {'gsfarc' : 'gsfarc'},
      install_requires=[
          'gsf>=1.0.0'
      ],
      package_data = {
          'gsfarc' : [
              'esri/toolboxes/*.xml',
              'esri/toolboxes/*.pyt',
              'doc/_images/*',
              'doc/_modules/*.html',
              'doc/_modules/gsfarc/*.html',
              'doc/_modules/gsfarc/gptool/parameter/*.html',
              'doc/_static/*',
              'doc/*.html',
              'doc/*.js'
          ]
      },
      license='MIT',
      zip_safe=False,
      scripts=['scripts/creategsftoolbox.py'],
      cmdclass=dict(test=TestCommand)
      )