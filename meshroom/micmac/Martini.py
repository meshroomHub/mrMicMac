__version__ = "1.1.1"

from meshroom.core import desc
from ..common import node

class Martini(node.MicmacNode, desc.CommandLineNode):
    commandLine = 'mm3d Martini {imagePatternValue} {allParams}'
    documentation = 'Martini: Initialize image orientations from triplets of images (experimental).'

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
        desc.BoolParam(
            name='Exe',
            label='Exe',
            description='If false, only print.', 
            value=True,
        ),
        desc.File(
            name='OriCalib',
            label='Ori Calib',
            description='Orientation for calibration.',
            value='',
        ),
        desc.File(
            name='SH',
            label='Homol Directory',
            description="Homol Directory.",
            value="",
        ),
        desc.StringParam(
            name='ExtName',
            label='Ext Name',
            description="User's added Prefix.",
            value='',
        ),
        desc.BoolParam(
            name='ExpTxt',
            label='Exp Txt',
            description='Is Homol in text format?.', 
            value=False,
        ),
        desc.StringParam(
            name='ModeNO',
            label='Mode NO',
            description="Mode (TTK StdNoTTK OnlyHomogr).",
            value='Std',
        ),
        desc.BoolParam(
            name='Debug',
            label='Debug',
            description='Debug', 
            value=False,
        ),
        desc.BoolParam(
            name='AUS',
            label='AUS',
            description='Accept non symetric homologous point.', 
            value=True,
        ),
        desc.IntParam(
            name='QNbPtTrip',
            label='Q Nb Pt Trip',
            description='Max num of triplets per edge (Quick mode).',
            value=8,
            range=(1, 20, 1),
        ),
        desc.IntParam(
            name='NbTrip',
            label='Nb Trip',
            description='Min num of points to calculate a triplet.',
            value=5,
            range=(1, 20, 1),
        ),
        desc.StringParam(
            name='OriOut',
            label='Output Orientation Name',
            description="Directory of Output Orientation",
            value="Martini",
        ),
    ]

    outputs = [
        desc.File(
            name='orientationDirectory',
            label='Orientation Directory',
            description="Directory of Output Orientation",
            value="{OriOutValue}",
            commandLineGroup='', # not a command line parameter
            invalidate=False,
        ),
    ]
