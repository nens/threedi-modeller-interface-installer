# 3Di-modeller-interface-installer

This repository contains a Makefile (which should be run in the accompanying docker container) that does the following:

- Downloads a specific complete QGIS installer 
- Uses NSIS to wrap this in a global installer that:
    - Silently installs QGIS (via its original installer) in a configurable directory (no QGIS shortcuts and links)
    - Copies preconfigured profile data (ini files) to the user's AppData for customization (including splash screen)
    - Sets registry keys for default (Python) plugin loading
    - Adds N&S toolboxes (downloaded from plugins.lizard.net) and external toolbbxes (downloaded from plugins.qgis.org)
    - Generate relevant start/desktop shortcuts

Usage
------

The versions of the internal and external plugins are hardcoded in the Makefile. When creating a new installer, update 
these version to the required version.

Check out the repo in a clean folder::

    $ mkdir /tmp/reallyclean
    $ cd /tmp/reallyclean
    $ git clone git@github.com:nens/3Di-modeller-interface-installer.git

    Build (if required) and run the container:  
    $ docker build . -t 3dimi-installer
    $ docker run -w /app/ -v "$(pwd):/app" -it 3dimi-installer make installer

The executable will be in the root folder.