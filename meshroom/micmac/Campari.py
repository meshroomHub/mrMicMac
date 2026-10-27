__version__ = "1.2.0"

import sys
from meshroom.core import desc
from ..common import node

class Campari(node.MicmacNode, desc.CommandLineNode):
    commandLine = 'mm3d Campari {imagePatternValue} {inputOrientationValue} {OutValue} {allParams}'
    documentation = 'Campari: Interface to Apero for bundle adjustment with heterogeneous measures (tie points, GCP, GPS).'

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
            label='In Orientation Directory',
            description="Input Orientation.",
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
            name='setEmGPS',
            label='Set Em GPS',
            description="Set EmGPS.",
            value=False,
            commandLineGroup='', # enable 'EmGPS' attribute
        ),
        desc.GroupAttribute(
            name='EmGPS',
            label='Em GPS',
            description="Embedded GPS: orientation directory of the camera centers and their uncertainty ([Dir,Sigma]).",
            brackets='[]',
            joinChar=',',
            enabled=lambda node: node.setEmGPS.value,
            items=[
                desc.File(
                    name="orientation",
                    label="GPS Orientation Directory",
                    description="Orientation directory of the GPS camera centers (e.g. output of OriConvert).",
                    value="",
                ),
                desc.FloatParam(
                    name="sigma",
                    label="Sigma",
                    description="GPS uncertainty (in meters).",
                    value=5.0,
                    range=(0.0, 100.0, 0.01),
                ),
            ]
        ),
        desc.BoolParam(
            name='enableGpsLa',
            label='Enable GpsLa',
            description="Enable GpsLa.",
            value=False,
            commandLineGroup='', # enable 'GpsLa', 'IncLA' attributes
        ),
        desc.BoolParam(
            name='setGCP',
            label='Set GCP',
            description="Set GCP.",
            value=False,
            commandLineGroup='', # enable 'GCP' attribute
        ),
        desc.GroupAttribute(
            name='GCP',
            label='GCP',
            description="Ground control points ([GrMes.xml,GrUncertainty,ImMes.xml,ImUnc]).",
            brackets='[]',
            joinChar=',',
            enabled=lambda node: node.setGCP.value,
            items=[
                desc.File(
                    name="gcpFile",
                    label="GCP File",
                    description="Ground coordinates of the GCPs (e.g. output of GCPConvert).",
                    value="",
                ),
                desc.FloatParam(
                    name="gcpUncertainty",
                    label="GCP Uncertainty",
                    description="Uncertainty of the ground coordinates (in meters).",
                    value=0.01,
                    range=(0.0, 100.0, 0.001),
                ),
                desc.File(
                    name="imageMeasurementsFile",
                    label="Image Measurements File",
                    description="Image measurements of the GCPs (e.g. Mesure-S2D.xml).",
                    value="",
                ),
                desc.FloatParam(
                    name="imageUncertainty",
                    label="Image Uncertainty",
                    description="Uncertainty of the image measurements (in pixels).",
                    value=1.0,
                    range=(0.0, 100.0, 0.01),
                ),
            ]
        ),
        desc.GroupAttribute(
            name='GpsLa',
            label='Gps La',
            description="Gps Lever Arm, in combination with EmGPS.",
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
            ]
        ),
        desc.GroupAttribute(
            name='IncLA',
            label='Inc LA',
            description="Inc on initial value of LA (Def not used).",
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
            ]
        ),
        desc.StringParam(
            name='PatGPS',
            label='Pat GPS',
            description="When EmGPS, filter images where GPS is used.",
            value="",
        ),
        desc.FloatParam(
            name='SigmaTieP',
            label='Sigma Tie P',
            description="Sigma use for TieP weighting (Def=1).",
            value=1.0,
            range=(-float('inf'), float('inf'), 0.01),
        ),
        desc.FloatParam(
            name='FactElimTieP',
            label='Fact Elim Tie P',
            description="Fact elimination of tie point (prop to SigmaTieP, Def=5).",
            value=5.0,
            range=(-float('inf'), float('inf'), 0.01),
        ),
        desc.BoolParam(
            name='CPI1',
            label='CPI1',
            description="Calib Per Im, Firt time.",
            value=False,
        ),
        desc.BoolParam(
            name='CPI2',
            label='CPI2',
            description="Calib Per Im, After first time, reUsing Calib Per Im As input.",
            value=False,
        ),
        desc.BoolParam(
            name='AllFree',
            label='All Free',
            description="Refine all calibration parameters (Def=false).",
            value=False,
        ),
        desc.StringParam(
            name='AllFreePat',
            label='All Free Pat',
            description="Pattern of images that will be subject to AllFree (Def=.*).",
            value="",
        ),
        desc.StringParam(
            name='GradualRefineCal',
            label='Gradual Refine Cal',
            description="Calibration model to refine gradually.",
            value="",
        ),
        desc.BoolParam(
            name='DetGCP',
            label='Det GCP',
            description="Detail on GCP (Def=false).",
            value=False,
        ),
        desc.FloatParam(
            name='Visc',
            label='Visc',
            description="Viscosity on external orientation in Levenberg-Marquardt like resolution (Def=1.0).",
            value=1.0,
            range=(-float('inf'), float('inf'), 0.01),
        ),
        desc.BoolParam(
            name='setAddViscInterne',
            label='Set Add Visc Interne',
            description="Set AddViscInterne.",
            value=False,
            commandLineGroup='', # enable 'AddViscInterne' attribute
        ),
        desc.BoolParam(
            name='AddViscInterne',
            label='Add Visc Interne',
            description="Add Viscosity on calibration parameter (Def=false, exept for GradualRefineCal).",
            value=False,
            enabled=lambda node: node.setAddViscInterne.value,
        ),
        desc.FloatParam(
            name='ViscInterne',
            label='Visc Interne',
            description="Viscosity on calibration parameter (Def=0.1), use it with AddViscInterne=true.",
            value=0.1,
            range=(-float('inf'), float('inf'), 0.01),
        ),
        desc.BoolParam(
            name='ExpTxt',
            label='Export In Txt',
            description="Export in text format (Def=false).",
            value=False,
        ),
        desc.BoolParam(
            name='PoseFigee',
            label='Pose Figee',
            description="Does the external orientation of the cameras are frozen or free (Def=false, i.e. camera poses are free).",
            value=False,
        ),
        desc.StringParam(
            name='FrozenPoses',
            label='Frozen Poses',
            description="List of frozen poses (pattern).",
            value="",
        ),
        desc.StringParam(
            name='FrozenCenters',
            label='Frozen Centers',
            description="List of frozen poses (pattern).",
            value="",
        ),
        desc.StringParam(
            name='FrozenOrients',
            label='Frozen Orients',
            description="List of frozen poses (pattern).",
            value="",
        ),
        desc.BoolParam(
            name='AcceptGB',
            label='Accept GB',
            description="Accepte new Generik Bundle image, Def=true, set false for perfect backward compatibility.",
            value=True,
        ),
        desc.StringParam(
            name='NameRTA',
            label='Name RTA',
            description="Name for save results of Rolling Test Appuis , Def=SauvRTA.xml.",
            value="",
        ),
        desc.IntParam(
            name='NbIterEnd',
            label='Nb Iter End',
            description="Number of iteration at end, Def = 4.",
            value=4,
            range=(-sys.maxsize, sys.maxsize, 1),
        ),
        desc.BoolParam(
            name='setFocFree',
            label='Set Foc Free',
            description="Set FocFree.",
            value=False,
            commandLineGroup='', # enable 'FocFree' attribute
        ),
        desc.BoolParam(
            name='FocFree',
            label='Foc Free',
            description="Foc Free (Def=true).",
            value=True,
            enabled=lambda node: node.setFocFree.value,
        ),
        desc.BoolParam(
            name='setPPFree',
            label='Set PP Free',
            description="Set PPFree.",
            value=False,
            commandLineGroup='', # enable 'PPFree' attribute
        ),
        desc.BoolParam(
            name='PPFree',
            label='PP Free',
            description="Principal Point Free (Def=true).",
            value=True,
            enabled=lambda node: node.setPPFree.value,
        ),
        desc.BoolParam(
            name='setAffineFree',
            label='Set Affine Free',
            description="Set AffineFree.",
            value=False,
            commandLineGroup='', # enable 'AffineFree' attribute
        ),
        desc.BoolParam(
            name='AffineFree',
            label='Affine Free',
            description="Affine Parameter (Def=true).",
            value=True,
            enabled=lambda node: node.setAffineFree.value,
        ),
        desc.BoolParam(
            name='setDegAdd',
            label='Set Deg Add',
            description="Set DegAdd.",
            value=False,
            commandLineGroup='', # enable 'DegAdd' attribute
        ),
        desc.IntParam(
            name='DegAdd',
            label='Deg Add',
            description="When specified, degree of additionnal parameter.",
            value=0,
            range=(0, 20, 1),
            enabled=lambda node: node.setDegAdd.value,
        ),
        desc.BoolParam(
            name='setDegFree',
            label='Set Deg Free',
            description="Set DegFree.",
            value=False,
            commandLineGroup='', # enable 'DegFree' attribute
        ),
        desc.IntParam(
            name='DegFree',
            label='Deg Free',
            description="When specified degree of freedom of parameters generiqs.",
            value=0,
            range=(0, 20, 1),
            enabled=lambda node: node.setDegFree.value,
        ),
        desc.BoolParam(
            name='setDRMax',
            label='Set DR Max',
            description="Set DRMax.",
            value=False,
            commandLineGroup='', # enable 'DRMax' attribute
        ),
        desc.IntParam(
            name='DRMax',
            label='DR Max',
            description="When specified degree of freedom of radial parameters.",
            value=0,
            range=(0, 20, 1),
            enabled=lambda node: node.setDRMax.value,
        ),
        desc.BoolParam(
            name='setLibCP',
            label='Set Lib CP',
            description="Set LibCP.",
            value=False,
            commandLineGroup='', # enable 'LibCP' attribute
        ),
        desc.BoolParam(
            name='LibCP',
            label='Lib CP',
            description="Free distorsion center, Def context dependant.",
            value=False,
            enabled=lambda node: node.setLibCP.value,
        ),
        desc.BoolParam(
            name='setLibCD',
            label='Set Lib CD',
            description="Set LibCD.",
            value=False,
            commandLineGroup='', # enable 'LibCD' attribute
        ),
        desc.BoolParam(
            name='LibCD',
            label='Lib CD',
            description="Free distorsion center, Def context dependant. Principal Point should be also free if CD is free.",
            value=False,
            enabled=lambda node: node.setLibCD.value,
        ),
        desc.BoolParam(
            name='setLibDec',
            label='Set Lib Dec',
            description="Set LibDec.",
            value=False,
            commandLineGroup='', # enable 'LibDec' attribute
        ),
        desc.BoolParam(
            name='LibDec',
            label='Lib Dec',
            description="Free decentric parameter, Def context dependant.",
            value=False,
            enabled=lambda node: node.setLibDec.value,
        ),
        desc.BoolParam(
            name='setSElimB',
            label='Set S Elim B',
            description="Set SElimB.",
            value=False,
            commandLineGroup='', # enable 'SElimB' attribute
        ),
        desc.IntParam(
            name='SElimB',
            label='S Elim B',
            description="Print stat on reason for bundle elimination (0,1,2).",
            value=0,
            range=(0, 2, 1),
            enabled=lambda node: node.setSElimB.value,
        ),
        desc.BoolParam(
            name='ExpMatMark',
            label='Exp Mat Mark',
            description="Export Cov Matrix to Matrix Market Format+Eigen/cmp.",
            value=False,
        ),
        desc.StringParam(
            name='SauvAutom',
            label='Sauv Autom',
            description="Save intermediary results to, Set NONE if dont want any.",
            value="",
        ),
        desc.BoolParam(
            name='setRatioMaxDistCS',
            label='Set Ratio Max Dist CS',
            description="Set RatioMaxDistCS.",
            value=False,
            commandLineGroup='', # enable 'RatioMaxDistCS' attribute
        ),
        desc.FloatParam(
            name='RatioMaxDistCS',
            label='Ratio Max Dist CS',
            description="Ratio max of distance P-Center.",
            value=0.0,
            range=(0.0, 100000.0, 0.01),
            enabled=lambda node: node.setRatioMaxDistCS.value,
        ),
        desc.BoolParam(
            name='setNbLiais',
            label='Set Nb Liais',
            description="Set NbLiais.",
            value=False,
            commandLineGroup='', # enable 'NbLiais' attribute
        ),
        desc.IntParam(
            name='NbLiais',
            label='Nb Liais',
            description="Param for relative weighting for tie points.",
            value=100,
            range=(0, 100000, 1),
            enabled=lambda node: node.setNbLiais.value,
        ),
        desc.FloatParam(
            name='PdsGBRot',
            label='Pds GB Rot',
            description="Weighting of the global rotation constraint (Generic bundle Def=0.002).",
            value=0.002,
            range=(0.0, 1.0, 0.001),
        ),
        desc.FloatParam(
            name='PdsGBId',
            label='Pds GB Id',
            description="Weighting of the global deformation constraint (Generic bundle Def=0.0).",
            value=0.0,
            range=(-float('inf'), float('inf'), 0.01),
        ),
        desc.BoolParam(
            name='setPdsGBIter',
            label='Set Pds GB Iter',
            description="Set PdsGBIter.",
            value=False,
            commandLineGroup='', # enable 'PdsGBIter' attribute
        ),
        desc.FloatParam(
            name='PdsGBIter',
            label='Pds GB Iter',
            description="Weighting of the change of the global rotation constraint between iterations (Generic bundle Def=1e-6).",
            value=0.000001,
            range=(0.0, 1.0, 0.000001),
            enabled=lambda node: node.setPdsGBIter.value,
        ),
        desc.BoolParam(
            name='ExportSensib',
            label='Export Sensib',
            description="Export sensiblity (accuracy) estimator : correlation , variance, inverse matrix variance ...",
            value=False,
        ),
        desc.BoolParam(
            name='setUseGaussJ',
            label='Set Use Gauss J',
            description="Set UseGaussJ.",
            value=False,
            commandLineGroup='', # enable 'UseGaussJ' attribute
        ),
        desc.BoolParam(
            name='UseGaussJ',
            label='Use Gauss J',
            description="Use GaussJ instead of Cholesky (Def depend of others).",
            value=False,
            enabled=lambda node: node.setUseGaussJ.value,
        ),
        desc.IntParam(
            name='NormEq',
            label='Norm Eq',
            description="Flag for Norm Eq, 1->Sc, 2-Tr, Def=3 (All), tuning purpose.",
            value=3,
            range=(-sys.maxsize, sys.maxsize, 1),
        ),
        desc.StringParam(
            name='StrDebugVTP',
            label='Str Debug VTP',
            description="String of debug for tie points.",
            value="",
        ),
        desc.BoolParam(
            name='setNAWNF',
            label='Set NAWNF',
            description="Set NAWNF.",
            value=False,
            commandLineGroup='', # enable 'NAWNF' attribute
        ),
        desc.IntParam(
            name='NAWNF',
            label='NAWNF',
            description="Num Attribute for Weigthing in New Format.",
            value=0,
            range=(0, 100, 1),
            enabled=lambda node: node.setNAWNF.value,
        ),
        desc.BoolParam(
            name='setWOP',
            label='Set WOP',
            description="Set WOP.",
            value=False,
            commandLineGroup='', # enable 'WOP' attribute
        ),
        desc.FloatParam(
            name='WOP',
            label='WOP',
            description="Weight of plane observation on centers.",
            value=0.0,
            range=(0.0, 100000.0, 0.01),
            enabled=lambda node: node.setWOP.value,
        ),
        desc.BoolParam(
            name='setExtIntZ',
            label='Set Ext Int Z',
            description="Set ExtIntZ.",
            value=False,
            commandLineGroup='', # enable 'ExtIntZ' attribute
        ),
        desc.FloatParam(
            name='ExtIntZ',
            label='Ext Int Z',
            description="Extension of Z Interval for elimination.",
            value=0.0,
            range=(0.0, 100000.0, 0.01),
            enabled=lambda node: node.setExtIntZ.value,
        ),
    ]

    outputs = [
        desc.File(
            name='Out',
            label='Orientation Directory',
            description="Output Orientation.",
            commandLineGroup='', # unnamed parameter
            value="Campari",
        ),
    ]
