# Rana Desktop Client Installer

This repository contains a Makefile (which should be run in the accompanying docker container) that does the following:

- Downloads a specific complete QGIS installer 
- Uses NSIS to wrap this in a global installer that:
    - Silently installs QGIS (via its original installer) in a configurable directory (no QGIS shortcuts and links, and only possible with admin rights) and generates relevant start/desktop shortcuts
    - Optionally:
        - Copies preconfigured profile data (ini files) to the user's AppData for customization (including splash screen)
        - Adds N&S toolboxes (downloaded from plugins.lizard.net) and external toolboxes (downloaded from plugins.qgis.org)

Usage
------

The versions of QGIS and the (internal and external) plugins are hardcoded in the Makefile. When creating a new installer, update 
these versions to the desired version.

Note that non-LTR releases might have a different internal folder or file naming (e.g "apps/qgis-ltr" vs "apps/qgis", "qgis-ltr.bat" vs "qgis.bat"). This is not automatically detected and the installer script might need to be adjusted to deal with this.

The current license text (LICENSE.txt) is directly copied from the LTR QGIS-OSGeo4W-3.40.6-1 installer UI. In case QGIS or the dependencies are updated, update this text as well.

Check out the repo in a clean folder::

    $ mkdir /tmp/reallyclean
    $ cd /tmp/reallyclean
    $ git clone git@github.com:nens/threedi-modeller-interface-installer.git
    $ cd threedi-modeller-interface-installer

    Build (if required) and run the container:  
    $ docker build . -t rana-installer
    $ docker run -w /app/ -v "$(pwd):/app" -it rana-installer make installer

The executable will be in the root folder.

Signing
-------

Explanation regarding setting up the USB dongle can be found at https://support.globalsign.com/code-signing.

The certificate will be installed via the browser (https://support.globalsign.com/digital-certificates/manage-digital-certificates/ie-compatability-microsoft-edge). Note that, in order to download the certificate to the dongle, Edge needs to run in IE compatibility mode and https://system.globalsign.com/ needs to be added to the Trusted Website in the Internet Options for ActiveX to work.

In case the user is not allowed to add it to the Thrusted Sites via the Internet Options, use the following:

In powershell, type:

    $ gpedit.msc

Go to:

Computer Configuration
 └ Administrative Templates
    └ Windows Components
       └ Internet Explorer
          └ Internet Control Panel
             └ Security Page

And add the following pair entry to "Site to Zone Assignment List" 
https://system.globalsign.com/ 2

Information regarding the actual signing can be found here: https://support.globalsign.com/code-signing/code-signing/code-signing-windows-7-8-and-10


Deploy
------

The installer is uploaded to https://artifacts.lizard.net/ through Github Actions on release. See `docs/release_instructions.txt` for instructions.

This can also be done manually, the Makefile contains a build recipe for this that
uses ``upload-rana-desktop-client.sh``. You'll need to set the ``$RANA_ARTIFACTS_KEY`` environment variable

    $ make upload
