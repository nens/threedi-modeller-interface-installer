#----------------------------------------------------------------
# Generated CMake target import file for configuration "Release".
#----------------------------------------------------------------

# Commands may need to know the format version.
set(CMAKE_IMPORT_FILE_VERSION 1)

# Import target "xdr" for configuration "Release"
set_property(TARGET xdr APPEND PROPERTY IMPORTED_CONFIGURATIONS RELEASE)
set_target_properties(xdr PROPERTIES
  IMPORTED_LINK_INTERFACE_LANGUAGES_RELEASE "C"
  IMPORTED_LINK_INTERFACE_LIBRARIES_RELEASE "ws2_32.lib"
  IMPORTED_LOCATION_RELEASE "${_IMPORT_PREFIX}/lib/xdr.lib"
  )

list(APPEND _IMPORT_CHECK_TARGETS xdr )
list(APPEND _IMPORT_CHECK_FILES_FOR_xdr "${_IMPORT_PREFIX}/lib/xdr.lib" )

# Import target "hdf" for configuration "Release"
set_property(TARGET hdf APPEND PROPERTY IMPORTED_CONFIGURATIONS RELEASE)
set_target_properties(hdf PROPERTIES
  IMPORTED_LINK_INTERFACE_LANGUAGES_RELEASE "C"
  IMPORTED_LINK_INTERFACE_LIBRARIES_RELEASE "C:/OSGeo4W64/lib/jpeg_i.lib;C:/OSGeo4W64/lib/zdll.lib"
  IMPORTED_LOCATION_RELEASE "${_IMPORT_PREFIX}/lib/hdf.lib"
  )

list(APPEND _IMPORT_CHECK_TARGETS hdf )
list(APPEND _IMPORT_CHECK_FILES_FOR_hdf "${_IMPORT_PREFIX}/lib/hdf.lib" )

# Import target "mfhdf" for configuration "Release"
set_property(TARGET mfhdf APPEND PROPERTY IMPORTED_CONFIGURATIONS RELEASE)
set_target_properties(mfhdf PROPERTIES
  IMPORTED_LINK_INTERFACE_LANGUAGES_RELEASE "C"
  IMPORTED_LINK_INTERFACE_LIBRARIES_RELEASE "xdr;hdf"
  IMPORTED_LOCATION_RELEASE "${_IMPORT_PREFIX}/lib/mfhdf.lib"
  )

list(APPEND _IMPORT_CHECK_TARGETS mfhdf )
list(APPEND _IMPORT_CHECK_FILES_FOR_mfhdf "${_IMPORT_PREFIX}/lib/mfhdf.lib" )

# Commands beyond this point should not need to know the version.
set(CMAKE_IMPORT_FILE_VERSION)
