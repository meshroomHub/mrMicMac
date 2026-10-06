__version__ = "1.2.0"

from meshroom.core import desc
from ..common import node

class GCPConvert(node.MicmacNode, desc.CommandLineNode):
    commandLine = 'mm3d GCPConvert {formatSpecificationValue} {GCPFileValue} {allParams}'
    documentation = 'GCPConvert: Convert ground control points from text files to MicMac XML format.'

    inputs = [
        desc.File(
            name='projectDirectory',
            label='Project Directory',
            description='Project Directory.',
            value='',
            commandLineGroup='', # required to execute mm3d command line
        ),
        desc.ChoiceParam(
            name='formatSpecification',
            label='Format Specification',
            description='Format specification of the GCP file.',
            commandLineGroup='', # unnamed parameter
            value='AppInFile',
            values=['AppEgels', 'AppGeoCub', 'AppInFile', 'AppXML'],
            exclusive=True,
        ),
        desc.File(
            name='GCPFile',
            label='In GCP File',
            description='Ground Control Points file.',
            commandLineGroup='', # unnamed parameter
            value='',
        ),
        desc.StringParam(
            name='Out',
            label='Output Filename',
            description='Xml out file (Def=GCP file name with xml extension).',
            value='',
        ),
        desc.File(
            name='ChSys',
            label='Change System File',
            description='Change coordinate file.',
            value='',
        ),
        desc.BoolParam(
            name='setOffs',
            label='Set Offs',
            description="Set Offs.",
            value=False,
            commandLineGroup='', # enable 'Offs' attribute
        ),
        desc.GroupAttribute(
            name='Offs',
            label='Offs',
            description="Offset to substract to all coordinates.",
            enabled=lambda node: node.setOffs.value,
            brackets='[]',
            joinChar=',',
            items=[
                desc.FloatParam(
                    name="x",
                    label="X",
                    description="x.",
                    value=0.0,
                    range=(-100000.0, 100000.0, 0.01),
                ),
                desc.FloatParam(
                    name="y",
                    label="Y",
                    description="y.",
                    value=0.0,
                    range=(-100000.0, 100000.0, 0.01),
                ),
                desc.FloatParam(
                    name="z",
                    label="Z",
                    description="z.",
                    value=0.0,
                    range=(-100000.0, 100000.0, 0.01),
                ),
            ]
        ),
        desc.BoolParam(
            name='setMulCo',
            label='Set Mul Co',
            description="Set Mul Co.",
            value=False,
            commandLineGroup='', # enable 'MulCo' attribute
            advanced=True,
        ),
        desc.FloatParam(
            name='MulCo',
            label='Mul Co',
            description="Multiplier of result (for development and testing use).",
            enabled=lambda node: node.setMulCo.value,
            value=1.0,
            range=(-100000.0, 100000.0, 0.01),
            advanced=True,
        ),
        desc.BoolParam(
            name='setMulInc',
            label='Set Mul Inc',
            description="Set Mul Inc.",
            value=False,
            commandLineGroup='', # enable 'MulInc' attribute
            advanced=True,
        ),
        desc.BoolParam(
            name='MulInc',
            label='Mul Inc',
            description="Multiplier also incertitude (for development and testing use).",
            enabled=lambda node: node.setMulInc.value,
            value=False,
            advanced=True,
        ),
    ]

    outputs = [
        desc.File(
            name='GCPFileOut',
            label='GCP File',
            description='Output Ground Control Points xml file.',
            value=lambda node: node.Out.value or node.GCPFile.value.replace('"', '').rsplit(".", 1)[0] + '.xml',
            commandLineGroup='', # not a command line parameter
            invalidate=False,
        ),
    ]
