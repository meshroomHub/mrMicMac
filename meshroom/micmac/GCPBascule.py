__version__ = "1.1.1"

import sys
from meshroom.core import desc
from meshroomMicmac.custom import node

class GCPBascule(node.MicmacNode):
    commandLine = 'mm3d GCPBascule {imagePatternValue} {orientationInValue} {orientationOutValue} {groundControlPointsFileValue} {imageMeasurementsFileValue} {allParams}'
    documentation = 'GCPBascule'

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
            name='orientationIn',
            label='Input Orientation',
            description="Input Orientation.",
            group='unnamedParams',
            uid=[0],
            value="",
        ),
        desc.File(
            name='groundControlPointsFile',
            label='GCP 3D coordinates File',
            description="Ground Control Points File",
            group='unnamedParams',
            uid=[0],
            value="",
        ),
        desc.File(
            name='imageMeasurementsFile',
            label='GCP Image corodinates File',
            description="Image Measurements File",
            group='unnamedParams',
            uid=[0],
            value="",
        ),
        desc.BoolParam(
            name='L1',
            label='L1',
            description="L1 minimisation vs L2",
            uid=[0],
            value=False,
            advanced=True,
        ),
        desc.BoolParam(
            name='CPI',
            label='CPI',
            description="when Calib Per Image has to be used",
            uid=[0],
            value=False,
        ),
        desc.BoolParam(
            name='ShowU',
            label='Show U',
            description="Show unused point",
            uid=[0],
            value=True,
            advanced=True,
        ),
        desc.BoolParam(
            name='ShowD',
            label='Show D',
            description="Show details",
            uid=[0],
            value=False,
            advanced=True,
        ),
        desc.StringParam(
            name='PatNLD',
            label='Pat NLD',
            description="Pattern for Non linear deformation, with aerial like geometry",
            uid=[0],
            value="",
            advanced=True,
        ),
        desc.BoolParam(
            name='NLFR',
            label='NLFR',
            description="Non Linear : Force True Rot",
            uid=[0],
            value=True,
            advanced=True,
        ),
        desc.BoolParam(
            name='NLShow',
            label='NL Show',
            description="Non Linear : Show Details",
            uid=[0],
            value=False,
            advanced=True,
        ),
      #  desc.StringParam(
      #      name='ForceSol',
      #      label='Force Sol',
      #      description="To Force Sol from existing solution (xml file)",
      #      uid=[0],
      #      value="",
      #      advanced=True,
      #  ),
    ]

    outputs = [
        desc.File(
		name='orientationOut',
		label='Output Orientation',
		description="Orientation out",
		group='unnamedParams',
		uid=[0],
		value="GCPBasc",
	),
    ]
