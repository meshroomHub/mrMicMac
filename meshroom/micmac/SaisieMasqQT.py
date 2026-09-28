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
            group='', # required to execute mm3d command line
            invalidate=True,
        ),
        desc.File(
            name='filePath',
            label='File Path',
            description='''Path of the file to open (image or PLY or camera XML).''',
            group='', # unnamed parameter
            value="",
            invalidate=True,
        ),
        desc.BoolParam(
            name='setPostfix',
            label='Set Postfix',
            description="Set postfix.",
            invalidate=True,
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
            invalidate=True,
            advanced=True,
        ),
        desc.BoolParam(
            name='setName',
            label='Set Name',
            description="Set name.",
            invalidate=True,
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
            invalidate=True,
            advanced=True,
        ),
        desc.BoolParam(
            name='setAttr',
            label='Set Attr',
            description="Set attr.",
            invalidate=True,
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
            invalidate=True,
            advanced=True,
        ),
        desc.BoolParam(
            name='setGamma',
            label='Set Gamma',
            description="Set gamma.",
            invalidate=True,
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
            invalidate=True,
            advanced=True,
        ),
    ]

    outputs = [
    ]
