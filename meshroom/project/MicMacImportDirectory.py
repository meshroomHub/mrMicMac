__version__ = "1.2.0"

import os
import shutil
from meshroom.core import desc
from ..common import node

class MicMacImportDirectory(node.MicmacPythonNode, desc.Node):
    documentation = 'MicMacImportDirectory: Copy an external directory (e.g. a reference orientation Ori-X) into the MicMac project directory.'

    inputs = [
        desc.File(
            name='projectDirectory',
            label='Project Directory',
            description='Project Directory.',
            value="",
        ),
        desc.File(
            name='inputDirectory',
            label='In Directory',
            description='Directory to copy into the project directory.',
            value="",
        ),
        desc.StringParam(
            name='Out',
            label='Output Directory Name',
            description="Name of the directory in the project directory (Def=name of the input directory).",
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
            name='directoryName',
            label='Directory Name',
            description="Name of the copied directory, relative to the project directory.",
            value=lambda node: node.Out.value.replace('"', '') or os.path.basename(os.path.normpath(node.inputDirectory.value.replace('"', ''))),
        ),
        desc.File(
            name='orientationName',
            label='Orientation Directory',
            description="Orientation name of the copied directory (without the 'Ori-' prefix), to use as calibration or orientation directory.",
            value=lambda node: (node.Out.value.replace('"', '') or os.path.basename(os.path.normpath(node.inputDirectory.value.replace('"', '')))).removeprefix('Ori-'),
        ),
    ]

    def run(self, chunk, projectDir):
        inputDirectory = chunk.node.inputDirectory.value.replace('"', '')
        if not inputDirectory:
            raise RuntimeError('"In Directory" is not set.')
        if not os.path.isdir(inputDirectory):
            raise RuntimeError('"In Directory" does not exist: ' + inputDirectory)

        outputDirectory = os.path.join(projectDir, chunk.node.directoryName.value.replace('"', '')).replace('\\', '/')
        if os.path.normcase(os.path.abspath(inputDirectory)) == os.path.normcase(os.path.abspath(outputDirectory)):
            chunk.logger.info('The directory is already in the project directory.')
            return
        chunk.logger.info('Copy ' + inputDirectory + ' to ' + outputDirectory)
        shutil.copytree(inputDirectory, outputDirectory, dirs_exist_ok=True)
