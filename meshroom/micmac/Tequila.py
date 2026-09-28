__version__ = "1.1.1"

from meshroom.core import desc
from meshroomMicmac.custom import node

class Tequila(node.MicmacNode):
    commandLine = 'mm3d Tequila {imagePatternValue} {orientationDirValue} {plyNameValue} {allParams}'
    documentation = '''Tequila'''

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
            name='orientationDir',
            label='Orientation Directory',
            description='Orientation directory name.',
            group='', # unnamed parameter
            value='',
            uid=[0],
        ),
        desc.File(
            name='plyName',
            label='Mesh',
            description='PLY Mesh filename.',
            group='', # unnamed parameter
            value='',
            uid=[0],
        ),
        desc.BoolParam(
            name='Bin',
            label='Bin',
            description='Write PLY in binary mode.', 
            value=True,
            uid=[0],
            advanced=True,
        ),
        desc.BoolParam(
            name='Optim',
            label='Optim',
            description='Graph-cut optimization.', 
            value=False,
            uid=[0],
            advanced=True,
        ),
        desc.FloatParam(
            name='Lambda',
            label='Lambda',
            description='Lambda.',
            value=0.01,
            range=(0.0, 10.0, 0.01),
            uid=[0],
            advanced=True,
        ),
        desc.IntParam(
            name='Iter',
            label='Iter',
            description='Optimization iteration number.',
            value=2,
            range=(0, 20, 1),
            uid=[0],
            advanced=True,
        ),
        desc.BoolParam(
            name='Filter',
            label='Filter',
            description='Remove border faces.', 
            value=False,
            uid=[0],
            advanced=True,
        ),
        desc.IntParam(
            name='Sz',
            label='Texture Size',
            description='Texture max size.',
            value=8192,
            range=(100, 16000, 1),
            uid=[0],
        ),
        desc.IntParam(
            name='Scale',
            label='Scale',
            description='Z-buffer downscale factor.',
            value=2,
            range=(0, 10, 1),
            uid=[0],
            advanced=True,
        ),
        desc.BoolParam(
            name='ZBufCache',
            label='ZBuf Cache',
            description='ZBuffer cache (if True: a little faster, more memory).',
            value=False,
            uid=[0],
            advanced=True,
        ),
        desc.IntParam(
            name='QUAL',
            label='Quality',
            description='jpeg compression quality.',
            value=70,
            range=(10, 100, 1),
            uid=[0],
        ),
        desc.FloatParam(
            name='Angle',
            label='Angle',
            description='Threshold angle, in degree, between triangle normal and image viewing direction',
            value=90.0,
            range=(0.0, 360.0, 0.01),
            uid=[0],
            advanced=True,
        ),
        desc.ChoiceParam(
            name="Mode",
            label="Mode",
            description="Mode.",
            value="Basic",
            values=["Basic", "Pack"],
            exclusive=True,
            uid=[0],
            advanced=True,
        ),
        desc.ChoiceParam(
            name="Crit",
            label="Crit",
            description="Texture choosing criterion.",
            value="Angle",
            values=["Angle", "Stretch", "AAngle"],
            exclusive=True,
            uid=[0],
            advanced=True,
        ),
    ]

    outputs = [
        desc.File(
            name='Out',
            label='Textured Mesh',
            description='Output PLY point cloud name.',
            value='Tequila.ply',
            uid=[],
        ),
    ]
