__version__ = "1.2.0"

from meshroom.core import desc
from ..common import node

class TiPunch(node.MicmacNode, desc.CommandLineNode):
    commandLine = 'mm3d TiPunch {plyNameValue} {allParams}'
    documentation = 'TiPunch: Compute a mesh from a dense point cloud (Poisson reconstruction).'

    inputs = [
        desc.File(
            name='projectDirectory',
            label='Project Directory',
            description='Project Directory.',
            value="",
            commandLineGroup='', # required to execute mm3d command line
        ),
        desc.File(
            name='Pattern',
            label='Image Pattern',
            description='Image Pattern.',
            value="",
        ),
        desc.File(
            name='plyName',
            label='Point Cloud Filename',
            description='Point cloud PLY filename.',
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
        desc.IntParam(
            name='Depth',
            label='Depth',
            description='Maximum reconstruction depth for PoissonRecon.',
            value=8,
            range=(0, 20, 1),
        ),
        desc.BoolParam(
            name='Rm',
            label='Rm',
            description='Remove intermediary Poisson mesh.',
            value=True,
            advanced=True,
        ),
        desc.BoolParam(
            name='Filter',
            label='Filter',
            description='Filter mesh.',
            value=True,
        ),
        desc.ChoiceParam(
            name="Mode",
            label="Mode",
            description="C3DC Mode.",
            value="QuickMac",
            values=["Ground", "Statue", "Forest", "QuickMac", "MicMac", "BigMac"],
            exclusive=True,
        ),
        desc.IntParam(
            name='Scale',
            label='Scale',
            description='Z-buffer downscale factor.',
            value=2,
            range=(0, 10, 1),
        ),
        desc.BoolParam(
            name='FFB',
            label='FFB',
            description='Filter from border.',
            value=True,
            advanced=True,
        ),
        desc.StringParam(
            name='Out',
            label='Output Filename',
            description='Output PLY mesh name.',
            value='TiPunch.ply',
        ),
    ]

    outputs = [
        desc.File(
            name='outMeshPath',
            label='Mesh',
            description='Output PLY mesh (absolute path).',
            value='{projectDirectoryValue}/{OutValue}',
            semantic='3d',
            commandLineGroup='', # not a command line parameter
            invalidate=False,
        ),
        desc.File(
            name='outMeshFilename',
            label='Mesh Filename',
            description='Output PLY mesh name, relative to the project directory.',
            value='{OutValue}',
            commandLineGroup='', # not a command line parameter
            invalidate=False,
        ),
    ]
