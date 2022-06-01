# 3Di-modeller-interface-installer

This repository contains a Makefile (which should be run in the accompanying docker container) that does the following:

- Download a specific complete QGIS installer 
- Uses NSIS to wrap this in a global installer that:
    - Silently installs QGIS (via its original installer) in a configurable directory (no QGIS shortcuts and links)
    - Copies preconfigured profile data (ini files) to the user's AppData for customization (including splash screen)
    - Sets registry keys for default (Python) plugin loading
    - Adds N&S toolboxes (downloaded from plugins.lizard.net)
    - Generate relevant start/desktop shortcuts

Usage
------

TODO: How to set versions of plugins

Check out the repo in a clean folder::

    $ mkdir /tmp/reallyclean
    $ cd /tmp/reallyclean
    $ git clone git@github.com:nens/3Di-modeller-interface-installer.git

    Build (if required) and run the container:  
    $ docker build . -t 3dimi-installer
    $ docker run -w /app/ -v "$(pwd):/app" -it 3dimi-installer make installer

The executable will be in the root folder.

Some specifics
--------------

This repository contains 4 fixed plugins that will be installed as well.

- crayfish
- valuetool
- profiletool
- quickmap services

