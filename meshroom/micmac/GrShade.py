__version__ = "1.2.0"

from meshroom.core import desc
from ..common import node

class GrShade(node.MicmacNode, desc.CommandLineNode):
    commandLine = 'mm3d GrShade {imageFileValue} {allParams}'
    documentation = 'GrShade: Compute a shaded relief image from a depth image (DEM).'

    inputs = [
        desc.File(
            name='projectDirectory',
            label='Project Directory',
            description='Project Directory.',
            value='',
            commandLineGroup='', # required to execute mm3d command line
        ),
        desc.File(
            name='imageFile',
            label='In Image File',
            description="Image of the relief file name.",
            commandLineGroup='', # unnamed parameter
            value='',
        ),
        desc.FloatParam(
            name='FZ',
            label='FZ',
            description='Step in z by which the relief is multiplied before being shaded.',
            value=1.0,
            range=(-3.0, 5.0, 0.1),
        ),
        desc.FloatParam(
            name='Anisotropie',
            label='Anisotropie',
            description='Anisotropie.',
            value=0.95,
            range=(0.0, 1.0, 0.05),
        ),
        desc.IntParam(
            name='Dequant',
            label='Dequant',
            description='Dequant.',
            value=0,
            range=(0, 10, 1),
        ),
        desc.BoolParam(
            name='setHypsoDyn',
            label='Set HypsoDyn',
            description='Set HypsoDyn.',
            value=False,
            advanced=True,
            commandLineGroup='', # enable 'HypsoDyn' attribute
        ),
        desc.FloatParam(
            name='HypsoDyn',
            label='HypsoDyn',
            description='HypsoDyn.',
            value=-1.0,
            range=(-5.0, 10.0, 0.5),
            enabled=lambda node: node.setHypsoDyn.value,
            advanced=True,
        ),
        desc.BoolParam(
            name='setHypsoSat',
            label='Set HypsoSat',
            description ='Set HypsoSat.',
            value=False,
            advanced=True,
            commandLineGroup='', # enable 'HypsoSat' attribute
        ),
        desc.FloatParam(
            name='HypsoSat',
            label='HypsoSat',
            description='HypsoSat.',
            value=0.5,
            range=(-5.0, 10.0, 0.5),
            enabled=lambda node: node.setHypsoSat.value,
            advanced=True,
        ),
        desc.BoolParam(
            name='Visu',
            label='Visu',
            description='Visu.',
            value=False,
            advanced=True,
        ),
        desc.File(
            name='FileCol',
            label='File Col',
            description='Color file.',
            value='',
        ),
        desc.StringParam(
            name='TypeMnt',
            label='Type Mnt',
            description='Type Mnt.',
            value='',
        ),
        desc.StringParam(
            name='TypeShade',
            label='Type Shade',
            description='Type Shade.',
            value='',
        ),
        desc.ChoiceParam(
            name='ModeOmbre',
            label='Mode Ombre',
            description='Mode Ombre.',
            value='IgnE',
            values=['CielVu','IgnE','Local','Med','Mixte'],
            exclusive=True,
        ),
        desc.File(
            name='Mask',
            label='Mask',
            description='Mask file.',
            value='',
        ),
        desc.StringParam(
            name='ModeColor',
            label='Mode Color',
            description='Color mode.',
            value='',
        ),
        desc.StringParam(
            name='Out',
            label='Output Filename',
            description='Output shaded image name.',
            value='Shade.tif',
        ),
    ]

    outputs = [
        desc.File(
            name='outImagePath',
            label='Shaded Image File',
            description='Output shaded image (absolute path).',
            value='{projectDirectoryValue}/{OutValue}',
            semantic='image',
            commandLineGroup='', # not a command line parameter
        ),
        desc.File(
            name='outImageFilename',
            label='Shaded Image Filename',
            description='Output shaded image name, relative to the project directory.',
            value='{OutValue}',
            commandLineGroup='', # not a command line parameter
        ),
    ]
