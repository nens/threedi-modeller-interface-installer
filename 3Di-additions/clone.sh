#!/bin/bash

git clone --branch final-3_4_13 --depth 1 https://github.com/qgis/qgis.git /installer/QGIS 
git clone --branch master --depth 1 https://github.com/nens/ThreeDiToolbox.git ./ms-windows/profiles/default/python/plugins/ThreeDiToolbox
git clone --branch master --depth 1 https://github.com/nens/ThreeDiCustomizations.git ./ms-windows/profiles/default/python/plugins/ThreeDiCustomizations
