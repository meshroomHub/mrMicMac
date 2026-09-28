__version__ = "0.0"

import sys
from meshroom.core import desc
from meshroomMicmac.custom import node

class MeshCheck(node.MicmacNode):
    commandLine = 'MMVII MeshCheck {CloudValue} {allParams}'
    documentation = 'MeshCheck'
    category = 'MicMacV2'

    inputs = [
        desc.File(
            name='projectDirectory',
            label='Project Directory',
            description='Project Directory.',
            value="",
            group="micmac",
            uid=[0],
        ),
        desc.File(
            name='Cloud',
            label='Mesh/Cloud',
            description='Name of input cloud/mesh',
            group='unnamedParams',
            value="",
            uid=[0],
        ),
        desc.BoolParam(
            name='Bin',
            label='Bin',
            description="Generate out in binary format ,[Default=false]",
            uid=[0],
            value=False,
        ),
        desc.BoolParam(
            name='Do2DC',
            label='Do2 DC',
            description="check also as a 2D-triangulation (orientation) ,[Default=false]",
            uid=[0],
            value=False,
        ),
        desc.BoolParam(
            name='Correct',
            label='Correct',
            description="Do correction, Defaut: Do It Out specified",
            uid=[0],
            value=True,
        ),
    ]

    outputs = [
        desc.File(
            name='Out',
            label='Corrected mesh',
            description="Name of output file if correction are done",
            uid=[0],
            value="Correc_mesh.ply",
        ),
    ]
