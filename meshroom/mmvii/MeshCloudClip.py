__version__ = "0.0"

import sys
from meshroom.core import desc
from ..common import node

class MeshCloudClip(node.MicmacNode, desc.CommandLineNode):
    commandLine = 'MMVII MeshCloudClip {CloudValue} {3DRegValue} {allParams}'
    documentation = 'MeshCloudClip: Clip a mesh or point cloud using a 3D region.'
    category = 'MicMacV2'

    inputs = [
        desc.File(
            name='projectDirectory',
            label='Project Directory',
            description='Project Directory.',
            value="",
            commandLineGroup='', # required to execute mm3d command line
        ),
        desc.File(
            name='Cloud',
            label='Input mesh',
            description='Name of input cloud mesh.',
            commandLineGroup='', # unnamed parameter
            value='',
        ),
        desc.File(
            name='3DReg',
            label='3D masq',
            description='Name of 3D masq.',
            commandLineGroup='', # unnamed parameter
            value='',
        ),
        desc.BoolParam(
            name='Bin',
            label='Bin',
            description="Generate out in binary format ,[Default=false].",
            value=False,
        ),
        desc.IntParam(
            name='NbMinV',
            label='Nb Min V',
            description="Number minimal of vertex to maintain a triangle ,[Default=3].",
            value=3,
            range=(-sys.maxsize, sys.maxsize, 1),
        ),
        desc.StringParam(
            name='Out',
            label='Output Filename',
            description="Name of output file (use a .pc.ply suffix when clipping a point cloud, to display it in the 3D Viewer).",
            value="Clip_mesh.ply",
        ),
    ]

    outputs = [
        desc.File(
            name='outMeshPath',
            label='Clipped Mesh',
            description="Output clipped mesh (absolute path).",
            value="{projectDirectoryValue}/{OutValue}",
            semantic='3d',
            commandLineGroup='', # not a command line parameter
            invalidate=False,
        ),
        desc.File(
            name='outMeshFilename',
            label='Clipped Mesh Filename',
            description="Name of output clipped mesh, relative to the project directory.",
            value="{OutValue}",
            commandLineGroup='', # not a command line parameter
            invalidate=False,
        ),
    ]
