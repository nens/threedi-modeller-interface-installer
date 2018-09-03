#-----------------------------------------------------------------------------
# HDF4 Config file for compiling against hdf4 install directory
#-----------------------------------------------------------------------------
GET_FILENAME_COMPONENT (SELF_DIR "${CMAKE_CURRENT_LIST_FILE}" PATH)
GET_FILENAME_COMPONENT(_IMPORT_PREFIX "${SELF_DIR}" PATH)
GET_FILENAME_COMPONENT(_IMPORT_PREFIX "${_IMPORT_PREFIX}" PATH)
IF (NOT WIN32)
  GET_FILENAME_COMPONENT(_IMPORT_PREFIX "${_IMPORT_PREFIX}" PATH)
ENDIF (NOT WIN32)

#-----------------------------------------------------------------------------
# User Options
#-----------------------------------------------------------------------------
SET (HDF4_ENABLE_PARALLEL OFF)
SET (HDF4_BUILD_FORTRAN   OFF)
SET (HDF4_BUILD_XDR_LIB   ON)
SET (HDF4_BUILD_TOOLS     OFF)
SET (HDF4_BUILD_UTILS     OFF)
SET (HDF4_ENABLE_JPEG_LIB_SUPPORT ON)
SET (HDF4_ENABLE_Z_LIB_SUPPORT ON)
SET (HDF4_ENABLE_SZIP_SUPPORT  OFF)
SET (HDF4_ENABLE_SZIP_ENCODING )
SET (HDF4_BUILD_SHARED_LIBS    OFF)
SET (HDF4_PACKAGE_EXTLIBS OFF)

#-----------------------------------------------------------------------------
# Directories
#-----------------------------------------------------------------------------
SET (HDF4_INCLUDE_DIR "${_IMPORT_PREFIX}/include")

IF (HDF4_BUILD_FORTRAN)
  SET (HDF4_INCLUDE_DIR_FORTRAN "${_IMPORT_PREFIX}/include")
ENDIF (HDF4_BUILD_FORTRAN)
  
IF (HDF4_BUILD_XDR_LIB)
  SET (HDF4_INCLUDE_DIR_XDR "${_IMPORT_PREFIX}/include")
ENDIF (HDF4_BUILD_XDR_LIB)

IF (HDF4_BUILD_TOOLS)
  SET (HDF4_INCLUDE_DIR_TOOLS "${_IMPORT_PREFIX}/include")
ENDIF (HDF4_BUILD_TOOLS)

IF (HDF4_BUILD_UTILS)
  SET (HDF4_INCLUDE_DIR_UTILS "${_IMPORT_PREFIX}/include")
  SET (HDF4_TOOLS_DIR "${_IMPORT_PREFIX}/bin" )
ENDIF (HDF4_BUILD_UTILS)

#-----------------------------------------------------------------------------
# Version Strings
#-----------------------------------------------------------------------------
SET (HDF4_VERSION_STRING 4.2.9)
SET (HDF4_VERSION_MAJOR  4.2)
SET (HDF4_VERSION_MINOR  9)

#-----------------------------------------------------------------------------
# Don't include targets if this file is being picked up by another
# project which has already built hdf4 as a subproject
#-----------------------------------------------------------------------------
IF (NOT TARGET "hdf4")
  IF (HDF4_ENABLE_JPEG_LIB_SUPPORT AND HDF4_PACKAGE_EXTLIBS AND NOT TARGET "jpeg")
    INCLUDE (${SELF_DIR}/../JPEG/-targets.cmake)
  ENDIF (HDF4_ENABLE_JPEG_LIB_SUPPORT AND HDF4_PACKAGE_EXTLIBS AND NOT TARGET "jpeg")
  IF (HDF4_ENABLE_Z_LIB_SUPPORT AND HDF4_PACKAGE_EXTLIBS AND NOT TARGET "zlib")
    INCLUDE (${SELF_DIR}/../ZLIB/-targets.cmake)
  ENDIF (HDF4_ENABLE_Z_LIB_SUPPORT AND HDF4_PACKAGE_EXTLIBS AND NOT TARGET "zlib")
  IF (HDF4_ENABLE_SZIP_SUPPORT AND HDF4_PACKAGE_EXTLIBS AND NOT TARGET "szip")
    INCLUDE (${SELF_DIR}/../SZIP/-targets.cmake)
  ENDIF (HDF4_ENABLE_SZIP_SUPPORT AND HDF4_PACKAGE_EXTLIBS AND NOT TARGET "szip")
  INCLUDE (${SELF_DIR}/hdf4-targets.cmake)
  SET (HDF4_LIBRARIES "xdr;hdf;mfhdf")
ENDIF (NOT TARGET "hdf4")
