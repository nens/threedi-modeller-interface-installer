@echo off
call "%~dp0\preremove-conf.bat">>%TEMP%\3Di-ltr-preremove.log 2>&1
echo OSGEO4W_ROOT=%OSGEO4W_ROOT%>>%TEMP%\3Di-ltr-preremove.log 2>&1
echo OSGEO4W_STARTMENU=%OSGEO4W_STARTMENU%>>%TEMP%\3Di-ltr-preremove.log 2>&1
echo OSGEO4W_DESKTOP=%OSGEO4W_DESKTOP%>>%TEMP%\3Di-ltr-preremove.log 2>&1
set OSGEO4W_ROOT_MSYS=%OSGEO4W_ROOT:\=/%>>%TEMP%\3Di-ltr-preremove.log 2>&1
if "%OSGEO4W_ROOT_MSYS:~1,1%"==":" set OSGEO4W_ROOT_MSYS=/%OSGEO4W_ROOT_MSYS:~0,1%/%OSGEO4W_ROOT_MSYS:~3%>>%TEMP%\3Di-ltr-preremove.log 2>&1
echo OSGEO4W_ROOT_MSYS=%OSGEO4W_ROOT_MSYS%>>%TEMP%\3Di-ltr-preremove.log 2>&1
PATH %OSGEO4W_ROOT%\bin;%PATH%>>%TEMP%\3Di-ltr-preremove.log 2>&1
cd /d "%OSGEO4W_ROOT%">>%TEMP%\3Di-ltr-preremove.log 2>&1
echo Running preremove grass.bat...>>%TEMP%\3Di-ltr-preremove.log 2>&1
%COMSPEC% /c etc\preremove\grass.bat>>%TEMP%\3Di-ltr-preremove.log 2>&1
ren etc\preremove\grass.bat grass.bat.done>>%TEMP%\3Di-ltr-preremove.log 2>&1
echo Running preremove opencl.bat...>>%TEMP%\3Di-ltr-preremove.log 2>&1
%COMSPEC% /c etc\preremove\opencl.bat>>%TEMP%\3Di-ltr-preremove.log 2>&1
ren etc\preremove\opencl.bat opencl.bat.done>>%TEMP%\3Di-ltr-preremove.log 2>&1
echo Running preremove pyqt5.bat...>>%TEMP%\3Di-ltr-preremove.log 2>&1
%COMSPEC% /c etc\preremove\pyqt5.bat>>%TEMP%\3Di-ltr-preremove.log 2>&1
ren etc\preremove\pyqt5.bat pyqt5.bat.done>>%TEMP%\3Di-ltr-preremove.log 2>&1
echo Running preremove python3-certifi.bat...>>%TEMP%\3Di-ltr-preremove.log 2>&1
%COMSPEC% /c etc\preremove\python3-certifi.bat>>%TEMP%\3Di-ltr-preremove.log 2>&1
ren etc\preremove\python3-certifi.bat python3-certifi.bat.done>>%TEMP%\3Di-ltr-preremove.log 2>&1
echo Running preremove python3-chardet.bat...>>%TEMP%\3Di-ltr-preremove.log 2>&1
%COMSPEC% /c etc\preremove\python3-chardet.bat>>%TEMP%\3Di-ltr-preremove.log 2>&1
ren etc\preremove\python3-chardet.bat python3-chardet.bat.done>>%TEMP%\3Di-ltr-preremove.log 2>&1
echo Running preremove python3-core.bat...>>%TEMP%\3Di-ltr-preremove.log 2>&1
%COMSPEC% /c etc\preremove\python3-core.bat>>%TEMP%\3Di-ltr-preremove.log 2>&1
ren etc\preremove\python3-core.bat python3-core.bat.done>>%TEMP%\3Di-ltr-preremove.log 2>&1
echo Running preremove python3-coverage.bat...>>%TEMP%\3Di-ltr-preremove.log 2>&1
%COMSPEC% /c etc\preremove\python3-coverage.bat>>%TEMP%\3Di-ltr-preremove.log 2>&1
ren etc\preremove\python3-coverage.bat python3-coverage.bat.done>>%TEMP%\3Di-ltr-preremove.log 2>&1
echo Running preremove python3-cycler.bat...>>%TEMP%\3Di-ltr-preremove.log 2>&1
%COMSPEC% /c etc\preremove\python3-cycler.bat>>%TEMP%\3Di-ltr-preremove.log 2>&1
ren etc\preremove\python3-cycler.bat python3-cycler.bat.done>>%TEMP%\3Di-ltr-preremove.log 2>&1
echo Running preremove python3-decorator.bat...>>%TEMP%\3Di-ltr-preremove.log 2>&1
%COMSPEC% /c etc\preremove\python3-decorator.bat>>%TEMP%\3Di-ltr-preremove.log 2>&1
ren etc\preremove\python3-decorator.bat python3-decorator.bat.done>>%TEMP%\3Di-ltr-preremove.log 2>&1
echo Running preremove python3-exifread.bat...>>%TEMP%\3Di-ltr-preremove.log 2>&1
%COMSPEC% /c etc\preremove\python3-exifread.bat>>%TEMP%\3Di-ltr-preremove.log 2>&1
ren etc\preremove\python3-exifread.bat python3-exifread.bat.done>>%TEMP%\3Di-ltr-preremove.log 2>&1
echo Running preremove python3-future.bat...>>%TEMP%\3Di-ltr-preremove.log 2>&1
%COMSPEC% /c etc\preremove\python3-future.bat>>%TEMP%\3Di-ltr-preremove.log 2>&1
ren etc\preremove\python3-future.bat python3-future.bat.done>>%TEMP%\3Di-ltr-preremove.log 2>&1
echo Running preremove python3-httplib2.bat...>>%TEMP%\3Di-ltr-preremove.log 2>&1
%COMSPEC% /c etc\preremove\python3-httplib2.bat>>%TEMP%\3Di-ltr-preremove.log 2>&1
ren etc\preremove\python3-httplib2.bat python3-httplib2.bat.done>>%TEMP%\3Di-ltr-preremove.log 2>&1
echo Running preremove python3-idna.bat...>>%TEMP%\3Di-ltr-preremove.log 2>&1
%COMSPEC% /c etc\preremove\python3-idna.bat>>%TEMP%\3Di-ltr-preremove.log 2>&1
ren etc\preremove\python3-idna.bat python3-idna.bat.done>>%TEMP%\3Di-ltr-preremove.log 2>&1
echo Running preremove python3-ipython-genutils.bat...>>%TEMP%\3Di-ltr-preremove.log 2>&1
%COMSPEC% /c etc\preremove\python3-ipython-genutils.bat>>%TEMP%\3Di-ltr-preremove.log 2>&1
ren etc\preremove\python3-ipython-genutils.bat python3-ipython-genutils.bat.done>>%TEMP%\3Di-ltr-preremove.log 2>&1
echo Running preremove python3-jinja2.bat...>>%TEMP%\3Di-ltr-preremove.log 2>&1
%COMSPEC% /c etc\preremove\python3-jinja2.bat>>%TEMP%\3Di-ltr-preremove.log 2>&1
ren etc\preremove\python3-jinja2.bat python3-jinja2.bat.done>>%TEMP%\3Di-ltr-preremove.log 2>&1
echo Running preremove python3-jsonschema.bat...>>%TEMP%\3Di-ltr-preremove.log 2>&1
%COMSPEC% /c etc\preremove\python3-jsonschema.bat>>%TEMP%\3Di-ltr-preremove.log 2>&1
ren etc\preremove\python3-jsonschema.bat python3-jsonschema.bat.done>>%TEMP%\3Di-ltr-preremove.log 2>&1
echo Running preremove python3-jupyter-core.bat...>>%TEMP%\3Di-ltr-preremove.log 2>&1
%COMSPEC% /c etc\preremove\python3-jupyter-core.bat>>%TEMP%\3Di-ltr-preremove.log 2>&1
ren etc\preremove\python3-jupyter-core.bat python3-jupyter-core.bat.done>>%TEMP%\3Di-ltr-preremove.log 2>&1
echo Running preremove python3-markupsafe.bat...>>%TEMP%\3Di-ltr-preremove.log 2>&1
%COMSPEC% /c etc\preremove\python3-markupsafe.bat>>%TEMP%\3Di-ltr-preremove.log 2>&1
ren etc\preremove\python3-markupsafe.bat python3-markupsafe.bat.done>>%TEMP%\3Di-ltr-preremove.log 2>&1
echo Running preremove python3-matplotlib.bat...>>%TEMP%\3Di-ltr-preremove.log 2>&1
%COMSPEC% /c etc\preremove\python3-matplotlib.bat>>%TEMP%\3Di-ltr-preremove.log 2>&1
ren etc\preremove\python3-matplotlib.bat python3-matplotlib.bat.done>>%TEMP%\3Di-ltr-preremove.log 2>&1
echo Running preremove python3-mock.bat...>>%TEMP%\3Di-ltr-preremove.log 2>&1
%COMSPEC% /c etc\preremove\python3-mock.bat>>%TEMP%\3Di-ltr-preremove.log 2>&1
ren etc\preremove\python3-mock.bat python3-mock.bat.done>>%TEMP%\3Di-ltr-preremove.log 2>&1
echo Running preremove python3-nbformat.bat...>>%TEMP%\3Di-ltr-preremove.log 2>&1
%COMSPEC% /c etc\preremove\python3-nbformat.bat>>%TEMP%\3Di-ltr-preremove.log 2>&1
ren etc\preremove\python3-nbformat.bat python3-nbformat.bat.done>>%TEMP%\3Di-ltr-preremove.log 2>&1
echo Running preremove python3-networkx.bat...>>%TEMP%\3Di-ltr-preremove.log 2>&1
%COMSPEC% /c etc\preremove\python3-networkx.bat>>%TEMP%\3Di-ltr-preremove.log 2>&1
ren etc\preremove\python3-networkx.bat python3-networkx.bat.done>>%TEMP%\3Di-ltr-preremove.log 2>&1
echo Running preremove python3-nose2.bat...>>%TEMP%\3Di-ltr-preremove.log 2>&1
%COMSPEC% /c etc\preremove\python3-nose2.bat>>%TEMP%\3Di-ltr-preremove.log 2>&1
ren etc\preremove\python3-nose2.bat python3-nose2.bat.done>>%TEMP%\3Di-ltr-preremove.log 2>&1
echo Running preremove python3-numpy.bat...>>%TEMP%\3Di-ltr-preremove.log 2>&1
%COMSPEC% /c etc\preremove\python3-numpy.bat>>%TEMP%\3Di-ltr-preremove.log 2>&1
ren etc\preremove\python3-numpy.bat python3-numpy.bat.done>>%TEMP%\3Di-ltr-preremove.log 2>&1
echo Running preremove python3-owslib.bat...>>%TEMP%\3Di-ltr-preremove.log 2>&1
%COMSPEC% /c etc\preremove\python3-owslib.bat>>%TEMP%\3Di-ltr-preremove.log 2>&1
ren etc\preremove\python3-owslib.bat python3-owslib.bat.done>>%TEMP%\3Di-ltr-preremove.log 2>&1
echo Running preremove python3-pbr.bat...>>%TEMP%\3Di-ltr-preremove.log 2>&1
%COMSPEC% /c etc\preremove\python3-pbr.bat>>%TEMP%\3Di-ltr-preremove.log 2>&1
ren etc\preremove\python3-pbr.bat python3-pbr.bat.done>>%TEMP%\3Di-ltr-preremove.log 2>&1
echo Running preremove python3-pip.bat...>>%TEMP%\3Di-ltr-preremove.log 2>&1
%COMSPEC% /c etc\preremove\python3-pip.bat>>%TEMP%\3Di-ltr-preremove.log 2>&1
ren etc\preremove\python3-pip.bat python3-pip.bat.done>>%TEMP%\3Di-ltr-preremove.log 2>&1
echo Running preremove python3-plotly.bat...>>%TEMP%\3Di-ltr-preremove.log 2>&1
%COMSPEC% /c etc\preremove\python3-plotly.bat>>%TEMP%\3Di-ltr-preremove.log 2>&1
ren etc\preremove\python3-plotly.bat python3-plotly.bat.done>>%TEMP%\3Di-ltr-preremove.log 2>&1
echo Running preremove python3-psycopg2.bat...>>%TEMP%\3Di-ltr-preremove.log 2>&1
%COMSPEC% /c etc\preremove\python3-psycopg2.bat>>%TEMP%\3Di-ltr-preremove.log 2>&1
ren etc\preremove\python3-psycopg2.bat python3-psycopg2.bat.done>>%TEMP%\3Di-ltr-preremove.log 2>&1
echo Running preremove python3-pygments.bat...>>%TEMP%\3Di-ltr-preremove.log 2>&1
%COMSPEC% /c etc\preremove\python3-pygments.bat>>%TEMP%\3Di-ltr-preremove.log 2>&1
ren etc\preremove\python3-pygments.bat python3-pygments.bat.done>>%TEMP%\3Di-ltr-preremove.log 2>&1
echo Running preremove python3-pyparsing.bat...>>%TEMP%\3Di-ltr-preremove.log 2>&1
%COMSPEC% /c etc\preremove\python3-pyparsing.bat>>%TEMP%\3Di-ltr-preremove.log 2>&1
ren etc\preremove\python3-pyparsing.bat python3-pyparsing.bat.done>>%TEMP%\3Di-ltr-preremove.log 2>&1
echo Running preremove python3-pyproj.bat...>>%TEMP%\3Di-ltr-preremove.log 2>&1
%COMSPEC% /c etc\preremove\python3-pyproj.bat>>%TEMP%\3Di-ltr-preremove.log 2>&1
ren etc\preremove\python3-pyproj.bat python3-pyproj.bat.done>>%TEMP%\3Di-ltr-preremove.log 2>&1
echo Running preremove python3-python-dateutil.bat...>>%TEMP%\3Di-ltr-preremove.log 2>&1
%COMSPEC% /c etc\preremove\python3-python-dateutil.bat>>%TEMP%\3Di-ltr-preremove.log 2>&1
ren etc\preremove\python3-python-dateutil.bat python3-python-dateutil.bat.done>>%TEMP%\3Di-ltr-preremove.log 2>&1
echo Running preremove python3-pytz.bat...>>%TEMP%\3Di-ltr-preremove.log 2>&1
%COMSPEC% /c etc\preremove\python3-pytz.bat>>%TEMP%\3Di-ltr-preremove.log 2>&1
ren etc\preremove\python3-pytz.bat python3-pytz.bat.done>>%TEMP%\3Di-ltr-preremove.log 2>&1
echo Running preremove python3-pywin32.bat...>>%TEMP%\3Di-ltr-preremove.log 2>&1
%COMSPEC% /c etc\preremove\python3-pywin32.bat>>%TEMP%\3Di-ltr-preremove.log 2>&1
ren etc\preremove\python3-pywin32.bat python3-pywin32.bat.done>>%TEMP%\3Di-ltr-preremove.log 2>&1
echo Running preremove python3-pyyaml.bat...>>%TEMP%\3Di-ltr-preremove.log 2>&1
%COMSPEC% /c etc\preremove\python3-pyyaml.bat>>%TEMP%\3Di-ltr-preremove.log 2>&1
ren etc\preremove\python3-pyyaml.bat python3-pyyaml.bat.done>>%TEMP%\3Di-ltr-preremove.log 2>&1
echo Running preremove python3-requests.bat...>>%TEMP%\3Di-ltr-preremove.log 2>&1
%COMSPEC% /c etc\preremove\python3-requests.bat>>%TEMP%\3Di-ltr-preremove.log 2>&1
ren etc\preremove\python3-requests.bat python3-requests.bat.done>>%TEMP%\3Di-ltr-preremove.log 2>&1
echo Running preremove python3-retrying.bat...>>%TEMP%\3Di-ltr-preremove.log 2>&1
%COMSPEC% /c etc\preremove\python3-retrying.bat>>%TEMP%\3Di-ltr-preremove.log 2>&1
ren etc\preremove\python3-retrying.bat python3-retrying.bat.done>>%TEMP%\3Di-ltr-preremove.log 2>&1
echo Running preremove python3-scipy.bat...>>%TEMP%\3Di-ltr-preremove.log 2>&1
%COMSPEC% /c etc\preremove\python3-scipy.bat>>%TEMP%\3Di-ltr-preremove.log 2>&1
ren etc\preremove\python3-scipy.bat python3-scipy.bat.done>>%TEMP%\3Di-ltr-preremove.log 2>&1
echo Running preremove python3-setuptools.bat...>>%TEMP%\3Di-ltr-preremove.log 2>&1
%COMSPEC% /c etc\preremove\python3-setuptools.bat>>%TEMP%\3Di-ltr-preremove.log 2>&1
ren etc\preremove\python3-setuptools.bat python3-setuptools.bat.done>>%TEMP%\3Di-ltr-preremove.log 2>&1
echo Running preremove python3-shapely.bat...>>%TEMP%\3Di-ltr-preremove.log 2>&1
%COMSPEC% /c etc\preremove\python3-shapely.bat>>%TEMP%\3Di-ltr-preremove.log 2>&1
ren etc\preremove\python3-shapely.bat python3-shapely.bat.done>>%TEMP%\3Di-ltr-preremove.log 2>&1
echo Running preremove python3-simplejson.bat...>>%TEMP%\3Di-ltr-preremove.log 2>&1
%COMSPEC% /c etc\preremove\python3-simplejson.bat>>%TEMP%\3Di-ltr-preremove.log 2>&1
ren etc\preremove\python3-simplejson.bat python3-simplejson.bat.done>>%TEMP%\3Di-ltr-preremove.log 2>&1
echo Running preremove python3-six.bat...>>%TEMP%\3Di-ltr-preremove.log 2>&1
%COMSPEC% /c etc\preremove\python3-six.bat>>%TEMP%\3Di-ltr-preremove.log 2>&1
ren etc\preremove\python3-six.bat python3-six.bat.done>>%TEMP%\3Di-ltr-preremove.log 2>&1
echo Running preremove python3-traitlets.bat...>>%TEMP%\3Di-ltr-preremove.log 2>&1
%COMSPEC% /c etc\preremove\python3-traitlets.bat>>%TEMP%\3Di-ltr-preremove.log 2>&1
ren etc\preremove\python3-traitlets.bat python3-traitlets.bat.done>>%TEMP%\3Di-ltr-preremove.log 2>&1
echo Running preremove python3-urllib3.bat...>>%TEMP%\3Di-ltr-preremove.log 2>&1
%COMSPEC% /c etc\preremove\python3-urllib3.bat>>%TEMP%\3Di-ltr-preremove.log 2>&1
ren etc\preremove\python3-urllib3.bat python3-urllib3.bat.done>>%TEMP%\3Di-ltr-preremove.log 2>&1
echo Running preremove python3-xlrd.bat...>>%TEMP%\3Di-ltr-preremove.log 2>&1
%COMSPEC% /c etc\preremove\python3-xlrd.bat>>%TEMP%\3Di-ltr-preremove.log 2>&1
ren etc\preremove\python3-xlrd.bat python3-xlrd.bat.done>>%TEMP%\3Di-ltr-preremove.log 2>&1
echo Running preremove python3-xlwt.bat...>>%TEMP%\3Di-ltr-preremove.log 2>&1
%COMSPEC% /c etc\preremove\python3-xlwt.bat>>%TEMP%\3Di-ltr-preremove.log 2>&1
ren etc\preremove\python3-xlwt.bat python3-xlwt.bat.done>>%TEMP%\3Di-ltr-preremove.log 2>&1

