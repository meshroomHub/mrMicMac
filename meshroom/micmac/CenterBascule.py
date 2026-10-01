__version__ = "1.2.0"

from meshroom.core import desc
from ..common import node

class CenterBascule(node.MicmacNode, desc.CommandLineNode):
    commandLine = 'mm3d CenterBascule {imagePatternValue} {orientationInValue} {LocalizationOfICentersValue} {orientationOutValue} {allParams}'
    documentation = 'CenterBascule: Transform a relative orientation into an absolute one using embedded GPS camera centers.'

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
            name='LocalizationOfICenters',
            label='Localization Of Information On Centers',
            description="Localization of information on centers.",
            commandLineGroup='', # unnamed parameter
            value="",
        ),
        desc.BoolParam(
            name='CalcV',
            label='Compute Speed',
            description="Compute Speed.",
            value=False,
        ),
        desc.BoolParam(
            name='setL1',
            label='Set L1',
            description="Set L1",
            value=False,
            commandLineGroup='', # enable 'L1' attribute
            advanced=True,
        ),
        desc.BoolParam(
            name='L1',
            label='L1',
            description="L1 minimisation vs L2.",
            enabled=lambda node: node.setL1.value,
            value=False,
            advanced=True,
        ),
        desc.BoolParam(
            name='setForceVert',
            label='Set Force Vert',
            description="Set Force Vert.",
            value=False,
            commandLineGroup='', # enable 'ForceVert' attribute
            advanced=True,
        ), 
        desc.FloatParam(
            name='ForceVert',
            label='Force Vert',
            description="Weight for forcing Axe of camera to vertical.",
            enabled=lambda node: node.setForceVert.value,
            value=0.0,
            range=(-10000.0, 10000.0, 0.01),
            advanced=True,
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
            commandLineGroup='', # unnamed parameter
        ),
    ]
