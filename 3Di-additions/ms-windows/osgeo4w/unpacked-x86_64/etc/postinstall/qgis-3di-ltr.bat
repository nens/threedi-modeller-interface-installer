set OSGEO4W_PROFILE=%OSGEO4W_PROFILE_FOLDER:\=\\%
textreplace -std -t bin\qgis-3di-ltr.bat
textreplace -sf bin\qgis-3di-ltr.bat -df bin\qgis-3di-ltr.bat -map @profile@ %OSGEO4W_PROFILE%

textreplace -std -t bin\qgis-designer.bat
textreplace -std -t bin\python-qgis.bat

REM get short path without blanks
for %%i in ("%OSGEO4W_ROOT%") do set O4W_ROOT=%%~fsi
if "%OSGEO4W_DESKTOP%"=="" set OSGEO4W_DESKTOP=~$folder.common_desktop$


if not %OSGEO4W_MENU_LINKS%==0 mkdir "%OSGEO4W_STARTMENU%"
if not %OSGEO4W_DESKTOP_LINKS%==0 mkdir "%OSGEO4W_DESKTOP%"


if not %OSGEO4W_MENU_LINKS%==0 nircmd shortcut "%O4W_ROOT%\bin\qgis-3di-ltr.bat" "%OSGEO4W_STARTMENU%" "3Di Modeller Interface" "" "%O4W_ROOT%\apps\qgis-ltr\icons\3Di.ico" "" "min"
if not %OSGEO4W_DESKTOP_LINKS%==0 nircmd shortcut "%O4W_ROOT%\bin\qgis-3di-ltr.bat" "%OSGEO4W_DESKTOP%" "3Di Modeller Interface" "" "%O4W_ROOT%\apps\qgis-ltr\icons\3Di.ico" "" "min"

del "%OSGEO4W_STARTMENU%\GRASS GIS 7.6.0.lnk"
del "%OSGEO4W_DESKTOP%\GRASS GIS 7.6.0.lnk"

set OSGEO4W_ROOT=%OSGEO4W_ROOT:\=\\%
textreplace -std -t "%O4W_ROOT%\apps\qgis-ltr\bin\qgis-3di.reg"
nircmd elevate "%WINDIR%\regedit" /s "%O4W_ROOT%\apps\qgis-ltr\bin\qgis-3di.reg"
del /s /q "%OSGEO4W_ROOT%\apps\qgis-ltr\python\*.pyc"
exit /b 0