echo Running preremove qgis-grass.bat...>>%TEMP%\3Di-ltr-preremove.log 2>&1
%COMSPEC% /c etc\preremove\qgis-grass.bat>>%TEMP%\3Di-ltr-preremove.log 2>&1
ren etc\preremove\qgis-gras.bat qgis-grass.bat.done>>%TEMP%\3Di-ltr-preremove.log 2>&1

REM echo Running preremove qgis-grass-plugin7.bat...>>%TEMP%\3Di-ltr-preremove.log 2>&1
REM %COMSPEC% /c etc\preremove\qgis-grass-plugin7.bat>>%TEMP%\3Di-ltr-preremove.log 2>&1
REM ren etc\preremove\qgis-grass-plugin7.bat qgis-grass-plugin7.bat.done>>%TEMP%\3Di-ltr-preremove.log 2>&1

REM echo Running preremove qgis.bat...>>%TEMP%\3Di-ltr-preremove.log 2>&1
REM %COMSPEC% /c etc\preremove\qgis.bat>>%TEMP%\3Di-ltr-preremove.log 2>&1
REM ren etc\preremove\qgis.bat qgis.bat.done>>%TEMP%\3Di-ltr-preremove.log 2>&1

echo Running preremove QGIS-NL-ltr.bat...>>%TEMP%\3Di-ltr-preremove.log 2>&1
%COMSPEC% /c etc\preremove\QGIS-NL-ltr.bat>>%TEMP%\3Di-ltr-preremove.log 2>&1
ren etc\preremove\QGIS-NL-ltr.bat QGIS-NL-ltr.bat.done>>%TEMP%\3Di-ltr-preremove.log 2>&1

