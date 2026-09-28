__version__ = "0.0"

import sys
from meshroom.core import desc
from ..common import node

class OriConvV1V2(node.MicmacNode, desc.CommandLineNode):
    commandLine = 'MMVII OriConvV1V2 Ori-{InValue}/ {OriValue}'
    documentation = 'OriConvV1V2'
    category = 'MicMacV2'

    inputs = [
        desc.File(
            name='projectDirectory',
            label='Project Directory',
            description='Project Directory.',
            value="",
            commandLineGroup="micmac",
            invalidate=True,
        ),
        desc.File(
            name='In',
            label='Orientation MicMac V1',
            description="Input Orientation for MMV1 Files",
            invalidate=True,
        commandLineGroup='unnamedParams',
            value="",
        ),
        
    ]

    outputs = [
    	desc.File(
            name='Ori',
            label='Orientation MMVII',
            description="Out Orientation for MMVII Files",
            invalidate=True,
        commandLineGroup='unnamedParams',
            value="OriV2",
        ),
    ]
