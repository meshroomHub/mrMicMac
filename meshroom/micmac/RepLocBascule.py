__version__ = "1.2.0"

from meshroom.core import desc
from ..common import node

class RepLocBascule(node.MicmacNode, desc.CommandLineNode):
    commandLine = 'mm3d RepLocBascule {imagePatternValue} {orientationDirValue} {imageMeasuresValue} {localFrameValue} {allParams}'
    documentation = 'RepLocBascule: Define a local coordinate frame without changing the orientation.'

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
            name='orientationDir',
            label='Orientation Directory',
            description='Orientation directory name.',
            commandLineGroup='', # unnamed parameter
            value='',
        ),
        desc.File(
            name='imageMeasures',
            label='Image Measurements File',
            description="Image measures xml file, set 'HOR' if horizontal line is wanted (HORVy if Y vertical), 'NONE' if unused.",
            commandLineGroup='', # unnamed parameter
            value="",
        ),
        desc.BoolParam(
            name='ExpTxt',
            label='Tie Points In Txt',
            description="Export in text format.",
            value=False,
        ),
        desc.StringParam(
            name='PostPlan',
            label='Post Plan',
            description="Postfix for plane name, (Def=_Masq).",
            value="",
            advanced=True,
        ),
        desc.BoolParam(
            name='OrthoCyl',
            label='Ortho Cyl',
            description="Is the coordinate system in ortho-cylindric mode?",
            value=False,
            advanced=True,
        ),
         desc.StringParam(
            name='localFrame',
            label='Output Filename',
            description="Output of Local Frame (Repere Local) xml file.",
            commandLineGroup='', # unnamed parameter
            value="RepLoc.xml",
        ),
    ]

    outputs = [
        desc.File(
            name='localFrameOut',
            label='Local Frame',
            description="Output of Local Frame (Repere Local) xml file.",
            invalidate=False,
            commandLineGroup='', # not a command line parameter
            value="{localFrameValue}",
        ),
    ]
