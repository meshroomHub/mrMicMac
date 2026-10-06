__version__ = "1.2.0"

from meshroom.core import desc
from ..common import node

class TapiocaAll(node.MicmacNode, desc.CommandLineNode):
    commandLine = 'mm3d Tapioca All {imagePatternValue} {imageSizeValue} {allParams} {wallisFilterValue}'
    documentation = 'Tapioca All: Detect and match tie points between all image pairs.'

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
            value='.*.(jpg|jpeg|JPG|JPEG|png|PNG|tif|tiff|TIF|TIFF)',
            commandLineGroup='', # unnamed parameter
        ),
        desc.File(
            name='Pat2',
            label='Second Image Pattern',
            description="Second image pattern.",
            value="",
            advanced=True,
        ),
        desc.IntParam(
            name='imageSize',
            label='Image Size',
            description='Size of image.',
            commandLineGroup='', # unnamed parameter
            value=1000,
            range=(-1, 50000, 10),
        ),
        desc.BoolParam(
            name='setByP',
            label='Set ByP',
            description='Set ByP.',
            value=False,
            commandLineGroup='', # enable 'ByP' attribute
        ),
        desc.IntParam(
            name='ByP',
            label='ByP',
            description='By process.',
            enabled=lambda node: node.setByP.value,
            value=-1,
            range=(-1, 64, 1),
            advanced=True,
        ),
        desc.BoolParam(
            name='ExpTxt',
            label='Tie Points In Txt',
            description='Export files in text format (if false binary).',
            value=False,
        ),
        desc.BoolParam(
            name='NoMax',
            label='No Max',
            description='No max.',
            value=False,
            advanced=True,
        ),
        desc.BoolParam(
            name='NoMin',
            label='No Min',
            description='No min.',
            value=False,
            advanced=True,
        ),
        desc.FloatParam(
            name='Ratio',
            label='ANN Ratio',
            description='ANN closeness ration.',
            value=0.6,
            range=(0.1, 1.0, 0.1),
            advanced=True,
        ),
        desc.ChoiceParam(
            name="wallisFilter",
            label="Wallis Filter",
            description="Apply Wallis filter.",
            commandLineGroup='', # unnamed parameter
            value="",
            values=["", "@SFS"],
            exclusive=True,
            advanced=True,
        ),
    ]

    outputs = [
        desc.File(
            name='PostFix',
            label='Homol Directory', # Directory Postfix
            description='Homol Directory.',
            value="All",
            invalidate=False,
        ),
    ]
