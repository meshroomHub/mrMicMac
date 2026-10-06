__version__ = "1.2.0"

from meshroom.core import desc
from ..common import node

class OriConvert(node.MicmacNode, desc.CommandLineNode):
    commandLine = 'mm3d OriConvert {formatSpecificationValue} {orientationFileValue} {targetedOrientationValue} {allParams}'
    documentation = 'OriConvert: Convert orientations (e.g. embedded GPS) from text files to MicMac XML format.'

    inputs = [
        desc.File(
            name='projectDirectory',
            label='Project Directory',
            description='Project Directory.',
            value='',
            commandLineGroup='', # required to execute mm3d command line
        ),
        desc.ChoiceParam(
            name='formatSpecification',
            label='Format Specification',
            description='Format specification of the orientation file.',
            commandLineGroup='', # unnamed parameter
            value='OriTxtInFile',
            values=['OriTxtAgiSoft', 'OriBluh', 'OriTxtInFile'],
            exclusive=True,
        ),
        desc.File(
            name='orientationFile',
            label='Orientation File',
            description='Image orientation file.',
            value='',
            commandLineGroup='', # unnamed parameter
        ),
        desc.File(
            name='targetedOrientation',
            label='Output Directory Name',
            description='Targeted orientation.',
            value='OriConvert',
            commandLineGroup='', # unnamed parameter
        ),
        desc.File(
            name='ChSys',
            label='Change System File',
            description='Change system file.',
            value='',
        ),
        desc.File(
            name='Calib',
            label='Calib',
            description="External XML calibration file.",
            value='',
            advanced=True,
        ),
        desc.BoolParam(
            name='setAddCalib',
            label='Set Add Calib',
            description="Set Add Calib.",
            value=False,
            commandLineGroup='', # enable 'AddCalib' attribute
            advanced=True,
        ),
        desc.BoolParam(
            name='AddCalib',
            label='Add Calib',
            description="Try to add calibration, def=true.",
            enabled=lambda node: node.setAddCalib.value,
            value=False,
            advanced=True,
        ),
        desc.StringParam(
            name='ConvOri',
            label='Conv Ori',
            description="Orientation convention (like eConvAngPhotoMGrade ...).",
            value='',
            advanced=True,
        ),
        desc.File(
            name='KN2I',
            label='K N2 I',
            description="Key 2 compute Name Image from Id in file.",
            value='',
            advanced=True,
        ),
        desc.BoolParam(
            name='setDN',
            label='Set D N',
            description="Set D N.",
            value=False,
            commandLineGroup='', # enable 'DN' attribute
            advanced=True,
        ),
        desc.FloatParam(
            name='DN',
            label='D N',
            description="Neighbooring distance for Image Graph.",
            enabled=lambda node: node.setDN.value,
            value=0.0,
            range=(-float('inf'), float('inf'), 0.01),
            advanced=True,
        ),
        desc.BoolParam(
            name='MTD1',
            label='MTD1',
            description="Compute Metadata only for first image (tuning).",
            value=True,
        ),
        desc.File(
            name='NameCple',
            label='Couple Image File',
            description='File (usually XML) listing the image pairs.',
            value='',
        ),
        desc.BoolParam(
            name='setCalcV',
            label='Set Compute Speed',
            description="Set Compute Speed.",
            value=False,
            commandLineGroup='', # enable 'CalcV' attribute
        ),
        desc.BoolParam(
            name='CalcV',
            label='Compute Speed',
            description="Compute Speed.",
            enabled=lambda node: node.setCalcV.value,
            value=False,
        ),
        desc.BoolParam(
            name='setRedSizeSC',
            label='Set Red Size S C',
            description="Set Red Size S C.",
            value=False,
            commandLineGroup='', # enable 'RedSizeSC' attribute
            advanced=True,
        ),
        desc.IntParam(
            name='RedSizeSC',
            label='Red Size S C',
            description="Reduced Size of image to use for Tapioca for AltiSol (Def=1000).",
            enabled=lambda node: node.setRedSizeSC.value,
            value=0,
            range=(1, 500, 1),
            advanced=True,
        ),
        desc.StringParam(
            name='Reexp',
            label='Reexp',
            description="Reexport as Matrix (internal set up).",
            value='',
            advanced=True,
        ),
        desc.BoolParam(
            name='setRegul',
            label='Set Regul',
            description="Set Regul.",
            value=False,
            commandLineGroup='', # enable 'Regul' attribute
            advanced=True,
        ),
        desc.FloatParam(
            name='Regul',
            label='Regul',
            description="Regularisation cost (Cost of hole), Def=5.0.",
            enabled=lambda node: node.setRegul.value,
            value=0.0,
            range=(-float('inf'), float('inf'), 0.01),
            advanced=True,
        ),
        desc.BoolParam(
            name='setRegNewBr',
            label='Set RegNewBr',
            description="Set RegNewBr.",
            value=False,
            commandLineGroup='', # enable 'RegNewBr' attribute
            advanced=True,
        ),
        desc.FloatParam(
            name='RegNewBr',
            label='Reg New Br',
            description="cost of creating a new branch (Def=0.4, prop to Regul).",
            enabled=lambda node: node.setRegNewBr.value,
            value=0.0,
            range=(-float('inf'), float('inf'), 0.01),
            advanced=True,
        ),
        desc.BoolParam(
            name='setReliab',
            label='Set Reliab',
            description="Set Reliab.",
            value=False,
            commandLineGroup='', # enable 'Reliab' attribute
            advanced=True,
        ),
        desc.FloatParam(
            name='Reliab',
            label='Reliab',
            description="Threshold for reliable speed, Def=0.75 (prop to Regul).",
            enabled=lambda node: node.setReliab.value,
            value=0.0,
            range=(-float('inf'), float('inf'), 0.01),
            advanced=True,
        ),
        desc.BoolParam(
            name='setDelay',
            label='Set Delay',
            description="Set delay.",
            value=False,
            commandLineGroup='', # enable 'Delay' attribute
            advanced=True,
        ),
        desc.FloatParam(
            name='Delay',
            label='Delay',
            description="Delay.",
            enabled=lambda node: node.setDelay.value,
            value=0.0,
            range=(-float('inf'), float('inf'), 0.01),
            advanced=True,
        ),
        desc.BoolParam(
            name='setTFC',
            label='Set T F C',
            description="Set T F C.",
            value=False,
            commandLineGroup='', # enable 'TFC' attribute
            advanced=True,
        ),
        desc.BoolParam(
            name='TFC',
            label='T F C',
            description="Teta from cap : compute orientation from speed).",
            enabled=lambda node: node.setTFC.value,
            value=False,
            advanced=True,
        ),
        desc.StringParam(
            name='RefOri',
            label='Ref Ori',
            description="Ref Orientation (internal purpose).",
            value='',
            advanced=True,
        ),
        desc.BoolParam(
            name='setSiftR',
            label='Set Sift R',
            description="Set Sift R.",
            value=False,
            commandLineGroup='', # enable 'SiftR' attribute
            advanced=True,
        ),
        desc.IntParam(
            name='SiftR',
            label='Sift R',
            description="Resolution of sift point for Tapioca ,when ImC, (Def No Sift).",
            enabled=lambda node: node.setSiftR.value,
            value=0,
            range=(-1000, 1000, 1),
            advanced=True,
        ),
        desc.BoolParam(
            name='setSiftLR',
            label='Set Sift L R',
            description="Set Sift L R.",
            value=False,
            commandLineGroup='', # enable 'SiftLR' attribute
            advanced=True,
        ),
        desc.IntParam(
            name='SiftLR',
            label='Sift L R',
            description="Low Resolution of sift point for MultisCale ,when ImC (Def no multicale).",
            enabled=lambda node: node.setSiftLR.value,
            value=0,
            range=(-1000, 1000, 1),
            advanced=True,
        ),
        desc.BoolParam(
            name='setDelaunay',
            label='Set Delaunay',
            description="Set Delaunay.",
            value=False,
            commandLineGroup='', # enable 'Delaunay' attribute
            advanced=True,
        ),
        desc.BoolParam(
            name='Delaunay',
            label='Delaunay',
            description="Add delaunay arc when save couple (Def=true).",
            enabled=lambda node: node.setDelaunay.value,
            value=False,
            advanced=True,
        ),
        desc.BoolParam(
            name='setDelaunayCross',
            label='Set DelaunayCross',
            description="Set DelaunayCross.",
            value=False,
            commandLineGroup='', # enable 'DelaunayCross' attribute
            advanced=True,
        ),
        desc.BoolParam(
            name='DelaunayCross',
            label='Delaunay Cross',
            description="Complete delaunay with some crossing trick arc when save couple (Def=true).",
            enabled=lambda node: node.setDelaunayCross.value,
            value=False,
            advanced=True,
        ),
        desc.BoolParam(
            name='setUOC',
            label='Set U O C',
            description="Set U O C.",
            value=False,
            commandLineGroup='', # enable 'UOC' attribute
            advanced=True,
        ),
        desc.BoolParam(
            name='UOC',
            label='U O C',
            description="Use Only Center (tuning).",
            enabled=lambda node: node.setUOC.value,
            value=False,
            advanced=True,
        ),
        desc.File(
            name='ImC',
            label='Image Center',
            description='Image Center for computing AltiSol.',
            value='',
        ),
        desc.BoolParam(
            name='setNbImC',
            label='Set Nb Adjacent Images',
            description="Set Nb Adjacent Images.",
            value=False,
            commandLineGroup='', # enable 'NbImC' attribute
        ),
        desc.IntParam(
            name='NbImC',
            label='Nb Adjacent Images',
            description='Number of neighboors around Image "Center" (Def=50).',
            enabled=lambda node: node.setNbImC.value,
            value=50,
            range=(1, 500, 1),
        ),
        desc.BoolParam(
            name='setLine',
            label='Set Line',
            description="Set Line.",
            value=False,
            commandLineGroup='', # enable 'Line' attribute
            advanced=True,
        ),
        desc.IntParam(
            name='Line',
            label='Line',
            description="Nb neighbour in the same line.",
            enabled=lambda node: node.setLine.value,
            value=0,
            range=(-1000, 1000, 1),
            advanced=True,
        ),
        desc.BoolParam(
            name='setCBF',
            label='Set C B F',
            description="Set C B F.",
            value=False,
            commandLineGroup='', # enable 'CBF' attribute
            advanced=True,
        ),
        desc.BoolParam(
            name='CBF',
            label='C B F',
            description="Export calib as a link to existing file.",
            enabled=lambda node: node.setCBF.value,
            value=False,
            advanced=True,
        ),
        desc.BoolParam(
            name='setAltiSol',
            label='Set Alti Sol',
            description="Set Alti Sol.",
            value=False,
            commandLineGroup='', # enable 'AltiSol' attribute
            advanced=True,
        ),
        desc.FloatParam(
            name='AltiSol',
            label='Alti Sol',
            description="Average altitude of ground.",
            enabled=lambda node: node.setAltiSol.value,
            value=0.0,
            range=(-10000.0, 10000.0, 0.01),
            advanced=True,
        ),
        desc.BoolParam(
            name='setProf',
            label='Set Prof',
            description="Set Prof.",
            value=False,
            commandLineGroup='', # enable 'Prof' attribute
            advanced=True,
        ),
        desc.FloatParam(
            name='Prof',
            label='Prof',
            description="Average Prof of images.",
            enabled=lambda node: node.setProf.value,
            value=0.0,
            range=(-10000.0, 10000.0, 0.01),
            advanced=True,
        ),
        desc.BoolParam(
            name='setOffsetXYZ',
            label='Set Offset X Y Z',
            description="Set Offset X Y Z.",
            value=False,
            commandLineGroup='', # enable 'OffsetXYZ' attribute
        ),
        desc.GroupAttribute(
            name='OffsetXYZ',
            label='Offset X Y Z',
            description="Offset to substract from X,Y,Z (To avoid possible round off error).",
            enabled=lambda node: node.setOffsetXYZ.value,
            brackets='[]',
            joinChar=',',
            items=[
                desc.FloatParam(
                    name="x",
                    label="X",
                    description="x.",
                    value=0.0,
                    range=(-10000.0, 10000.0, 0.01),
                    advanced=True,
                ),
                desc.FloatParam(
                    name="y",
                    label="Y",
                    description="y.",
                    value=0.0,
                    range=(-10000.0, 10000.0, 0.01),
                ),
                desc.FloatParam(
                    name="z",
                    label="Z",
                    description="z.",
                    value=0.0,
                    range=(-10000.0, 10000.0, 0.01),
                ),
            ]
        ),
        desc.StringParam(
            name='CalOFC',
            label='Cal O F C',
            description="When specified compute initial orientation from centers (in Ori-GenFromC) Ori-${CalOFC.",
            value="",
            advanced=True,
        ),
        desc.BoolParam(
            name='setOkNoIm',
            label='Set Ok No Im',
            description="Set Ok No Im.",
            value=False,
            commandLineGroup='', # enable 'OkNoIm' attribute
        ),
        desc.BoolParam(
            name='OkNoIm',
            label='Ok No Im',
            description="Do not create error if image does not exist (def = false).",
            enabled=lambda node: node.setOkNoIm.value,
            value=False,
            advanced=True,
        ),
        desc.File(
            name='FNI',
            label='F N I',
            description="File to Create when non exist.",
            value="",
            advanced=True,
        ),
        desc.BoolParam(
            name='setSzW',
            label='Set Sz W',
            description="Set Sz W.",
            value=False,
            commandLineGroup='', # enable 'SzW' attribute
            advanced=True,
        ),
        desc.FloatParam(
            name='SzW',
            label='Sz W',
            description="Size for visualisation.",
            enabled=lambda node: node.setSzW.value,
            value=0.0,
            range=(-10000.0, 10000.0, 0.01),
            advanced=True,
        ),
        desc.BoolParam(
            name='setUniteAng',
            label='Set Unite Ang',
            description="Set Unite Ang.",
            value=False,
            commandLineGroup='', # enable 'UniteAng' attribute
            advanced=True,
        ),
        desc.StringParam(
            name='UniteAng',
            label='Unite Ang',
            description="in [Degre,Radian,Grade], Def=Degre.",
            enabled=lambda node: node.setUniteAng.value,
            value='',
            advanced=True,
        ),
    ]

    outputs = [
        desc.File(
            name='orientationOut',
            label='Targeted Orientation',
            description='Targeted orientation.',
            value="{targetedOrientationValue}",
            commandLineGroup='', # not a command line parameter
        ),
    ]
