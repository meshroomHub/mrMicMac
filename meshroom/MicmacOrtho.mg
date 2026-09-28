{
    "header": {
        "pipelineVersion": "2.2",
        "releaseVersion": "2023.3.0-develop",
        "fileVersion": "1.1",
        "template": true,
        "nodesVersions": {
            "C3DC": "1.1.1",
            "SaisieMasqQT": "1.1.1",
            "TapiocaMulScale": "1.1.1",
            "AperiCloud": "1.1.1",
            "RepLocBascule": "0.0",
            "MicMacProject": "1.0",
            "CameraInit": "9.0",
            "Pims2Mnt": "1.1.1",
            "Tapas": "1.1.1",
            "Tawny": "1.1.1"
        }
    },
    "graph": {
        "CameraInit_1": {
            "nodeType": "CameraInit",
            "position": [
                0,
                0
            ],
            "inputs": {}
        },
        "MicMacProject_1": {
            "nodeType": "MicMacProject",
            "position": [
                200,
                0
            ],
            "inputs": {
                "input": "{CameraInit_1.output}"
            }
        },
        "TapiocaMulScale_1": {
            "nodeType": "TapiocaMulScale",
            "position": [
                400,
                0
            ],
            "inputs": {
                "projectDirectory": "{MicMacProject_1.projectDirectory}",
                "imageSizeHighResolution": 1000
            }
        },
        "Tapas_1": {
            "nodeType": "Tapas",
            "position": [
                600,
                0
            ],
            "inputs": {
                "projectDirectory": "{TapiocaMulScale_1.projectDirectory}",
                "imagePattern": "IMGP416[0-5].JPG",
                "calibrationModel": "FraserBasic",
                "SH": "{TapiocaMulScale_1.PostFix}",
                "Out": "Calib"
            },
            "internalInputs": {
                "label": "Tapas Calib"
            }
        },
        "AperiCloud_1": {
            "nodeType": "AperiCloud",
            "position": [
                806,
                187
            ],
            "inputs": {
                "projectDirectory": "{Tapas_1.projectDirectory}",
                "imagePattern": "{Tapas_1.imagePattern}",
                "SH": "{Tapas_1.SH}",
                "orientationDir": "{Tapas_1.orientationDirectory}",
                "RGB": false,
                "Out": "AperiCloud_Calib.ply"
            },
            "internalInputs": {
                "label": "AperiCloud Calib"
            }
        },
        "SaisieMasqQT_1": {
            "nodeType": "SaisieMasqQT",
            "position": [
                1198,
                2
            ],
            "inputs": {
                "projectDirectory": "{AperiCloud_2.projectDirectory}",
                "filePath": "{AperiCloud_2.pointCloud}"
            },
            "internalInputs": {
                "label": "SaisieMasqQT 3D"
            }
        },
        "C3DC_1": {
            "nodeType": "C3DC",
            "position": [
                1394,
                -4
            ],
            "inputs": {
                "projectDirectory": "{SaisieMasqQT_1.projectDirectory}",
                "imagePattern": "{AperiCloud_2.imagePattern}",
                "SH": "{AperiCloud_2.SH}",
                "orientationDir": "{AperiCloud_2.orientationDir}",
                "Masq3D": "AperiCloud_polyg3d.xml"
            }
        },
        "Pims2Mnt_1": {
            "nodeType": "Pims2Mnt",
            "position": [
                1795,
                -5
            ],
            "inputs": {
                "projectDirectory": "{C3DC_1.projectDirectory}",
                "dirOrPIM": "Quickmac",
                "Repere": "{RepLocBascule_1.localFrameOut}",
                "DoOrtho": true
            }
        },
        "RepLocBascule_1": {
            "nodeType": "RepLocBascule",
            "position": [
                1594,
                -6
            ],
            "inputs": {
                "projectDirectory": "{SaisieMasqQT_2.projectDirectory}",
                "imagePattern": "{C3DC_1.imagePattern}",
                "orientationDir": "{AperiCloud_2.orientationDir}",
                "imageMeasures": "HOR"
            },
            "internalInputs": {
                "comment": "Need to rename HomolMulScale in Homol.\nWaiting for SH option in RepLoc to come in july, then in precomp binaries before november."
            }
        },
        "Tawny_1": {
            "nodeType": "Tawny",
            "position": [
                2006,
                -4
            ],
            "inputs": {
                "projectDirectory": "{Pims2Mnt_1.projectDirectory}",
                "orthoDirectory": "{Pims2Mnt_1.orthoDirectory}",
                "RadiomEgal": false
            }
        },
        "Tapas_2": {
            "nodeType": "Tapas",
            "position": [
                804,
                -5
            ],
            "inputs": {
                "projectDirectory": "{Tapas_1.projectDirectory}",
                "imagePattern": "IMGP41(6[7-9]|[7-8].).JPG",
                "calibrationModel": "Figee",
                "InCal": "{Tapas_1.orientationDirectory}",
                "SH": "{Tapas_1.SH}",
                "Out": "Relative"
            },
            "internalInputs": {
                "label": "Tapas All"
            }
        },
        "AperiCloud_2": {
            "nodeType": "AperiCloud",
            "position": [
                1003,
                2
            ],
            "inputs": {
                "projectDirectory": "{Tapas_2.projectDirectory}",
                "imagePattern": "{Tapas_2.imagePattern}",
                "SH": "{Tapas_2.SH}",
                "orientationDir": "{Tapas_2.orientationDirectory}",
                "RGB": false
            },
            "internalInputs": {
                "label": "AperiCloud All"
            }
        },
        "SaisieMasqQT_2": {
            "nodeType": "SaisieMasqQT",
            "position": [
                1400,
                153
            ],
            "inputs": {
                "projectDirectory": "{SaisieMasqQT_1.projectDirectory}",
                "filePath": "IMGP4176.JPG"
            },
            "internalInputs": {
                "label": "SaisieMasqQT 2D"
            }
        }
    }
}