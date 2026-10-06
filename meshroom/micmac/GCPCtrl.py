__version__ = "1.2.0"

from meshroom.core import desc
from ..common import node

class GCPCtrl(node.MicmacNode, desc.CommandLineNode):
    commandLine = 'mm3d GCPCtrl {imagePatternValue} {orientationInValue} {GCPFileValue} {imageMeasurementsFileValue} {allParams}'
    documentation = 'GCPCtrl: Control the accuracy of an orientation with ground control points.'

    inputs = [
        desc.File(
            name='projectDirectory',
            label='Project Directory',
            description='Project Directory.',
            value='',
            commandLineGroup='', # required to execute mm3d command line
        ),
        desc.File(
            name='imagePattern',
            label='Image Pattern',
            description='Image Pattern.',
            commandLineGroup='', # unnamed parameter
            value='',
        ),
        desc.File(
            name='orientationIn',
            label='Orientation Directory',
            description='Orientation in.',
            commandLineGroup='', # unnamed parameter
            value='',
        ),
        desc.File(
            name='GCPFile',
            label='GCP File',
            description='Ground Control Points file.',
            commandLineGroup='', # unnamed parameter
            value='',
        ),
        desc.File(
            name='imageMeasurementsFile',
            label='Image Measurements File',
            description='Image measurements file.',
            commandLineGroup='', # unnamed parameter
            value='',
        ),
        desc.BoolParam(
            name='CPI',
            label='CPI',
            description='When Calib Per Image has to be used.',
            value=False,
            advanced=True,
        ),
        desc.BoolParam(
            name='ShowU',
            label='Show Unused Point',
            description='Show unused point.',
            value=False,
            advanced=True,
        ),
        desc.BoolParam(
            name='WithDetProj',
            label='With Det Proj',
            description='With detail on all proj.',
            value=False,
            advanced=True,
        ),
        desc.StringParam(
            name='OutTxt',
            label='Output Txt Filename',
            description='TXT file name for Ctrl.',
            value='',
        ),
        desc.File(
            name='OutJSON',
            label='Output JSON Filename',
            description='.geojson file name for Ctrl result.',
            value='',
        ),
    ]

    outputs = [
        desc.File(
            name='OutTxtFile',
            label='Ctrl Txt File',
            description='Output Ctrl txt file.',
            value='{OutTxtValue}.txt',
            commandLineGroup='', # not a command line parameter
        ),
        desc.File(
            name='OutJSONFile',
            label='Ctrl JSON File',
            description='Output Ctrl JSON file.',
            value='{OutJSONValue}.geojson',
            commandLineGroup='', # not a command line parameter
        ),
    ]
