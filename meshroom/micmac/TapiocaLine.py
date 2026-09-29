__version__ = "1.1.1"

from meshroom.core import desc
from ..common import node

class TapiocaLine(node.MicmacNode, desc.CommandLineNode):
    commandLine = 'mm3d Tapioca Line {imagePatternValue} {imageSizeValue} {nbAdjacentImagesValue} {allParams}'
    documentation = '''Tapioca Line'''

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
        desc.IntParam(
            name='imageSize',
            label='Image Size',
            description='Size of image.',
            commandLineGroup='', # unnamed parameter
            value=-1,
            range=(-1, 16000, 10),
        ),
        desc.IntParam(
            name='nbAdjacentImages',
            label='Nb Adjacent Images',
            description='Number of adjacent images to look for.',
            commandLineGroup='', # unnamed parameter
            value=5,
            range=(1, 100, 1),
        ),
        desc.BoolParam(
            name='ExpTxt',
            label='Export Files In Txt',
            description='Export files in text format (if false binary).', 
            value=False,
        ),
        desc.BoolParam(
            name='ForceAdSupResol',
            label='Force Ad Sup Resol',
            description='To force computation even when Resol < Adj.', 
            value=False,
        ),
        desc.BoolParam(
            name='NoMax',
            label='No Max',
            description='No max.', 
            value=False,
        ),
        desc.BoolParam(
            name='NoMin',
            label='No Min',
            description='No min.', 
            value=False,
        ),
        desc.BoolParam(
            name='NoUnknown',
            label='No Unknown',
            description='No unknown.', 
            value=False,
        ),
        desc.FloatParam(
            name='Ratio',
            label='ANN Ratio',
            description='ANN closeness ration.',
            value=0.6,
            range=(0.1, 1.0, 0.1),
        ),
    ]

    outputs = [
        desc.File(
            name='PostFix',
            label='Homol Directory', # Directory Postfix
            description='Homol Directory.',
            value="Tapioca",
            invalidate=False,
        ),
    ]
