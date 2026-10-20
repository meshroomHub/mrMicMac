__version__ = "1.2.0"

from meshroom.core import desc
from ..common import node

class Tarama(node.MicmacNode, desc.CommandLineNode):
    commandLine = 'mm3d Tarama {imagePatternValue} {orientationDirValue} {allParams}'
    documentation = 'Tarama: Compute a rectified image assembly (TA), typically used to draw a mask for Malt Ortho.'

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
            value="",
        ),
        desc.ChoiceParam(
            name='Zoom',
            label='Zoom',
            description="Resolution (Def=8, must be a power of 2).",
            value=8,
            values=[1, 2, 4, 8, 16, 32, 64],
            exclusive=True,
        ),
        desc.File(
            name='Repere',
            label='Repere',
            description="Local coordinate system as created with RepLocBascule.",
            value="",
            advanced=True,
        ),
        desc.BoolParam(
            name='setZMoy',
            label='Set Average Z',
            description="Set ZMoy.",
            value=False,
            commandLineGroup='', # enable 'ZMoy' attribute
            advanced=True,
        ),
        desc.FloatParam(
            name='ZMoy',
            label='Average Z',
            description="Average value of Z.",
            enabled=lambda node: node.setZMoy.value,
            value=0.0,
            range=(-100000.0, 100000.0, 0.01),
            advanced=True,
        ),
        desc.BoolParam(
            name='setKNadir',
            label='Set K Nadir',
            description="Set KNadir.",
            value=False,
            commandLineGroup='', # enable 'KNadir' attribute
            advanced=True,
        ),
        desc.IntParam(
            name='KNadir',
            label='K Nadir',
            description="KBest image or Nadir (when exist).",
            enabled=lambda node: node.setKNadir.value,
            value=1,
            range=(0, 100, 1),
            advanced=True,
        ),
        desc.BoolParam(
            name='setIncMax',
            label='Set Max Incidence',
            description="Set IncMax.",
            value=False,
            commandLineGroup='', # enable 'IncMax' attribute
            advanced=True,
        ),
        desc.FloatParam(
            name='IncMax',
            label='Max Incidence',
            description="Maximum incidence of image.",
            enabled=lambda node: node.setIncMax.value,
            value=1.0,
            range=(0.0, 10.0, 0.01),
            advanced=True,
        ),
        desc.BoolParam(
            name='setUnUseAXC',
            label='Set Un Use AXC',
            description="Set UnUseAXC.",
            value=False,
            commandLineGroup='', # enable 'UnUseAXC' attribute
            advanced=True,
        ),
        desc.BoolParam(
            name='UnUseAXC',
            label='Un Use AXC',
            description="Internal use for unanamorphosed ortho.",
            enabled=lambda node: node.setUnUseAXC.value,
            value=True,
            advanced=True,
        ),
        desc.StringParam(
            name='Out',
            label='Output Directory Name',
            description="Directory for output (Def=TA).",
            value="TA",
        ),
    ]

    outputs = [
        desc.File(
            name='taDirectory',
            label='TA Directory',
            description="Directory of the rectified image assembly (to use as Malt 'DirTA').",
            value="{OutValue}",
            commandLineGroup='', # not a command line parameter
        ),
        desc.File(
            name='taImage',
            label='TA Image',
            description="Rectified image assembly, relative to the project directory (to draw a mask on with SaisieMasqQT).",
            value="{OutValue}/TA_LeChantier.tif",
            commandLineGroup='', # not a command line parameter
        ),
    ]
