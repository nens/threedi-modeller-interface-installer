#############################################################################
#
# MODULE:   	Grass Compilation
# AUTHOR(S):	Original author unknown - probably CERL
#		Markus Neteler - Germany/Italy - neteler@itc.it
#   	    	Justin Hickey - Thailand - jhickey@hpcc.nectec.or.th
#   	    	Huidae Cho - Korea - grass4u@gmail.com
#   	    	Eric G. Miller - egm2@jps.net
# PURPOSE:  	The source file for this Makefile is in src/CMD/head/head.in.
#		It is the top part of a file called make.rules which is used
#		for compiling all GRASS modules. This part of the file provides
#		make variables that are dependent on the results of the
#		configure script.
# COPYRIGHT:    (C) 2000 by the GRASS Development Team
#
#               This program is free software under the GNU General Public
#   	    	License (>=v2). Read the file COPYING that comes with GRASS
#   	    	for details.
#
#############################################################################

############################## Make Variables ###############################

CC                  = gcc
CXX                 = c++
LEX                 = flex
YACC                = bison -y
PERL                = no
AR                  = ar
RANLIB              = ranlib
MKDIR               = mkdir -p
CHMOD               = chmod
INSTALL             = /usr/bin/install -c 
INSTALL_DATA        = ${INSTALL} -m 644

prefix              = /c/OSGeo4W64/apps/grass
exec_prefix         = ${prefix}
ARCH                = x86_64-w64-mingw32
UNIX_BIN            = /c/OSGeo4W64/bin
INST_DIR            = ${prefix}/grass-7.4.1

GRASS_HOME          = /c/OSGeo4W64/apps/grass/grass-7.4.1
RUN_GISBASE         = C:/msys64/usr/src/grass741/dist.x86_64-w64-mingw32

GRASS_VERSION_MAJOR = 7
GRASS_VERSION_MINOR = 4
GRASS_VERSION_RELEASE = 1
GRASS_VERSION_DATE  = 2018
GRASS_VERSION_SVN   = r72807

STRIPFLAG           = 
LD_SEARCH_FLAGS     = 
LD_LIBRARY_PATH_VAR = PATH

#generate static (ST) or shared (SH)
GRASS_LIBRARY_TYPE  = shlib

#static libs:
STLIB_LD            = ${AR} cr
STLIB_PREFIX        = lib
STLIB_SUFFIX        = .a

#shared libs
SHLIB_PREFIX        = lib
SHLIB_LD            = gcc -shared
SHLIB_LDFLAGS       = 
SHLIB_CFLAGS        = 
SHLIB_SUFFIX        = .dll
EXE                 = .exe

DEFAULT_DATABASE    =
DEFAULT_LOCATION    =

CPPFLAGS            =   -I/c/OSGeo4W64/include
CFLAGS              = -g -O2 
CXXFLAGS            = -g -O2
INCLUDE_DIRS        =  -I/c/OSGeo4W64/include
LINK_FLAGS          =  -L/c/msys64/usr/src/grass741/mswindows/osgeo4w/lib -lz -Wl,--export-dynamic,--enable-runtime-pseudo-reloc  -L/c/msys64/usr/src/grass741/mswindows/osgeo4w/lib

DLLIB               = 
XCFLAGS             = 
XLIBPATH            = 
XLIB                =  
XEXTRALIBS          = 
USE_X11             = 

MATHLIB             =  
ICONVLIB            = -liconv
INTLLIB             = -lintl
SOCKLIB             = 

#ZLIB:
ZLIB                =  -lz 
ZLIBINCPATH         = 
ZLIBLIBPATH         = 

#BZIP2:
BZLIB                =  -lbz2 
BZLIBINCPATH         = 
BZLIBLIBPATH         = 

DBMIEXTRALIB        = 

#readline
READLINEINCPATH     = 
READLINELIBPATH     = 
READLINELIB         = 
HISTORYLIB          = 

#PostgreSQL:
PQINCPATH           = 
PQLIBPATH           = 
PQLIB               =  -lpq 
USE_POSTGRES        = 1

#MySQL:
MYSQLINCPATH        = 
MYSQLLIBPATH        = 
MYSQLLIB            = 
MYSQLDLIB           = 

#SQLite:
SQLITEINCPATH       = 
SQLITELIBPATH       = 
SQLITELIB           =  -lsqlite3 

#ODBC:
ODBCINC             = 
ODBCLIB             =  -lodbc32 

