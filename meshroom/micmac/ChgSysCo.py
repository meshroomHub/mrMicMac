__version__ = "1.2.0"

from meshroom.core import desc
from ..common import node

class ChgSysCo(node.MicmacNode, desc.CommandLineNode):
    commandLine = 'mm3d ChgSysCo {imagePatternValue} {orientationInValue} {ChgSystValue} {orientationOutValue} {allParams}'
    documentation = 'ChgSysCo: Change the coordinate system of an orientation.'

    inputs = [
        desc.File(
            name='projectDirectory',
            label='Project Directory',
            description='Project Directory.',
            value="",
            commandLineGroup='', # required to execute mm3d command line
        ),
        desc.File(
            name='imagePattern',
            label='Image Pattern',
            description='Image Pattern.',
            commandLineGroup='', # unnamed parameter
            value="",
        ),
        desc.File(
            name='orientationIn',
            label='Input Orientation',
            description="Input Orientation.",
            commandLineGroup='', # unnamed parameter
            value="",
        ),
        desc.File(
            name='ChgSyst',
            label='Changing system file',
            description="Changing system file.",
            commandLineGroup='', # unnamed parameter
            value="",
        ),
        desc.BoolParam(
            name='FR',
            label='F R',
            description="Force orientation matrix to be pure rotation.",
            value=False,
        ),
        desc.StringParam(
            name='Out',
            label='Output Directory Name',
            description="Name or the directory of the output orientation file.",
            commandLineGroup='', # for output parameter
            value="",
        ),
    ]

    outputs = [
        desc.File(
            name='orientationOut',
            label='Output Orientation',
            description="Output orientation.",
            value="{OutValue}",
            commandLineGroup='',  # unnamed parameter
        ),
    ]
