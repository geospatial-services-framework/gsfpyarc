"""

"""
import os
from setuptools import setup, find_packages

here = os.path.abspath(os.path.dirname(__file__))

# Get the long description from the README file
with open(os.path.join(here, 'README.md')) as f:
    long_description = f.read()

setup(name='gsfarc',
      version='2.0.0',
      description='GSF Py Client Utilities for ArcGIS',
      long_description=long_description,
      url='https://github.com/geospatial-services-framework/gsfpyarc',
      author='NV5 Geospatial',
      author_email='gsf@harris.com',
      packages=find_packages(),
      install_requires=[
          'gsf>=2.0.0.dev18'
      ],
      package_data = {
          'gsfarc': [
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
      entry_points={
          'console_scripts': [
                'gsftoolbox = gsfarc.__main__:main'
            ]
      }
      )