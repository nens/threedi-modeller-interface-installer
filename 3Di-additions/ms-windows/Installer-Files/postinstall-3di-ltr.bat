@echo off
if exist postinstall-3di-ltr.log del postinstall-3di-ltr.log
set OSGEO4W_ROOT_MSYS=%OSGEO4W_ROOT:\=/%>>postinstall-3di-ltr.log 2>&1
if "%OSGEO4W_ROOT_MSYS:~1,1%"==":" set OSGEO4W_ROOT_MSYS=/%OSGEO4W_ROOT_MSYS:~0,1%/%OSGEO4W_ROOT_MSYS:~3%>>postinstall-3di-ltr.log 2>&1
del preremove-conf.bat>>postinstall-3di-ltr.log 2>&1
echo set OSGEO4W_ROOT=%OSGEO4W_ROOT%>>preremove-conf.bat
echo set OSGEO4W_ROOT_MSYS=%OSGEO4W_ROOT_MSYS%>>preremove-conf.bat
echo set OSGEO4W_STARTMENU=%OSGEO4W_STARTMENU%>>preremove-conf.bat
echo set OSGEO4W_DESKTOP=%OSGEO4W_DESKTOP%>>preremove-conf.bat
echo OSGEO4W_ROOT=%OSGEO4W_ROOT%>>postinstall-3di-ltr.log 2>&1
echo OSGEO4W_ROOT_MSYS=%OSGEO4W_ROOT_MSYS%>>postinstall-3di-ltr.log 2>&1
echo OSGEO4W_STARTMENU=%OSGEO4W_STARTMENU%>>postinstall-3di-ltr.log 2>&1
echo OSGEO4W_DESKTOP=%OSGEO4W_DESKTOP%>>postinstall-3di-ltr.log 2>&1
PATH %OSGEO4W_ROOT%\bin;%PATH%>>postinstall-3di-ltr.log 2>&1
cd /d %OSGEO4W_ROOT%>>postinstall-3di-ltr.log 2>&1
echo Running postinstall gdal-python.bat...>>postinstall-3di-ltr.log 2>&1
%COMSPEC% /c etc\postinstall\gdal-python.bat>>postinstall-3di-ltr.log 2>&1
ren etc\postinstall\gdal-python.bat gdal-python.bat.done>>postinstall-3di-ltr.log 2>&1

rem echo Running postinstall grass.bat...>>postinstall-3di-ltr.log 2>&1
rem %COMSPEC% /c etc\postinstall\grass.bat>>postinstall-3di-ltr.log 2>&1
rem ren etc\postinstall\grass.bat grass.bat.done>>postinstall-3di-ltr.log 2>&1

echo Running postinstall liblas.bat...>>postinstall-3di-ltr.log 2>&1
%COMSPEC% /c etc\postinstall\liblas.bat>>postinstall-3di-ltr.log 2>&1
ren etc\postinstall\liblas.bat liblas.bat.done>>postinstall-3di-ltr.log 2>&1
echo Running postinstall msvcrt-2008.bat...>>postinstall-3di-ltr.log 2>&1
%COMSPEC% /c etc\postinstall\msvcrt-2008.bat>>postinstall-3di-ltr.log 2>&1
ren etc\postinstall\msvcrt-2008.bat msvcrt-2008.bat.done>>postinstall-3di-ltr.log 2>&1
echo Running postinstall msvcrt-2010.bat...>>postinstall-3di-ltr.log 2>&1
%COMSPEC% /c etc\postinstall\msvcrt-2010.bat>>postinstall-3di-ltr.log 2>&1
ren etc\postinstall\msvcrt-2010.bat msvcrt-2010.bat.done>>postinstall-3di-ltr.log 2>&1
echo Running postinstall msvcrt-2013.bat...>>postinstall-3di-ltr.log 2>&1
%COMSPEC% /c etc\postinstall\msvcrt-2013.bat>>postinstall-3di-ltr.log 2>&1
ren etc\postinstall\msvcrt-2013.bat msvcrt-2013.bat.done>>postinstall-3di-ltr.log 2>&1
echo Running postinstall msvcrt2015.bat...>>postinstall-3di-ltr.log 2>&1
%COMSPEC% /c etc\postinstall\msvcrt2015.bat>>postinstall-3di-ltr.log 2>&1
ren etc\postinstall\msvcrt2015.bat msvcrt2015.bat.done>>postinstall-3di-ltr.log 2>&1
echo Running postinstall opencl.bat...>>postinstall-3di-ltr.log 2>&1
%COMSPEC% /c etc\postinstall\opencl.bat>>postinstall-3di-ltr.log 2>&1
ren etc\postinstall\opencl.bat opencl.bat.done>>postinstall-3di-ltr.log 2>&1
echo Running postinstall openssl.bat...>>postinstall-3di-ltr.log 2>&1
%COMSPEC% /c etc\postinstall\openssl.bat>>postinstall-3di-ltr.log 2>&1
ren etc\postinstall\openssl.bat openssl.bat.done>>postinstall-3di-ltr.log 2>&1
echo Running postinstall pyqt5.bat...>>postinstall-3di-ltr.log 2>&1
%COMSPEC% /c etc\postinstall\pyqt5.bat>>postinstall-3di-ltr.log 2>&1
ren etc\postinstall\pyqt5.bat pyqt5.bat.done>>postinstall-3di-ltr.log 2>&1
echo Running postinstall python-core.bat...>>postinstall-3di-ltr.log 2>&1
%COMSPEC% /c etc\postinstall\python-core.bat>>postinstall-3di-ltr.log 2>&1
ren etc\postinstall\python-core.bat python-core.bat.done>>postinstall-3di-ltr.log 2>&1
echo Running postinstall python3-pip.bat...>>postinstall-3di-ltr.log 2>&1
%COMSPEC% /c etc\postinstall\python3-pip.bat>>postinstall-3di-ltr.log 2>&1
ren etc\postinstall\python3-pip.bat python3-pip.bat.done>>postinstall-3di-ltr.log 2>&1
echo Running postinstall python3-setuptools.bat...>>postinstall-3di-ltr.log 2>&1
%COMSPEC% /c etc\postinstall\python3-setuptools.bat>>postinstall-3di-ltr.log 2>&1
ren etc\postinstall\python3-setuptools.bat python3-setuptools.bat.done>>postinstall-3di-ltr.log 2>&1

