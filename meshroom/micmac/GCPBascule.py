__version__ = "1.2.0"

from meshroom.core import desc
from ..common import node

class GCPBascule(node.MicmacNode, desc.CommandLineNode):
    commandLine = 'mm3d GCPBascule {imagePatternValue} {orientationInValue} {orientationOutValue} {GCPFileValue} {imageMeasurementsFileValue} {allParams}'
    documentation = 'GCPBascule: Transform a relative orientation into an absolute one using ground control points.'

    inputs = [
        desc.File(
            name='projectDirectory',
            label='Project Directory',
            description='Project Directory.',
            value='',
            commandLineGroup='', # required to execute mm3d command line
        ),
        desc.File(
            name='imagePattern',
            label='Image Pattern',
            description='Image Pattern.',
            commandLineGroup='', # unnamed parameter
            value='',
        ),
        desc.File(
            name='orientationIn',
            label='Input Orientation',
            description="Input Orientation.",
            commandLineGroup='', # unnamed parameter
            value='',
        ),
        desc.File(
            name='GCPFile',
            label='GCP 3D Coordinates File',
            description="Ground Control Points file.",
            commandLineGroup='', # unnamed parameter
            value='',
        ),
        desc.File(
            name='imageMeasurementsFile',
            label='GCP Image Coordinates File',
            description="Image measurements file.",
            commandLineGroup='', # unnamed parameter
            value='',
        ),
        desc.BoolParam(
            name='L1',
            label='L1',
            description="L1 minimisation vs L2.",
            value=False,
            advanced=True,
        ),
        desc.BoolParam(
            name='CPI',
            label='CPI',
            description="when Calib Per Image has to be used.",
            value=False,
        ),
        desc.BoolParam(
            name='ShowU',
            label='Show U',
            description="Show unused point.",
            value=True,
            advanced=True,
        ),
        desc.BoolParam(
            name='ShowD',
            label='Show D',
            description="Show details.",
            value=False,
            advanced=True,
        ),
        desc.StringParam(
            name='PatNLD',
            label='Pat NLD',
            description="Pattern for non linear deformation, with aerial like geometry.",
            value='',
            advanced=True,
        ),
        desc.BoolParam(
            name='NLFR',
            label='NLFR',
            description="Non Linear: force true rot.",
            value=True,
            advanced=True,
        ),
        desc.BoolParam(
            name='NLShow',
            label='NL Show',
            description="Non Linear: show details.",
            value=False,
            advanced=True,
        ),
    ]

    outputs = [
        desc.File(
            name='orientationOut',
            label='Output Orientation',
            description="Output orientation.",
            commandLineGroup='', # unnamed parameter
            value="GCPBasc",
        ),
    ]
