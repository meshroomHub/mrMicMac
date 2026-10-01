__version__ = "1.2.0"

from meshroom.core import desc
from ..common import node

class SetExif(node.MicmacNode, desc.CommandLineNode):
    commandLine = 'mm3d SetExif {imagePatternValue} {allParams}'
    documentation = 'SetExif: Modify image EXIF metadata such as focal length or camera model (requires exiv2).'

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
        desc.BoolParam(
            name='setF',
            label='Set F',
            description='Set Focal lenght?', 
            value=False,
            commandLineGroup='', # enable 'F' attribute
        ),
        desc.FloatParam(
            name='F',
            label='F',
            description='Focal lenght',
            enabled=lambda node: node.setF.value,
            value=50.0,
            range=(0.0, 800.0, 0.1),
        ),
        desc.BoolParam(
            name='setF35',
            label='Set F35',
            description='Set Focal lenght equiv 35mm?', 
            value=False,
            commandLineGroup='', # enable 'F35' attribute
        ),
        desc.FloatParam(
            name='F35',
            label='F35',
            description='Focal lenght equiv 35mm',
            enabled=lambda node: node.setF35.value,
            value=50.0,
            range=(0.0, 800.0, 0.1),
        ),
        desc.StringParam(
            name='Cam',
            label='Cam',
            description='Camera model',
            value='',
        ),
        desc.StringParam(
            name='Tps',
            label='Tps',
            description='Image timestamp',
            value='',
        ),
        desc.BoolParam(
            name='Purge',
            label='Purge',
            description='Purge created exiv2 command file', 
            value=True,
        ),
    ]

    outputs = [
    ]
