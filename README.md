# 3Di-modeller-interface-installer

Basic workings
--------------

This Repository contains the 3Di Modeler interface installer build files. To create a working installer this repository needs to be checked out in combination with a working QGIS version. De file tree needs to be:

    - <Build dir>/3Di-additions
    - <Build dir>/QGIS (Checkout of QGIS repository)

When the docker image is build provided in this repository and the directories are placed correctly an installer can be created by executing the script ``./create_qgis_3di_nsis.pl`` in the docker::

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

Installer creation
------------------