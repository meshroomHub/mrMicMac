import re
import psutil
import shlex

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
        cmdline = super().buildCommandLine(chunk)                                             # build node command line
        cmdline = re.sub(r'--(\w+)\s', lambda m: '{name}='.format(name=m.group(1)), cmdline)                 # use "name=value" instead of "--name value"
        cmdline = re.sub(r'(?<==)(True|False)(?=\s|$)', lambda m: str(int(m.group(1) == 'True')), cmdline)   # use 0 / 1 instead of False / True (only as a whole value)
        cmdline = re.sub(r'(\w+=\"\"\s)', lambda m: '', cmdline)                                             # remove value with empty string (optional parameter)
        cmdline = re.sub(r'(\w+=\[\])', lambda m: '', cmdline)                                               # remove value with empty list (optional parameter)
        return cmdline

    def processChunk(self, chunk):
        try:
            with open(chunk.logFile, 'w') as logF:
                cmd = self.buildCommandLine(chunk) + ' @ExitOnBrkp @ExitOnWarn @ExitOnNan' # build command line and add MicMac enter key flags
                projectDir = chunk.node._expVars['projectDirectoryValue'].replace('"','')  # get project directory from parameter (and remove quotes)
                chunk.status.commandLine = cmd
                chunk.saveStatusFile()
                print(' - commandLine: {}'.format(cmd))
                print(' - logFile: {}'.format(chunk.logFile))
                print(' - projectDir: {}'.format(projectDir))
                chunk.subprocess = psutil.Popen(shlex.split(cmd), stdout=logF, stderr=logF, cwd=projectDir) # execute in project directory
                chunk.statThread.proc = chunk.subprocess
                stdout, stderr = chunk.subprocess.communicate()
                chunk.subprocess.wait()

                chunk.status.returnCode = chunk.subprocess.returncode

            if chunk.subprocess.returncode != 0:
                with open(chunk.logFile, 'r') as logF:
                    logContent = ''.join(logF.readlines())
                raise RuntimeError('Error on node "{}":\nLog:\n{}'.format(chunk.name, logContent))
        except:
            raise
        finally:
            chunk.subprocess = None
