__version__ = "1.2.0"

import os
import shutil
from meshroom.core import desc
from ..common import node

class MicMacImportFile(node.MicmacPythonNode, desc.Node):
    documentation = 'MicMacImportFile: Copy an external file (GPS, GCP, coordinate system...) into the MicMac project directory.'

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
            description='File to copy into the project directory.',
            value="",
        ),
        desc.StringParam(
            name='Out',
            label='Output Filename',
            description="Name of the file in the project directory (Def=name of the input file).",
            value="",
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
            name='filePath',
            label='File',
            description="Copied file (absolute path).",
            value=lambda node: os.path.join(node.projectDirectory.value.replace('"', ''), node.Out.value.replace('"', '') or os.path.basename(node.inputFile.value.replace('"', ''))).replace('\\', '/'),
        ),
    ]

    def run(self, chunk, projectDir):
        inputFile = chunk.node.inputFile.value.replace('"', '')
        if not inputFile:
            raise RuntimeError('"In File" is not set.')
        if not os.path.isfile(inputFile):
            raise RuntimeError('"In File" does not exist: ' + inputFile)

        outputFile = os.path.join(projectDir, chunk.node.filename.value.replace('"', '')).replace('\\', '/')
        chunk.logger.info('Copy ' + inputFile + ' to ' + outputFile)
        try:
            shutil.copy2(inputFile, outputFile)
        except shutil.SameFileError:
            chunk.logger.info('The file is already in the project directory.')
