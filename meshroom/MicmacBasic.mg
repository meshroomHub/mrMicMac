{
    "header": {
        "pipelineVersion": "2.2",
        "releaseVersion": "2023.3.0-develop",
        "fileVersion": "1.1",
        "template": true,
        "nodesVersions": {
            "Tapas": "1.1.1",
            "AperiCloud": "1.1.1",
            "TapiocaMulScale": "1.1.1",
            "MicMacProject": "1.0",
            "CameraInit": "9.0",
            "C3DC": "1.1.1"
        }
    },
    "graph": {
        "CameraInit_1": {
            "nodeType": "CameraInit",
            "position": [
                -6,
                -243
            ],
            "inputs": {}
        },
        "MicMacProject_1": {
            "nodeType": "MicMacProject",
            "position": [
                196,
                -246
            ],
            "inputs": {
                "input": "{CameraInit_1.output}"
            }
        },
        "TapiocaMulScale_1": {
            "nodeType": "TapiocaMulScale",
            "position": [
                409,
                -247
            ],
            "inputs": {
                "projectDirectory": "{MicMacProject_1.projectDirectory}"
            }
        },
        "AperiCloud_1": {
            "nodeType": "AperiCloud",
            "position": [
                902,
                -255
            ],
            "inputs": {
                "projectDirectory": "{Tapas_1.projectDirectory}",
                "imagePattern": "{Tapas_1.imagePattern}",
                "SH": "{Tapas_1.SH}",
                "orientationDir": "{Tapas_1.orientationDirectory}"
            }
        },
        "C3DC_1": {
            "nodeType": "C3DC",
            "position": [
                908,
                -92
            ],
            "inputs": {
                "projectDirectory": "{Tapas_1.projectDirectory}",
                "imagePattern": "{Tapas_1.imagePattern}",
                "SH": "{Tapas_1.SH}",
                "orientationDir": "{Tapas_1.orientationDirectory}",
                "mode": "MicMac"
            }
        },
        "Tapas_1": {
            "nodeType": "Tapas",
            "position": [
                635,
                -251
            ],
            "inputs": {
                "projectDirectory": "{TapiocaMulScale_1.projectDirectory}",
                "imagePattern": "{TapiocaMulScale_1.imagePattern}",
                "calibrationModel": "FraserBasic",
                "SH": "{TapiocaMulScale_1.PostFix}",
                "Out": "Relative"
            }
        }
    }
}