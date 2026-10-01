__version__ = "0.1"

import sys
from meshroom.core import desc
from ..common import node

class Schnaps(node.MicmacNode, desc.CommandLineNode):
    commandLine = 'mm3d Schnaps {imagePatternValue} {allParams}'
    documentation = 'Schnaps: Reduce and filter tie points in image geometry.'

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
            name='HomolIn',
            label='Homol In',
            description="Input Homol directory suffix",
            value="",
        ),
        desc.IntParam(
            name='NbWin',
            label='Nb Win',
            description="Minimal homol points in each image (default: 1000)",
            value=1000,
            range=(-sys.maxsize, sys.maxsize, 1),
        ),
        desc.BoolParam(
            name='AppendHomolOut',
            label='Append Homol Out',
            description="Append to existing HomolOut for multi-step computaton (default: false)",
            value=False,
        ),
        desc.BoolParam(
            name='ExpTxt',
            label='Exp Txt',
            description="Ascii format for in and out, def=false",
            value=False,
        ),
        desc.BoolParam(
            name='VeryStrict',
            label='Very Strict',
            description="Be very strict with homols (remove any suspect), def=false",
            value=False,
        ),
        desc.BoolParam(
            name='ShowStats',
            label='Show Stats',
            description="Show Homol points stats before and after filtering, def=false",
            value=False,
        ),
        desc.BoolParam(
            name='DoNotFilter',
            label='Do Not Filter',
            description="Write homol after recomposition, without filtering, def=false",
            value=False,
        ),
        desc.GroupAttribute(
            name='FixSz',
            label='Fix Sz',
            description="Use a fixed size for image, do not read size in files",
            brackets='[]',
            joinChar=',',
            items=[
            desc.IntParam(
                name="x",
                label="X",
                description="x.",
                value=0,
                range=(-sys.maxsize, sys.maxsize, 1),
            ),
            desc.IntParam(
                name="y",
                label="Y",
                description="y.",
                value=0,
                range=(-sys.maxsize, sys.maxsize, 1),
            ),
        ]),
        desc.FloatParam(
            name='minPercentCoverage',
            label='Min Percent Coverage',
            description="Minimum % of coverage to avoid adding to poubelle, def=30",
            value=0.0,
            range=(-float('inf'), float('inf'), 0.01),
        ),
        desc.BoolParam(
            name='MoveBadImgs',
            label='Move Bad Imgs',
            description="Move bad images to a trash folder called Poubelle, Def=false",
            value=False,
        ),
        desc.IntParam(
            name='MiniMulti',
            label='Mini Multi',
            description="Minimal Multiplicity of selected points, Def=1",
            value=0,
            range=(-sys.maxsize, sys.maxsize, 1),
        ),
        desc.BoolParam(
            name='NetworkExport',
            label='Network Export',
            description="Export Network (in js), Def=false",
            value=False,
        ),
        desc.IntParam(
            name='DivPH',
            label='Div P H',
            description="in exported network, denominator to decrease the number of tie point which is used for displaying strength of a relation between 2 images, def 10.",
            value=0,
            range=(-sys.maxsize, sys.maxsize, 1),
        ),
        desc.BoolParam(
            name='ExeWrite',
            label='Exe Write',
            description="Do write output homol dir, def=true",
            value=True,
        ),
    ]

    outputs = [
        desc.File(
            name='HomolOut',
            label='Homol Out',
            description="Output Homol directory suffix (default: _mini)",
            value="_mini",
        ),
        desc.File(
            name='PoubelleName',
            label='Poubelle Name',
            description="Output filename with the list of suspicious images, def='Schnaps_poubelle.txt'",
            value="Schnaps_poubelle.txt",
        ),
        desc.File(
            name='OutTrash',
            label='Out Trash',
            description="Output name of trash folder if MoveBadImgs, Def=Poubelle",
            value="Poubelle",
        ),
    ]
