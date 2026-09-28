#!/usr/bin/env python

# MicMac v1.1.1 command-line to Meshroom node
# Custom script written from meshroom_newNodeType

from __future__ import print_function

import argparse
import os
import re
import sys
import shlex
import subprocess
from pprint import pprint

def trim(s):
    """
    All repetition of any kind of space is replaced by a single space
    and remove trailing space at beginning or end.
    """
    # regex to replace all space groups by a single space
    # use split() to remove trailing space at beginning/end
    return re.sub('\s+', ' ', s).strip()


def quotesForStrings(valueStr):
    """
    Return the input string with quotes if it cannot be cast into another builtin type.
    """
    v = valueStr
    try:
        int(valueStr)
    except ValueError:
        try:
            float(valueStr)
        except ValueError:
            if "'" in valueStr:
                v = "'''{}'''".format(valueStr)
            else:
                v = "'{}'".format(valueStr)
    return v

def convertToLabel(name):
    camelCaseToLabel = re.sub('()([A-Z][a-z]*?)', r'\1 \2', name)
    if camelCaseToLabel[0] == ' ': # begin with uppercase
        camelCaseToLabel = camelCaseToLabel[1:]
    snakeToLabel = ' '.join(word.capitalize() for word in camelCaseToLabel.split('_'))
    snakeToLabel = ' '.join(word.capitalize() for word in snakeToLabel.split(' '))
    return snakeToLabel

parser = argparse.ArgumentParser(description='Create a new MicMac Node')
parser.add_argument('--node', metavar='NODE_NAME', type=str,
                    help='New node name')
parser.add_argument('--bin', metavar='CMDLINE', type=str,
                    default=None,
                    help='Input executable')
parser.add_argument('--args', metavar='CMDLINE', type=str,
                    default='',
                    help='Input executable parameters')
parser.add_argument('--output', metavar='DIR', type=str,
                    default=os.path.dirname(__file__),
                    help='Output plugin folder')
parser.add_argument("--force", help="Allows to overwrite the output plugin file.",
                    action="store_true")

