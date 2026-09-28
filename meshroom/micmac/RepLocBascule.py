__version__ = "0.0"

import sys
from meshroom.core import desc
from meshroomMicmac.custom import node

class RepLocBascule(node.MicmacNode):
    commandLine = 'mm3d RepLocBascule {imagePatternValue} {orientationDirValue} {imageMeasuresValue} {localFrameValue} {allParams}'
    documentation = 'RepLocBascule'
    category = 'MicMac'

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
            name='imagePattern',
            label='Image Pattern',
            description='Image Pattern.',
            group='', # unnamed parameter
            value="",
            uid=[0],
        ),
        desc.File(
            name='orientationDir',
            label='Orientation Directory',
            description='Orientation directory name.',
            group='', # unnamed parameter
            value='',
            uid=[0],
        ),
        desc.File(
            name='imageMeasures',
            label='Image measures',
            description="Image measures xml file, set 'HOR' if horizontal line is wanted (HORVy if Y vertical), 'NONE' if unused",
            uid=[0],
            group='', # unnamed parameter
            value="",
        ),
        desc.BoolParam(
            name='ExpTxt',
            label='Tie Points In Txt',
            description="Export in text format.",
            uid=[0],
            value=False,
        ),
        desc.StringParam(
            name='PostPlan',
            label='Post Plan',
            description="Postfix for plane name, (Def=_Masq)",
            uid=[0],
            value="",
            advanced=True,
        ),
        desc.BoolParam(
            name='OrthoCyl',
            label='Ortho Cyl',
            description="Is the coordinate system in ortho-cylindric mode?",
            uid=[0],
            value=False,
            advanced=True,
        ),
         desc.StringParam(
            name='localFrame',
            label='Local Frame name',
            description="Output of Local Frame (Repere Local) xml file",
            uid=[0],
            group='', # unnamed parameter
            value="RepLoc.xml",
        ),
    ]

    outputs = [
        desc.File(
            name='localFrameOut',
            label='Local Frame',
            description="Output of Local Frame (Repere Local) xml file",
            uid=[],
            group='', # unnamed parameter
            value="{localFrameValue}",
        ),
    ]
