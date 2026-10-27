import os
import re
import psutil
import shlex
import xml.etree.ElementTree as ET
from meshroom.core import desc

class MicmacNode:
    '''
    Mixin for MicMac nodes, to use with desc.CommandLineNode:
        class MyNode(MicmacNode, desc.CommandLineNode)
    Not a desc.Node itself, so Meshroom does not register it as a node.
    '''
    category = 'MicMac'

    def buildCommandLine(self, chunk):
        '''
        Fix command line for MicMac
        '''
        cmdline = super().buildCommandLine(chunk)                                                            # build node command line
        cmdline = re.sub(r'--(\w+)\s', lambda m: '{name}='.format(name=m.group(1)), cmdline)                 # use "name=value" instead of "--name value"
        cmdline = re.sub(r'(?<==)(True|False)(?=\s|$)', lambda m: str(int(m.group(1) == 'True')), cmdline)   # use 0 / 1 instead of False / True (only as a whole value)
        cmdline = re.sub(r'(\w+=\"\"(?:\s|$))', lambda m: '', cmdline)                                       # remove value with empty string (optional parameter)
        cmdline = re.sub(r'(\w+=\[\])', lambda m: '', cmdline)                                               # remove value with empty list (optional parameter)
        return cmdline

    def buildCommandLines(self, chunk):
        '''
        Command lines to execute for a chunk (one by default, override to run several)
        '''
        return [self.buildCommandLine(chunk)]

    def processChunk(self, chunk):
        try:
            with open(chunk.logFile, 'w') as logF:
                cmds = [cmd + ' @ExitOnBrkp @ExitOnWarn @ExitOnNan' for cmd in self.buildCommandLines(chunk)] # build command lines and add MicMac enter key flags
                projectDir = chunk.node._expVars['projectDirectoryValue'].replace('"','')  # get project directory from parameter (and remove quotes)
                chunk.status.commandLine = '\n'.join(cmds)
                chunk.saveStatusFile()
                print(' - logFile: {}'.format(chunk.logFile))
                print(' - projectDir: {}'.format(projectDir))
                returnCode = 0
                for cmd in cmds:
                    print(' - commandLine: {}'.format(cmd))
                    chunk.subprocess = psutil.Popen(shlex.split(cmd), stdout=logF, stderr=logF, cwd=projectDir) # execute in project directory
                    chunk.statThread.proc = chunk.subprocess
                    stdout, stderr = chunk.subprocess.communicate()
                    chunk.subprocess.wait()

                    returnCode = chunk.subprocess.returncode
                    chunk.status.returnCode = returnCode
                    if returnCode != 0:
                        break # stop at the first failing command

            if returnCode != 0:
                with open(chunk.logFile, 'r') as logF:
                    logContent = ''.join(logF.readlines())
                raise RuntimeError('Error on node "{}":\nLog:\n{}'.format(chunk.name, logContent))
        except:
            raise
        finally:
            chunk.subprocess = None


class MicmacSaisieNode(MicmacNode):
    '''
    Mixin for interactive MicMac nodes (Saisie*), to use with desc.CommandLineNode:
        class MyNode(MicmacSaisieNode, desc.CommandLineNode)
    The user can close the window without saving, so the node is set in error
    if an output file has not been written during the run.
    '''

    def outputsToCheck(self, node):
        '''
        Output attributes that must be written by the run (all File outputs by default)
        '''
        return [attr for attr in node.attributes if attr.isOutput and isinstance(attr.desc, desc.File)]

    @staticmethod
    def hasData(path):
        '''
        True if the XML file contains data (its root element has at least one child)
        '''
        try:
            return len(ET.parse(path).getroot()) > 0
        except ET.ParseError:
            return False

    def processChunk(self, chunk):
        projectDir = chunk.node._expVars['projectDirectoryValue'].replace('"','')  # get project directory from parameter (and remove quotes)
        outputs = [os.path.join(projectDir, attr.value.replace('"','')) for attr in self.outputsToCheck(chunk.node)] # relative to the project directory (unchanged if absolute)
        mtimes = {path: os.path.getmtime(path) if os.path.exists(path) else None for path in outputs} # detect outputs of a previous run
        super().processChunk(chunk)
        notWritten = [path for path in outputs if not os.path.exists(path) or os.path.getmtime(path) == mtimes[path]]
        if notWritten:
            raise RuntimeError('Error on node "{}": output not written (closed without saving?):\n{}'.format(chunk.name, '\n'.join(notWritten)))
        xmlOutputs = [path for path in outputs if path.lower().endswith('.xml')]
        if xmlOutputs and not any(self.hasData(path) for path in xmlOutputs):
            raise RuntimeError('Error on node "{}": output written without data (saved before measuring?):\n{}'.format(chunk.name, '\n'.join(xmlOutputs)))

class MicmacPythonNode:
    '''
    Mixin for MicMac nodes implemented in Python, to use with desc.Node:
        class MyNode(MicmacPythonNode, desc.Node)
    The node defines 'projectDirectory' (input or output) and 'verboseLevel', and implements run(chunk, projectDir).
    Not a desc.Node itself, so Meshroom does not register it as a node.
    '''
    category = 'MicMac'

    def run(self, chunk, projectDir):
        raise NotImplementedError()

    def processChunk(self, chunk):
        try:
            chunk.logManager.start(chunk.node.verboseLevel.value)
            projectDir = chunk.node.projectDirectory.value.replace('"', '')
            if not projectDir:
                raise RuntimeError('"Project Directory" is not set.')
            projectDir = os.path.normpath(projectDir).replace('\\', '/')
            chunk.logger.debug('Project directory: ' + projectDir)
            os.makedirs(projectDir, exist_ok=True)
            self.run(chunk, projectDir)
        finally:
            chunk.logManager.end()
