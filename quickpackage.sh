#!/bin/bash
###########################################################################
#    quickpackage.sh
#    ---------------------
#    Date                 : November 2010
#    Copyright            : (C) 2010 by Tim Sutton
#    Email                : tim at kartoza dot com
###########################################################################
#                                                                         #
#   This program is free software; you can redistribute it and/or modify  #
#   it under the terms of the GNU General Public License as published by  #
#   the Free Software Foundation; either version 2 of the License, or     #
#   (at your option) any later version.                                   #
#                                                                         #
###########################################################################


# This script is just for if you want to run the nsis (under linux) part 
# of the package building process. Typically you should use 
#
# osgeo4w/creatensis.pl
#
# rather to do the complete package build process. However running this 
# script can be useful if you have manually tweaked the package contents 
# under osgeo4w/unpacked and want to create a new package based on that.
#
# Tim Sutton November 2010

# MD (Md-kwadraat) 12 juli 2018
# adapted for 3Di


# By default x86_64, 32 bit distribution needs further work (h5py, netcdf4)
OSGEO4WDIR=osgeo4w/unpacked-x86_64
DARCH="x86_64"
INSTALLER_NAME="3Di-modeler-interface-Setup-x64.exe"

if [[ "$1" == "32" ]]
then
    echo "* Building 32-bit installer…" 
    OSGEO4WDIR=osgeo4w/unpacked-x86
    DARCH="x86"
    INSTALLER_NAME="3Di-modeler-interface-Setup32.exe"
else
    echo "* Building 64-bit installer…"
fi 
echo
# get latest ThreeDiToolbox master from github
# TODO: get the latest tag instead of master?
pushd profile/python/plugins "$@">/dev/null
if [ -d ThreeDiToolbox ];
then
    echo "* ThreeDiToolbox already exists, leaving it as is."
    echo "  To use the latest release from github, remove the directory."
else
    echo "* Fetching recent ThreeDiToolbox…"
    git clone -b master --single-branch git@github.com:/nens/ThreeDiToolbox.git
    rm -rf ThreeDiToolbox/.git*
fi
popd "$@">/dev/null
echo

# get latest ThreeDiCustomizations master from github
# TODO: get the latest tag instead of master?
pushd profile/python/plugins "$@">/dev/null
if [ -d ThreeDiCustomizations ];
then
    echo "* ThreeDiCustomizations already exists, leaving it as is."
    echo "  To use the latest release from github, remove the directory."
else
    echo "* Fetching recent ThreeDiCustomizations…"
    git clone -b master --single-branch git@github.com:/nens/ThreeDiCustomizations.git
    rm -rf ThreeDiCustomizations.git*
fi
popd "$@">/dev/null
echo
echo "* Installer package is being made…"
echo
makensis \
    -DVERSION_NUMBER='2.18.21' \
    -DPROFILE_VERSION_NUMBER='1.3' \
    -DVERSION_NAME='Nelen & Schuurmans' \
    -DSVN_REVISION='0' \
    -DQGIS_BASE='3Di_Modeler_Interface' \
    -DQGIS_PROFILE='3Di_Modeler_Interface_Profile' \
    -DINSTALLER_NAME=${INSTALLER_NAME} \
    -DDISPLAYED_NAME='3Di_Modeler_Interface' \
    -DBINARY_REVISION=1 \
    -DINSTALLER_TYPE=OSGeo4W \
    -DPACKAGE_FOLDER=${OSGEO4WDIR} \
    -DPROFILE_FOLDER=profile \
    -DSHORTNAME=3Di \
    -DARCH=$DARCH \
    -V2 \
    QGIS-Installer.nsi
