# 3Di-modeller-interface-installer

This repository contains a Makefile (which should be run in the accompanying docker container) that does the following:

- Download a specific complete QGIS installer (via WGET)
- Uses NSIS to wrap this in a global installer that:
    - Silently installs QGIS (via its original installer) in a configurable directory (no QGIS shortcuts and links)
    - Copies preconfigured profile data (ini files) to the user's AppData for customization (including splash screen)
    - Sets registry keys for default (Python) plugin loading

TODO:
    - Add toolboxes
    - Add packages if required (from osgeo4w folder)
    - Generate license file, if required
    - Generate relevant start/desktop shortcuts

TESTING
    - Are all dependencies present? Right version (Spatialite etc)
    - Is the directotry structure in ProgramFiles ok?
    - QGIS has quite advanced messaging regarding upgrading/downgrading, we won't have that
        - We just run the standard QGIS uninstaller and clear the programfiles folder of the ModelerInterface
    - We disabled generation of start/desktop shortcuts by the QGIS installer
    - Does AppData need to be cleaned at an uninstall?
    - Do multiple versions next to each other work?

Usage
------

Check out this repository 

Build a local docker (if required):  
    docker build . -t 3dimi-installer
Run that docker 
    docker run -w /app/ -v "$(pwd):/app" -it 3dimi-installer make installer

The executable will be in the root folder folder


OLD:


Basic workings
--------------

This Repository contains the 3Di Modeler interface installer build files. To create a working installer this repository needs to be checked out in combination with a working QGIS version. De file tree needs to be:

    - <Build dir>/3Di-additions
    - <Build dir>/QGIS (Checkout of QGIS repository)

When the docker image is build provided in this repository and the directories are placed correctly an installer can be created by executing the script ``./create_qgis_3di_nsis.pl`` in the docker:

    docker run -v $(pwd)/QGIS:/installer/QGIS -v $(pwd)/3Di-additions:/installer/3Di-additions -it -e PYTHONUNBUFFERED=0 3dimi-installer ./create_qgis_3di_nsis.pl


Some specifics
--------------

The ``3Di-additions/ms-windows`` directory contains all files and scripts to make the 3Di modeller interface from a standard QGIS application during the installation. 

Important steps to create look and feel of the modeller interface application after installation are adding the correct plugins in the plugin folder ``./3Di-additions/ms-windows/profiles/default/python/plugins``  before creating the installer. Plugins needed for the current modeler interface are:

- ThreeDiToolbox (Toolbox for editing and analyzing 3Di models.)
- ThreeDiCustomizations (Plugin to creat look and feel of the 3Di Modeler interface.)
- crayfish
- valuetool
- profiletool
- quickmap services

