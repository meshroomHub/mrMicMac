__version__ = "1.2.0"

import os
import shutil
import json
from meshroom.core import desc
from ..common import node

class MicMacProject(node.MicmacPythonNode, desc.Node):
    documentation = 'MicMacProject: Copy the SfMData (CameraInit) images into a MicMac project directory.'

    inputs = [
        desc.File(
            name='input',
            label='SfMData',
            description='SfMData file.',
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
            name='projectDirectory',
            label='Project Directory',
            description='Project Directory.',
            commandLineGroup='',  # required to execute mm3d command line
            value='{nodeCacheFolder}/project',
        ),
    ]

    def run(self, chunk, projectDir):
        chunk.logger.info("Copy images from input SfMData file")

        with open(chunk.node.input.value, 'r', encoding='utf-8', errors='ignore') as f:
            data = json.load(f)

        views = [{k: v for k, v in item.items()} for item in data.get("views", [])]
        for view in views:
            inputPath = view['path']
            outputPath = os.path.normpath(os.path.join(projectDir, os.path.basename(inputPath))).replace('\\', '/')
            chunk.logger.debug('Copy of image: ' + inputPath)
            shutil.copy2(inputPath, outputPath)

        chunk.logger.info('Images have been copied in directory: ' + projectDir)
