__version__ = "0.0"

import sys
from meshroom.core import desc
from ..common import node

class Campari(node.MicmacNode, desc.CommandLineNode):
    commandLine = 'mm3d Campari {imagePatternValue} {inputOrientationValue} {OutValue} {allParams}'
    documentation = 'Campari'

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
            name='inputOrientation',
            label='Orientation Directory',
            description="Input Orientation",
            commandLineGroup='', # unnamed parameter
            value="",
        ),
        desc.File(
            name='SH',
            label='Homol Directory',
            description="Homol Directory.",
            value="",
        ),
        desc.BoolParam(
            name='enableGpsLa',
            label='Enable GpsLa',
            description="Enable GpsLa.",
            value=False,
            commandLineGroup='', # enable 'GpsLa', 'IncLA' attributes
        ),
        desc.GroupAttribute(
            name='GCP',
            label='GCP',
            description="Give the start and end image that you want to put in a new folder.",
            brackets='[]',
            joinChar=',',
            items=[
                desc.ListAttribute(
                    name='GCPCtrl',
                    label='GCP Ctrl',
                    description="[GCPTerr.xml,GCPIm.xml,Scale]-> true 3D coordinates+image observations+residual vector scaling factor.",
                    joinChar=',',
                    elementDesc=desc.StringParam(
                        name="GCPCtrlItem",
                        label="GCP Ctrl Item",
                        description="GCP Ctrl item.",
                        value="",
                    ),
            )],
        ),
        desc.GroupAttribute(
            name='GpsLa',
            label='Gps La',
            description="Gps Lever Arm, in combination with EmGPS",
            brackets='[]',
            joinChar=',',
            enabled=lambda node: node.enableGpsLa.value,
            items=[
            desc.FloatParam(
                name="x",
                label="X",
                description="x.",
                value=0.0,
                range=(-float('inf'), float('inf'), 0.01),
            ),
            desc.FloatParam(
                name="y",
                label="Y",
                description="y.",
                value=0.0,
                range=(-float('inf'), float('inf'), 0.01),
            ),
            desc.FloatParam(
                name="z",
                label="Z",
                description="z.",
                value=0.0,
                range=(-float('inf'), float('inf'), 0.01),
            ),
        ]),
        desc.GroupAttribute(
            name='IncLA',
            label='Inc L A',
            description="Inc on initial value of LA (Def not used)",
            brackets='[]',
            joinChar=',',
            enabled=lambda node: node.enableGpsLa.value,
            items=[
            desc.FloatParam(
                name="x",
                label="X",
                description="x.",
                value=0.0,
                range=(-float('inf'), float('inf'), 0.01),
            ),
            desc.FloatParam(
                name="y",
                label="Y",
                description="y.",
                value=0.0,
                range=(-float('inf'), float('inf'), 0.01),
            ),
            desc.FloatParam(
                name="z",
                label="Z",
                description="z.",
                value=0.0,
                range=(-float('inf'), float('inf'), 0.01),
            ),
        ]),
        desc.StringParam(
            name='PatGPS',
            label='Pat G P S',
            description="When EmGPS, filter images where GPS is used",
            value="",
        ),
        desc.FloatParam(
            name='SigmaTieP',
            label='Sigma Tie P',
            description="Sigma use for TieP weighting (Def=1)",
            value=5.0,
            range=(-float('inf'), float('inf'), 0.01),
        ),
        desc.FloatParam(
            name='FactElimTieP',
            label='Fact Elim Tie P',
            description="Fact elimination of tie point (prop to SigmaTieP, Def=5)",
            value=5.0,
            range=(-float('inf'), float('inf'), 0.01),
        ),
        desc.BoolParam(
            name='CPI1',
            label='C P I1',
            description="Calib Per Im, Firt time",
            value=False,
        ),
        desc.BoolParam(
            name='CPI2',
            label='C P I2',
            description="Calib Per Im, After first time, reUsing Calib Per Im As input",
            value=False,
        ),
        desc.BoolParam(
            name='AllFree',
            label='All Free',
            description="Refine all calibration parameters (Def=false)",
            value=False,
        ),
        desc.StringParam(
            name='AllFreePat',
            label='All Free Pat',
            description="Pattern of images that will be subject to AllFree (Def=.*)",
            value="",
        ),
        desc.StringParam(
            name='GradualRefineCal',
            label='Gradual Refine Cal',
            description="Calibration model to refine gradually",
            value="",
        ),
        desc.BoolParam(
            name='DetGCP',
            label='Det G C P',
            description="Detail on GCP (Def=false)",
            value=False,
        ),
        desc.FloatParam(
            name='Visc',
            label='Visc',
            description="Viscosity on external orientation in Levenberg-Marquardt like resolution (Def=1.0)",
            value=1.0,
            range=(-float('inf'), float('inf'), 0.01),
        ),
        desc.BoolParam(
            name='AddViscInterne',
            label='Add Visc Interne',
            description="Add Viscosity on calibration parameter (Def=false, exept for GradualRefineCal)",
            value=False,
        ),
        desc.FloatParam(
            name='ViscInterne',
            label='Visc Interne',
            description="Viscosity on calibration parameter (Def=0.1), use it with AddViscInterne=true",
            value=0.1,
            range=(-float('inf'), float('inf'), 0.01),
        ),
        desc.BoolParam(
            name='ExpTxt',
            label='Exp Txt',
            description="Export in text format (Def=false)",
            value=False,
        ),
        desc.BoolParam(
            name='PoseFigee',
            label='Pose Figee',
            description="Does the external orientation of the cameras are frozen or free (Def=false, i.e. camera poses are free)",
            value=False,
        ),
        desc.StringParam(
            name='FrozenPoses',
            label='Frozen Poses',
            description="List of frozen poses (pattern)",
            value="",
        ),
        desc.StringParam(
            name='FrozenCenters',
            label='Frozen Centers',
            description="List of frozen poses (pattern)",
            value="",
        ),
        desc.StringParam(
            name='FrozenOrients',
            label='Frozen Orients',
            description="List of frozen poses (pattern)",
            value="",
        ),
        desc.BoolParam(
            name='AcceptGB',
            label='Accept G B',
            description="Accepte new Generik Bundle image, Def=true, set false for perfect backward compatibility",
            value=False,
        ),
        desc.StringParam(
            name='NameRTA',
            label='Name R T A',
            description="Name for save results of Rolling Test Appuis , Def=SauvRTA.xml",
            value="",
        ), 
        desc.IntParam(
            name='NbIterEnd',
            label='Nb Iter End',
            description="Number of iteration at end, Def = 4",
            value=4,
            range=(-sys.maxsize, sys.maxsize, 1),
        ),
        desc.BoolParam(
            name='FocFree',
            label='Foc Free',
            description="Foc Free (Def=true)",
            value=False,
        ),
        desc.BoolParam(
            name='PPFree',
            label='P P Free',
            description="Principal Point Free (Def=true)",
            value=False,
        ),
        desc.BoolParam(
            name='AffineFree',
            label='Affine Free',
            description="Affine Parameter (Def=true)",
            value=False,
        ),
        desc.IntParam(
            name='DegAdd',
            label='Deg Add',
            description="When specified, degree of additionnal parameter",
            value=0,
            range=(-sys.maxsize, sys.maxsize, 1),
        ),
        desc.IntParam(
            name='DegFree',
            label='Deg Free',
            description="When specified degree of freedom of parameters generiqs",
            value=0,
            range=(-sys.maxsize, sys.maxsize, 1),
        ),
        desc.IntParam(
            name='DRMax',
            label='D R Max',
            description="When specified degree of freedom of radial parameters",
            value=0,
            range=(-sys.maxsize, sys.maxsize, 1),
        ),
        desc.BoolParam(
            name='LibCP',
            label='Lib C P',
            description="Free distorsion center, Def context dependant",
            value=False,
        ),
        desc.BoolParam(
            name='LibCD',
            label='Lib C D',
            description="Free distorsion center, Def context dependant. Principal Point should be also free if CD is free",
            value=False,
        ),
        desc.BoolParam(
            name='LibDec',
            label='Lib Dec',
            description="Free decentric parameter, Def context dependant",
            value=False,
        ),
        desc.IntParam(
            name='SElimB',
            label='S Elim B',
            description="Print stat on reason for bundle elimination (0,1,2)",
            value=0,
            range=(-sys.maxsize, sys.maxsize, 1),
        ),
        desc.BoolParam(
            name='ExpMatMark',
            label='Exp Mat Mark',
            description="Export Cov Matrix to Matrix Market Format+Eigen/cmp",
            value=False,
        ),
        desc.StringParam(
            name='SauvAutom',
            label='Sauv Autom',
            description="Save intermediary results to, Set NONE if dont want any",
            value="",
        ),
        desc.FloatParam(
            name='RatioMaxDistCS',
            label='Ratio Max Dist C S',
            description="Ratio max of distance P-Center",
            value=0.0,
            range=(-float('inf'), float('inf'), 0.01),
        ),
        desc.IntParam(
            name='NbLiais',
            label='Nb Liais',
            description="Param for relative weighting for tie points",
            value=100,
            range=(-sys.maxsize, sys.maxsize, 1),
        ),
        desc.FloatParam(
            name='PdsGBRot',
            label='Pds G B Rot',
            description="Weighting of the global rotation constraint (Generic bundle Def=0.002)",
            value=0.0,
            range=(-float('inf'), float('inf'), 0.01),
        ),
        desc.FloatParam(
            name='PdsGBId',
            label='Pds G B Id',
            description="Weighting of the global deformation constraint (Generic bundle Def=0.0)",
            value=0.0,
            range=(-float('inf'), float('inf'), 0.01),
        ),
        desc.FloatParam(
            name='PdsGBIter',
            label='Pds G B Iter',
            description="Weighting of the change of the global rotation constraint between iterations (Generic bundle Def=1e-6)",
            value=0.0,
            range=(-float('inf'), float('inf'), 0.01),
        ),
        desc.BoolParam(
            name='ExportSensib',
            label='Export Sensib',
            description="Export sensiblity (accuracy) estimator : correlation , variance, inverse matrix variance ...",
            value=False,
        ),
        desc.BoolParam(
            name='UseGaussJ',
            label='Use Gauss J',
            description="Use GaussJ instead of Cholesky (Def depend of others)",
            value=False,
        ),
        desc.IntParam(
            name='NormEq',
            label='Norm Eq',
            description="Flag for Norm Eq, 1->Sc, 2-Tr, Def=3 (All), tuning purpose",
            value=3,
            range=(-sys.maxsize, sys.maxsize, 1),
        ),
        desc.StringParam(
            name='StrDebugVTP',
            label='Str Debug V T P',
            description="String of debug for tie points",
            value="",
        ),
        desc.IntParam(
            name='NAWNF',
            label='N A W N F',
            description="Num Attribute for Weigthing in New Format",
            value=0,
            range=(-sys.maxsize, sys.maxsize, 1),
        ), 
        desc.FloatParam(
            name='WOP',
            label='W O P',
            description="Weight of plane observation on centers",
            value=0.0,
            range=(-float('inf'), float('inf'), 0.01),
        ),
        desc.FloatParam(
            name='ExtIntZ',
            label='Ext Int Z',
            description="Extension of Z Interval for elimination",
            value=0.0,
            range=(-float('inf'), float('inf'), 0.01),
        ),
    ]

    outputs = [
        desc.File(
            name='Out',
            label='Orientation Directory',
            description="Output Orientation",
            commandLineGroup='', # unnamed parameter
            value="Campari",
        ), 
    ]
