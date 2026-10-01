__version__ = "1.2.0"

from meshroom.core import desc
from ..common import node

class TapiocaFile(node.MicmacNode, desc.CommandLineNode):
    commandLine = 'mm3d Tapioca File {xmlPathValue} {resolutionValue} {allParams}'
    documentation = 'Tapioca File: Detect and match tie points between image pairs listed in an XML file.'

    inputs = [
        desc.File(
            name='projectDirectory',
            label='Project Directory',
            description='Project Directory.',
            value="",
            commandLineGroup='', # required to execute mm3d command line
        ),
        desc.File(
            name='xmlPath',
            label='XML File Path',
            description='XML file path of pair.',
            commandLineGroup='', # unnamed parameter
            value="",
        ),
        desc.IntParam(
            name='resolution',
            label='Resolution',
            description='Resolution.',
            commandLineGroup='', # unnamed parameter
            value=-1,
            range=(-1, 16000, 10),
        ),
        desc.BoolParam(
            name='ExpTxt',
            label='Export Files In Txt',
            description='Export files in text format (if false binary).', 
            value=False,
        ),
        desc.BoolParam(
            name='NoMax',
            label='No Max',
            description='No max.', 
            value=False,
        ),
        desc.BoolParam(
            name='NoMin',
            label='No Min',
            description='No min.', 
            value=False,
        ),
        desc.BoolParam(
            name='NoUnknown',
            label='No Unknown',
            description='No unknown.', 
            value=False,
        ),
        desc.FloatParam(
            name='Ratio',
            label='ANN Ratio',
            description='ANN closeness ration.',
            value=0.6,
            range=(0.1, 1.0, 0.1),
        ),
    ]

    outputs = [
        desc.File(
            name='PostFix',
            label='Homol Directory', # Directory Postfix
            description='Homol Directory.',
            value="Tapioca",
            invalidate=False,
        ),
    ]