rem echo Running postinstall qgis-common.bat...>>postinstall-3di-ltr.log 2>&1
rem %COMSPEC% /c etc\postinstall\qgis-common.bat>>postinstall-3di-ltr.log 2>&1
rem ren etc\postinstall\qgis-common.bat qgis-common.bat.done>>postinstall-3di-ltr.log 2>&1

rem GRASS
rem first our own, then the rest
echo Running postinstall qgis-grass.bat...>>postinstall-3di-ltr.log 2>&1
%COMSPEC% /c etc\postinstall\qgis-grass.bat>>postinstall-3di-ltr.log 2>&1
ren etc\postinstall\qgis-grass.bat qgis-grass.bat.done>>postinstall-3di-ltr.log 2>&1

echo Running postinstall grass.bat...>>postinstall-3di-ltr.log 2>&1
%COMSPEC% /c etc\postinstall\grass.bat>>postinstall-3di-ltr.log 2>&1
ren etc\postinstall\grass.bat grass.bat.done>>postinstall-3di-ltr.log 2>&1

echo Running postinstall qgis-3di-ltr.bat...>>postinstall-3di-ltr.log 2>&1
%COMSPEC% /c etc\postinstall\qgis-3di-ltr.bat>>postinstall-3di-ltr.log 2>&1
ren etc\postinstall\qgis-3di-ltr.bat qgis-3di-ltr.bat.done>>postinstall-3di-ltr.log 2>&1

REM echo Running postinstall qgis.bat...>>postinstall-3di-ltr.log 2>&1
REM %COMSPEC% /c etc\postinstall\qgis.bat>>postinstall-3di-ltr.log 2>&1
REM ren etc\postinstall\qgis.bat qgis.bat.done>>postinstall-3di-ltr.log 2>&1

echo Running postinstall qt5-libs.bat...>>postinstall-3di-ltr.log 2>&1
%COMSPEC% /c etc\postinstall\qt5-libs.bat>>postinstall-3di-ltr.log 2>&1
ren etc\postinstall\qt5-libs.bat qt5-libs.bat.done>>postinstall-3di-ltr.log 2>&1

rem echo Running postinstall saga-ltr.bat...>>postinstall-3di-ltr.log 2>&1
rem %COMSPEC% /c etc\postinstall\saga-ltr.bat>>postinstall-3di-ltr.log 2>&1
rem ren etc\postinstall\saga-ltr.bat saga-ltr.bat.done>>postinstall-3di-ltr.log 2>&1

rem echo Running postinstall setup.bat...>>postinstall-3di-ltr.log 2>&1
rem %COMSPEC% /c etc\postinstall\setup.bat>>postinstall-3di-ltr.log 2>&1
rem ren etc\postinstall\setup.bat setup.bat.done>>postinstall-3di-ltr.log 2>&1

echo Running postinstall shell.bat...>>postinstall-3di-ltr.log 2>&1
%COMSPEC% /c etc\postinstall\shell.bat>>postinstall-3di-ltr.log 2>&1
ren etc\postinstall\shell.bat shell.bat.done>>postinstall-3di-ltr.log 2>&1

echo Running postinstall sip-qt5.bat...>>postinstall-3di-ltr.log 2>&1
%COMSPEC% /c etc\postinstall\sip-qt5.bat>>postinstall-3di-ltr.log 2>&1
ren etc\postinstall\sip-qt5.bat sip-qt5.bat.done>>postinstall-3di-ltr.log 2>&1

ren postinstall-3di-ltr.bat postinstall-3di-ltr.bat.done>>postinstall-3di-ltr.log 2>&1
