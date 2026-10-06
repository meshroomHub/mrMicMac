__version__ = "1.2.0"

from meshroom.core import desc
from ..common import node

class MaltOrtho(node.MicmacNode, desc.CommandLineNode):
    commandLine = 'mm3d Malt Ortho {imagePatternValue} {orientationDirValue} {allParams}'
    documentation = 'MaltOrtho: Simplified interface to MicMac dense matching in Ortho mode, producing a DEM and individual orthophotos.'

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
        desc.File(
            name='orientationDir',
            label='Orientation Directory',
            description='Orientation directory name.',
            commandLineGroup='', # unnamed parameter
            value="",
        ),
        desc.BoolParam(
            name='EZA',
            label='Export Z Absolute',
            description="Export Z absolute.",
            value=True,
        ),
        desc.BoolParam(
            name='DoMEC',
            label='Do The Matching',
            description="Do the matching.",
            value=True,
        ),
        desc.StringParam(
            name='DirMEC',
            label='Dir MEC',
            description="Subdirectory where the results will be stored.",
            value="",
        ),
        desc.StringParam(
            name='DirOF',
            label='Dir OF',
            description="Subdirectory for ortho (Def in Ortho-DirMEC).",
            value="",
        ),
        desc.StringParam(
            name='ImOrtho',
            label='Im Ortho',
            description="Filter to select images used for ortho (Def All).",
            value="",
        ),
        desc.IntParam(
            name='ZoomF',
            label='Zoom F',
            description="Final zoom (Def 2 in ortho).",
            value=2,
            range=(1, 64, 1),
        ),
        desc.BoolParam(
            name='setRegul',
            label='Set Regul',
            description="Set Regul.",
            value=False,
            commandLineGroup='', # enable 'Regul' attribute
        ),
        desc.FloatParam(
            name='Regul',
            label='Regul',
            description="Regularization factor.",
            enabled=lambda node: node.setRegul.value,
            value=0.05,
            range=(0.0, 10.0, 0.001),
        ),
        # Advanced usage
        desc.BoolParam(
            name='setSzW',
            label='Set Sz W',
            description="Set Sz W.",
            value=False,
            commandLineGroup='', # enable 'SzW' attribute
            advanced=True,
        ),
        desc.IntParam(
            name='SzW',
            label='Correlation Window Size',
            description="Correlation window size (1 means 3x3).",
            enabled=lambda node: node.setSzW.value,
            value=1,
            range=(1, 20, 1),
            advanced=True,
        ),
        desc.IntParam(
            name='NbVI',
            label='Nb VI',
            description="Number of visible images required (Def=3), use 2 when the overlap is low.",
            value=3,
            range=(1, 100, 1),
            advanced=True,
        ),
        desc.File(
            name='Repere',
            label='Repere',
            description="Local system of coordinates.",
            value="",
            advanced=True,
        ),
        desc.StringParam(
            name='DirPyram',
            label='Dir Pyram',
            description="Subdirectory where the pyramids will be stored.",
            value="",
            advanced=True,
        ),
        desc.File(
            name='Masq3D',
            label='3D Mask',
            description="Name of 3D Masq.",
            value="",
            advanced=True,
        ),
        desc.StringParam(
            name='MasqIm',
            label='Masq Im',
            description='Masq per image (Def None), use "Masq" for standard result of SaisieMasq.',
            value="",
            advanced=True,
        ),
        desc.StringParam(
            name='MasqImGlob',
            label='Masq Im Glob',
            description="Global Masq per image: if used, give full name of masq (e.g. a.tif).",
            value="",
            advanced=True,
        ),
        desc.BoolParam(
            name='setBoxTerrain',
            label='Set Box Terrain',
            description="Set Box Terrain.",
            value=False,
            commandLineGroup='', # enable 'BoxTerrain' attribute
            advanced=True,
        ),
        desc.GroupAttribute(
            name='BoxTerrain',
            label='Box Terrain',
            description="Ground box ([Xmin,Ymin,Xmax,Ymax]).",
            brackets='[]',
            joinChar=',',
            enabled=lambda node: node.setBoxTerrain.value,
            advanced=True,
            items=[
                desc.FloatParam(
                    name="xMin",
                    label="X Min",
                    description="X Min.",
                    value=0.0,
                    range=(-1000000.0, 1000000.0, 0.01),
                ),
                desc.FloatParam(
                    name="yMin",
                    label="Y Min",
                    description="Y Min.",
                    value=0.0,
                    range=(-1000000.0, 1000000.0, 0.01),
                ),
                desc.FloatParam(
                    name="xMax",
                    label="X Max",
                    description="X Max.",
                    value=0.0,
                    range=(-1000000.0, 1000000.0, 0.01),
                ),
                desc.FloatParam(
                    name="yMax",
                    label="Y Max",
                    description="Y Max.",
                    value=0.0,
                    range=(-1000000.0, 1000000.0, 0.01),
                ),
            ]
        ),
        desc.BoolParam(
            name='setResolTerrain',
            label='Set Resol Terrain',
            description="Set Resol Terrain.",
            value=False,
            commandLineGroup='', # enable 'ResolTerrain' attribute
            advanced=True,
        ),
        desc.FloatParam(
            name='ResolTerrain',
            label='Resol Terrain',
            description="Ground resolution (Def automatically computed).",
            enabled=lambda node: node.setResolTerrain.value,
            value=1.0,
            range=(0.0, 100000.0, 0.001),
            advanced=True,
        ),
        desc.FloatParam(
            name='ResolOrtho',
            label='Resol Ortho',
            description="Resolution of ortho, relatively to images (Def=1.0; 0.5 means smaller images, i.e. decrease the resolution).",
            value=1.0,
            range=(0.0, 10.0, 0.01),
            advanced=True,
        ),
        desc.BoolParam(
            name='Purge',
            label='Purge',
            description="Purge the directory of results before compute.",
            value=True,
            advanced=True,
        ),
        desc.BoolParam(
            name='setZoomI',
            label='Set Zoom I',
            description="Set Zoom I.",
            value=False,
            commandLineGroup='', # enable 'ZoomI' attribute
            advanced=True,
        ),
        desc.IntParam(
            name='ZoomI',
            label='Zoom I',
            description="Initial zoom (Def depends on number of images).",
            enabled=lambda node: node.setZoomI.value,
            value=32,
            range=(1, 128, 1),
            advanced=True,
        ),
        desc.IntParam(
            name='UseTA',
            label='Use TA',
            description="Use TA as Masq when it exists (Def is true).",
            value=1,
            range=(0, 1, 1),
            advanced=True,
        ),
        desc.StringParam(
            name='DirTA',
            label='Dir TA',
            description="Directory of TA (for mask).",
            value="",
            advanced=True,
        ),
        desc.FloatParam(
            name='ZPas',
            label='Z Pas',
            description="Quantification step in equivalent pixel (Def=0.4).",
            value=0.4,
            range=(0.0, 10.0, 0.01),
            advanced=True,
        ),
        desc.BoolParam(
            name='setHrOr',
            label='Set Hr Or',
            description="Set Hr Or.",
            value=False,
            commandLineGroup='', # enable 'HrOr' attribute
            advanced=True,
        ),
        desc.BoolParam(
            name='HrOr',
            label='Hr Or',
            description="Compute high resolution ortho.",
            enabled=lambda node: node.setHrOr.value,
            value=True,
            advanced=True,
        ),
        desc.BoolParam(
            name='setLrOr',
            label='Set Lr Or',
            description="Set Lr Or.",
            value=False,
            commandLineGroup='', # enable 'LrOr' attribute
            advanced=True,
        ),
        desc.BoolParam(
            name='LrOr',
            label='Lr Or',
            description="Compute low resolution ortho.",
            enabled=lambda node: node.setLrOr.value,
            value=True,
            advanced=True,
        ),
        desc.BoolParam(
            name='setUnAnam',
            label='Set Un Anam',
            description="Set Un Anam.",
            value=False,
            commandLineGroup='', # enable 'UnAnam' attribute
            advanced=True,
        ),
        desc.BoolParam(
            name='UnAnam',
            label='Un Anam',
            description="Compute the un-anamorphosed DTM and ortho (Def context dependent).",
            enabled=lambda node: node.setUnAnam.value,
            value=True,
            advanced=True,
        ),
        desc.BoolParam(
            name='set2Ortho',
            label='Set 2 Ortho',
            description="Set 2 Ortho.",
            value=False,
            commandLineGroup='', # enable '2Ortho' attribute
            advanced=True,
        ),
        desc.BoolParam(
            name='2Ortho',
            label='2 Ortho',
            description="Do both anamorphosed and un-anamorphosed ortho (when applicable).",
            enabled=lambda node: node.set2Ortho.value,
            value=True,
            advanced=True,
        ),
        desc.FloatParam(
            name='ZInc',
            label='Z Uncertainty',
            description="Uncertainty on Z (in proportion of average depth, Def=0.3).",
            value=0.3,
            range=(0.0, 10.0, 0.01),
            advanced=True,
        ),
        desc.FloatParam(
            name='DefCor',
            label='Def Cor',
            description="Default correlation in uncorrelated pixels (Def=0.2).",
            value=0.2,
            range=(0.0, 1.0, 0.01),
            advanced=True,
        ),
        desc.BoolParam(
            name='AffineLast',
            label='Affine Last',
            description="Affine last step with step Z/2 (Def=true).",
            value=True,
            advanced=True,
        ),
        desc.BoolParam(
            name='setZMoy',
            label='Set ZMoy',
            description="Set ZMoy.",
            value=False,
            commandLineGroup='', # enable 'ZMoy' attribute
            advanced=True,
        ),
        desc.FloatParam(
            name='ZMoy',
            label='Average Z',
            description="Average value of Z.",
            enabled=lambda node: node.setZMoy.value,
            value=0.0,
            range=(-100000.0, 100000.0, 0.01),
            advanced=True,
        ),
    ]

    outputs = [
        desc.File(
            name='mecDirectory',
            label='MEC Directory',
            description="Directory of the matching results.",
            value=lambda node: node.DirMEC.value or 'MEC-Malt',
            commandLineGroup='', # not a command line parameter
            invalidate=False,
        ),
        desc.File(
            name='orthoDirectory',
            label='Ortho Directory',
            description="Directory of the individual orthophotos.",
            value=lambda node: node.DirOF.value or 'Ortho-' + (node.DirMEC.value or 'MEC-Malt'),
            commandLineGroup='', # not a command line parameter
            invalidate=False,
        ),
    ]
