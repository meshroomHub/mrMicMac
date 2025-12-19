# MeshroomMicMac

![](./assets/banner_meshroomMicmac.jpg)

MeshroomMicMac is a set of [MicMac](https://github.com/micmacIGN/micmac) nodes and pipelines for [Meshroom](https://github.com/alicevision/Meshroom).

## Required

- Install MicMac ([repository](https://github.com/micmacIGN/micmac) or [pre-compiled binaries](https://github.com/micmacIGN/micmac/releases))
- Install Meshroom ([repository](https://github.com/alicevision/Meshroom) or [pre-compiled binaries](https://github.com/alicevision/Meshroom/releases))

*For now, please use MicMac 1.1.1 and Meshroom 2023.3.0.*

*For now, please avoid white spaces and special characters in the MicMac installation path.* 

## How to install 

1) Clone this repository: 
```
git clone https://github.com/alicevision/MeshroomMicMac
```

2) Add MicMac nodes to Meshroom by setting `MESHROOM_NODES_PATH` environment variable:
```
MESHROOM_NODES_PATH = path/to/MeshroomMicMac
```

3) Add MicMac pipelines to Meshroom by setting `MESHROOM_PIPELINE_TEMPLATES_PATH` environment variable:
```
MESHROOM_PIPELINE_TEMPLATES_PATH = path/to/MeshroomMicMac/pipelines
```

You can now find MicMac nodes and pipelines in Meshroom.

