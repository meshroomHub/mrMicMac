__version__ = "1.1.1"

from meshroom.core import desc
from ..common import node

class TapiocaGraph(node.MicmacNode, desc.CommandLineNode):
    commandLine = 'mm3d Tapioca Graph {imagePatternValue} {imageSizeValue} {allParams}'
    documentation = '''Tapioca Graph'''

    inputs = [
        desc.File(
            name='projectDirectory',
            label='Project Directory',
            description='Project Directory.',
            value="",
            group='', # required to execute mm3d command line
            invalidate=True,
        ),
        desc.File(
            name='imagePattern',
            label='Image Pattern',
            description='Image Pattern.',
            group='', # unnamed parameter
            value="",
            invalidate=True,
        ),
        desc.IntParam(
            name='imageSize',
            label='Image Size',
            description='Size of image (greater dimension).',
            group='', # unnamed parameter
            value=-1,
            range=(-1, 16000, 10),
            invalidate=True,
        ),
        desc.IntParam(
            name='MaxPoint',
            label='Max Point',
            description='Number of points used per image to construct the graph.',
            value=200,
            range=(1, 1000, 1),
            invalidate=True,
        ),
        desc.FloatParam(
            name="MinScale",
            label="Min Scale",
            description='Points with a lesser scale are ignored.',
            value=0.0,
            range=(0.0, 10000000000.0, 0.1),
            invalidate=True,
        ),
        desc.FloatParam(
            name="MaxScale",
            label="Max Scale",
            description='Points with a greater scale are ignored.',
            value=10000000000.0,
            range=(0.0, 10000000000.0, 0.1),
            invalidate=True,
        ),
        desc.IntParam(
            name='NbRequired',
            label='Nb Required',
            description='Number of matches to create a connexion between two images.',
            value=1,
            range=(1, 10000, 1),
            invalidate=True,
        ),
        desc.BoolParam(
            name='PrintGraph',
            label='Print Graph',
            description='Print result graph in standard output.', 
            value=False,
            invalidate=True,
        ),
    ]

    outputs = [
        desc.File(
            name='Out',
            label='Connectivity Graph',
            description='Name of the produced XML file.',
            value="tapioca_connectivity_graph.xml",
            invalidate=False,
        ),
    ]
