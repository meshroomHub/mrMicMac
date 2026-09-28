__version__ = "1.1.1"

import sys
from meshroom.core import desc
from ..common import node

class Pims2Mnt(node.MicmacNode, desc.CommandLineNode):
    commandLine = 'mm3d Pims2Mnt {dirOrPIMValue} {allParams}'
    documentation = 'Pims2Mnt'

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
            name='dirOrPIM',
            label='Dir Or PIM-Type',
            description="Dir or PIM-Type (QuickMac ....)",
            group='', # unnamed parameter
            invalidate=True,
            value="",
        ),
        desc.FloatParam(
            name='DS',
            label='D S',
            description="Downscale, Def=1.0",
            invalidate=True,
            value=1.0,
            range=(-float('inf'), float('inf'), 0.01),
        ),
        desc.StringParam(
            name='Repere',
            label='Repere',
            description="Repair (Euclid or Cyl)",
            invalidate=True,
            value="",
        ),
        desc.BoolParam(
            name='DoMnt',
            label='Do Mnt',
            description="Compute DTM (use false to return only ortho)",
            invalidate=True,
            value=True,
        ),
        desc.BoolParam(
            name='DoOrtho',
            label='Do Ortho',
            description="Generate ortho photo",
            invalidate=True,
            value=False,
        ),
        desc.StringParam(
            name='MasqImGlob',
            label='Masq Im Glob',
            description="Global Masq for ortho: if used, give full name of masq (e.g. MasqGlob.tif)",
            invalidate=True,
            value="",
        ),
        desc.BoolParam(
            name='UseTA',
            label='Use T A',
            description="Use TA as filter when exist",
            invalidate=True,
            value=False,
        ),
        desc.FloatParam(
            name='RI',
            label='R I',
            description="Resol Im, def=1",
            invalidate=True,
            value=1.0,
            range=(0.0, 10.0, 0.01),
        ),
        desc.FloatParam(
            name='SeuilE',
            label='Seuil E',
            description="Seuil d'etirement des triangle, Def=5",
            invalidate=True,
            value=5.0,
            range=(0.0, 100.0, 0.01),
        ),
        desc.IntParam(
            name='ZoomF',
            label='Zoom F',
            description="ZoomF",
            invalidate=True,
            value=2,
            range=(-sys.maxsize, sys.maxsize, 1),
        ),
        desc.File(
            name='DirMTD',
            label='Dir M T D',
            description="Subdirectory where the temporary results will be stored",
            invalidate=True,
            value="PIMs-TmpMnt/",
        ),
        desc.File(
            name='DirOrtho',
            label='Dir Ortho',
            description="Subdirectory for ortho images",
            invalidate=True,
            value="PIMs-ORTHO/",
        ),
        desc.File(
            name='DirBasc',
            label='Dir Basc',
            description="Subdirectory for surface model",
            invalidate=True,
            value="PIMs-TmpBasc/",
        ),
        desc.StringParam(
            name='NameMerge',
            label='Name Merge',
            description="BaseName of the surface model (*.xml)",
            invalidate=True,
            value="PIMs-Merged.xml",
        ),
        desc.BoolParam(
            name='Debug',
            label='Debug',
            description="Debug mode",
            invalidate=True,
            value=False,
        ),
    ]

    outputs = [
    ]
