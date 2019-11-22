@ECHO OFF
set BASE=C:\Program Files\3DiModellerInterface 3.4

 
set PATH=%BASE%\bin;%PATH%
set PATH=%PATH%;%BASE%\apps\qgis\bin

call "%BASE%\bin\o4w_env.bat"
call "%BASE%\bin\qt5_env.bat"
call "%BASE%\bin\py3_env.bat

cd /d %~dp0

@ECHO ON

call pyrcc5 ui\resources.qrc -o gui\generated\resources_rc.py

@ECHO OFF

GOTO END

:ERROR
   echo "Compile Error"
   set ERRORLEVEL=%ERRORLEVEL%
   pause  
:END

::pause
 