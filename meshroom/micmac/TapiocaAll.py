__version__ = "1.1.1"

from meshroom.core import desc
from meshroomMicmac.custom import node

class TapiocaAll(node.MicmacNode):
    commandLine = 'mm3d Tapioca All {imagePatternValue} {imageSizeValue} {allParams} {wallisFilterValue}'
    documentation = '''Tapioca All'''

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
            name='imagePattern',
            label='Image Pattern',
            description='Image Pattern.',
            value='.*.(jpg|jpeg|JPG|JPEG|png|PNG|tif|tiff|TIF|TIFF)',
            group='', # unnamed parameter
            uid=[0],
        ),    
        desc.File(
            name='Pat2',
            label='Second Image Pattern',
            description="Second image pattern.",
            uid=[0],
            value="",
            advanced=True,
        ),
        desc.IntParam(
            name='imageSize',
            label='Image Size',
            description='Size of image.',
            group='', # unnamed parameter
            value=1000,
            range=(-1, 50000, 10),
            uid=[0],
        ),
        desc.BoolParam(
            name='setByP',
            label='Set ByP',
            description='Set ByP.', 
            value=False,
            uid=[0],
            group='',
        ),
        desc.IntParam(
            name='ByP',
            label='By P',
            description='By process.',
            enabled=lambda node: node.setByP.value,
            value=-1,
            range=(-1, 64, 1),
            uid=[0],
            advanced=True,
        ),
        desc.BoolParam(
            name='ExpTxt',
            label='Tie Points In Txt',
            description='Export files in text format (if false binary).', 
            value=False,
            uid=[0],
        ),
        desc.BoolParam(
            name='NoMax',
            label='No Max',
            description='No max.', 
            value=False,
            uid=[0],
            advanced=True,
        ),
        desc.BoolParam(
            name='NoMin',
            label='No Min',
            description='No min.', 
            value=False,
            uid=[0],
            advanced=True,
        ),
        desc.FloatParam(
            name='Ratio',
            label='ANN Ratio',
            description='ANN closeness ration.',
            value=0.6,
            range=(0.1, 1.0, 0.1),
            uid=[0],
            advanced=True,
        ),
        desc.ChoiceParam(
            name="wallisFilter",
            label="Wallis Filter",
            description="Apply Wallis filter.",
            group='', # keys
            value="",
            values=["", "@SFS"],
            exclusive=True,
            uid=[0],
            advanced=True,
        ),
    ]

    outputs = [
        desc.File(
            name='PostFix',
            label='Homol Directory', # Directory Postfix
            description='Homol Directory.',
            value="All",
            uid=[],
        ),
    ]