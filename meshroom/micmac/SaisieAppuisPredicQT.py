__version__ = "1.2.0"

from meshroom.core import desc
from ..common import node

class SaisieAppuisPredicQT(node.MicmacNode, desc.CommandLineNode):
    commandLine = 'mm3d SaisieAppuisPredicQT {imagePatternValue} {orientationInValue} {groundControlPointsFileValue} {imageMeasurementsFileValue} {allParams}'
    documentation = 'SaisieAppuisPredicQT: Interactive tool for assisted (predictive) capture of GCP image measurements.'

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
            label='Input Orientation',
            description="Input Orientation.",
            commandLineGroup='', # unnamed parameter
            value="",
        ),
        desc.File(
            name='groundControlPointsFile',
            label='GCP File',
            description="Ground Control Points file.",
            commandLineGroup='', # unnamed parameter
            value="",
        ),
        desc.StringParam(
            name='imageMeasurementsFile',
            label='Image Measurements File',
            description="Image measurements file.",
            invalidate=False,
            commandLineGroup='', # unnamed parameter
            value="Mesure.xml",
        ),
        desc.GroupAttribute(
            name='SzW',
            label='Size of the window',
            description='Size of the window.',
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
        desc.GroupAttribute(
            name='NbF',
            label='Number of Subwindows',
            description='Number of Subwindows.',
            brackets='[]',
            joinChar=',',
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
            name='setWBlur',
            label='Set WBlur',
            description='Set WBlur.',
            value=False,
            advanced=True,
            commandLineGroup='', # enable 'WBlur' attribute
        ),
        desc.FloatParam(
            name='WBlur',
            label='W Blur',
            enabled=lambda node: node.setWBlur.value,
            description='Size in ground geometry of bluring for target.',
            value=0.0,
            range=(0.0, 10.0, 0.1),
            advanced=True,
        ),
        desc.ChoiceParam(
            name='Type',
            label='Type',
            description='Type.',
            value='MaxLoc',
            values=['MaxLoc', 'MinLoc', 'GeoCube'],
            exclusive=True,
            advanced=True,
        ),
        desc.BoolParam(
            name='ForceGray',
            label='Force gray image',
            description='Force gray image.',
            value=True,
            advanced=True,
        ),
        desc.StringParam(
            name='OriMode',
            label='Orientation type',
            description='Orientation type.',
            value='Std',
            advanced=True,
        ),
        desc.BoolParam(
            name='setZMoy',
            label='Set ZMoy',
            description='Set ZMoy.',
            value=False,
            advanced=True,
            commandLineGroup='', # enable 'ZMoy' attribute
        ),
        desc.FloatParam(
            name='ZMoy',
            label='Average Z',
            description='Average Z.',
            value=0.0,
            range=(0.0, 50.0, 10.0),
            enabled=lambda node: node.setZMoy.value,
            advanced=True,
        ),
        desc.BoolParam(
            name='setZInc',
            label='Set ZInc',
            description='Set ZInc.',
            value=False,
            advanced=True,
            commandLineGroup='', # enable 'ZInc' attribute
        ),
        desc.FloatParam(
            name='ZInc',
            label='Incertitude on Z',
            description='Incertitude on Z, Mandatory in PB.',
            value=0.0,
            range=(0.0, 1.0, 0.1),
            advanced=True,
            enabled=lambda node: node.setZInc.value,
        ),
        desc.File(
            name='Masq3D',
            label='3D Masq',
            description='3D Masq used for visibility.',
            value="",
            advanced=True,
        ),
        desc.File(
            name='PIMsF',
            label='PIMs Filter',
            description='PIMs filter used for visibility.',
            value="",
            advanced=True,
        ),
        desc.File(
            name='InputSec',
            label='InputSec',
            description='InputSec.',
            value="",
            advanced=True,
        ),
    ]

    outputs = [
        desc.File(
            name='imageMeasurements2D',
            label='imageMeasurements2D',
            description="Image Measurements 2D file.",
            invalidate=False,
            value=lambda node: node.imageMeasurementsFile.value.split(".")[0].replace('"', '')+"-S2D.xml",
            commandLineGroup='', # not a command line parameter
        ),
        desc.File(
            name='imageMeasurements3D',
            label='imageMeasurements3D',
            description="Image Measurements 3D file.",
            invalidate=False,
            value=lambda node: node.imageMeasurementsFile.value.split(".")[0].replace('"', '')+"-S3D.xml",
            commandLineGroup='', # not a command line parameter
        ),
    ]
