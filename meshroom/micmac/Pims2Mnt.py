__version__ = "1.2.0"

import sys
from meshroom.core import desc
from ..common import node

class Pims2Mnt(node.MicmacNode, desc.CommandLineNode):
    commandLine = 'mm3d Pims2Mnt {dirOrPIMValue} {allParams}'
    documentation = 'Pims2Mnt: Generate a DEM (and optionally an orthophoto) from Per Image Matchings (PIMs).'

    inputs = [
        desc.File(
            name='projectDirectory',
            label='Project Directory',
            description='Project Directory.',
            value="",
            commandLineGroup='', # required to execute mm3d command line
        ),
        desc.File(
            name='dirOrPIM',
            label='Dir Or PIM-Type',
            description="Dir or PIM-Type (QuickMac ....).",
            commandLineGroup='', # unnamed parameter
            value="",
        ),
        desc.FloatParam(
            name='DS',
            label='D S',
            description="Downscale, Def=1.0.",
            value=1.0,
            range=(-float('inf'), float('inf'), 0.01),
        ),
        desc.StringParam(
            name='Repere',
            label='Repere',
            description="Repair (Euclid or Cyl).",
            value="",
        ),
        desc.BoolParam(
            name='DoMnt',
            label='Do Mnt',
            description="Compute DTM (use false to return only ortho).",
            value=True,
        ),
        desc.BoolParam(
            name='DoOrtho',
            label='Do Ortho',
            description="Generate ortho photo.",
            value=False,
        ),
        desc.StringParam(
            name='MasqImGlob',
            label='Masq Im Glob',
            description="Global Masq for ortho: if used, give full name of masq (e.g. MasqGlob.tif).",
            value="",
        ),
        desc.BoolParam(
            name='UseTA',
            label='Use TA',
            description="Use TA as filter when exist.",
            value=False,
        ),
        desc.FloatParam(
            name='RI',
            label='R I',
            description="Resol Im, def=1.",
            value=1.0,
            range=(0.0, 10.0, 0.01),
        ),
        desc.FloatParam(
            name='SeuilE',
            label='Seuil E',
            description="Seuil d'etirement des triangle, Def=5.",
            value=5.0,
            range=(0.0, 100.0, 0.01),
        ),
        desc.IntParam(
            name='ZoomF',
            label='Zoom F',
            description="ZoomF.",
            value=2,
            range=(-sys.maxsize, sys.maxsize, 1),
        ),
        desc.File(
            name='DirMTD',
            label='Dir M T D',
            description="Subdirectory where the temporary results will be stored.",
            value="PIMs-TmpMnt/",
        ),
        desc.File(
            name='DirOrtho',
            label='Dir Ortho',
            description="Subdirectory for ortho images.",
            value="PIMs-ORTHO/",
        ),
        desc.File(
            name='DirBasc',
            label='Dir Basc',
            description="Subdirectory for surface model.",
            value="PIMs-TmpBasc/",
        ),
        desc.StringParam(
            name='NameMerge',
            label='Name Merge',
            description="BaseName of the surface model (*.xml).",
            value="PIMs-Merged.xml",
        ),
        desc.BoolParam(
            name='Debug',
            label='Debug',
            description="Debug mode.",
            value=False,
        ),
    ]

    outputs = [
    ]
