__version__ = "0.0"

import sys
from meshroom.core import desc
from ..common import node

class MeshCheck(node.MicmacNode, desc.CommandLineNode):
    commandLine = 'MMVII MeshCheck {CloudValue} {allParams}'
    documentation = 'MeshCheck'
    category = 'MicMacV2'

    inputs = [
        desc.File(
            name='projectDirectory',
            label='Project Directory',
            description='Project Directory.',
            value="",
            commandLineGroup="micmac",
        ),
        desc.File(
            name='Cloud',
            label='Mesh/Cloud',
            description='Name of input cloud/mesh',
            commandLineGroup='unnamedParams',
            value="",
        ),
        desc.BoolParam(
            name='Bin',
            label='Bin',
            description="Generate out in binary format ,[Default=false]",
            value=False,
        ),
        desc.BoolParam(
            name='Do2DC',
            label='Do2 DC',
            description="check also as a 2D-triangulation (orientation) ,[Default=false]",
            value=False,
        ),
        desc.BoolParam(
            name='Correct',
            label='Correct',
            description="Do correction, Defaut: Do It Out specified",
            value=True,
        ),
    ]

    outputs = [
        desc.File(
            name='Out',
            label='Corrected mesh',
            description="Name of output file if correction are done",
            value="Correc_mesh.ply",
        ),
    ]
