__version__ = "1.2.0"

from meshroom.core import desc
from ..common import node

class Tequila(node.MicmacNode, desc.CommandLineNode):
    commandLine = 'mm3d Tequila {imagePatternValue} {orientationDirValue} {plyNameValue} {allParams}'
    documentation = 'Tequila: Texture a mesh from oriented images.'

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
            value='',
        ),
        desc.File(
            name='plyName',
            label='Mesh',
            description='PLY Mesh filename.',
            commandLineGroup='', # unnamed parameter
            value='',
        ),
        desc.BoolParam(
            name='Bin',
            label='Bin',
            description='Write PLY in binary mode.',
            value=True,
            advanced=True,
        ),
        desc.BoolParam(
            name='Optim',
            label='Optim',
            description='Graph-cut optimization.',
            value=False,
            advanced=True,
        ),
        desc.FloatParam(
            name='Lambda',
            label='Lambda',
            description='Lambda.',
            value=0.01,
            range=(0.0, 10.0, 0.01),
            advanced=True,
        ),
        desc.IntParam(
            name='Iter',
            label='Iter',
            description='Optimization iteration number.',
            value=2,
            range=(0, 20, 1),
            advanced=True,
        ),
        desc.BoolParam(
            name='Filter',
            label='Filter',
            description='Remove border faces.',
            value=False,
            advanced=True,
        ),
        desc.IntParam(
            name='Sz',
            label='Texture Size',
            description='Texture max size.',
            value=8192,
            range=(100, 16000, 1),
        ),
        desc.IntParam(
            name='Scale',
            label='Scale',
            description='Z-buffer downscale factor.',
            value=2,
            range=(0, 10, 1),
            advanced=True,
        ),
        desc.BoolParam(
            name='ZBufCache',
            label='ZBuf Cache',
            description='ZBuffer cache (if True: a little faster, more memory).',
            value=False,
            advanced=True,
        ),
        desc.IntParam(
            name='QUAL',
            label='Quality',
            description='jpeg compression quality.',
            value=70,
            range=(10, 100, 1),
        ),
        desc.FloatParam(
            name='Angle',
            label='Angle',
            description='Threshold angle, in degree, between triangle normal and image viewing direction.',
            value=90.0,
            range=(0.0, 360.0, 0.01),
            advanced=True,
        ),
        desc.ChoiceParam(
            name="Mode",
            label="Mode",
            description="Mode.",
            value="Basic",
            values=["Basic", "Pack"],
            exclusive=True,
            advanced=True,
        ),
        desc.ChoiceParam(
            name="Crit",
            label="Crit",
            description="Texture choosing criterion.",
            value="Angle",
            values=["Angle", "Stretch", "AAngle"],
            exclusive=True,
            advanced=True,
        ),
        desc.StringParam(
            name='Out',
            label='Output Filename',
            description='Output PLY textured mesh name.',
            value='Tequila.ply',
        ),
    ]

    outputs = [
        desc.File(
            name='outMeshPath',
            label='Textured Mesh',
            description='Output PLY textured mesh (absolute path).',
            value='{projectDirectoryValue}/{OutValue}',
            semantic='3d',
            commandLineGroup='', # not a command line parameter
            invalidate=False,
        ),
        desc.File(
            name='outMeshFilename',
            label='Textured Mesh Filename',
            description='Output PLY textured mesh name, relative to the project directory.',
            value='{OutValue}',
            commandLineGroup='', # not a command line parameter
            invalidate=False,
        ),
    ]
