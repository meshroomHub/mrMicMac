__version__ = "0.1"

import sys
from meshroom.core import desc
from meshroomMicmac.custom import node

class Schnaps(node.MicmacNode):
    commandLine = 'mm3d Schnaps {imagePatternValue} {allParams}'
    documentation = 'Schnaps'

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
            name='imagePattern',
            label='Image Pattern',
            description='Image Pattern.',
            group='unnamedParams',
            value="",
            uid=[0],
        ),
        desc.File(
            name='HomolIn',
            label='Homol In',
            description="Input Homol directory suffix",
            uid=[0],
            value="",
        ),
        desc.IntParam(
            name='NbWin',
            label='Nb Win',
            description="Minimal homol points in each image (default: 1000)",
            uid=[0],
            value=1000,
            range=(-sys.maxsize, sys.maxsize, 1),
        ),
        desc.BoolParam(
            name='AppendHomolOut',
            label='Append Homol Out',
            description="Append to existing HomolOut for multi-step computaton (default: false)",
            uid=[0],
            value=False,
        ),
        desc.BoolParam(
            name='ExpTxt',
            label='Exp Txt',
            description="Ascii format for in and out, def=false",
            uid=[0],
            value=False,
        ),
        desc.BoolParam(
            name='VeryStrict',
            label='Very Strict',
            description="Be very strict with homols (remove any suspect), def=false",
            uid=[0],
            value=False,
        ),
        desc.BoolParam(
            name='ShowStats',
            label='Show Stats',
            description="Show Homol points stats before and after filtering, def=false",
            uid=[0],
            value=False,
        ),
        desc.BoolParam(
            name='DoNotFilter',
            label='Do Not Filter',
            description="Write homol after recomposition, without filtering, def=false",
            uid=[0],
            value=False,
        ),
        desc.GroupAttribute(
            name='FixSz',
            label='Fix Sz',
            description="Use a fixed size for image, do not read size in files",
            brackets='[]',
            joinChar=',',
            groupDesc=[
            desc.IntParam(
                name="x",
                label="X",
                description="x.",
                value=0,
                range=(-sys.maxsize, sys.maxsize, 1),
                uid=[0],
            ),
            desc.IntParam(
                name="y",
                label="Y",
                description="y.",
                value=0,
                range=(-sys.maxsize, sys.maxsize, 1),
                uid=[0],
            ),
        ]),
        desc.FloatParam(
            name='minPercentCoverage',
            label='Min Percent Coverage',
            description="Minimum % of coverage to avoid adding to poubelle, def=30",
            uid=[0],
            value=0.0,
            range=(-float('inf'), float('inf'), 0.01),
        ),
        desc.BoolParam(
            name='MoveBadImgs',
            label='Move Bad Imgs',
            description="Move bad images to a trash folder called Poubelle, Def=false",
            uid=[0],
            value=False,
        ),
        desc.IntParam(
            name='MiniMulti',
            label='Mini Multi',
            description="Minimal Multiplicity of selected points, Def=1",
            uid=[0],
            value=0,
            range=(-sys.maxsize, sys.maxsize, 1),
        ),
        desc.BoolParam(
            name='NetworkExport',
            label='Network Export',
            description="Export Network (in js), Def=false",
            uid=[0],
            value=False,
        ),
        desc.IntParam(
            name='DivPH',
            label='Div P H',
            description="in exported network, denominator to decrease the number of tie point which is used for displaying strength of a relation between 2 images, def 10.",
            uid=[0],
            value=0,
            range=(-sys.maxsize, sys.maxsize, 1),
        ),
        desc.BoolParam(
            name='ExeWrite',
            label='Exe Write',
            description="Do write output homol dir, def=true",
            uid=[0],
            value=True,
        ),
    ]

    outputs = [
        desc.File(
            name='HomolOut',
            label='Homol Out',
            description="Output Homol directory suffix (default: _mini)",
            uid=[0],
            value="_mini",
        ),
        desc.File(
            name='PoubelleName',
            label='Poubelle Name',
            description="Output filename with the list of suspicious images, def='Schnaps_poubelle.txt'",
            uid=[0],
            value="Schnaps_poubelle.txt",
        ),
        desc.File(
            name='OutTrash',
            label='Out Trash',
            description="Output name of trash folder if MoveBadImgs, Def=Poubelle",
            uid=[0],
            value="Poubelle",
        ),
    ]
