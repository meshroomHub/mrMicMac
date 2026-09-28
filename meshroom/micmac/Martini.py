__version__ = "1.1.1"

from meshroom.core import desc
from meshroomMicmac.custom import node

class Martini(node.MicmacNode):
    commandLine = 'mm3d Martini {imagePatternValue} {allParams}'
    documentation = '''Martini'''

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
        desc.BoolParam(
            name='Exe',
            label='Exe',
            description='If false, only print.', 
            value=True,
            uid=[0],
        ),
        desc.File(
            name='OriCalib',
            label='Ori Calib',
            description='Orientation for calibration.',
            value='',
            uid=[0],
        ),
        desc.File(
            name='SH',
            label='Homol Directory',
            description="Homol Directory.",
            uid=[0],
            value="",
        ),
        desc.StringParam(
            name='ExtName',
            label='Ext Name',
            description="User's added Prefix.",
            value='',
            uid=[0],
        ),
        desc.BoolParam(
            name='ExpTxt',
            label='Exp Txt',
            description='Is Homol in text format?.', 
            value=False,
            uid=[0],
        ),
        desc.StringParam(
            name='ModeNO',
            label='Mode NO',
            description="Mode (TTK StdNoTTK OnlyHomogr).",
            value='Std',
            uid=[0],
        ),
        desc.BoolParam(
            name='Debug',
            label='Debug',
            description='Debug', 
            value=False,
            uid=[0],
        ),
        desc.BoolParam(
            name='AUS',
            label='AUS',
            description='Accept non symetric homologous point.', 
            value=True,
            uid=[0],
        ),
        desc.IntParam(
            name='QNbPtTrip',
            label='Q Nb Pt Trip',
            description='Max num of triplets per edge (Quick mode).',
            value=8,
            range=(1, 20, 1),
            uid=[0],
        ),
        desc.IntParam(
            name='NbTrip',
            label='Nb Trip',
            description='Min num of points to calculate a triplet.',
            value=5,
            range=(1, 20, 1),
            uid=[0],
        ),
        desc.StringParam(
            name='OriOut',
            label='Output Orientation Name',
            description="Directory of Output Orientation",
            value="Martini",
            uid=[0],
        ),
    ]

    outputs = [
        desc.File(
            name='orientationDirectory',
            label='Orientation Directory',
            description="Directory of Output Orientation",
            value="{OriOutValue}",
            group='', # not a command line parameter
            uid=[],
        ),
    ]
