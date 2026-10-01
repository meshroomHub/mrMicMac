__version__ = "1.2.0"

from meshroom.core import desc
from ..common import node

class TapiocaGraph(node.MicmacNode, desc.CommandLineNode):
    commandLine = 'mm3d Tapioca Graph {imagePatternValue} {imageSizeValue} {allParams}'
    documentation = 'Tapioca Graph: Compute an image connectivity graph (XML pairs file) from a few tie points per image.'

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
            description='Size of image (greater dimension).',
            commandLineGroup='', # unnamed parameter
            value=-1,
            range=(-1, 16000, 10),
        ),
        desc.IntParam(
            name='MaxPoint',
            label='Max Point',
            description='Number of points used per image to construct the graph.',
            value=200,
            range=(1, 1000, 1),
        ),
        desc.FloatParam(
            name="MinScale",
            label="Min Scale",
            description='Points with a lesser scale are ignored.',
            value=0.0,
            range=(0.0, 10000000000.0, 0.1),
        ),
        desc.FloatParam(
            name="MaxScale",
            label="Max Scale",
            description='Points with a greater scale are ignored.',
            value=10000000000.0,
            range=(0.0, 10000000000.0, 0.1),
        ),
        desc.IntParam(
            name='NbRequired',
            label='Nb Required',
            description='Number of matches to create a connexion between two images.',
            value=1,
            range=(1, 10000, 1),
        ),
        desc.BoolParam(
            name='PrintGraph',
            label='Print Graph',
            description='Print result graph in standard output.',
            value=False,
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
