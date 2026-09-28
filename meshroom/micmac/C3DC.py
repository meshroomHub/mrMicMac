__version__ = "1.1.1"

from meshroom.core import desc
from ..common import node

class C3DC(node.MicmacNode, desc.CommandLineNode):
    commandLine = 'mm3d C3DC {modeValue} {imagePatternValue} {orientationDirValue} {allParams}'
    documentation = '''C3DC'''

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
            value="",
            commandLineGroup='', # unnamed parameter
            invalidate=True,
        ),    
        desc.File(
            name='SH',
            label='Homol Directory',
            description="Homol Directory.",
            invalidate=True,
            value="",
        ),
        desc.File(
            name='orientationDir',
            label='Orientation Directory',
            description='Orientation directory name.',
            commandLineGroup='', # unnamed parameter
            value='',
            invalidate=True,
        ),
        desc.ChoiceParam(
            name="mode",
            label="Mode",
            description="Mode.",
            commandLineGroup='', # unnamed parameter
            value="QuickMac",
            values=["Ground", "Statue", "Forest", "QuickMac", "MicMac", "BigMac"],
            exclusive=True,
            invalidate=True,
        ),
        desc.StringParam(
            name='Masq3D',
            label='Masq 3D',
            description='3D masq for point selection.',
            value="",
            invalidate=True,
        ),
        desc.IntParam(
            name='SzNorm',
            label='Sz Norm',
            description='Size of param for normal evaluation (<=0 if none, 2 means 5x5).',
            value=2,
            range=(-1, 20, 1),
            invalidate=True,
            advanced=True,
        ),
        desc.BoolParam(
            name='PlyCoul',
            label='Ply Color',
            description='Colour in ply.', 
            value=True,
            invalidate=True,
            advanced=True,
        ),
        desc.BoolParam(
            name='Purge',
            label='Purge',
            description='Purge result.', 
            value=True,
            invalidate=True,
            advanced=True,
        ),
        desc.BoolParam(
            name='ExpTxt',
            label='Tie Points In Txt',
            description='Use txt tie points for determining image pairs.', 
            value=False,
            invalidate=True,
        ),
        desc.BoolParam(
            name='Bin',
            label='Bin',
            description='PLY in binary mode.',  
            value=True,
            invalidate=True,
            advanced=True,
        ),
        desc.BoolParam(
            name='NormByC',
            label='Norm By C',
            description='Replace normal with camera position in PLY.',
            value=False,
            invalidate=True,
            advanced=True,
        ),
        desc.FloatParam(
            name='TetaOpt',
            label='Teta Opt',
            description='For the choice of secondary images: Optimal angle of stereoscopy, in radian.',
            value=0.17,
            range=(0.0, 1.0, 0.01),
            invalidate=True,
            advanced=True,
        ),
        desc.BoolParam(
            name='ExpImSec',
            label='Exp Im Sec',
            description="Export Images Second.",
            invalidate=True,
            value=True,
            advanced=True,
        ),
        desc.BoolParam(
            name='setCustomZoomF',
            label='Set Custom ZoomF',
            description="Set custom ZoomF.",
            invalidate=True,
            value=False,
            commandLineGroup='',
            advanced=True,
        ),
        desc.IntParam(
            name='ZoomF',
            label='Zoom F',
            description="Zoom final.",
            enabled=lambda node: node.setCustomZoomF.value,
            invalidate=True,
            value=2,
            range=(0, 100, 1),
        ),
        desc.StringParam(
            name='FilePair',
            label='FilePair',
            description='Explicit pairs of images (as in Tapioca).',
            value="",
            invalidate=True,
            advanced=True,
        ),
        desc.GroupAttribute(
            name='OffsetPly',
            label='Ply Offset',
            description="Ply offset to overcome 32 bits problem.",
            brackets='[]',
            joinChar=',',
            enabled=lambda node: node.enableGpsLa.value,
            advanced=True,
            items=[
            desc.FloatParam(
                name="x",
                label="X",
                description="x.",
                value=0.0,
                range=(0.0, float('inf'), 0.01),
                invalidate=True,
            ),
            desc.FloatParam(
                name="y",
                label="Y",
                description="y.",
                value=0.0,
                range=(0.0, float('inf'), 0.01),
                invalidate=True,
            ),
            desc.FloatParam(
                name="z",
                label="Z",
                description="z.",
                value=0.0,
                range=(0.0, float('inf'), 0.01),
                invalidate=True,
            ),
        ]),
        desc.StringParam(
            name='Out',
            label='Output Name',
            description='Output PLY point cloud name.',
            value='C3DC.ply',
            invalidate=True,
        ),
    ]

    outputs = [
        desc.File(
            name='pointCloud',
            label='Dense Point Cloud',
            description='Output PLY point cloud name.',
            value='{OutValue}',
            commandLineGroup='', # not a command line parameter
            invalidate=False,
        ),
    ]