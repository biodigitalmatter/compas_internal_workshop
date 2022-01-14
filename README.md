# compas_internal_workshop

## Schedule

<https://github.com/compas-teaching/COMPAS-II-FS2021>

## 09.15-10.00: Why python? Why compas? + setup

[Stack Overflow survey 2021](https://insights.stackoverflow.com/survey/2021#most-popular-technologies-language)

### CAD-programs built using Python

- Blender
- FreeCAD
- KiCAD

### Programs with 1st party support for Python (3)

- Dynamo (Revit)
- Unreal
- Houdini

### Programs with 1st party support for Python (3) for workflow and scripting

- ArchiCAD (JSON-api with bindings, no geo)
- Unity3d

### 3rd party support

- OpenScad

### Bibliotek (med bindings)

- Igl
- wildmeshing
- cgal (with some caveats)
- opencascade,
- threejs
- matplotlib
- processing

### compas

[Slides from COMPAS II, PhD course at ITA, ETH](https://github.com/compas-teaching/COMPAS-II-FS2021)

![compas ecosystem](https://compas.dev/images/COMPAS_ecosystem_update.png)

- Rhino
- Grasshopper
- Blender

### Other parts

[Extensions](https://compas.dev/extensions.html)

- [compas_slicer](https://compas.dev/compas_slicer/latest/)

### Setup

- Rhino3d 7
- Robot Studio
- Anaconda
- [Docker](https://www.docker.com/get-started)
  - [WSL2](https://docs.microsoft.com/en-us/windows/wsl/install)
  - [Kernel update](https://docs.microsoft.com/en-us/windows/wsl/install-manual#step-4---download-the-linux-kernel-update-package)
- [VSCode](https://code.visualstudio.com/docs/?dv=win)
  - [Python extension](vscode:extension/ms-python.python)
  - [Docker extension](vscode:extension/ms-azuretools.vscode-docker)

#### First conda env

#### Install compas

[https://compas.dev/compas/latest/installation.html](Installation docs)

## 10.15-11.00: Hello world in GhPython



## 11.15-12.00: Geometry as objects

- [compas API](https://compas.dev/compas/latest/api.html)
- [RhinoCommon](https://developer.rhino3d.com/api/RhinoCommon/html/R_Project_RhinoCommon.htm)
- [RhinoScriptSyntax](https://developer.rhino3d.com/api/RhinoScriptSyntax/)
- [Blender Python API](https://docs.blender.org/api/current/index.html)
- [FreeCAD](https://wiki.freecadweb.org/Part_Module)

## 13.15-14.00: Some robotics + compas_fab

[Slides from COMPAS II, PhD course at ITA, ETH](https://github.com/compas-teaching/COMPAS-II-FS2021)

- robots 101
- compared to 3D-printers
- coordinate systems/frames
- joints and links, URDF
- kinematics
- Robot control modes
- Offline/Online
- Realtime?
- ROS
- Planning
- MoveIt

[compas_fab api](https://gramaziokohler.github.io/compas_fab/latest/reference.html)

[compas_fab examples](https://gramaziokohler.github.io/compas_fab/latest/examples.html)

## 14.15-15.00: compas_rrc + ABB robot

![RRC deployment](https://compas-rrc.github.io/compas_rrc/latest/_images/overview-diagram.png)

[compas_rrc_start](https://github.com/compas-rrc/compas_rrc_start)
