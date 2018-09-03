3Di-modeller-interface-installer
================================

Build script and binaries to make 3Di-modeller installer for Win64. The build script is a Linux bash script.

Installation requirements
-------------------------
- nsis (``# apt install nsis`` if necessary).

Usage
-----
- Run the script ``quickpackage.sh`` within the working directory.
- Installer script pulls latest releases of ThreeDiToolbox, ThreeDICustomizations and packages an installer executable named ``3Di-modeler-interface-Setup-x64.exe``

TODO
----
- Should include the deployment part eventually.
