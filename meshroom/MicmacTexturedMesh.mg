{
    "header": {
        "pipelineVersion": "2.2",
        "releaseVersion": "2023.3.0-develop",
        "fileVersion": "1.1",
        "template": true,
        "nodesVersions": {
            "AperiCloud": "1.1.1",
            "TapiocaMulScale": "1.1.1",
            "Tequila": "1.1.1",
            "MicMacProject": "1.0",
            "TiPunch": "1.1.1",
            "C3DC": "1.1.1",
            "CameraInit": "9.0",
            "Tapas": "1.1.1"
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
        "AperiCloud_1": {
            "nodeType": "AperiCloud",
            "position": [
                800,
                0
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
                800,
                160
            ],
            "inputs": {
                "projectDirectory": "{Tapas_1.projectDirectory}",
                "imagePattern": "{Tapas_1.imagePattern}",
                "SH": "{Tapas_1.SH}",
                "orientationDir": "{Tapas_1.orientationDirectory}"
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
                "imagePattern": "{TapiocaMulScale_1.imagePattern}",
                "SH": "{TapiocaMulScale_1.PostFix}",
                "Out": "Relative"
            }
        },
        "TiPunch_1": {
            "nodeType": "TiPunch",
            "position": [
                1000,
                0
            ],
            "inputs": {
                "projectDirectory": "{C3DC_1.projectDirectory}",
                "Pattern": "{C3DC_1.imagePattern}",
                "plyName": "{C3DC_1.pointCloud}",
                "Mode": "{C3DC_1.mode}"
            }
        },
        "Tequila_1": {
            "nodeType": "Tequila",
            "position": [
                1200,
                0
            ],
            "inputs": {
                "projectDirectory": "{TiPunch_1.projectDirectory}",
                "imagePattern": ".*JPG",
                "orientationDir": "{C3DC_1.orientationDir}",
                "plyName": "{TiPunch_1.Out}",
                "Iter": 15,
                "Sz": 4000
            }
        }
    }
}