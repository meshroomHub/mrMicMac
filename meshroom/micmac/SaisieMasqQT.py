__version__ = "1.1.1"

from meshroom.core import desc
from ..common import node

class SaisieMasqQT(node.MicmacNode, desc.CommandLineNode):
    commandLine = 'mm3d SaisieMasqQT {filePathValue} {allParams}'
    documentation = '''SaisieMasqQT'''

    inputs = [
        desc.File(
            name='projectDirectory',
            label='Project Directory',
            description='Project Directory.',
            value="",
            commandLineGroup='', # required to execute mm3d command line
        ),
        desc.File(
            name='filePath',
            label='File Path',
            description='''Path of the file to open (image or PLY or camera XML).''',
            commandLineGroup='', # unnamed parameter
            value="",
        ),
        desc.BoolParam(
            name='setPostfix',
            label='Set Postfix',
            description="Set postfix.",
            value=False,
            commandLineGroup='',
            advanced=True,
        ),
        desc.StringParam(
            name='Post',
            label='File Postfix',
            description="Output file postfix.",
            enabled=lambda node: node.setPostfix.value,
            value="_Masq",
            advanced=True,
        ),
        desc.BoolParam(
            name='setSzW',
            label='Set Window Size',
            description="Set window size.",
            value=False,
            commandLineGroup='', # unnamed parameter
            advanced=True,
        ),
        desc.GroupAttribute(
            name='SzW',
            label='Window Size',
            description="Set window size.",
            brackets='[]',
            joinChar=',',
            advanced=True,
            enabled=lambda node: node.setSzW.value,
            items=[
                desc.IntParam(
                    name="width",
                    label="Width",
                    description="Window width.",
                    value=900,
                    range=(0, 7680, 1),
                ),  
                desc.IntParam(
                    name="height",
                    label="Height",
                    description="Window height.",
                    value=600,
                    range=(0, 4320, 1),
                ),
            ]
        ),
        desc.BoolParam(
            name='setName',
            label='Set Name',
            description="Set name.",
            value=False,
            commandLineGroup='',
            advanced=True,
        ),
        desc.StringParam(
            name='Name',
            label='Name',
            description='''Set output filename (dafault=input+_Masq).''',
            enabled=lambda node: node.setName.value,
            value="",
            advanced=True,
        ),
        desc.BoolParam(
            name='setAttr',
            label='Set Attr',
            description="Set attr.",
            value=False,
            commandLineGroup='',
            advanced=True,
        ),
        desc.StringParam(
            name='Attr',
            label='Attr',
            description='''String to add to postfix..''',
            enabled=lambda node: node.setAttr.value,
            value="",
            advanced=True,
        ),
        desc.BoolParam(
            name='setGamma',
            label='Set Gamma',
            description="Set gamma.",
            value=False,
            commandLineGroup='',
            advanced=True,
        ),
        desc.FloatParam(
            name='Gama',
            label='Gamma',
            description='Apply gamma to image.',
            enabled=lambda node: node.setGamma.value,
            value=1.5,
            range=(1.0, 4.0, 0.01),
            advanced=True,
        ),
    ]

    outputs = [
    ]
