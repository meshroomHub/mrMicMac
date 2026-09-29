# ![mrMicMac - MicMac Nodes for Meshroom](/docs/banner-mrMicMac.png)

mrMicMac is a set of [MicMac](https://github.com/micmacIGN/micmac) nodes and pipelines for [Meshroom](https://github.com/alicevision/Meshroom).

## Required

- Install MicMac ([repository](https://github.com/micmacIGN/micmac) or [pre-compiled binaries](https://github.com/micmacIGN/micmac/releases))
- Install Meshroom ([repository](https://github.com/alicevision/Meshroom) or [pre-compiled binaries](https://github.com/alicevision/Meshroom/releases))

> [!IMPORTANT]
> mrMicMac requires Meshroom 2026+.
>
> Avoid white spaces and special characters in the MicMac installation path.

## How to install 

1) Clone this repository: 
```
git clone https://github.com/meshroomHub/mrMicMac.git
```

2) Add mrMicMac plugin to Meshroom by setting `MESHROOM_PLUGINS_PATH` environment variable:
```
MESHROOM_PLUGINS_PATH = path/to/mrMicMac
```

You can now find MicMac nodes and pipelines in Meshroom.