echo Running preremove saga-ltr.bat...>>%TEMP%\3Di-ltr-preremove.log 2>&1
%COMSPEC% /c etc\preremove\saga-ltr.bat>>%TEMP%\3Di-ltr-preremove.log 2>&1
ren etc\preremove\saga-ltr.bat saga-ltr.bat.done>>%TEMP%\3Di-ltr-preremove.log 2>&1
echo Running preremove setup.bat...>>%TEMP%\3Di-ltr-preremove.log 2>&1
%COMSPEC% /c etc\preremove\setup.bat>>%TEMP%\3Di-ltr-preremove.log 2>&1
ren etc\preremove\setup.bat setup.bat.done>>%TEMP%\3Di-ltr-preremove.log 2>&1
echo Running preremove shell.bat...>>%TEMP%\3Di-ltr-preremove.log 2>&1
%COMSPEC% /c etc\preremove\shell.bat>>%TEMP%\3Di-ltr-preremove.log 2>&1
ren etc\preremove\shell.bat shell.bat.done>>%TEMP%\3Di-ltr-preremove.log 2>&1
echo Running preremove sip-qt5.bat...>>%TEMP%\3Di-ltr-preremove.log 2>&1
%COMSPEC% /c etc\preremove\sip-qt5.bat>>%TEMP%\3Di-ltr-preremove.log 2>&1
ren etc\preremove\sip-qt5.bat sip-qt5.bat.done>>%TEMP%\3Di-ltr-preremove.log 2>&1

ren preremove-3di-ltr.bat preremove-3di-ltr.bat.done>>%TEMP%\3Di-ltr-preremove-nl.log 2>&1