#Image formats:
PNGINC              = 
PNGLIB              =  -lpng  -lz  
USE_PNG             = 1

TIFFINCPATH         = 
TIFFLIBPATH         = 
TIFFLIB             =  -ltiff 

#openGL files for NVIZ/r3.showdspf
OPENGLINC           = 
OPENGLLIB           =   -lopengl32 
OPENGLULIB          =   -lglu32 
OPENGL_X11          = 
OPENGL_AQUA         = 
OPENGL_WINDOWS      = 1
USE_OPENGL          = 1

#FFTW:
FFTWINC             = 
FFTWLIB             =  -lfftw3 

#LAPACK/BLAS stuff for gmath lib:
BLASLIB             = 
BLASINC             = 
LAPACKLIB           = 
LAPACKINC           = 

#GDAL/OGR
GDALLIBS            = /c/OSGeo4W64/lib/gdal_i.lib
GDALCFLAGS          = -I/c/OSGeo4W64/include
USE_GDAL            = 1
USE_OGR             = 1

#NetCDF
NETCDFLIBS          = 
NETCDFCFLAGS        =     
USE_NETCDF          = 

#LAS LiDAR through libLAS
LASLIBS             = /c/OSGeo4W64/lib/liblas_c.lib
LASCFLAGS           = 
LASINC              = -I/c/OSGeo4W64/include
USE_LIBLAS          = 1

#LAS LiDAR through PDAL
PDALLIBS             = 
PDALCPPFLAGS         = 
PDALINC              = 
USE_PDAL             = 

#GEOS
GEOSLIBS            =  -lgeos_c 
GEOSCFLAGS          = -I/c/OSGeo4W64/include
USE_GEOS            = 1

#FreeType:
FTINC               =  -I/c/OSGeo4W64/include/freetype2
FTLIB               =  -lfreetype 

#PROJ.4:
PROJINC             =  $(GDALCFLAGS)
PROJLIB             =  -lproj 
NAD2BIN             = /c/OSGeo4W64/bin/nad2bin
PROJSHARE           = /c/OSGeo4W64/share/proj

#OPENDWG:
OPENDWGINCPATH      = 
OPENDWGLIBPATH      = 
OPENDWGLIB          = 
USE_OPENDWG         = 

#cairo
CAIROINC                  = -mms-bitfields -IC:/msys64/mingw64/include/cairo -IC:/msys64/mingw64/include/pixman-1 -IC:/msys64/mingw64/include -I/mingw64/include/freetype2 -I/mingw64/include/libpng16 -I/mingw64/include/harfbuzz -I/mingw64/include/glib-2.0 -I/mingw64/lib/glib-2.0/include -IC:/msys64/mingw64/include -IC:/msys64/mingw64/include/freetype2 -IC:/msys64/mingw64/include -IC:/msys64/mingw64/include/libpng16 -IC:/msys64/mingw64/include/harfbuzz -IC:/msys64/mingw64/include/glib-2.0 -IC:/msys64/mingw64/lib/glib-2.0/include 
CAIROLIB                  = -LC:/msys64/mingw64/lib -lz -lcairo -lfontconfig -lfreetype   
USE_CAIRO                 = 1
CAIRO_HAS_XRENDER         = 
CAIRO_HAS_XRENDER_SURFACE = 

#Python
PYTHON              = python

#regex
REGEXINCPATH        = 
REGEXLIBPATH        = 
REGEXLIB            =  -lregex 
USE_REGEX           = 1

#pthreads
PTHREADINCPATH      = 
PTHREADLIBPATH      = 
PTHREADLIB          = 
USE_PTHREAD         = 

#OpenMP
OMPINCPATH          = 
OMPLIBPATH          = 
OMPLIB              = 
OMPCFLAGS           = 
USE_OPENMP          = 

#OpenCL
OCLINCPATH          = 
OCLLIBPATH          = 
OCLLIB              = 
USE_OPENCL          = 

#i18N
HAVE_NLS            = 1

#Large File Support (LFS)
USE_LARGEFILES      = 1
LFS_CFLAGS          = -D_FILE_OFFSET_BITS=64

#BSD sockets
HAVE_SOCKET         = 

MINGW		    = yes
MACOSX_APP	    = 
MACOSX_ARCHS        = 
MACOSX_SDK          = 

# Cross compilation
CROSS_COMPILING     =  
