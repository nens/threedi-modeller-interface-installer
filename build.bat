@ECHO OFF

TITLE Creating 3Di Modeler interface installer

rd /S /Q "%cd%/3Di-additions/ms-windows/profiles/default/python/plugins/ThreeDiToolbox"
mkdir "%cd%/3Di-additions/ms-windows/profiles/default/python/plugins/ThreeDiToolbox"

rd /S /Q "%cd%/3Di-additions/ms-windows/profiles/default/python/plugins/ThreeDiCustomizations"
mkdir "%cd%/3Di-additions/ms-windows/profiles/default/python/plugins/ThreeDiCustomizations"

rd /S /Q "%cd%/QGIS"
mkdir "%cd%/QGIS"

docker build -t 3dimi-installer:latest .

docker run -v %cd%\QGIS:/installer/QGIS -v %cd%\3Di-additions:/installer/3Di-additions -it -e PYTHONUNBUFFERED=0 3dimi-installer ./clone.sh

docker run -v %cd%\QGIS:/installer/QGIS -v %cd%\3Di-additions:/installer/3Di-additions -it -e PYTHONUNBUFFERED=0 3dimi-installer ./create_qgis_3di_nsis.pl
