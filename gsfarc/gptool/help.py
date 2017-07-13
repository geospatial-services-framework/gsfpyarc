"""

"""
import xml.etree.cElementTree as ET

html_begin = '<DIV STYLE="text-align:Left;"><DIV><P><SPAN>'
html_end = '</SPAN></P></DIV></DIV>'


def create(filename, task, alias):
    """Creates a gptool help xml file."""

    metadata = ET.Element('metadata', {'xml:lang': 'en'})
    tool = ET.SubElement(metadata, 'tool', name=task.name,
                         displayname=task.display_name,
                         toolboxalias=alias)
    
    summary = ET.SubElement(tool, 'summary')
    summary.text = ''.join((html_begin, task.description, html_end))

    parameters = ET.SubElement(tool, 'parameters')
    for task_param in task.parameters:
        param = ET.SubElement(parameters, 'param',
                              name=task_param['name'],
                              displayname=task_param['display_name']
                              )
        dialog_ref = ET.SubElement(param, 'dialogReference')
        dialog_ref.text = ''.join((html_begin, task_param['description'], html_end))
        python_ref = ET.SubElement(param, 'pythonReference')
        python_ref.text = ''.join((html_begin,  task_param['description'], html_end))

    dataIdInfo = ET.SubElement(metadata, 'dataIdInfo')
    searchKeys = ET.SubElement(dataIdInfo,'searchKeys')
    keyword1 = ET.SubElement(searchKeys,'keyword')
    keyword1.text = 'GSF'
    keyword2 = ET.SubElement(searchKeys,'keyword')
    keyword2.text = task.name
    idCitation = ET.SubElement(dataIdInfo,'idCitation')
    resTitle = ET.SubElement(idCitation,'resTitle')
    resTitle.text = task.name
    idAbs = ET.SubElement(dataIdInfo,'idAbs')
    idAbs.text = ''.join((html_begin, task.description, html_end))
    idCredit = ET.SubElement(dataIdInfo,'idCredit')
    idCredit.text = '(c) 2017 Exelis Visual Information Solutions, Inc.'
    resTitle.text = task.name
    tree = ET.ElementTree(metadata)
    tree.write(filename)