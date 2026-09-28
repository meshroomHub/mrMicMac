__version__ = "0.0"

import sys
from meshroom.core import desc
from meshroomMicmac.custom import node

class MeshCloudClip(node.MicmacNode):
    commandLine = 'MMVII MeshCloudClip {CloudValue} {3DRegValue} {allParams}'
    documentation = 'MeshCloudClip'
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
            label='Input mesh',
            description='Name of input cloud mesh',
            group='unnamedParams',
            value='',
            uid=[0],
        ),
        desc.File(
            name='3DReg',
            label='3D masq',
            description='Name of 3D masq',
            group='unnamedParams',
            value='',
            uid=[0],
        ),
        desc.BoolParam(
            name='Bin',
            label='Bin',
            description="Generate out in binary format ,[Default=false]",
            uid=[0],
            value=False,
        ),
        desc.IntParam(
            name='NbMinV',
            label='Nb Min V',
            description="Number minimal of vertex to maintain a triangle ,[Default=3]",
            uid=[0],
            value=3,
            range=(-sys.maxsize, sys.maxsize, 1),
        ),
    ]

    outputs = [
        desc.File(
            name='Out',
            label='Clipped mesh',
            description="Name of output file",
            uid=[0],
            value="Clip_mesh.ply",
        ),
    ]
