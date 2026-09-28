__version__ = "1.1.1"

import sys
from meshroom.core import desc
from meshroomMicmac.custom import node

class Pims2Mnt(node.MicmacNode):
    commandLine = 'mm3d Pims2Mnt {dirOrPIMValue} {allParams}'
    documentation = 'Pims2Mnt'

    inputs = [
        desc.File(
            name='projectDirectory',
            label='Project Directory',
            description='Project Directory.',
            value="",
            group='', # required to execute mm3d command line
            uid=[0],
        ),
        desc.File(
            name='dirOrPIM',
            label='Dir Or PIM-Type',
            description="Dir or PIM-Type (QuickMac ....)",
            group='', # unnamed parameter
            uid=[0],
            value="",
        ),
        desc.FloatParam(
            name='DS',
            label='D S',
            description="Downscale, Def=1.0",
            uid=[0],
            value=1.0,
            range=(-float('inf'), float('inf'), 0.01),
        ),
        desc.StringParam(
            name='Repere',
            label='Repere',
            description="Repair (Euclid or Cyl)",
            uid=[0],
            value="",
        ),
        desc.BoolParam(
            name='DoMnt',
            label='Do Mnt',
            description="Compute DTM (use false to return only ortho)",
            uid=[0],
            value=True,
        ),
        desc.BoolParam(
            name='DoOrtho',
            label='Do Ortho',
            description="Generate ortho photo",
            uid=[0],
            value=False,
        ),
        desc.StringParam(
            name='MasqImGlob',
            label='Masq Im Glob',
            description="Global Masq for ortho: if used, give full name of masq (e.g. MasqGlob.tif)",
            uid=[0],
            value="",
        ),
        desc.BoolParam(
            name='UseTA',
            label='Use T A',
            description="Use TA as filter when exist",
            uid=[0],
            value=False,
        ),
        desc.FloatParam(
            name='RI',
            label='R I',
            description="Resol Im, def=1",
            uid=[0],
            value=1.0,
            range=(0.0, 10.0, 0.01),
        ),
        desc.FloatParam(
            name='SeuilE',
            label='Seuil E',
            description="Seuil d'etirement des triangle, Def=5",
            uid=[0],
            value=5.0,
            range=(0.0, 100.0, 0.01),
        ),
        desc.IntParam(
            name='ZoomF',
            label='Zoom F',
            description="ZoomF",
            uid=[0],
            value=2,
            range=(-sys.maxsize, sys.maxsize, 1),
        ),
        desc.File(
            name='DirMTD',
            label='Dir M T D',
            description="Subdirectory where the temporary results will be stored",
            uid=[0],
            value="PIMs-TmpMnt/",
        ),
        desc.File(
            name='DirOrtho',
            label='Dir Ortho',
            description="Subdirectory for ortho images",
            uid=[0],
            value="PIMs-ORTHO/",
        ),
        desc.File(
            name='DirBasc',
            label='Dir Basc',
            description="Subdirectory for surface model",
            uid=[0],
            value="PIMs-TmpBasc/",
        ),
        desc.StringParam(
            name='NameMerge',
            label='Name Merge',
            description="BaseName of the surface model (*.xml)",
            uid=[0],
            value="PIMs-Merged.xml",
        ),
        desc.BoolParam(
            name='Debug',
            label='Debug',
            description="Debug mode",
            uid=[0],
            value=False,
        ),
    ]

    outputs = [
    ]
