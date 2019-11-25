textreplace -std -t bin\grass76.bat

rem ## we only use grass as plugin in QGIS ##


rem if "%OSGEO4W_DESKTOP%"=="" set OSGEO4W_DESKTOP=~$folder.common_desktop$

copy bin\qgis-ltr-bin.exe bin\qgis-ltr-bin-g7.exe
copy bin\qgis-ltr-bin.vars bin\qgis-ltr-bin-g7.vars
rem call "%OSGEO4W_ROOT%\bin\@package@-grass@grassmajor@.bat" --postinstall

rem if not %OSGEO4W_MENU_LINKS%==0 mkdir "%OSGEO4W_STARTMENU%"
rem if not %OSGEO4W_DESKTOP_LINKS%==0 mkdir "%OSGEO4W_DESKTOP%"

rem if not %OSGEO4W_MENU_LINKS%==0 nircmd shortcut "%OSGEO4W_ROOT%\bin\@package@-bin-g@grassmajor@.exe" "%OSGEO4W_STARTMENU%" "QGIS Desktop @version@ with GRASS @grassversion@"
rem if not %OSGEO4W_DESKTOP_LINKS%==0 nircmd shortcut "%OSGEO4W_ROOT%\bin\@package@-bin-g@grassmajor@.exe" "%OSGEO4W_DESKTOP%" "QGIS Desktop @version@ with GRASS @grassversion@"
