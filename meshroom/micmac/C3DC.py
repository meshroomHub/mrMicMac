__version__ = "1.1.1"

from meshroom.core import desc
from meshroomMicmac.custom import node

class C3DC(node.MicmacNode):
    commandLine = 'mm3d C3DC {modeValue} {imagePatternValue} {orientationDirValue} {allParams}'
    documentation = '''C3DC'''

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
            value="",
            group='', # unnamed parameter
            uid=[0],
        ),    
        desc.File(
            name='SH',
            label='Homol Directory',
            description="Homol Directory.",
            uid=[0],
            value="",
        ),
        desc.File(
            name='orientationDir',
            label='Orientation Directory',
            description='Orientation directory name.',
            group='', # unnamed parameter
            value='',
            uid=[0],
        ),
        desc.ChoiceParam(
            name="mode",
            label="Mode",
            description="Mode.",
            group='', # unnamed parameter
            value="QuickMac",
            values=["Ground", "Statue", "Forest", "QuickMac", "MicMac", "BigMac"],
            exclusive=True,
            uid=[0],
        ),
        desc.StringParam(
            name='Masq3D',
            label='Masq 3D',
            description='3D masq for point selection.',
            value="",
            uid=[0],
        ),
        desc.IntParam(
            name='SzNorm',
            label='Sz Norm',
            description='Size of param for normal evaluation (<=0 if none, 2 means 5x5).',
            value=2,
            range=(-1, 20, 1),
            uid=[0],
            advanced=True,
        ),
        desc.BoolParam(
            name='PlyCoul',
            label='Ply Color',
            description='Colour in ply.', 
            value=True,
            uid=[0],
            advanced=True,
        ),
        desc.BoolParam(
            name='Purge',
            label='Purge',
            description='Purge result.', 
            value=True,
            uid=[0],
            advanced=True,
        ),
        desc.BoolParam(
            name='ExpTxt',
            label='Tie Points In Txt',
            description='Use txt tie points for determining image pairs.', 
            value=False,
            uid=[0],
        ),
        desc.BoolParam(
            name='Bin',
            label='Bin',
            description='PLY in binary mode.',  
            value=True,
            uid=[0],
            advanced=True,
        ),
        desc.BoolParam(
            name='NormByC',
            label='Norm By C',
            description='Replace normal with camera position in PLY.',
            value=False,
            uid=[0],
            advanced=True,
        ),
        desc.FloatParam(
            name='TetaOpt',
            label='Teta Opt',
            description='For the choice of secondary images: Optimal angle of stereoscopy, in radian.',
            value=0.17,
            range=(0.0, 1.0, 0.01),
            uid=[0],
            advanced=True,
        ),
        desc.BoolParam(
            name='ExpImSec',
            label='Exp Im Sec',
            description="Export Images Second.",
            uid=[0],
            value=True,
            advanced=True,
        ),
        desc.BoolParam(
            name='setCustomZoomF',
            label='Set Custom ZoomF',
            description="Set custom ZoomF.",
            uid=[0],
            value=False,
            group='',
            advanced=True,
        ),
        desc.IntParam(
            name='ZoomF',
            label='Zoom F',
            description="Zoom final.",
            enabled=lambda node: node.setCustomZoomF.value,
            uid=[0],
            value=2,
            range=(0, 100, 1),
        ),
        desc.StringParam(
            name='FilePair',
            label='FilePair',
            description='Explicit pairs of images (as in Tapioca).',
            value="",
            uid=[0],
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
            groupDesc=[
            desc.FloatParam(
                name="x",
                label="X",
                description="x.",
                value=0.0,
                range=(0.0, float('inf'), 0.01),
                uid=[0],
            ),
            desc.FloatParam(
                name="y",
                label="Y",
                description="y.",
                value=0.0,
                range=(0.0, float('inf'), 0.01),
                uid=[0],
            ),
            desc.FloatParam(
                name="z",
                label="Z",
                description="z.",
                value=0.0,
                range=(0.0, float('inf'), 0.01),
                uid=[0],
            ),
        ]),
        desc.StringParam(
            name='Out',
            label='Output Name',
            description='Output PLY point cloud name.',
            value='C3DC.ply',
            uid=[0],
        ),
    ]

    outputs = [
        desc.File(
            name='pointCloud',
            label='Dense Point Cloud',
            description='Output PLY point cloud name.',
            value='{OutValue}',
            group='', # not a command line parameter
            uid=[],
        ),
    ]