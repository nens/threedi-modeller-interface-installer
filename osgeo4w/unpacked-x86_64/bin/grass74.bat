@echo off
rem #########################################################################
rem #
rem # GRASS initialization bat script (OSGeo4W)
rem #
rem #########################################################################

SET OSGEO4W_ROOT=C:\OSGeo4W64_md

rem
rem Set environmental variables
rem
call %OSGEO4W_ROOT%\bin\o4w_env.bat
call %OSGEO4W_ROOT%\apps\grass\grass-7.4.1\etc\env.bat

rem
rem Launch GRASS GIS
rem
"%GRASS_PYTHON%" "%GISBASE%\etc\grass74.py" %*

rem
rem Pause on error
rem
if %ERRORLEVEL% GEQ 1 pause
