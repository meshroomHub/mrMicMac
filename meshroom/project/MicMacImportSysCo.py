__version__ = "1.2.0"

import os
from meshroom.core import desc
from .MicMacImportFile import MicMacImportFile

def changeSystem(node):
    '''
    Coordinate system change towards the copied file: Source@File, or the file alone for 'InFile'
    '''
    filename = node.Out.value.replace('"', '') or os.path.basename(node.inputFile.value.replace('"', ''))
    if node.sourceType.value == 'InFile':
        return filename
    if node.sourceType.value == 'File':
        return node.sourceFile.value.replace('"', '') + '@' + filename
    return node.source.value + '@' + filename

class MicMacImportSysCo(MicMacImportFile):
    documentation = 'MicMacImportSysCo: Copy a coordinate system file into the MicMac project directory and build the coordinate system change (ChSys, ChgSyst) towards it.'

    inputs = [
        desc.File(
            name='projectDirectory',
            label='Project Directory',
            description='Project Directory.',
            value="",
        ),
        desc.File(
            name='inputFile',
            label='In File',
            description='Coordinate system file (SystemeCoord, or ChangementCoordonnees with Source System Type "InFile") to copy into the project directory.',
            value="",
        ),
        desc.StringParam(
            name='Out',
            label='Output Filename',
            description="Name of the file in the project directory (Def=name of the input file).",
            value="",
        ),
        desc.ChoiceParam(
            name='sourceType',
            label='Source System Type',
            description="Source system of the change: a predefined MicMac system ('Source System'), another coordinate system file ('Source System File'), or 'InFile' when the imported file is a whole ChangementCoordonnees (source and target).",
            value='Predefined',
            values=['Predefined', 'File', 'InFile'],
            exclusive=True,
        ),
        desc.ChoiceParam(
            name='source',
            label='Source System',
            description="Predefined MicMac system: DegreeWGS84 (WGS84 in degrees), WGS84 (WGS84 in radians), GeoC (geocentric), Lambert93.",
            value='DegreeWGS84',
            values=['DegreeWGS84', 'WGS84', 'GeoC', 'Lambert93'],
            exclusive=True,
            enabled=lambda node: node.sourceType.value == 'Predefined',
        ),
        desc.File(
            name='sourceFile',
            label='Source System File',
            description="Source coordinate system file, relative to the project directory (e.g. the local tangent system for a map projection).",
            value="",
            enabled=lambda node: node.sourceType.value == 'File',
        ),
        desc.ChoiceParam(
            name='verboseLevel',
            label='Verbose Level',
            description='Verbosity level (fatal, error, warning, info, debug, trace).',
            value='info',
            values=['fatal', 'error', 'warning', 'info', 'debug', 'trace'],
            exclusive=True,
            invalidate=False,
        ),
    ]

    outputs = [
        desc.File(
            name='filename',
            label='Filename',
            description="Name of the copied file, relative to the project directory.",
            value=lambda node: node.Out.value.replace('"', '') or os.path.basename(node.inputFile.value.replace('"', '')),
        ),
        desc.File(
            name='changeSystem',
            label='Change System',
            description="Coordinate system change towards the copied file (Source@File, or the file alone for 'InFile'), for OriConvert / GCPConvert 'ChSys' and ChgSysCo.",
            value=changeSystem,
        ),
    ]

    def run(self, chunk, projectDir):
        if chunk.node.sourceType.value == 'File' and not chunk.node.sourceFile.value.replace('"', ''):
            raise RuntimeError('"Source System File" is not set.')
        super().run(chunk, projectDir)
