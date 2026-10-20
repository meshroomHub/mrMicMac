__version__ = "1.2.0"

from meshroom.core import desc
from ..common import node

class SaisieBascQT(node.MicmacSaisieNode, desc.CommandLineNode):
    commandLine = 'mm3d SaisieBascQT {imagePatternValue} {orientationInValue} {imageMeasurementsFileValue} {allParams}'
    documentation = 'SaisieBascQT: Interactive tool to capture the image measurements (origin, axis, scale) used by SBGlobBascule or RepLocBascule.'

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
            name='orientationIn',
            label='Orientation Directory',
            description="Input Orientation (NONE if unused).",
            commandLineGroup='', # unnamed parameter
            value="",
        ),
        desc.StringParam(
            name='imageMeasurementsFile',
            label='Image Measurements File',
            description="Image measurements file.",
            commandLineGroup='', # unnamed parameter
            value="MesureBasc.xml",
        ),
        desc.GroupAttribute(
            name='SzW',
            label='Window Size',
            description='Total size of the window.',
            brackets='[]',
            joinChar=',',
            items=[
                desc.IntParam(
                    name='SzW1',
                    label='SzW1',
                    description='Size of the window 1.',
                    value=800,
                    range=(100, 2000, 100),
                ),
                desc.IntParam(
                    name='SzW2',
                    label='SzW2',
                    description='Size of the window 2.',
                    value=800,
                    range=(100, 2000, 100),
                ),
            ],
        ),
        desc.BoolParam(
            name='setNbF',
            label='Set Number Of Subwindows',
            description='Set NbF (Def depends on the number of images).',
            value=False,
            commandLineGroup='', # enable 'NbF' attribute
        ),
        desc.GroupAttribute(
            name='NbF',
            label='Number Of Subwindows',
            description='Number of Subwindows.',
            brackets='[]',
            joinChar=',',
            enabled=lambda node: node.setNbF.value,
            items=[
                desc.IntParam(
                    name='NbF1',
                    label='NbF1',
                    description='Number of Subwindows 1.',
                    value=2,
                    range=(1, 5, 1),
                ),
                desc.IntParam(
                    name='NbF2',
                    label='NbF2',
                    description='Number of Subwindows 2.',
                    value=2,
                    range=(1, 5, 1),
                ),
            ],
        ),
        desc.BoolParam(
            name='ForceGray',
            label='Force Gray Image',
            description='Force gray image.',
            value=True,
            advanced=True,
        ),
        desc.BoolParam(
            name='setGama',
            label='Set Gamma',
            description='Set Gama.',
            value=False,
            advanced=True,
            commandLineGroup='', # enable 'Gama' attribute
        ),
        desc.FloatParam(
            name='Gama',
            label='Gamma',
            description='Apply gamma to image.',
            enabled=lambda node: node.setGama.value,
            value=1.0,
            range=(0.0, 4.0, 0.01),
            advanced=True,
        ),
    ]

    outputs = [
        desc.File(
            name='imageMeasurements2D',
            label='Image Measurements 2D',
            description="Image Measurements 2D file (input of SBGlobBascule / RepLocBascule).",
            value=lambda node: node.imageMeasurementsFile.value.replace('"', '').rsplit(".", 1)[0]+"-S2D.xml",
            commandLineGroup='', # not a command line parameter
        ),
    ]
