__version__ = "1.1.1"

from meshroom.core import desc
from ..common import node

class TiPunch(node.MicmacNode, desc.CommandLineNode):
    commandLine = 'mm3d TiPunch {plyNameValue} {allParams}'
    documentation = '''TiPunch'''

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
            name='Pattern',
            label='Image Pattern',
            description='Image Pattern.',
            value="",
            invalidate=True,
        ),
        desc.File(
            name='plyName',
            label='Point Cloud',
            description='Point cloud PLY filename.',
            commandLineGroup='', # unnamed parameter
            value='',
            invalidate=True,
        ),
        desc.BoolParam(
            name='Bin',
            label='Bin',
            description='Write PLY in binary mode.', 
            value=True,
            invalidate=True,
            advanced=True,
        ),
        desc.IntParam(
            name='Depth',
            label='Depth',
            description='Maximum reconstruction depth for PoissonRecon.',
            value=8,
            range=(0, 20, 1),
            invalidate=True,
        ),
        desc.BoolParam(
            name='Rm',
            label='Rm',
            description='Remove intermediary Poisson mesh.', 
            value=True,
            invalidate=True,
            advanced=True,
        ),
        desc.BoolParam(
            name='Filter',
            label='Filter',
            description='Filter mesh.', 
            value=True,
            invalidate=True,
        ),
        desc.ChoiceParam(
            name="Mode",
            label="Mode",
            description="C3DC Mode.",
            value="QuickMac",
            values=["Ground", "Statue", "Forest", "QuickMac", "MicMac", "BigMac"],
            exclusive=True,
            invalidate=True,
        ),
        desc.IntParam(
            name='Scale',
            label='Scale',
            description='Z-buffer downscale factor.',
            value=2,
            range=(0, 10, 1),
            invalidate=True,
        ),
        desc.BoolParam(
            name='FFB',
            label='FFB',
            description='Filter from border.', 
            value=True,
            invalidate=True,
            advanced=True,
        ),
    ]

    outputs = [
        desc.File(
            name='Out',
            label='Mesh',
            description='Output PLY mesh name.',
            value='TiPunch.ply',
            invalidate=False,
        ),
    ]
