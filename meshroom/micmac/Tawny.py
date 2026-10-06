__version__ = "1.2.0"

import sys
from meshroom.core import desc
from ..common import node

class Tawny(node.MicmacNode, desc.CommandLineNode):
    commandLine = 'mm3d Tawny {orthoDirectoryValue} {allParams}'
    documentation = 'Tawny: Interface to Porto to generate an orthophoto mosaic with radiometric equalization.'

    inputs = [
        desc.File(
            name='projectDirectory',
            label='Project Directory',
            description='Project Directory.',
            value="",
            commandLineGroup='', # required to execute mm3d command line
        ),
        desc.File(
            name='orthoDirectory',
            label='Ortho Directory',
            description="Ortho directory.",
            commandLineGroup='', # unnamed parameter
            value="",
        ),
        desc.BoolParam(
            name='RadiomEgal',
            label='Radiom Egal',
            description="Perform or not radiometric egalization.",
            value=True,
        ),
        desc.BoolParam(
            name='setDEq',
            label='Set DEq',
            description="Set DEq.",
            value=False,
            commandLineGroup='', # enable 'DEq' attribute
            advanced=True,
        ),
        desc.IntParam(
            name='DEq',
            label='DEq',
            description="Degree of equalization.",
            enabled=lambda node: node.setDEq.value,
            value=1,
            range=(-sys.maxsize, sys.maxsize, 1),
            advanced=True,
        ),
        desc.BoolParam(
            name='setDEqXY',
            label='Set DEqXY',
            description="Set DEqXY.",
            value=False,
            commandLineGroup='', # enable 'DEqXY' attribute
            advanced=True,
        ),
        desc.GroupAttribute(
            name='DEqXY',
            label='DEqXY',
            description="Degree of equalization, if diff in X and Y.",
            brackets='[]',
            joinChar=',',
            enabled=lambda node: node.setDEqXY.value,
            advanced=True,
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
            ]
        ),
        desc.BoolParam(
            name='setAddCste',
            label='Set Add Cste',
            description="Set add cste.",
            value=False,
            commandLineGroup='', # enable 'AddCste' attribute
            advanced=True,
        ),
        desc.BoolParam(
            name='AddCste',
            label='Add Cste',
            description="Add unknown constant for equalization.",
            enabled=lambda node: node.setAddCste.value,
            value=False,
            advanced=True,
        ),
        desc.BoolParam(
            name='setDegRap',
            label='Set DegRap',
            description="Set DegRap.",
            value=False,
            commandLineGroup='', # enable 'DegRap' attribute
            advanced=True,
        ),
        desc.IntParam(
            name='DegRap',
            label='DegRap',
            description="Degree of rappel to initial values.",
            enabled=lambda node: node.setDegRap.value,
            value=0,
            range=(-sys.maxsize, sys.maxsize, 1),
            advanced=True,
        ),
        desc.BoolParam(
            name='setDegRapXY',
            label='Set DegRapXY',
            description="Set DegRapXY.",
            value=False,
            commandLineGroup='', # enable 'DegRapXY' attribute
            advanced=True,
        ),
        desc.GroupAttribute(
            name='DegRapXY',
            label='DegRapXY',
            description="Degree of rappel to initial values.",
            brackets='[]',
            joinChar=',',
            enabled=lambda node: node.setDegRapXY.value,
            advanced=True,
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
            ]
        ),
        desc.BoolParam(
            name='setRGP',
            label='Set RGP',
            description="Set RGP.",
            value=False,
            commandLineGroup='', # enable 'RGP' attribute
            advanced=True,
        ),
        desc.BoolParam(
            name='RGP',
            label='RGP',
            description="Rappel glob on physically equalized.",
            enabled=lambda node: node.setRGP.value,
            value=True,
            advanced=True,
        ),
        desc.BoolParam(
            name='setDynG',
            label='Set DynG',
            description="Set DynG.",
            value=False,
            commandLineGroup='', # enable 'DynG' attribute
            advanced=True,
        ),
        desc.FloatParam(
            name='DynG',
            label='DynG',
            description="Global Dynamic (to correct saturation problems).",
            enabled=lambda node: node.setDynG.value,
            value=0.0,
            range=(-float('inf'), float('inf'), 0.01),
            advanced=True,
        ),
        desc.BoolParam(
            name='setImPrio',
            label='Set Im Prio',
            description="Set Im Prio.",
            value=False,
            commandLineGroup='', # enable 'ImPrio' attribute
            advanced=True,
        ),
        desc.StringParam(
            name='ImPrio',
            label='Im Prio',
            description="Pattern of image with high prio.",
            enabled=lambda node: node.setImPrio.value,
            value=".*",
            advanced=True,
        ),
        desc.BoolParam(
            name='setSzV',
            label='Set SzV',
            description="Set SzV.",
            value=False,
            commandLineGroup='', # enable 'SzV' attribute
            advanced=True,
        ),
        desc.IntParam(
            name='SzV',
            label='SzV',
            description="Size of Window for equalization (1 means 3x3).",
            enabled=lambda node: node.setSzV.value,
            value=1,
            range=(-sys.maxsize, sys.maxsize, 1),
            advanced=True,
        ),
        desc.BoolParam(
            name='setCorThr',
            label='Set Cor Thr',
            description="Set Cor Thr.",
            value=False,
            commandLineGroup='', # enable 'CorThr' attribute
            advanced=True,
        ),
        desc.FloatParam(
            name='CorThr',
            label='Cor Thr',
            description="Threshold of correlation to validate homologous.",
            enabled=lambda node: node.setCorThr.value,
            value=0.7,
            range=(-float('inf'), float('inf'), 0.01),
            advanced=True,
        ),
        desc.BoolParam(
            name='setNbPerIm',
            label='Set Nb Per Im',
            description="Set Nb Per Im.",
            value=False,
            commandLineGroup='', # enable 'NbPerIm' attribute
            advanced=True,
        ),
        desc.FloatParam(
            name='NbPerIm',
            label='Nb Per Im',
            description="Average number of point per image.",
            enabled=lambda node: node.setNbPerIm.value,
            value=1e4,
            range=(-float('inf'), float('inf'), 0.01),
            advanced=True,
        ),
        desc.BoolParam(
            name='setL1F',
            label='Set L1 F',
            description="Set L1 F.",
            value=False,
            commandLineGroup='', # enable 'L1F' attribute
            advanced=True,
        ),
        desc.BoolParam(
            name='L1F',
            label='L1 F',
            description="Do L1 Filter on couple.",
            enabled=lambda node: node.setL1F.value,
            value=True,
            advanced=True,
        ),
        desc.BoolParam(
            name='setSatThresh',
            label='Set Sat Thresh',
            description="Set Sat Thresh.",
            value=False,
            commandLineGroup='', # enable 'SatThresh' attribute
            advanced=True,
        ),
        desc.FloatParam(
            name='SatThresh',
            label='Sat Thresh',
            description="Threshold determining saturation value (pixel >SatThresh will be ignored).",
            enabled=lambda node: node.setSatThresh.value,
            value=0.0,
            range=(-float('inf'), float('inf'), 0.01),
            advanced=True,
        ),
        desc.StringParam(
            name='Out',
            label='Output Filename',
            description="Name of output file (in the folder).",
            value="Orthophotomosaic.tif",
        ),
    ]

    outputs = [
        desc.File(
            name='outImagePath',
            label='Orthophoto File',
            description="Output orthophoto (absolute path).",
            value='{projectDirectoryValue}/{orthoDirectoryValue}/{OutValue}',
            semantic='image',
            commandLineGroup='', # not a command line parameter
        ),
        desc.File(
            name='outImageFilename',
            label='Orthophoto Filename',
            description="Output orthophoto name, relative to the project directory.",
            value='{orthoDirectoryValue}/{OutValue}',
            commandLineGroup='', # not a command line parameter
        ),
    ]
