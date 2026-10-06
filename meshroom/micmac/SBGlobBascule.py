__version__ = "1.2.0"

from meshroom.core import desc
from ..common import node

class SBGlobBascule(node.MicmacNode, desc.CommandLineNode):
    commandLine = 'mm3d SBGlobBascule {imagePatternValue} {orientationInValue} {imageMeasuresValue} {orientationOutValue} {allParams}'
    documentation = 'SBGlobBascule: Scene-based global bascule, orient the model using a plane, an axis and a scale measured in the images.'

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
            label='In Orientation Directory',
            description="Input Orientation.",
            commandLineGroup='', # unnamed parameter
            value="",
        ),
        desc.File(
            name='imageMeasures',
            label='Image Measures',
            description="Image measures xml file.",
            commandLineGroup='', # unnamed parameter
            value="",
        ),
        desc.BoolParam(
            name='ExpTxt',
            label='Tie Points In Txt',
            description="Tie Points use txt format.",
            value=False,
        ),
        desc.StringParam(
            name='PostPlan',
            label='Post Plan',
            description="Postfix for plane name.",
            value="",
        ),
        desc.BoolParam(
            name='setDistFS',
            label='Set DistFS',
            description="Set DistFS (if not set no scaling).",
            value=False,
            commandLineGroup='', # enable 'DistFS' attribute
        ),
        desc.FloatParam(
            name='DistFS',
            label='Dist FS',
            description="Distance between Ech1 and Ech2 to fix scale.",
            enabled=lambda node: node.setDistFS.value,
            value=1.0,
            range=(0.0, 100000.0, 0.01),
        ),
        desc.StringParam(
            name='Rep',
            label='Rep',
            description="Target coordinate system (Def = ki, ie normal is vertical).",
            value="",
            advanced=True,
        ),
        desc.BoolParam(
            name='CPI',
            label='CPI',
            description="Calibration Per Image.",
            value=False,
        ),
        desc.StringParam(
            name='Out',
            label='Output Directory Name',
            description="Name or the directory of the output orientation file.",
            commandLineGroup='', # for output parameter
            value="SBGlobBasc",
        ),
    ]

    outputs = [
        desc.File(
            name='orientationOut',
            label='Orientation Directory',
            description="Output orientation.",
            value="{OutValue}",
            commandLineGroup='', # unnamed parameter
        ),
    ]
