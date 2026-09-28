__version__ = "1.1.1"

import sys
from meshroom.core import desc
from ..common import node

class GCPBascule(node.MicmacNode, desc.CommandLineNode):
    commandLine = 'mm3d GCPBascule {imagePatternValue} {orientationInValue} {orientationOutValue} {groundControlPointsFileValue} {imageMeasurementsFileValue} {allParams}'
    documentation = 'GCPBascule'

    inputs = [
        desc.File(
            name='projectDirectory',
            label='Project Directory',
            description='Project Directory.',
            value="",
            commandLineGroup='', # required to execute mm3d command line
            invalidate=True,
        ),
        desc.File(
            name='imagePattern',
            label='Image Pattern',
            description='Image Pattern.',
            commandLineGroup='', # unnamed parameter
            value="",
            invalidate=True,
        ),
        desc.File(
            name='orientationIn',
            label='Input Orientation',
            description="Input Orientation.",
            commandLineGroup='unnamedParams',
            invalidate=True,
            value="",
        ),
        desc.File(
            name='groundControlPointsFile',
            label='GCP 3D coordinates File',
            description="Ground Control Points File",
            commandLineGroup='unnamedParams',
            invalidate=True,
            value="",
        ),
        desc.File(
            name='imageMeasurementsFile',
            label='GCP Image corodinates File',
            description="Image Measurements File",
            commandLineGroup='unnamedParams',
            invalidate=True,
            value="",
        ),
        desc.BoolParam(
            name='L1',
            label='L1',
            description="L1 minimisation vs L2",
            invalidate=True,
            value=False,
            advanced=True,
        ),
        desc.BoolParam(
            name='CPI',
            label='CPI',
            description="when Calib Per Image has to be used",
            invalidate=True,
            value=False,
        ),
        desc.BoolParam(
            name='ShowU',
            label='Show U',
            description="Show unused point",
            invalidate=True,
            value=True,
            advanced=True,
        ),
        desc.BoolParam(
            name='ShowD',
            label='Show D',
            description="Show details",
            invalidate=True,
            value=False,
            advanced=True,
        ),
        desc.StringParam(
            name='PatNLD',
            label='Pat NLD',
            description="Pattern for Non linear deformation, with aerial like geometry",
            invalidate=True,
            value="",
            advanced=True,
        ),
        desc.BoolParam(
            name='NLFR',
            label='NLFR',
            description="Non Linear : Force True Rot",
            invalidate=True,
            value=True,
            advanced=True,
        ),
        desc.BoolParam(
            name='NLShow',
            label='NL Show',
            description="Non Linear : Show Details",
            invalidate=True,
            value=False,
            advanced=True,
        ),
      #  desc.StringParam(
      #      name='ForceSol',
      #      label='Force Sol',
      #      description="To Force Sol from existing solution (xml file)",
      #      invalidate=True,
      #      value="",
      #      advanced=True,
      #  ),
    ]

    outputs = [
        desc.File(
		name='orientationOut',
		label='Output Orientation',
		description="Orientation out",
		commandLineGroup='unnamedParams',
		invalidate=True,
		value="GCPBasc",
	),
    ]