args = parser.parse_args()
inputCmdLineDoc = None  
proc = subprocess.Popen(args=shlex.split(args.bin) + [args.args] + ['-help'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
stdout, stderr = proc.communicate()
inputCmdLineDoc = stdout if stdout else stderr

if not inputCmdLineDoc:
    print('No input documentation.')
    print('Usage: YOUR_COMMAND -help | {cmd}'.format(cmd=os.path.splitext(__file__)[0]))
    sys.exit(-1)


args_re = re.compile(
    '^\s+\*\s+'                   # space(s) + '*' + space(s)
    '(\[Name='                    # '[Name='
    '(?P<argName>\w+)'            # argument name
    '\]'                          # ']'
    '\s+)?'                       # space(s)
    '(?P<argType>\w+)'            # argument type 
    '\s+'                         # space(s)
    '::'                          # '::'
    '\s+'                         # space(s)
    '{(?P<argDescription>.*?)?}'  # argument description in {}
    , re.MULTILINE)

cmdLineArgs = args_re.findall(inputCmdLineDoc.decode('utf-8'))

print('='*80)

outputNodeStr = ''
inputNodeStr = ''
nbUnnamedParams = 0

for cmdLineArg in cmdLineArgs:
    argStr = None
    # cmdLineArg[0] is optional
    argName = cmdLineArg[1]
    argType = cmdLineArg[2].lower()
    argDesc = trim(cmdLineArg[3])
    isOutput = False
    isUnnamed = False

    cmdLineArgLower = ' '.join([argName, argDesc]).lower()

    if len(argName) == 0 :
        nbUnnamedParams += 1
        argName = 'unnamed_' + str(nbUnnamedParams)
        isUnnamed = True

    if argType =='string' and ('path' in cmdLineArgLower or 'folder' in cmdLineArgLower or 'file' in cmdLineArgLower or 'directory' in cmdLineArgLower or 'dir' in cmdLineArgLower) :
        argType='file'

    if 'output' in cmdLineArgLower :
        isOutput = True

    print([argName, argType, argDesc])

    paramStr="""
            name='{name}',
            label='{label}',
            description="{description}",
            uid=[0],""".format(name=argName, label=convertToLabel(argName), description=argDesc)
    
    if isUnnamed:
        paramStr += """
            group='', # unnamed parameter"""

    if argType == 'bool':
        argStr="""
        desc.BoolParam({params}
            value=False,
        ),""".format(params=paramStr)
    elif argType == 'file':
        argStr = """
        desc.File({params}
            value="",
        ),""".format(params=paramStr)
    elif argType == 'string':
        argStr = """
        desc.StringParam({params}
            value="",
        ),""".format(params=paramStr)
    elif argType == 'int' or argType == 'size_t':
        argStr = """
        desc.IntParam({params}
            value=0,
            range=(-sys.maxsize, sys.maxsize, 1),
        ),""".format(params=paramStr)
    elif argType == 'real':
        argStr = """
        desc.FloatParam({params}
            value=0.0,
            range=(-float('inf'), float('inf'), 0.01),
        ),""".format(params=paramStr)
    elif argType == 'vector<string>':
        argStr = """
        desc.ListAttribute({params}
            elementDesc=desc.StringParam(
                name="{name}Item",
                label="{label} Item",
                description="{description}",
                value='',
                uid=[0],
            ),
        ),""".format(params=paramStr, name=argName, label=convertToLabel(argName), description=argDesc)
    elif argType == 'vector<double>':
        argStr = """
        desc.ListAttribute({params}
            elementDesc=desc.FloatParam(
                name="{name}Item",
                label="{label} Item",
                description="{description}",
                value=0.0,
                range=(-float('inf'), float('inf'), 0.01),
                uid=[0],
            ),
        ),""".format(params=paramStr, name=argName, label=convertToLabel(argName), description=argDesc)
    elif argType == 'pt2di':
        argStr = """
        desc.GroupAttribute(
            name='{name}',
            label='{label}',
            description="{description}",
            brackets='[]',
            joinChar=',',
            groupDesc=[
            desc.IntParam(
                name="x",
                label="X",
                description="x.",
                value=0,
                range=(-sys.maxsize, sys.maxsize, 1),
                uid=[0],
            ),
            desc.IntParam(
                name="y",
                label="Y",
                description="y.",
                value=0,
                range=(-sys.maxsize, sys.maxsize, 1),
                uid=[0],
            ),
        ]),""".format(name=argName, label=convertToLabel(argName), description=argDesc)
    elif argType == 'pt3di':
        argStr = """
        desc.GroupAttribute(
            name='{name}',
            label='{label}',
            description="{description}",
            brackets='[]',
            joinChar=',',
            groupDesc=[
            desc.IntParam(
                name="x",
                label="X",
                description="x.",
                value=0,
                range=(-sys.maxsize, sys.maxsize, 1),
                uid=[0],
            ),
            desc.IntParam(
                name="y",
                label="Y",
                description="y.",
                value=0,
                range=(-sys.maxsize, sys.maxsize, 1),
                uid=[0],
            ),
            desc.IntParam(
                name="z",
                label="Z",
                description="z.",
                value=0,
                range=(-sys.maxsize, sys.maxsize, 1),
                uid=[0],
            ),
        ]),""".format(name=argName, label=convertToLabel(argName), description=argDesc)
    elif argType == 'pt2dr':
        argStr = """
        desc.GroupAttribute(
            name='{name}',
            label='{label}',
            description="{description}",
            brackets='[]',
            joinChar=',',
            groupDesc=[
            desc.FloatParam(
                name="x",
                label="X",
                description="x.",
                value=0.0,
                range=(-float('inf'), float('inf'), 0.01),
                uid=[0],
            ),
            desc.FloatParam(
                name="y",
                label="Y",
                description="y.",
                value=0.0,
                range=(-float('inf'), float('inf'), 0.01),
                uid=[0],
            ),
        ]),""".format(name=argName, label=convertToLabel(argName), description=argDesc)
    elif argType == 'pt3dr':
        argStr = """
        desc.GroupAttribute(
            name='{name}',
            label='{label}',
            description="{description}",
            brackets='[]',
            joinChar=',',
            groupDesc=[
            desc.FloatParam(
                name="x",
                label="X",
                description="x.",
                value=0.0,
                range=(-float('inf'), float('inf'), 0.01),
                uid=[0],
            ),
            desc.FloatParam(
                name="y",
                label="Y",
                description="y.",
                value=0.0,
                range=(-float('inf'), float('inf'), 0.01),
                uid=[0],
            ),
            desc.FloatParam(
                name="z",
                label="Z",
                description="z.",
                value=0.0,
                range=(-float('inf'), float('inf'), 0.01),
                uid=[0],
            ),
        ]),""".format(name=argName, label=convertToLabel(argName), description=argDesc)
    else:
        print('New MicMac Node Aborted: unknown type (type: ' + argType + ').')
        sys.exit(-1)

    if isOutput:
        outputNodeStr += argStr
    else:
        inputNodeStr += argStr

outputNodeStr = re.sub('(uid=\[0\])', lambda m: 'uid=[]', outputNodeStr) # remove uid for output parameters

fileStr = '''__version__ = "0.0"

import sys
from meshroom.core import desc
from ..common import node

class {nodeName}(node.MicmacNode, desc.CommandLineNode):
    commandLine = '{cmd} {allParams}'
    documentation = '{nodeName}'
    category = 'MicMac'

    inputs = [
        desc.File(
            name='projectDirectory',
            label='Project Directory',
            description='Project Directory.',
            value="",
            group='', # required to execute mm3d command line
            uid=[0],
        ),{inputNodes}
    ]

    outputs = [{outputNodes}
    ]
'''.format(nodeName=args.node, cmd=args.bin + ' ' + args.args, allParams= '{allParams}', inputNodes=inputNodeStr, outputNodes=outputNodeStr)

outputFilepath = os.path.join(args.output, args.node + '.py')

if not args.force and os.path.exists(outputFilepath):
    print('Plugin "{}" already exists "{}".'.format(args.node, outputFilepath))
    sys.exit(-1)

with open(outputFilepath, 'w') as pluginFile:
    pluginFile.write(fileStr)

print('New node exported to: "{}"'.format(outputFilepath))
