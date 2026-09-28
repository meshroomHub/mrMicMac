__version__ = "0.0"

import sys
from meshroom.core import desc
from meshroomMicmac.custom import node

class OriConvV1V2(node.MicmacNode):
    commandLine = 'MMVII OriConvV1V2 Ori-{InValue}/ {OriValue}'
    documentation = 'OriConvV1V2'
    category = 'MicMacV2'

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
            name='In',
            label='Orientation MicMac V1',
            description="Input Orientation for MMV1 Files",
            uid=[0],
        group='unnamedParams',
            value="",
        ),
        
    ]

    outputs = [
    	desc.File(
            name='Ori',
            label='Orientation MMVII',
            description="Out Orientation for MMVII Files",
            uid=[0],
        group='unnamedParams',
            value="OriV2",
        ),
    ]
