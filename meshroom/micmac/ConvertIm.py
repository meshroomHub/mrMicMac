__version__ = "1.2.0"

from meshroom.core import desc
from ..common import node

class ConvertIm(node.MicmacNode, desc.CommandLineNode):
    commandLine = 'mm3d ConvertIm {imageValue} {allParams}'
    documentation = 'ConvertIm: Convert an image (format, type, channels, size, crop, dynamic).'

    inputs = [
        desc.File(
            name='projectDirectory',
            label='Project Directory',
            description='Project Directory.',
            value="",
            commandLineGroup='', # required to execute mm3d command line
        ),
        desc.File(
            name='image',
            label='In Image File',
            description='Image.',
            commandLineGroup='', # unnamed parameter
            value="",
        ),
        desc.StringParam(
            name='Out',
            label='Output Filename',
            description="Output image name (Def=input+_Out).",
            value="",
        ),
        desc.StringParam(
            name='Ext',
            label='Extension',
            description="Output image extension (Def=tif).",
            value="",
        ),
        desc.BoolParam(
            name='setType',
            label='Set Type',
            description="Set Type.",
            value=False,
            commandLineGroup='', # enable 'Type' attribute
        ),
        desc.ChoiceParam(
            name='Type',
            label='Type',
            description="Output pixel type.",
            enabled=lambda node: node.setType.value,
            value='u_int1',
            values=['u_int1', 'int1', 'u_int2', 'int2', 'int4', 'real4', 'real8'],
            exclusive=True,
        ),
        desc.BoolParam(
            name='setCol',
            label='Set Color',
            description="Set Color.",
            value=False,
            commandLineGroup='', # enable 'Col' attribute
        ),
        desc.ChoiceParam(
            name='Col',
            label='Color',
            description="Col in RGB BW.",
            enabled=lambda node: node.setCol.value,
            value='RGB',
            values=['RGB', 'BW'],
            exclusive=True,
        ),
        desc.BoolParam(
            name='setSzOut',
            label='Set Sz Out',
            description="Set Sz Out.",
            value=False,
            commandLineGroup='', # enable 'SzOut' attribute
            advanced=True,
        ),
        desc.GroupAttribute(
            name='SzOut',
            label='Sz Out',
            description="Size out.",
            enabled=lambda node: node.setSzOut.value,
            brackets='[]',
            joinChar=',',
            items=[
                desc.IntParam(
                    name="x",
                    label="X",
                    description="x.",
                    value=0,
                    range=(0, 100000, 1),
                ),
                desc.IntParam(
                    name="y",
                    label="Y",
                    description="y.",
                    value=0,
                    range=(0, 100000, 1),
                ),
            ],
            advanced=True,
        ),
        desc.BoolParam(
            name='setP0',
            label='Set P0',
            description="Set P0.",
            value=False,
            commandLineGroup='', # enable 'P0' attribute
            advanced=True,
        ),
        desc.GroupAttribute(
            name='P0',
            label='P0',
            description="Origin of the output in the input image.",
            enabled=lambda node: node.setP0.value,
            brackets='[]',
            joinChar=',',
            items=[
                desc.IntParam(
                    name="x",
                    label="X",
                    description="x.",
                    value=0,
                    range=(0, 100000, 1),
                ),
                desc.IntParam(
                    name="y",
                    label="Y",
                    description="y.",
                    value=0,
                    range=(0, 100000, 1),
                ),
            ],
            advanced=True,
        ),
        desc.BoolParam(
            name='setReducXY',
            label='Set Reduc XY',
            description="Set Reduc XY.",
            value=False,
            commandLineGroup='', # enable 'ReducXY' attribute
            advanced=True,
        ),
        desc.IntParam(
            name='ReducXY',
            label='Reduc XY',
            description="Reduction factor in X and Y.",
            enabled=lambda node: node.setReducXY.value,
            value=1,
            range=(1, 1000, 1),
            advanced=True,
        ),
        desc.BoolParam(
            name='setReducX',
            label='Set Reduc X',
            description="Set Reduc X.",
            value=False,
            commandLineGroup='', # enable 'ReducX' attribute
            advanced=True,
        ),
        desc.IntParam(
            name='ReducX',
            label='Reduc X',
            description="Reduction factor in X.",
            enabled=lambda node: node.setReducX.value,
            value=1,
            range=(1, 1000, 1),
            advanced=True,
        ),
        desc.BoolParam(
            name='setReducY',
            label='Set Reduc Y',
            description="Set Reduc Y.",
            value=False,
            commandLineGroup='', # enable 'ReducY' attribute
            advanced=True,
        ),
        desc.IntParam(
            name='ReducY',
            label='Reduc Y',
            description="Reduction factor in Y.",
            enabled=lambda node: node.setReducY.value,
            value=1,
            range=(1, 1000, 1),
            advanced=True,
        ),
        desc.BoolParam(
            name='setVisu',
            label='Set Visu',
            description="Set Visu.",
            value=False,
            commandLineGroup='', # enable 'Visu' attribute
            advanced=True,
        ),
        desc.IntParam(
            name='Visu',
            label='Visu',
            description="Visu.",
            enabled=lambda node: node.setVisu.value,
            value=0,
            range=(0, 1, 1),
            advanced=True,
        ),
        desc.BoolParam(
            name='setSzTifTile',
            label='Set Sz Tif Tile',
            description="Set Sz Tif Tile.",
            value=False,
            commandLineGroup='', # enable 'SzTifTile' attribute
            advanced=True,
        ),
        desc.GroupAttribute(
            name='SzTifTile',
            label='Sz Tif Tile',
            description="Size of tif tiles.",
            enabled=lambda node: node.setSzTifTile.value,
            brackets='[]',
            joinChar=',',
            items=[
                desc.IntParam(
                    name="x",
                    label="X",
                    description="x.",
                    value=0,
                    range=(0, 100000, 1),
                ),
                desc.IntParam(
                    name="y",
                    label="Y",
                    description="y.",
                    value=0,
                    range=(0, 100000, 1),
                ),
            ],
            advanced=True,
        ),
        desc.BoolParam(
            name='setSzTileInterne',
            label='Set Sz Tile Interne',
            description="Set Sz Tile Interne.",
            value=False,
            commandLineGroup='', # enable 'SzTileInterne' attribute
            advanced=True,
        ),
        desc.GroupAttribute(
            name='SzTileInterne',
            label='Sz Tile Interne',
            description="Size of internal tiles.",
            enabled=lambda node: node.setSzTileInterne.value,
            brackets='[]',
            joinChar=',',
            items=[
                desc.IntParam(
                    name="x",
                    label="X",
                    description="x.",
                    value=0,
                    range=(0, 100000, 1),
                ),
                desc.IntParam(
                    name="y",
                    label="Y",
                    description="y.",
                    value=0,
                    range=(0, 100000, 1),
                ),
            ],
            advanced=True,
        ),
        desc.BoolParam(
            name='setDyn',
            label='Set Dyn',
            description="Set Dyn.",
            value=False,
            commandLineGroup='', # enable 'Dyn' attribute
            advanced=True,
        ),
        desc.FloatParam(
            name='Dyn',
            label='Dyn',
            description="Dynamic applied to pixel values.",
            enabled=lambda node: node.setDyn.value,
            value=1.0,
            range=(-100000.0, 100000.0, 0.01),
            advanced=True,
        ),
        desc.BoolParam(
            name='setKCh',
            label='Set KCh',
            description="Set KCh.",
            value=False,
            commandLineGroup='', # enable 'KCh' attribute
            advanced=True,
        ),
        desc.IntParam(
            name='KCh',
            label='KCh',
            description="Index of the channel to extract.",
            enabled=lambda node: node.setKCh.value,
            value=0,
            range=(0, 100, 1),
            advanced=True,
        ),
        desc.BoolParam(
            name='setNoTile',
            label='Set No Tile',
            description="Set No Tile.",
            value=False,
            commandLineGroup='', # enable 'NoTile' attribute
            advanced=True,
        ),
        desc.IntParam(
            name='NoTile',
            label='No Tile',
            description="Do not tile the output file.",
            enabled=lambda node: node.setNoTile.value,
            value=1,
            range=(0, 1, 1),
            advanced=True,
        ),
        desc.StringParam(
            name='Permut',
            label='Permut',
            description="Permutation of channels, as [i,j,k].",
            value="",
            advanced=True,
        ),
        desc.StringParam(
            name='F2',
            label='F2',
            description="F2.",
            value="",
            advanced=True,
        ),
    ]

    outputs = [
        desc.File(
            name='outImageFilename',
            label='Image Filename',
            description="Output image name, relative to the project directory.",
            value=lambda node: node.Out.value or ((node.Ext.value or '_Out') + '.').join(node.image.value.replace('"', '').rsplit('.', 1)),
            commandLineGroup='', # not a command line parameter
            invalidate=False,
        ),
        desc.File(
            name='outImagePath',
            label='Image File',
            description="Output image (absolute path).",
            value='{projectDirectoryValue}/{outImageFilenameValue}',
            semantic='image',
            commandLineGroup='', # not a command line parameter
            invalidate=False,
        ),
    ]
