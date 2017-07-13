"""

"""
from __future__ import absolute_import
from ..template import Template as ParamTemplate
from string import Template


class ENVIVECTOR(ParamTemplate):
    def get_parameter(self, task_param):
        if task_param['direction'].upper() == 'OUTPUT':
            return Template('''
        $name = arcpy.Parameter(
            displayName="$displayName",
            name="$name",
            datatype="$dataType",
            parameterType="$paramType",
            direction="$direction",
            multiValue=$multiValue
        )
''')
        # Return the input template
        else:
            return Template('''
        $name = arcpy.Parameter(
            displayName="$displayName",
            name="$name",
            datatype=["$dataType","GPString"],
            parameterType="$paramType",
            direction="$direction",
            multiValue=$multiValue
        )
''')

    def parameter_names(self, task_param):
        return [Template('$name')]

    def default_value(self):
        return Template('''
        ${name}.value = "$defaultValue"
''')

    def update_parameter(self):
        return Template('')

    def pre_execute(self):
        return Template('''

        path = str(parameters[self.i${name}].value)
        parsed_path = urlparse(path)
        # Use a file scheme if the user does not provide one
        schemes = ['http','file']
        if any(scheme in parsed_path.scheme for scheme in schemes):
            pathUri = path
        else:
            pathUri = pathname2url(path)
            pathUri = urljoin('file:',pathUri)
        input_params['${name}'] = {'url': pathUri,
                                   'factory':'URLVector'
                                  }
''')

    def post_execute(self):
        return Template('''
        if '${name}' in task_results:
            parsed_url = urlparse(task_results['${name}']['url'])
            schemes = ['http', 'https', 'ftp', 'ftps']
            if any(scheme in parsed_url.scheme for scheme in schemes):

                # Download $name to the scratch directory
                filename = task_results['${name}']['url'].split('/')[-1]
                scratch_file = os.path.join(arcpy.env.scratchFolder, filename)
                urlretrieve(task_results['${name}']['url'], scratch_file)

                # Download $name auxiliary data to the scratch directory
                if 'auxiliary_url' in task_results['${name}']:
                    for auxiliary_url in task_results['${name}']['auxiliary_url']:
                        aux_filename = auxiliary_url.split('/')[-1]
                        scratch_aux_file = os.path.join(arcpy.env.scratchFolder, aux_filename)
                        urlretrieve(auxiliary_url, scratch_aux_file)

                parameters[self.i${name}].value = scratch_file
            else:
                parameters[self.i${name}].value = task_results['${name}']['url']
''')


def template():
    return ENVIVECTOR('DEShapefile')