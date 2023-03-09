# 3Di-modeller-interface-installer

This repository contains a Makefile (which should be run in the accompanying docker container) that does the following:

- Downloads a specific complete QGIS installer 
- Uses NSIS to wrap this in a global installer that:
    - Silently installs QGIS (via its original installer) in a configurable directory (no QGIS shortcuts and links)
    - Copies preconfigured profile data (ini files) to the user's AppData for customization (including splash screen)
    - Sets registry keys for default (Python) plugin loading
    - Adds N&S toolboxes (downloaded from plugins.3di.live) and external toolboxes (downloaded from plugins.qgis.org)
    - Generates relevant start/desktop shortcuts

Usage
------

The versions of QGIS and the (internal and external) plugins are hardcoded in the Makefile. When creating a new installer, update 
these versions to the desired version. 

The current license text (LICENSE.txt) is directly copied from the QGIS-OSGeo4W-3.28.4-2 installer UI. In case QGIS or the dependencies 
are updated, update this text as well.

Check out the repo in a clean folder::

    $ mkdir /tmp/reallyclean
    $ cd /tmp/reallyclean
    $ git clone git@github.com:nens/3Di-modeller-interface-installer.git
    $ cd 3Di-modeller-interface-installer

    Build (if required) and run the container:  
    $ docker build . -t 3dimi-installer
    $ docker run -w /app/ -v "$(pwd):/app" -it 3dimi-installer make installer

The executable will be in the root folder.

Deploy
------

The installer can be uploaded to https://artifacts.lizard.net/. The Makefile contains a build recipe for this that
uses ``upload-modeller-interface.sh``. You'll need to set the $MODELLER_INTERFACE_ARTIFACTS_KEY environment variable

    $ make upload