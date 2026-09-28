__version__ = "1.1.1"

from meshroom.core import desc
from meshroomMicmac.custom import node

class SaisieMasqQT(node.MicmacNode):
    commandLine = 'mm3d SaisieMasqQT {filePathValue} {allParams}'
    documentation = '''SaisieMasqQT'''

    inputs = [
        desc.File(
            name='projectDirectory',
            label='Project Directory',
            description='Project Directory.',
            value="",
            group='', # required to execute mm3d command line
            uid=[0],
        ),
        desc.File(
            name='filePath',
            label='File Path',
            description='''Path of the file to open (image or PLY or camera XML).''',
            group='', # unnamed parameter
            value="",
            uid=[0],
        ),
        desc.BoolParam(
            name='setPostfix',
            label='Set Postfix',
            description="Set postfix.",
            uid=[0],
            value=False,
            group='',
            advanced=True,
        ),
        desc.StringParam(
            name='Post',
            label='File Postfix',
            description="Output file postfix.",
            enabled=lambda node: node.setPostfix.value,
            value="_Masq",
            uid=[0],
            advanced=True,
        ),
        desc.BoolParam(
            name='setName',
            label='Set Name',
            description="Set name.",
            uid=[0],
            value=False,
            group='',
            advanced=True,
        ),
        desc.StringParam(
            name='Name',
            label='Name',
            description='''Set output filename (dafault=input+_Masq).''',
            enabled=lambda node: node.setName.value,
            value="",
            uid=[0],
            advanced=True,
        ),
        desc.BoolParam(
            name='setAttr',
            label='Set Attr',
            description="Set attr.",
            uid=[0],
            value=False,
            group='',
            advanced=True,
        ),
        desc.StringParam(
            name='Attr',
            label='Attr',
            description='''String to add to postfix..''',
            enabled=lambda node: node.setAttr.value,
            value="",
            uid=[0],
            advanced=True,
        ),
        desc.BoolParam(
            name='setGamma',
            label='Set Gamma',
            description="Set gamma.",
            uid=[0],
            value=False,
            group='',
            advanced=True,
        ),
        desc.FloatParam(
            name='Gama',
            label='Gamma',
            description='Apply gamma to image.',
            enabled=lambda node: node.setGamma.value,
            value=1.5,
            range=(1.0, 4.0, 0.01),
            uid=[0],
            advanced=True,
        ),
    ]

    outputs = [
    ]
