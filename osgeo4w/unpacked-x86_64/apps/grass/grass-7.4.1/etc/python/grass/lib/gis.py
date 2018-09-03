'''Wrapper for gis.h

Generated with:
./ctypesgen.py --cpp gcc -E -I/c/OSGeo4W64/include -D_FILE_OFFSET_BITS=64     -I/c/msys64/usr/src/grass741/dist.x86_64-w64-mingw32/include -I/c/msys64/usr/src/grass741/dist.x86_64-w64-mingw32/include -D__GLIBC_HAVE_LONG_LONG -lgrass_gis.7.4.1 -lintl-8 C:/msys64/usr/src/grass741/dist.x86_64-w64-mingw32/include/grass/gis.h C:/msys64/usr/src/grass741/dist.x86_64-w64-mingw32/include/grass/defs/gis.h C:/msys64/usr/src/grass741/dist.x86_64-w64-mingw32/include/grass/colors.h C:/msys64/usr/src/grass741/dist.x86_64-w64-mingw32/include/grass/defs/colors.h -o OBJ.x86_64-w64-mingw32/gis.py

Do not modify this file.
'''

__docformat__ = 'restructuredtext'


_libs = {}
_libdirs = []

from .ctypes_preamble import *
from .ctypes_preamble import _variadic_function
from .ctypes_loader import *

add_library_search_dirs([])

# Begin libraries

_libs["grass_gis.7.4.1"] = load_library("grass_gis.7.4.1")
_libs["intl-8"] = load_library("intl-8")

# 2 libraries
# End libraries

# No modules

# C:/msys64/mingw64/x86_64-w64-mingw32/include/stdio.h: 26
class struct__iobuf(Structure):
    pass

struct__iobuf.__slots__ = [
    '_ptr',
    '_cnt',
    '_base',
    '_flag',
    '_file',
    '_charbuf',
    '_bufsiz',
    '_tmpfname',
]
struct__iobuf._fields_ = [
    ('_ptr', String),
    ('_cnt', c_int),
    ('_base', String),
    ('_flag', c_int),
    ('_file', c_int),
    ('_charbuf', c_int),
    ('_bufsiz', c_int),
    ('_tmpfname', String),
]

FILE = struct__iobuf # C:/msys64/mingw64/x86_64-w64-mingw32/include/stdio.h: 36

off_t = c_int64 # C:/msys64/mingw64/x86_64-w64-mingw32/include/_mingw_off_t.h: 24

# C:/msys64/usr/src/grass741/dist.x86_64-w64-mingw32/include/grass/datetime.h: 27
class struct_DateTime(Structure):
    pass

struct_DateTime.__slots__ = [
    'mode',
    '_from',
    'to',
    'fracsec',
    'year',
    'month',
    'day',
    'hour',
    'minute',
    'second',
    'positive',
    'tz',
]
struct_DateTime._fields_ = [
    ('mode', c_int),
    ('_from', c_int),
    ('to', c_int),
    ('fracsec', c_int),
    ('year', c_int),
    ('month', c_int),
    ('day', c_int),
    ('hour', c_int),
    ('minute', c_int),
    ('second', c_double),
    ('positive', c_int),
    ('tz', c_int),
]

DateTime = struct_DateTime # C:/msys64/usr/src/grass741/dist.x86_64-w64-mingw32/include/grass/datetime.h: 27

enum_anon_2 = c_int # C:\\msys64\\usr\\src\\grass741\\dist.x86_64-w64-mingw32\\include\\grass\\gis.h: 308

G_OPT_UNDEFINED = 0 # C:\\msys64\\usr\\src\\grass741\\dist.x86_64-w64-mingw32\\include\\grass\\gis.h: 308

G_OPT_DB_SQL = (G_OPT_UNDEFINED + 1) # C:\\msys64\\usr\\src\\grass741\\dist.x86_64-w64-mingw32\\include\\grass\\gis.h: 308

G_OPT_DB_WHERE = (G_OPT_DB_SQL + 1) # C:\\msys64\\usr\\src\\grass741\\dist.x86_64-w64-mingw32\\include\\grass\\gis.h: 308

G_OPT_DB_TABLE = (G_OPT_DB_WHERE + 1) # C:\\msys64\\usr\\src\\grass741\\dist.x86_64-w64-mingw32\\include\\grass\\gis.h: 308

G_OPT_DB_DRIVER = (G_OPT_DB_TABLE + 1) # C:\\msys64\\usr\\src\\grass741\\dist.x86_64-w64-mingw32\\include\\grass\\gis.h: 308

G_OPT_DB_DATABASE = (G_OPT_DB_DRIVER + 1) # C:\\msys64\\usr\\src\\grass741\\dist.x86_64-w64-mingw32\\include\\grass\\gis.h: 308

G_OPT_DB_SCHEMA = (G_OPT_DB_DATABASE + 1) # C:\\msys64\\usr\\src\\grass741\\dist.x86_64-w64-mingw32\\include\\grass\\gis.h: 308

G_OPT_DB_COLUMN = (G_OPT_DB_SCHEMA + 1) # C:\\msys64\\usr\\src\\grass741\\dist.x86_64-w64-mingw32\\include\\grass\\gis.h: 308

G_OPT_DB_COLUMNS = (G_OPT_DB_COLUMN + 1) # C:\\msys64\\usr\\src\\grass741\\dist.x86_64-w64-mingw32\\include\\grass\\gis.h: 308

G_OPT_DB_KEYCOLUMN = (G_OPT_DB_COLUMNS + 1) # C:\\msys64\\usr\\src\\grass741\\dist.x86_64-w64-mingw32\\include\\grass\\gis.h: 308

G_OPT_I_GROUP = (G_OPT_DB_KEYCOLUMN + 1) # C:\\msys64\\usr\\src\\grass741\\dist.x86_64-w64-mingw32\\include\\grass\\gis.h: 308

G_OPT_I_SUBGROUP = (G_OPT_I_GROUP + 1) # C:\\msys64\\usr\\src\\grass741\\dist.x86_64-w64-mingw32\\include\\grass\\gis.h: 308

G_OPT_R_INPUT = (G_OPT_I_SUBGROUP + 1) # C:\\msys64\\usr\\src\\grass741\\dist.x86_64-w64-mingw32\\include\\grass\\gis.h: 308

G_OPT_R_INPUTS = (G_OPT_R_INPUT + 1) # C:\\msys64\\usr\\src\\grass741\\dist.x86_64-w64-mingw32\\include\\grass\\gis.h: 308

G_OPT_R_OUTPUT = (G_OPT_R_INPUTS + 1) # C:\\msys64\\usr\\src\\grass741\\dist.x86_64-w64-mingw32\\include\\grass\\gis.h: 308

G_OPT_R_OUTPUTS = (G_OPT_R_OUTPUT + 1) # C:\\msys64\\usr\\src\\grass741\\dist.x86_64-w64-mingw32\\include\\grass\\gis.h: 308

G_OPT_R_MAP = (G_OPT_R_OUTPUTS + 1) # C:\\msys64\\usr\\src\\grass741\\dist.x86_64-w64-mingw32\\include\\grass\\gis.h: 308

G_OPT_R_MAPS = (G_OPT_R_MAP + 1) # C:\\msys64\\usr\\src\\grass741\\dist.x86_64-w64-mingw32\\include\\grass\\gis.h: 308

G_OPT_R_BASE = (G_OPT_R_MAPS + 1) # C:\\msys64\\usr\\src\\grass741\\dist.x86_64-w64-mingw32\\include\\grass\\gis.h: 308

G_OPT_R_COVER = (G_OPT_R_BASE + 1) # C:\\msys64\\usr\\src\\grass741\\dist.x86_64-w64-mingw32\\include\\grass\\gis.h: 308

G_OPT_R_ELEV = (G_OPT_R_COVER + 1) # C:\\msys64\\usr\\src\\grass741\\dist.x86_64-w64-mingw32\\include\\grass\\gis.h: 308

G_OPT_R_ELEVS = (G_OPT_R_ELEV + 1) # C:\\msys64\\usr\\src\\grass741\\dist.x86_64-w64-mingw32\\include\\grass\\gis.h: 308

G_OPT_R_TYPE = (G_OPT_R_ELEVS + 1) # C:\\msys64\\usr\\src\\grass741\\dist.x86_64-w64-mingw32\\include\\grass\\gis.h: 308

G_OPT_R_INTERP_TYPE = (G_OPT_R_TYPE + 1) # C:\\msys64\\usr\\src\\grass741\\dist.x86_64-w64-mingw32\\include\\grass\\gis.h: 308

G_OPT_R_BASENAME_INPUT = (G_OPT_R_INTERP_TYPE + 1) # C:\\msys64\\usr\\src\\grass741\\dist.x86_64-w64-mingw32\\include\\grass\\gis.h: 308

G_OPT_R_BASENAME_OUTPUT = (G_OPT_R_BASENAME_INPUT + 1) # C:\\msys64\\usr\\src\\grass741\\dist.x86_64-w64-mingw32\\include\\grass\\gis.h: 308

G_OPT_R3_INPUT = (G_OPT_R_BASENAME_OUTPUT + 1) # C:\\msys64\\usr\\src\\grass741\\dist.x86_64-w64-mingw32\\include\\grass\\gis.h: 308

G_OPT_R3_INPUTS = (G_OPT_R3_INPUT + 1) # C:\\msys64\\usr\\src\\grass741\\dist.x86_64-w64-mingw32\\include\\grass\\gis.h: 308

G_OPT_R3_OUTPUT = (G_OPT_R3_INPUTS + 1) # C:\\msys64\\usr\\src\\grass741\\dist.x86_64-w64-mingw32\\include\\grass\\gis.h: 308

G_OPT_R3_MAP = (G_OPT_R3_OUTPUT + 1) # C:\\msys64\\usr\\src\\grass741\\dist.x86_64-w64-mingw32\\include\\grass\\gis.h: 308

G_OPT_R3_MAPS = (G_OPT_R3_MAP + 1) # C:\\msys64\\usr\\src\\grass741\\dist.x86_64-w64-mingw32\\include\\grass\\gis.h: 308

G_OPT_R3_TYPE = (G_OPT_R3_MAPS + 1) # C:\\msys64\\usr\\src\\grass741\\dist.x86_64-w64-mingw32\\include\\grass\\gis.h: 308

G_OPT_R3_PRECISION = (G_OPT_R3_TYPE + 1) # C:\\msys64\\usr\\src\\grass741\\dist.x86_64-w64-mingw32\\include\\grass\\gis.h: 308

G_OPT_R3_TILE_DIMENSION = (G_OPT_R3_PRECISION + 1) # C:\\msys64\\usr\\src\\grass741\\dist.x86_64-w64-mingw32\\include\\grass\\gis.h: 308

G_OPT_R3_COMPRESSION = (G_OPT_R3_TILE_DIMENSION + 1) # C:\\msys64\\usr\\src\\grass741\\dist.x86_64-w64-mingw32\\include\\grass\\gis.h: 308

G_OPT_V_INPUT = (G_OPT_R3_COMPRESSION + 1) # C:\\msys64\\usr\\src\\grass741\\dist.x86_64-w64-mingw32\\include\\grass\\gis.h: 308

G_OPT_V_INPUTS = (G_OPT_V_INPUT + 1) # C:\\msys64\\usr\\src\\grass741\\dist.x86_64-w64-mingw32\\include\\grass\\gis.h: 308

G_OPT_V_OUTPUT = (G_OPT_V_INPUTS + 1) # C:\\msys64\\usr\\src\\grass741\\dist.x86_64-w64-mingw32\\include\\grass\\gis.h: 308

G_OPT_V_MAP = (G_OPT_V_OUTPUT + 1) # C:\\msys64\\usr\\src\\grass741\\dist.x86_64-w64-mingw32\\include\\grass\\gis.h: 308

G_OPT_V_MAPS = (G_OPT_V_MAP + 1) # C:\\msys64\\usr\\src\\grass741\\dist.x86_64-w64-mingw32\\include\\grass\\gis.h: 308

G_OPT_V_TYPE = (G_OPT_V_MAPS + 1) # C:\\msys64\\usr\\src\\grass741\\dist.x86_64-w64-mingw32\\include\\grass\\gis.h: 308

G_OPT_V3_TYPE = (G_OPT_V_TYPE + 1) # C:\\msys64\\usr\\src\\grass741\\dist.x86_64-w64-mingw32\\include\\grass\\gis.h: 308

G_OPT_V_FIELD = (G_OPT_V3_TYPE + 1) # C:\\msys64\\usr\\src\\grass741\\dist.x86_64-w64-mingw32\\include\\grass\\gis.h: 308

G_OPT_V_FIELD_ALL = (G_OPT_V_FIELD + 1) # C:\\msys64\\usr\\src\\grass741\\dist.x86_64-w64-mingw32\\include\\grass\\gis.h: 308

G_OPT_V_CAT = (G_OPT_V_FIELD_ALL + 1) # C:\\msys64\\usr\\src\\grass741\\dist.x86_64-w64-mingw32\\include\\grass\\gis.h: 308

G_OPT_V_CATS = (G_OPT_V_CAT + 1) # C:\\msys64\\usr\\src\\grass741\\dist.x86_64-w64-mingw32\\include\\grass\\gis.h: 308

G_OPT_V_ID = (G_OPT_V_CATS + 1) # C:\\msys64\\usr\\src\\grass741\\dist.x86_64-w64-mingw32\\include\\grass\\gis.h: 308

G_OPT_V_IDS = (G_OPT_V_ID + 1) # C:\\msys64\\usr\\src\\grass741\\dist.x86_64-w64-mingw32\\include\\grass\\gis.h: 308

G_OPT_F_INPUT = (G_OPT_V_IDS + 1) # C:\\msys64\\usr\\src\\grass741\\dist.x86_64-w64-mingw32\\include\\grass\\gis.h: 308

G_OPT_F_BIN_INPUT = (G_OPT_F_INPUT + 1) # C:\\msys64\\usr\\src\\grass741\\dist.x86_64-w64-mingw32\\include\\grass\\gis.h: 308

G_OPT_F_OUTPUT = (G_OPT_F_BIN_INPUT + 1) # C:\\msys64\\usr\\src\\grass741\\dist.x86_64-w64-mingw32\\include\\grass\\gis.h: 308

G_OPT_F_SEP = (G_OPT_F_OUTPUT + 1) # C:\\msys64\\usr\\src\\grass741\\dist.x86_64-w64-mingw32\\include\\grass\\gis.h: 308

G_OPT_C = (G_OPT_F_SEP + 1) # C:\\msys64\\usr\\src\\grass741\\dist.x86_64-w64-mingw32\\include\\grass\\gis.h: 308

G_OPT_CN = (G_OPT_C + 1) # C:\\msys64\\usr\\src\\grass741\\dist.x86_64-w64-mingw32\\include\\grass\\gis.h: 308

G_OPT_M_UNITS = (G_OPT_CN + 1) # C:\\msys64\\usr\\src\\grass741\\dist.x86_64-w64-mingw32\\include\\grass\\gis.h: 308

G_OPT_M_DATATYPE = (G_OPT_M_UNITS + 1) # C:\\msys64\\usr\\src\\grass741\\dist.x86_64-w64-mingw32\\include\\grass\\gis.h: 308

G_OPT_M_MAPSET = (G_OPT_M_DATATYPE + 1) # C:\\msys64\\usr\\src\\grass741\\dist.x86_64-w64-mingw32\\include\\grass\\gis.h: 308

G_OPT_M_LOCATION = (G_OPT_M_MAPSET + 1) # C:\\msys64\\usr\\src\\grass741\\dist.x86_64-w64-mingw32\\include\\grass\\gis.h: 308

G_OPT_M_DBASE = (G_OPT_M_LOCATION + 1) # C:\\msys64\\usr\\src\\grass741\\dist.x86_64-w64-mingw32\\include\\grass\\gis.h: 308

G_OPT_M_COORDS = (G_OPT_M_DBASE + 1) # C:\\msys64\\usr\\src\\grass741\\dist.x86_64-w64-mingw32\\include\\grass\\gis.h: 308

G_OPT_M_COLR = (G_OPT_M_COORDS + 1) # C:\\msys64\\usr\\src\\grass741\\dist.x86_64-w64-mingw32\\include\\grass\\gis.h: 308

G_OPT_M_DIR = (G_OPT_M_COLR + 1) # C:\\msys64\\usr\\src\\grass741\\dist.x86_64-w64-mingw32\\include\\grass\\gis.h: 308

G_OPT_M_REGION = (G_OPT_M_DIR + 1) # C:\\msys64\\usr\\src\\grass741\\dist.x86_64-w64-mingw32\\include\\grass\\gis.h: 308

G_OPT_M_NULL_VALUE = (G_OPT_M_REGION + 1) # C:\\msys64\\usr\\src\\grass741\\dist.x86_64-w64-mingw32\\include\\grass\\gis.h: 308

G_OPT_STDS_INPUT = (G_OPT_M_NULL_VALUE + 1) # C:\\msys64\\usr\\src\\grass741\\dist.x86_64-w64-mingw32\\include\\grass\\gis.h: 308

G_OPT_STDS_INPUTS = (G_OPT_STDS_INPUT + 1) # C:\\msys64\\usr\\src\\grass741\\dist.x86_64-w64-mingw32\\include\\grass\\gis.h: 308

G_OPT_STDS_OUTPUT = (G_OPT_STDS_INPUTS + 1) # C:\\msys64\\usr\\src\\grass741\\dist.x86_64-w64-mingw32\\include\\grass\\gis.h: 308

G_OPT_STRDS_INPUT = (G_OPT_STDS_OUTPUT + 1) # C:\\msys64\\usr\\src\\grass741\\dist.x86_64-w64-mingw32\\include\\grass\\gis.h: 308

G_OPT_STRDS_INPUTS = (G_OPT_STRDS_INPUT + 1) # C:\\msys64\\usr\\src\\grass741\\dist.x86_64-w64-mingw32\\include\\grass\\gis.h: 308

G_OPT_STRDS_OUTPUT = (G_OPT_STRDS_INPUTS + 1) # C:\\msys64\\usr\\src\\grass741\\dist.x86_64-w64-mingw32\\include\\grass\\gis.h: 308

G_OPT_STR3DS_INPUT = (G_OPT_STRDS_OUTPUT + 1) # C:\\msys64\\usr\\src\\grass741\\dist.x86_64-w64-mingw32\\include\\grass\\gis.h: 308

G_OPT_STR3DS_INPUTS = (G_OPT_STR3DS_INPUT + 1) # C:\\msys64\\usr\\src\\grass741\\dist.x86_64-w64-mingw32\\include\\grass\\gis.h: 308

G_OPT_STR3DS_OUTPUT = (G_OPT_STR3DS_INPUTS + 1) # C:\\msys64\\usr\\src\\grass741\\dist.x86_64-w64-mingw32\\include\\grass\\gis.h: 308

G_OPT_STVDS_INPUT = (G_OPT_STR3DS_OUTPUT + 1) # C:\\msys64\\usr\\src\\grass741\\dist.x86_64-w64-mingw32\\include\\grass\\gis.h: 308

G_OPT_STVDS_INPUTS = (G_OPT_STVDS_INPUT + 1) # C:\\msys64\\usr\\src\\grass741\\dist.x86_64-w64-mingw32\\include\\grass\\gis.h: 308

G_OPT_STVDS_OUTPUT = (G_OPT_STVDS_INPUTS + 1) # C:\\msys64\\usr\\src\\grass741\\dist.x86_64-w64-mingw32\\include\\grass\\gis.h: 308

G_OPT_MAP_INPUT = (G_OPT_STVDS_OUTPUT + 1) # C:\\msys64\\usr\\src\\grass741\\dist.x86_64-w64-mingw32\\include\\grass\\gis.h: 308

G_OPT_MAP_INPUTS = (G_OPT_MAP_INPUT + 1) # C:\\msys64\\usr\\src\\grass741\\dist.x86_64-w64-mingw32\\include\\grass\\gis.h: 308

G_OPT_STDS_TYPE = (G_OPT_MAP_INPUTS + 1) # C:\\msys64\\usr\\src\\grass741\\dist.x86_64-w64-mingw32\\include\\grass\\gis.h: 308

G_OPT_MAP_TYPE = (G_OPT_STDS_TYPE + 1) # C:\\msys64\\usr\\src\\grass741\\dist.x86_64-w64-mingw32\\include\\grass\\gis.h: 308

G_OPT_T_TYPE = (G_OPT_MAP_TYPE + 1) # C:\\msys64\\usr\\src\\grass741\\dist.x86_64-w64-mingw32\\include\\grass\\gis.h: 308

G_OPT_T_WHERE = (G_OPT_T_TYPE + 1) # C:\\msys64\\usr\\src\\grass741\\dist.x86_64-w64-mingw32\\include\\grass\\gis.h: 308

G_OPT_T_SAMPLE = (G_OPT_T_WHERE + 1) # C:\\msys64\\usr\\src\\grass741\\dist.x86_64-w64-mingw32\\include\\grass\\gis.h: 308

STD_OPT = enum_anon_2 # C:\\msys64\\usr\\src\\grass741\\dist.x86_64-w64-mingw32\\include\\grass\\gis.h: 308

enum_anon_3 = c_int # C:\\msys64\\usr\\src\\grass741\\dist.x86_64-w64-mingw32\\include\\grass\\gis.h: 324

G_FLG_UNDEFINED = 0 # C:\\msys64\\usr\\src\\grass741\\dist.x86_64-w64-mingw32\\include\\grass\\gis.h: 324

G_FLG_V_TABLE = (G_FLG_UNDEFINED + 1) # C:\\msys64\\usr\\src\\grass741\\dist.x86_64-w64-mingw32\\include\\grass\\gis.h: 324

G_FLG_V_TOPO = (G_FLG_V_TABLE + 1) # C:\\msys64\\usr\\src\\grass741\\dist.x86_64-w64-mingw32\\include\\grass\\gis.h: 324

STD_FLG = enum_anon_3 # C:\\msys64\\usr\\src\\grass741\\dist.x86_64-w64-mingw32\\include\\grass\\gis.h: 324

enum_rule_type = c_int # C:\\msys64\\usr\\src\\grass741\\dist.x86_64-w64-mingw32\\include\\grass\\gis.h: 327

RULE_EXCLUSIVE = 0 # C:\\msys64\\usr\\src\\grass741\\dist.x86_64-w64-mingw32\\include\\grass\\gis.h: 327

RULE_REQUIRED = (RULE_EXCLUSIVE + 1) # C:\\msys64\\usr\\src\\grass741\\dist.x86_64-w64-mingw32\\include\\grass\\gis.h: 327

RULE_REQUIRES = (RULE_REQUIRED + 1) # C:\\msys64\\usr\\src\\grass741\\dist.x86_64-w64-mingw32\\include\\grass\\gis.h: 327

RULE_REQUIRES_ALL = (RULE_REQUIRES + 1) # C:\\msys64\\usr\\src\\grass741\\dist.x86_64-w64-mingw32\\include\\grass\\gis.h: 327

RULE_EXCLUDES = (RULE_REQUIRES_ALL + 1) # C:\\msys64\\usr\\src\\grass741\\dist.x86_64-w64-mingw32\\include\\grass\\gis.h: 327

RULE_COLLECTIVE = (RULE_EXCLUDES + 1) # C:\\msys64\\usr\\src\\grass741\\dist.x86_64-w64-mingw32\\include\\grass\\gis.h: 327

enum_anon_4 = c_int # C:\\msys64\\usr\\src\\grass741\\dist.x86_64-w64-mingw32\\include\\grass\\gis.h: 374

G_ELEMENT_RASTER = 1 # C:\\msys64\\usr\\src\\grass741\\dist.x86_64-w64-mingw32\\include\\grass\\gis.h: 374

G_ELEMENT_RASTER3D = 2 # C:\\msys64\\usr\\src\\grass741\\dist.x86_64-w64-mingw32\\include\\grass\\gis.h: 374

G_ELEMENT_VECTOR = 3 # C:\\msys64\\usr\\src\\grass741\\dist.x86_64-w64-mingw32\\include\\grass\\gis.h: 374

G_ELEMENT_ASCIIVECTOR = 4 # C:\\msys64\\usr\\src\\grass741\\dist.x86_64-w64-mingw32\\include\\grass\\gis.h: 374

G_ELEMENT_LABEL = 5 # C:\\msys64\\usr\\src\\grass741\\dist.x86_64-w64-mingw32\\include\\grass\\gis.h: 374

G_ELEMENT_REGION = 6 # C:\\msys64\\usr\\src\\grass741\\dist.x86_64-w64-mingw32\\include\\grass\\gis.h: 374

G_ELEMENT_GROUP = 7 # C:\\msys64\\usr\\src\\grass741\\dist.x86_64-w64-mingw32\\include\\grass\\gis.h: 374

# C:\\msys64\\usr\\src\\grass741\\dist.x86_64-w64-mingw32\\include\\grass\\gis.h: 390
class struct_Cell_head(Structure):
    pass

struct_Cell_head.__slots__ = [
    'format',
    'compressed',
    'rows',
    'rows3',
    'cols',
    'cols3',
    'depths',
    'proj',
    'zone',
    'ew_res',
    'ew_res3',
    'ns_res',
    'ns_res3',
    'tb_res',
    'north',
    'south',
    'east',
    'west',
    'top',
    'bottom',
]
struct_Cell_head._fields_ = [
    ('format', c_int),
    ('compressed', c_int),
    ('rows', c_int),
    ('rows3', c_int),
    ('cols', c_int),
    ('cols3', c_int),
    ('depths', c_int),
    ('proj', c_int),
    ('zone', c_int),
    ('ew_res', c_double),
    ('ew_res3', c_double),
    ('ns_res', c_double),
    ('ns_res3', c_double),
    ('tb_res', c_double),
    ('north', c_double),
    ('south', c_double),
    ('east', c_double),
    ('west', c_double),
    ('top', c_double),
    ('bottom', c_double),
]

# C:\\msys64\\usr\\src\\grass741\\dist.x86_64-w64-mingw32\\include\\grass\\gis.h: 452
class struct_G_3dview(Structure):
    pass

struct_G_3dview.__slots__ = [
    'pgm_id',
    'from_to',
    'fov',
    'twist',
    'exag',
    'mesh_freq',
    'poly_freq',
    'display_type',
    'lightson',
    'dozero',
    'colorgrid',
    'shading',
    'fringe',
    'surfonly',
    'doavg',
    'grid_col',
    'bg_col',
    'other_col',
    'lightpos',
    'lightcol',
    'ambient',
    'shine',
    'vwin',
]
struct_G_3dview._fields_ = [
    ('pgm_id', c_char * 40),
    ('from_to', (c_float * 3) * 2),
    ('fov', c_float),
    ('twist', c_float),
    ('exag', c_float),
    ('mesh_freq', c_int),
    ('poly_freq', c_int),
    ('display_type', c_int),
    ('lightson', c_int),
    ('dozero', c_int),
    ('colorgrid', c_int),
    ('shading', c_int),
    ('fringe', c_int),
    ('surfonly', c_int),
    ('doavg', c_int),
    ('grid_col', c_char * 40),
    ('bg_col', c_char * 40),
    ('other_col', c_char * 40),
    ('lightpos', c_float * 4),
    ('lightcol', c_float * 3),
    ('ambient', c_float),
    ('shine', c_float),
    ('vwin', struct_Cell_head),
]

# C:\\msys64\\usr\\src\\grass741\\dist.x86_64-w64-mingw32\\include\\grass\\gis.h: 479
class struct_Key_Value(Structure):
    pass

struct_Key_Value.__slots__ = [
    'nitems',
    'nalloc',
    'key',
    'value',
]
struct_Key_Value._fields_ = [
    ('nitems', c_int),
    ('nalloc', c_int),
    ('key', POINTER(POINTER(c_char))),
    ('value', POINTER(POINTER(c_char))),
]

# C:\\msys64\\usr\\src\\grass741\\dist.x86_64-w64-mingw32\\include\\grass\\gis.h: 509
class struct_Option(Structure):
    pass

struct_Option.__slots__ = [
    'key',
    'type',
    'required',
    'multiple',
    'options',
    'opts',
    'key_desc',
    'label',
    'description',
    'descriptions',
    'descs',
    'answer',
    '_def',
    'answers',
    'next_opt',
    'gisprompt',
    'guisection',
    'guidependency',
    'checker',
    'count',
]
struct_Option._fields_ = [
    ('key', String),
    ('type', c_int),
    ('required', c_int),
    ('multiple', c_int),
    ('options', String),
    ('opts', POINTER(POINTER(c_char))),
    ('key_desc', String),
    ('label', String),
    ('description', String),
    ('descriptions', String),
    ('descs', POINTER(POINTER(c_char))),
    ('answer', String),
    ('_def', String),
    ('answers', POINTER(POINTER(c_char))),
    ('next_opt', POINTER(struct_Option)),
    ('gisprompt', String),
    ('guisection', String),
    ('guidependency', String),
    ('checker', CFUNCTYPE(UNCHECKED(c_int), String)),
    ('count', c_int),
]

# C:\\msys64\\usr\\src\\grass741\\dist.x86_64-w64-mingw32\\include\\grass\\gis.h: 538
class struct_Flag(Structure):
    pass

struct_Flag.__slots__ = [
    'key',
    'answer',
    'suppress_required',
    'suppress_overwrite',
    'label',
    'description',
    'guisection',
    'next_flag',
]
struct_Flag._fields_ = [
    ('key', c_char),
    ('answer', c_char),
    ('suppress_required', c_char),
    ('suppress_overwrite', c_char),
    ('label', String),
    ('description', String),
    ('guisection', String),
    ('next_flag', POINTER(struct_Flag)),
]

# C:\\msys64\\usr\\src\\grass741\\dist.x86_64-w64-mingw32\\include\\grass\\gis.h: 555
class struct_GModule(Structure):
    pass

struct_GModule.__slots__ = [
    'label',
    'description',
    'keywords',
    'overwrite',
    'verbose',
]
struct_GModule._fields_ = [
    ('label', String),
    ('description', String),
    ('keywords', POINTER(POINTER(c_char))),
    ('overwrite', c_int),
    ('verbose', c_int),
]

# C:\\msys64\\usr\\src\\grass741\\dist.x86_64-w64-mingw32\\include\\grass\\gis.h: 565
class struct_TimeStamp(Structure):
    pass

struct_TimeStamp.__slots__ = [
    'dt',
    'count',
]
struct_TimeStamp._fields_ = [
    ('dt', DateTime * 2),
    ('count', c_int),
]

# C:\\msys64\\usr\\src\\grass741\\dist.x86_64-w64-mingw32\\include\\grass\\gis.h: 571
class struct_Counter(Structure):
    pass

struct_Counter.__slots__ = [
    'value',
]
struct_Counter._fields_ = [
    ('value', c_int),
]

# C:\\msys64\\usr\\src\\grass741\\dist.x86_64-w64-mingw32\\include\\grass\\gis.h: 575
class struct_Popen(Structure):
    pass

struct_Popen.__slots__ = [
    'fp',
    'pid',
]
struct_Popen._fields_ = [
    ('fp', POINTER(FILE)),
    ('pid', c_int),
]

CELL = c_int # C:\\msys64\\usr\\src\\grass741\\dist.x86_64-w64-mingw32\\include\\grass\\gis.h: 580

DCELL = c_double # C:\\msys64\\usr\\src\\grass741\\dist.x86_64-w64-mingw32\\include\\grass\\gis.h: 581

FCELL = c_float # C:\\msys64\\usr\\src\\grass741\\dist.x86_64-w64-mingw32\\include\\grass\\gis.h: 582

# C:\\msys64\\usr\\src\\grass741\\dist.x86_64-w64-mingw32\\include\\grass\\gis.h: 584
class struct__Color_Value_(Structure):
    pass

struct__Color_Value_.__slots__ = [
    'value',
    'red',
    'grn',
    'blu',
]
struct__Color_Value_._fields_ = [
    ('value', DCELL),
    ('red', c_ubyte),
    ('grn', c_ubyte),
    ('blu', c_ubyte),
]

# C:\\msys64\\usr\\src\\grass741\\dist.x86_64-w64-mingw32\\include\\grass\\gis.h: 592
class struct__Color_Rule_(Structure):
    pass

struct__Color_Rule_.__slots__ = [
    'low',
    'high',
    'next',
    'prev',
]
struct__Color_Rule_._fields_ = [
    ('low', struct__Color_Value_),
    ('high', struct__Color_Value_),
    ('next', POINTER(struct__Color_Rule_)),
    ('prev', POINTER(struct__Color_Rule_)),
]

# C:\\msys64\\usr\\src\\grass741\\dist.x86_64-w64-mingw32\\include\\grass\\gis.h: 604
class struct_anon_5(Structure):
    pass

struct_anon_5.__slots__ = [
    'red',
    'grn',
    'blu',
    'set',
    'nalloc',
    'active',
]
struct_anon_5._fields_ = [
    ('red', POINTER(c_ubyte)),
    ('grn', POINTER(c_ubyte)),
    ('blu', POINTER(c_ubyte)),
    ('set', POINTER(c_ubyte)),
    ('nalloc', c_int),
    ('active', c_int),
]

# C:\\msys64\\usr\\src\\grass741\\dist.x86_64-w64-mingw32\\include\\grass\\gis.h: 614
class struct_anon_6(Structure):
    pass

struct_anon_6.__slots__ = [
    'vals',
    'rules',
    'nalloc',
    'active',
]
struct_anon_6._fields_ = [
    ('vals', POINTER(DCELL)),
    ('rules', POINTER(POINTER(struct__Color_Rule_))),
    ('nalloc', c_int),
    ('active', c_int),
]

# C:\\msys64\\usr\\src\\grass741\\dist.x86_64-w64-mingw32\\include\\grass\\gis.h: 599
class struct__Color_Info_(Structure):
    pass

struct__Color_Info_.__slots__ = [
    'rules',
    'n_rules',
    'lookup',
    'fp_lookup',
    'min',
    'max',
]
struct__Color_Info_._fields_ = [
    ('rules', POINTER(struct__Color_Rule_)),
    ('n_rules', c_int),
    ('lookup', struct_anon_5),
    ('fp_lookup', struct_anon_6),
    ('min', DCELL),
    ('max', DCELL),
]

# C:\\msys64\\usr\\src\\grass741\\dist.x86_64-w64-mingw32\\include\\grass\\gis.h: 626
class struct_Colors(Structure):
    pass

struct_Colors.__slots__ = [
    'version',
    'shift',
    'invert',
    'is_float',
    'null_set',
    'null_red',
    'null_grn',
    'null_blu',
    'undef_set',
    'undef_red',
    'undef_grn',
    'undef_blu',
    'fixed',
    'modular',
    'cmin',
    'cmax',
    'organizing',
]
struct_Colors._fields_ = [
    ('version', c_int),
    ('shift', DCELL),
    ('invert', c_int),
    ('is_float', c_int),
    ('null_set', c_int),
    ('null_red', c_ubyte),
    ('null_grn', c_ubyte),
    ('null_blu', c_ubyte),
    ('undef_set', c_int),
    ('undef_red', c_ubyte),
    ('undef_grn', c_ubyte),
    ('undef_blu', c_ubyte),
    ('fixed', struct__Color_Info_),
    ('modular', struct__Color_Info_),
    ('cmin', DCELL),
    ('cmax', DCELL),
    ('organizing', c_int),
]

# C:\\msys64\\usr\\src\\grass741\\dist.x86_64-w64-mingw32\\include\\grass\\gis.h: 650
class struct_ilist(Structure):
    pass

struct_ilist.__slots__ = [
    'value',
    'n_values',
    'alloc_values',
]
struct_ilist._fields_ = [
    ('value', POINTER(c_int)),
    ('n_values', c_int),
    ('alloc_values', c_int),
]

# C:/msys64/usr/src/grass741/dist.x86_64-w64-mingw32/include/grass/defs/gis.h: 95
if hasattr(_libs['grass_gis.7.4.1'], 'G_adjust_Cell_head'):
    G_adjust_Cell_head = _libs['grass_gis.7.4.1'].G_adjust_Cell_head
    G_adjust_Cell_head.restype = None
    G_adjust_Cell_head.argtypes = [POINTER(struct_Cell_head), c_int, c_int]

# C:/msys64/usr/src/grass741/dist.x86_64-w64-mingw32/include/grass/defs/gis.h: 96
if hasattr(_libs['grass_gis.7.4.1'], 'G_adjust_Cell_head3'):
    G_adjust_Cell_head3 = _libs['grass_gis.7.4.1'].G_adjust_Cell_head3
    G_adjust_Cell_head3.restype = None
    G_adjust_Cell_head3.argtypes = [POINTER(struct_Cell_head), c_int, c_int, c_int]

# C:/msys64/usr/src/grass741/dist.x86_64-w64-mingw32/include/grass/defs/gis.h: 97
if hasattr(_libs['grass_gis.7.4.1'], 'G_adjust_window_ll'):
    G_adjust_window_ll = _libs['grass_gis.7.4.1'].G_adjust_window_ll
    G_adjust_window_ll.restype = c_int
    G_adjust_window_ll.argtypes = [POINTER(struct_Cell_head)]

# C:/msys64/usr/src/grass741/dist.x86_64-w64-mingw32/include/grass/defs/gis.h: 103
if hasattr(_libs['grass_gis.7.4.1'], 'G__malloc'):
    G__malloc = _libs['grass_gis.7.4.1'].G__malloc
    G__malloc.restype = POINTER(None)
    G__malloc.argtypes = [String, c_int, c_size_t]

# C:/msys64/usr/src/grass741/dist.x86_64-w64-mingw32/include/grass/defs/gis.h: 104
if hasattr(_libs['grass_gis.7.4.1'], 'G__calloc'):
    G__calloc = _libs['grass_gis.7.4.1'].G__calloc
    G__calloc.restype = POINTER(None)
    G__calloc.argtypes = [String, c_int, c_size_t, c_size_t]

# C:/msys64/usr/src/grass741/dist.x86_64-w64-mingw32/include/grass/defs/gis.h: 105
if hasattr(_libs['grass_gis.7.4.1'], 'G__realloc'):
    G__realloc = _libs['grass_gis.7.4.1'].G__realloc
    G__realloc.restype = POINTER(None)
    G__realloc.argtypes = [String, c_int, POINTER(None), c_size_t]

# C:/msys64/usr/src/grass741/dist.x86_64-w64-mingw32/include/grass/defs/gis.h: 106
if hasattr(_libs['grass_gis.7.4.1'], 'G_free'):
    G_free = _libs['grass_gis.7.4.1'].G_free
    G_free.restype = None
    G_free.argtypes = [POINTER(None)]

# C:/msys64/usr/src/grass741/dist.x86_64-w64-mingw32/include/grass/defs/gis.h: 122
if hasattr(_libs['grass_gis.7.4.1'], 'G_begin_cell_area_calculations'):
    G_begin_cell_area_calculations = _libs['grass_gis.7.4.1'].G_begin_cell_area_calculations
    G_begin_cell_area_calculations.restype = c_int
    G_begin_cell_area_calculations.argtypes = []

# C:/msys64/usr/src/grass741/dist.x86_64-w64-mingw32/include/grass/defs/gis.h: 123
if hasattr(_libs['grass_gis.7.4.1'], 'G_area_of_cell_at_row'):
    G_area_of_cell_at_row = _libs['grass_gis.7.4.1'].G_area_of_cell_at_row
    G_area_of_cell_at_row.restype = c_double
    G_area_of_cell_at_row.argtypes = [c_int]

# C:/msys64/usr/src/grass741/dist.x86_64-w64-mingw32/include/grass/defs/gis.h: 124
if hasattr(_libs['grass_gis.7.4.1'], 'G_begin_polygon_area_calculations'):
    G_begin_polygon_area_calculations = _libs['grass_gis.7.4.1'].G_begin_polygon_area_calculations
    G_begin_polygon_area_calculations.restype = c_int
    G_begin_polygon_area_calculations.argtypes = []

# C:/msys64/usr/src/grass741/dist.x86_64-w64-mingw32/include/grass/defs/gis.h: 125
if hasattr(_libs['grass_gis.7.4.1'], 'G_area_of_polygon'):
    G_area_of_polygon = _libs['grass_gis.7.4.1'].G_area_of_polygon
    G_area_of_polygon.restype = c_double
    G_area_of_polygon.argtypes = [POINTER(c_double), POINTER(c_double), c_int]

# C:/msys64/usr/src/grass741/dist.x86_64-w64-mingw32/include/grass/defs/gis.h: 128
if hasattr(_libs['grass_gis.7.4.1'], 'G_begin_zone_area_on_ellipsoid'):
    G_begin_zone_area_on_ellipsoid = _libs['grass_gis.7.4.1'].G_begin_zone_area_on_ellipsoid
    G_begin_zone_area_on_ellipsoid.restype = None
    G_begin_zone_area_on_ellipsoid.argtypes = [c_double, c_double, c_double]

# C:/msys64/usr/src/grass741/dist.x86_64-w64-mingw32/include/grass/defs/gis.h: 129
if hasattr(_libs['grass_gis.7.4.1'], 'G_darea0_on_ellipsoid'):
    G_darea0_on_ellipsoid = _libs['grass_gis.7.4.1'].G_darea0_on_ellipsoid
    G_darea0_on_ellipsoid.restype = c_double
    G_darea0_on_ellipsoid.argtypes = [c_double]

# C:/msys64/usr/src/grass741/dist.x86_64-w64-mingw32/include/grass/defs/gis.h: 130
if hasattr(_libs['grass_gis.7.4.1'], 'G_area_for_zone_on_ellipsoid'):
    G_area_for_zone_on_ellipsoid = _libs['grass_gis.7.4.1'].G_area_for_zone_on_ellipsoid
    G_area_for_zone_on_ellipsoid.restype = c_double
    G_area_for_zone_on_ellipsoid.argtypes = [c_double, c_double]

# C:/msys64/usr/src/grass741/dist.x86_64-w64-mingw32/include/grass/defs/gis.h: 133
if hasattr(_libs['grass_gis.7.4.1'], 'G_begin_ellipsoid_polygon_area'):
    G_begin_ellipsoid_polygon_area = _libs['grass_gis.7.4.1'].G_begin_ellipsoid_polygon_area
    G_begin_ellipsoid_polygon_area.restype = None
    G_begin_ellipsoid_polygon_area.argtypes = [c_double, c_double]

# C:/msys64/usr/src/grass741/dist.x86_64-w64-mingw32/include/grass/defs/gis.h: 134
if hasattr(_libs['grass_gis.7.4.1'], 'G_ellipsoid_polygon_area'):
    G_ellipsoid_polygon_area = _libs['grass_gis.7.4.1'].G_ellipsoid_polygon_area
    G_ellipsoid_polygon_area.restype = c_double
    G_ellipsoid_polygon_area.argtypes = [POINTER(c_double), POINTER(c_double), c_int]

# C:/msys64/usr/src/grass741/dist.x86_64-w64-mingw32/include/grass/defs/gis.h: 137
if hasattr(_libs['grass_gis.7.4.1'], 'G_planimetric_polygon_area'):
    G_planimetric_polygon_area = _libs['grass_gis.7.4.1'].G_planimetric_polygon_area
    G_planimetric_polygon_area.restype = c_double
    G_planimetric_polygon_area.argtypes = [POINTER(c_double), POINTER(c_double), c_int]

# C:/msys64/usr/src/grass741/dist.x86_64-w64-mingw32/include/grass/defs/gis.h: 140
if hasattr(_libs['grass_gis.7.4.1'], 'G_begin_zone_area_on_sphere'):
    G_begin_zone_area_on_sphere = _libs['grass_gis.7.4.1'].G_begin_zone_area_on_sphere
    G_begin_zone_area_on_sphere.restype = None
    G_begin_zone_area_on_sphere.argtypes = [c_double, c_double]

# C:/msys64/usr/src/grass741/dist.x86_64-w64-mingw32/include/grass/defs/gis.h: 141
if hasattr(_libs['grass_gis.7.4.1'], 'G_darea0_on_sphere'):
    G_darea0_on_sphere = _libs['grass_gis.7.4.1'].G_darea0_on_sphere
    G_darea0_on_sphere.restype = c_double
    G_darea0_on_sphere.argtypes = [c_double]

# C:/msys64/usr/src/grass741/dist.x86_64-w64-mingw32/include/grass/defs/gis.h: 142
if hasattr(_libs['grass_gis.7.4.1'], 'G_area_for_zone_on_sphere'):
    G_area_for_zone_on_sphere = _libs['grass_gis.7.4.1'].G_area_for_zone_on_sphere
    G_area_for_zone_on_sphere.restype = c_double
    G_area_for_zone_on_sphere.argtypes = [c_double, c_double]

# C:/msys64/usr/src/grass741/dist.x86_64-w64-mingw32/include/grass/defs/gis.h: 145
if hasattr(_libs['grass_gis.7.4.1'], 'G_ascii_check'):
    G_ascii_check = _libs['grass_gis.7.4.1'].G_ascii_check
    G_ascii_check.restype = None
    G_ascii_check.argtypes = [String]

# C:/msys64/usr/src/grass741/dist.x86_64-w64-mingw32/include/grass/defs/gis.h: 158
if hasattr(_libs['grass_gis.7.4.1'], 'G_asprintf'):
    _func = _libs['grass_gis.7.4.1'].G_asprintf
    _restype = c_int
    _argtypes = [POINTER(POINTER(c_char)), String]
    G_asprintf = _variadic_function(_func,_restype,_argtypes)

# C:/msys64/usr/src/grass741/dist.x86_64-w64-mingw32/include/grass/defs/gis.h: 161
if hasattr(_libs['grass_gis.7.4.1'], 'G_rasprintf'):
    _func = _libs['grass_gis.7.4.1'].G_rasprintf
    _restype = c_int
    _argtypes = [POINTER(POINTER(c_char)), POINTER(c_size_t), String]
    G_rasprintf = _variadic_function(_func,_restype,_argtypes)

# C:/msys64/usr/src/grass741/dist.x86_64-w64-mingw32/include/grass/defs/gis.h: 165
if hasattr(_libs['grass_gis.7.4.1'], 'G_basename'):
    G_basename = _libs['grass_gis.7.4.1'].G_basename
    G_basename.restype = ReturnString
    G_basename.argtypes = [String, String]

# C:/msys64/usr/src/grass741/dist.x86_64-w64-mingw32/include/grass/defs/gis.h: 166
if hasattr(_libs['grass_gis.7.4.1'], 'G_get_num_decimals'):
    G_get_num_decimals = _libs['grass_gis.7.4.1'].G_get_num_decimals
    G_get_num_decimals.restype = c_size_t
    G_get_num_decimals.argtypes = [String]

# C:/msys64/usr/src/grass741/dist.x86_64-w64-mingw32/include/grass/defs/gis.h: 167
if hasattr(_libs['grass_gis.7.4.1'], 'G_double_to_basename_format'):
    G_double_to_basename_format = _libs['grass_gis.7.4.1'].G_double_to_basename_format
    G_double_to_basename_format.restype = ReturnString
    G_double_to_basename_format.argtypes = [c_double, c_size_t, c_size_t]

# C:/msys64/usr/src/grass741/dist.x86_64-w64-mingw32/include/grass/defs/gis.h: 168
if hasattr(_libs['grass_gis.7.4.1'], 'G_get_basename_separator'):
    G_get_basename_separator = _libs['grass_gis.7.4.1'].G_get_basename_separator
    G_get_basename_separator.restype = ReturnString
    G_get_basename_separator.argtypes = []

# C:/msys64/usr/src/grass741/dist.x86_64-w64-mingw32/include/grass/defs/gis.h: 169
if hasattr(_libs['grass_gis.7.4.1'], 'G_join_basename_strings'):
    G_join_basename_strings = _libs['grass_gis.7.4.1'].G_join_basename_strings
    G_join_basename_strings.restype = ReturnString
    G_join_basename_strings.argtypes = [POINTER(POINTER(c_char)), c_size_t]

# C:/msys64/usr/src/grass741/dist.x86_64-w64-mingw32/include/grass/defs/gis.h: 170
if hasattr(_libs['grass_gis.7.4.1'], 'G_generate_basename'):
    G_generate_basename = _libs['grass_gis.7.4.1'].G_generate_basename
    G_generate_basename.restype = ReturnString
    G_generate_basename.argtypes = [String, c_double, c_size_t, c_size_t]

# C:/msys64/usr/src/grass741/dist.x86_64-w64-mingw32/include/grass/defs/gis.h: 173
if hasattr(_libs['grass_gis.7.4.1'], 'G_bresenham_line'):
    G_bresenham_line = _libs['grass_gis.7.4.1'].G_bresenham_line
    G_bresenham_line.restype = None
    G_bresenham_line.argtypes = [c_int, c_int, c_int, c_int, CFUNCTYPE(UNCHECKED(c_int), c_int, c_int)]

# C:/msys64/usr/src/grass741/dist.x86_64-w64-mingw32/include/grass/defs/gis.h: 176
if hasattr(_libs['grass_gis.7.4.1'], 'G_clicker'):
    G_clicker = _libs['grass_gis.7.4.1'].G_clicker
    G_clicker.restype = None
    G_clicker.argtypes = []

# C:/msys64/usr/src/grass741/dist.x86_64-w64-mingw32/include/grass/defs/gis.h: 179
if hasattr(_libs['grass_gis.7.4.1'], 'G_color_rules_options'):
    G_color_rules_options = _libs['grass_gis.7.4.1'].G_color_rules_options
    G_color_rules_options.restype = ReturnString
    G_color_rules_options.argtypes = []

# C:/msys64/usr/src/grass741/dist.x86_64-w64-mingw32/include/grass/defs/gis.h: 180
if hasattr(_libs['grass_gis.7.4.1'], 'G_color_rules_descriptions'):
    G_color_rules_descriptions = _libs['grass_gis.7.4.1'].G_color_rules_descriptions
    G_color_rules_descriptions.restype = ReturnString
    G_color_rules_descriptions.argtypes = []

# C:/msys64/usr/src/grass741/dist.x86_64-w64-mingw32/include/grass/defs/gis.h: 181
if hasattr(_libs['grass_gis.7.4.1'], 'G_list_color_rules'):
    G_list_color_rules = _libs['grass_gis.7.4.1'].G_list_color_rules
    G_list_color_rules.restype = None
    G_list_color_rules.argtypes = [POINTER(FILE)]

# C:/msys64/usr/src/grass741/dist.x86_64-w64-mingw32/include/grass/defs/gis.h: 182
if hasattr(_libs['grass_gis.7.4.1'], 'G_find_color_rule'):
    G_find_color_rule = _libs['grass_gis.7.4.1'].G_find_color_rule
    G_find_color_rule.restype = c_int
    G_find_color_rule.argtypes = [String]

# C:/msys64/usr/src/grass741/dist.x86_64-w64-mingw32/include/grass/defs/gis.h: 185
if hasattr(_libs['grass_gis.7.4.1'], 'G_num_standard_colors'):
    G_num_standard_colors = _libs['grass_gis.7.4.1'].G_num_standard_colors
    G_num_standard_colors.restype = c_int
    G_num_standard_colors.argtypes = []

# C:/msys64/usr/src/grass741/dist.x86_64-w64-mingw32/include/grass/defs/gis.h: 188
if hasattr(_libs['grass_gis.7.4.1'], 'G_insert_commas'):
    G_insert_commas = _libs['grass_gis.7.4.1'].G_insert_commas
    G_insert_commas.restype = c_int
    G_insert_commas.argtypes = [String]

# C:/msys64/usr/src/grass741/dist.x86_64-w64-mingw32/include/grass/defs/gis.h: 189
if hasattr(_libs['grass_gis.7.4.1'], 'G_remove_commas'):
    G_remove_commas = _libs['grass_gis.7.4.1'].G_remove_commas
    G_remove_commas.restype = None
    G_remove_commas.argtypes = [String]

# C:/msys64/usr/src/grass741/dist.x86_64-w64-mingw32/include/grass/defs/gis.h: 192
if hasattr(_libs['grass_gis.7.4.1'], 'G_compressor_number'):
    G_compressor_number = _libs['grass_gis.7.4.1'].G_compressor_number
    G_compressor_number.restype = c_int
    G_compressor_number.argtypes = [String]

# C:/msys64/usr/src/grass741/dist.x86_64-w64-mingw32/include/grass/defs/gis.h: 193
if hasattr(_libs['grass_gis.7.4.1'], 'G_compressor_name'):
    G_compressor_name = _libs['grass_gis.7.4.1'].G_compressor_name
    G_compressor_name.restype = ReturnString
    G_compressor_name.argtypes = [c_int]

# C:/msys64/usr/src/grass741/dist.x86_64-w64-mingw32/include/grass/defs/gis.h: 194
if hasattr(_libs['grass_gis.7.4.1'], 'G_check_compressor'):
    G_check_compressor = _libs['grass_gis.7.4.1'].G_check_compressor
    G_check_compressor.restype = c_int
    G_check_compressor.argtypes = [c_int]

# C:/msys64/usr/src/grass741/dist.x86_64-w64-mingw32/include/grass/defs/gis.h: 195
if hasattr(_libs['grass_gis.7.4.1'], 'G_write_compressed'):
    G_write_compressed = _libs['grass_gis.7.4.1'].G_write_compressed
    G_write_compressed.restype = c_int
    G_write_compressed.argtypes = [c_int, POINTER(c_ubyte), c_int, c_int]

# C:/msys64/usr/src/grass741/dist.x86_64-w64-mingw32/include/grass/defs/gis.h: 196
for _lib in _libs.values():
    if hasattr(_lib, 'G_write_unompressed'):
        G_write_unompressed = _lib.G_write_unompressed
        G_write_unompressed.restype = c_int
        G_write_unompressed.argtypes = [c_int, POINTER(c_ubyte), c_int]
        break

# C:/msys64/usr/src/grass741/dist.x86_64-w64-mingw32/include/grass/defs/gis.h: 197
if hasattr(_libs['grass_gis.7.4.1'], 'G_read_compressed'):
    G_read_compressed = _libs['grass_gis.7.4.1'].G_read_compressed
    G_read_compressed.restype = c_int
    G_read_compressed.argtypes = [c_int, c_int, POINTER(c_ubyte), c_int, c_int]

# C:/msys64/usr/src/grass741/dist.x86_64-w64-mingw32/include/grass/defs/gis.h: 198
if hasattr(_libs['grass_gis.7.4.1'], 'G_compress'):
    G_compress = _libs['grass_gis.7.4.1'].G_compress
    G_compress.restype = c_int
    G_compress.argtypes = [POINTER(c_ubyte), c_int, POINTER(c_ubyte), c_int, c_int]

# C:/msys64/usr/src/grass741/dist.x86_64-w64-mingw32/include/grass/defs/gis.h: 199
if hasattr(_libs['grass_gis.7.4.1'], 'G_expand'):
    G_expand = _libs['grass_gis.7.4.1'].G_expand
    G_expand.restype = c_int
    G_expand.argtypes = [POINTER(c_ubyte), c_int, POINTER(c_ubyte), c_int, c_int]

# C:/msys64/usr/src/grass741/dist.x86_64-w64-mingw32/include/grass/defs/gis.h: 203
if hasattr(_libs['grass_gis.7.4.1'], 'G_no_compress'):
    G_no_compress = _libs['grass_gis.7.4.1'].G_no_compress
    G_no_compress.restype = c_int
    G_no_compress.argtypes = [POINTER(c_ubyte), c_int, POINTER(c_ubyte), c_int]

# C:/msys64/usr/src/grass741/dist.x86_64-w64-mingw32/include/grass/defs/gis.h: 206
if hasattr(_libs['grass_gis.7.4.1'], 'G_no_expand'):
    G_no_expand = _libs['grass_gis.7.4.1'].G_no_expand
    G_no_expand.restype = c_int
    G_no_expand.argtypes = [POINTER(c_ubyte), c_int, POINTER(c_ubyte), c_int]

# C:/msys64/usr/src/grass741/dist.x86_64-w64-mingw32/include/grass/defs/gis.h: 211
if hasattr(_libs['grass_gis.7.4.1'], 'G_rle_compress'):
    G_rle_compress = _libs['grass_gis.7.4.1'].G_rle_compress
    G_rle_compress.restype = c_int
    G_rle_compress.argtypes = [POINTER(c_ubyte), c_int, POINTER(c_ubyte), c_int]

# C:/msys64/usr/src/grass741/dist.x86_64-w64-mingw32/include/grass/defs/gis.h: 214
if hasattr(_libs['grass_gis.7.4.1'], 'G_rle_expand'):
    G_rle_expand = _libs['grass_gis.7.4.1'].G_rle_expand
    G_rle_expand.restype = c_int
    G_rle_expand.argtypes = [POINTER(c_ubyte), c_int, POINTER(c_ubyte), c_int]

# C:/msys64/usr/src/grass741/dist.x86_64-w64-mingw32/include/grass/defs/gis.h: 219
if hasattr(_libs['grass_gis.7.4.1'], 'G_zlib_compress'):
    G_zlib_compress = _libs['grass_gis.7.4.1'].G_zlib_compress
    G_zlib_compress.restype = c_int
    G_zlib_compress.argtypes = [POINTER(c_ubyte), c_int, POINTER(c_ubyte), c_int]

# C:/msys64/usr/src/grass741/dist.x86_64-w64-mingw32/include/grass/defs/gis.h: 222
if hasattr(_libs['grass_gis.7.4.1'], 'G_zlib_expand'):
    G_zlib_expand = _libs['grass_gis.7.4.1'].G_zlib_expand
    G_zlib_expand.restype = c_int
    G_zlib_expand.argtypes = [POINTER(c_ubyte), c_int, POINTER(c_ubyte), c_int]

# C:/msys64/usr/src/grass741/dist.x86_64-w64-mingw32/include/grass/defs/gis.h: 227
if hasattr(_libs['grass_gis.7.4.1'], 'G_lz4_compress'):
    G_lz4_compress = _libs['grass_gis.7.4.1'].G_lz4_compress
    G_lz4_compress.restype = c_int
    G_lz4_compress.argtypes = [POINTER(c_ubyte), c_int, POINTER(c_ubyte), c_int]

# C:/msys64/usr/src/grass741/dist.x86_64-w64-mingw32/include/grass/defs/gis.h: 230
if hasattr(_libs['grass_gis.7.4.1'], 'G_lz4_expand'):
    G_lz4_expand = _libs['grass_gis.7.4.1'].G_lz4_expand
    G_lz4_expand.restype = c_int
    G_lz4_expand.argtypes = [POINTER(c_ubyte), c_int, POINTER(c_ubyte), c_int]

# C:/msys64/usr/src/grass741/dist.x86_64-w64-mingw32/include/grass/defs/gis.h: 235
if hasattr(_libs['grass_gis.7.4.1'], 'G_bz2_compress'):
    G_bz2_compress = _libs['grass_gis.7.4.1'].G_bz2_compress
    G_bz2_compress.restype = c_int
    G_bz2_compress.argtypes = [POINTER(c_ubyte), c_int, POINTER(c_ubyte), c_int]

# C:/msys64/usr/src/grass741/dist.x86_64-w64-mingw32/include/grass/defs/gis.h: 238
if hasattr(_libs['grass_gis.7.4.1'], 'G_bz2_expand'):
    G_bz2_expand = _libs['grass_gis.7.4.1'].G_bz2_expand
    G_bz2_expand.restype = c_int
    G_bz2_expand.argtypes = [POINTER(c_ubyte), c_int, POINTER(c_ubyte), c_int]

# C:/msys64/usr/src/grass741/dist.x86_64-w64-mingw32/include/grass/defs/gis.h: 244
if hasattr(_libs['grass_gis.7.4.1'], 'G_recursive_copy'):
    G_recursive_copy = _libs['grass_gis.7.4.1'].G_recursive_copy
    G_recursive_copy.restype = c_int
    G_recursive_copy.argtypes = [String, String]

# C:/msys64/usr/src/grass741/dist.x86_64-w64-mingw32/include/grass/defs/gis.h: 247
if hasattr(_libs['grass_gis.7.4.1'], 'G_copy_file'):
    G_copy_file = _libs['grass_gis.7.4.1'].G_copy_file
    G_copy_file.restype = c_int
    G_copy_file.argtypes = [String, String]

# C:/msys64/usr/src/grass741/dist.x86_64-w64-mingw32/include/grass/defs/gis.h: 250
if hasattr(_libs['grass_gis.7.4.1'], 'G_is_initialized'):
    G_is_initialized = _libs['grass_gis.7.4.1'].G_is_initialized
    G_is_initialized.restype = c_int
    G_is_initialized.argtypes = [POINTER(c_int)]

# C:/msys64/usr/src/grass741/dist.x86_64-w64-mingw32/include/grass/defs/gis.h: 251
if hasattr(_libs['grass_gis.7.4.1'], 'G_initialize_done'):
    G_initialize_done = _libs['grass_gis.7.4.1'].G_initialize_done
    G_initialize_done.restype = None
    G_initialize_done.argtypes = [POINTER(c_int)]

# C:/msys64/usr/src/grass741/dist.x86_64-w64-mingw32/include/grass/defs/gis.h: 252
if hasattr(_libs['grass_gis.7.4.1'], 'G_init_counter'):
    G_init_counter = _libs['grass_gis.7.4.1'].G_init_counter
    G_init_counter.restype = None
    G_init_counter.argtypes = [POINTER(struct_Counter), c_int]

# C:/msys64/usr/src/grass741/dist.x86_64-w64-mingw32/include/grass/defs/gis.h: 253
if hasattr(_libs['grass_gis.7.4.1'], 'G_counter_next'):
    G_counter_next = _libs['grass_gis.7.4.1'].G_counter_next
    G_counter_next.restype = c_int
    G_counter_next.argtypes = [POINTER(struct_Counter)]

# C:/msys64/usr/src/grass741/dist.x86_64-w64-mingw32/include/grass/defs/gis.h: 256
if hasattr(_libs['grass_gis.7.4.1'], 'G_date'):
    G_date = _libs['grass_gis.7.4.1'].G_date
    G_date.restype = ReturnString
    G_date.argtypes = []

# C:/msys64/usr/src/grass741/dist.x86_64-w64-mingw32/include/grass/defs/gis.h: 259
if hasattr(_libs['grass_gis.7.4.1'], 'G_get_datum_by_name'):
    G_get_datum_by_name = _libs['grass_gis.7.4.1'].G_get_datum_by_name
    G_get_datum_by_name.restype = c_int
    G_get_datum_by_name.argtypes = [String]

# C:/msys64/usr/src/grass741/dist.x86_64-w64-mingw32/include/grass/defs/gis.h: 260
if hasattr(_libs['grass_gis.7.4.1'], 'G_datum_name'):
    G_datum_name = _libs['grass_gis.7.4.1'].G_datum_name
    G_datum_name.restype = ReturnString
    G_datum_name.argtypes = [c_int]

# C:/msys64/usr/src/grass741/dist.x86_64-w64-mingw32/include/grass/defs/gis.h: 261
if hasattr(_libs['grass_gis.7.4.1'], 'G_datum_description'):
    G_datum_description = _libs['grass_gis.7.4.1'].G_datum_description
    G_datum_description.restype = ReturnString
    G_datum_description.argtypes = [c_int]

# C:/msys64/usr/src/grass741/dist.x86_64-w64-mingw32/include/grass/defs/gis.h: 262
if hasattr(_libs['grass_gis.7.4.1'], 'G_datum_ellipsoid'):
    G_datum_ellipsoid = _libs['grass_gis.7.4.1'].G_datum_ellipsoid
    G_datum_ellipsoid.restype = ReturnString
    G_datum_ellipsoid.argtypes = [c_int]

# C:/msys64/usr/src/grass741/dist.x86_64-w64-mingw32/include/grass/defs/gis.h: 263
if hasattr(_libs['grass_gis.7.4.1'], 'G_get_datumparams_from_projinfo'):
    G_get_datumparams_from_projinfo = _libs['grass_gis.7.4.1'].G_get_datumparams_from_projinfo
    G_get_datumparams_from_projinfo.restype = c_int
    G_get_datumparams_from_projinfo.argtypes = [POINTER(struct_Key_Value), String, String]

# C:/msys64/usr/src/grass741/dist.x86_64-w64-mingw32/include/grass/defs/gis.h: 264
if hasattr(_libs['grass_gis.7.4.1'], 'G_read_datum_table'):
    G_read_datum_table = _libs['grass_gis.7.4.1'].G_read_datum_table
    G_read_datum_table.restype = None
    G_read_datum_table.argtypes = []

# C:/msys64/usr/src/grass741/dist.x86_64-w64-mingw32/include/grass/defs/gis.h: 268
if hasattr(_libs['grass_gis.7.4.1'], 'G_init_debug'):
    G_init_debug = _libs['grass_gis.7.4.1'].G_init_debug
    G_init_debug.restype = None
    G_init_debug.argtypes = []

# C:/msys64/usr/src/grass741/dist.x86_64-w64-mingw32/include/grass/defs/gis.h: 269
if hasattr(_libs['grass_gis.7.4.1'], 'G_debug'):
    _func = _libs['grass_gis.7.4.1'].G_debug
    _restype = c_int
    _argtypes = [c_int, String]
    G_debug = _variadic_function(_func,_restype,_argtypes)

# C:/msys64/usr/src/grass741/dist.x86_64-w64-mingw32/include/grass/defs/gis.h: 272
if hasattr(_libs['grass_gis.7.4.1'], 'G_begin_distance_calculations'):
    G_begin_distance_calculations = _libs['grass_gis.7.4.1'].G_begin_distance_calculations
    G_begin_distance_calculations.restype = c_int
    G_begin_distance_calculations.argtypes = []

# C:/msys64/usr/src/grass741/dist.x86_64-w64-mingw32/include/grass/defs/gis.h: 273
if hasattr(_libs['grass_gis.7.4.1'], 'G_distance'):
    G_distance = _libs['grass_gis.7.4.1'].G_distance
    G_distance.restype = c_double
    G_distance.argtypes = [c_double, c_double, c_double, c_double]

# C:/msys64/usr/src/grass741/dist.x86_64-w64-mingw32/include/grass/defs/gis.h: 274
if hasattr(_libs['grass_gis.7.4.1'], 'G_distance_between_line_segments'):
    G_distance_between_line_segments = _libs['grass_gis.7.4.1'].G_distance_between_line_segments
    G_distance_between_line_segments.restype = c_double
    G_distance_between_line_segments.argtypes = [c_double, c_double, c_double, c_double, c_double, c_double, c_double, c_double]

# C:/msys64/usr/src/grass741/dist.x86_64-w64-mingw32/include/grass/defs/gis.h: 276
if hasattr(_libs['grass_gis.7.4.1'], 'G_distance_point_to_line_segment'):
    G_distance_point_to_line_segment = _libs['grass_gis.7.4.1'].G_distance_point_to_line_segment
    G_distance_point_to_line_segment.restype = c_double
    G_distance_point_to_line_segment.argtypes = [c_double, c_double, c_double, c_double, c_double, c_double]

# C:/msys64/usr/src/grass741/dist.x86_64-w64-mingw32/include/grass/defs/gis.h: 280
if hasattr(_libs['grass_gis.7.4.1'], 'G_done_msg'):
    _func = _libs['grass_gis.7.4.1'].G_done_msg
    _restype = None
    _argtypes = [String]
    G_done_msg = _variadic_function(_func,_restype,_argtypes)

# C:/msys64/usr/src/grass741/dist.x86_64-w64-mingw32/include/grass/defs/gis.h: 283
if hasattr(_libs['grass_gis.7.4.1'], 'G_is_little_endian'):
    G_is_little_endian = _libs['grass_gis.7.4.1'].G_is_little_endian
    G_is_little_endian.restype = c_int
    G_is_little_endian.argtypes = []

# C:/msys64/usr/src/grass741/dist.x86_64-w64-mingw32/include/grass/defs/gis.h: 286
if hasattr(_libs['grass_gis.7.4.1'], 'G_init_env'):
    G_init_env = _libs['grass_gis.7.4.1'].G_init_env
    G_init_env.restype = None
    G_init_env.argtypes = []

# C:/msys64/usr/src/grass741/dist.x86_64-w64-mingw32/include/grass/defs/gis.h: 287
if hasattr(_libs['grass_gis.7.4.1'], 'G_getenv'):
    G_getenv = _libs['grass_gis.7.4.1'].G_getenv
    G_getenv.restype = ReturnString
    G_getenv.argtypes = [String]

# C:/msys64/usr/src/grass741/dist.x86_64-w64-mingw32/include/grass/defs/gis.h: 288
if hasattr(_libs['grass_gis.7.4.1'], 'G_getenv2'):
    G_getenv2 = _libs['grass_gis.7.4.1'].G_getenv2
    G_getenv2.restype = ReturnString
    G_getenv2.argtypes = [String, c_int]

# C:/msys64/usr/src/grass741/dist.x86_64-w64-mingw32/include/grass/defs/gis.h: 289
if hasattr(_libs['grass_gis.7.4.1'], 'G_getenv_nofatal'):
    G_getenv_nofatal = _libs['grass_gis.7.4.1'].G_getenv_nofatal
    G_getenv_nofatal.restype = ReturnString
    G_getenv_nofatal.argtypes = [String]

# C:/msys64/usr/src/grass741/dist.x86_64-w64-mingw32/include/grass/defs/gis.h: 290
if hasattr(_libs['grass_gis.7.4.1'], 'G_getenv_nofatal2'):
    G_getenv_nofatal2 = _libs['grass_gis.7.4.1'].G_getenv_nofatal2
    G_getenv_nofatal2.restype = ReturnString
    G_getenv_nofatal2.argtypes = [String, c_int]

# C:/msys64/usr/src/grass741/dist.x86_64-w64-mingw32/include/grass/defs/gis.h: 291
if hasattr(_libs['grass_gis.7.4.1'], 'G_setenv'):
    G_setenv = _libs['grass_gis.7.4.1'].G_setenv
    G_setenv.restype = None
    G_setenv.argtypes = [String, String]

# C:/msys64/usr/src/grass741/dist.x86_64-w64-mingw32/include/grass/defs/gis.h: 292
if hasattr(_libs['grass_gis.7.4.1'], 'G_setenv2'):
    G_setenv2 = _libs['grass_gis.7.4.1'].G_setenv2
    G_setenv2.restype = None
    G_setenv2.argtypes = [String, String, c_int]

# C:/msys64/usr/src/grass741/dist.x86_64-w64-mingw32/include/grass/defs/gis.h: 293
if hasattr(_libs['grass_gis.7.4.1'], 'G_setenv_nogisrc'):
    G_setenv_nogisrc = _libs['grass_gis.7.4.1'].G_setenv_nogisrc
    G_setenv_nogisrc.restype = None
    G_setenv_nogisrc.argtypes = [String, String]

# C:/msys64/usr/src/grass741/dist.x86_64-w64-mingw32/include/grass/defs/gis.h: 294
if hasattr(_libs['grass_gis.7.4.1'], 'G_setenv_nogisrc2'):
    G_setenv_nogisrc2 = _libs['grass_gis.7.4.1'].G_setenv_nogisrc2
    G_setenv_nogisrc2.restype = None
    G_setenv_nogisrc2.argtypes = [String, String, c_int]

# C:/msys64/usr/src/grass741/dist.x86_64-w64-mingw32/include/grass/defs/gis.h: 295
if hasattr(_libs['grass_gis.7.4.1'], 'G_unsetenv'):
    G_unsetenv = _libs['grass_gis.7.4.1'].G_unsetenv
    G_unsetenv.restype = None
    G_unsetenv.argtypes = [String]

# C:/msys64/usr/src/grass741/dist.x86_64-w64-mingw32/include/grass/defs/gis.h: 296
if hasattr(_libs['grass_gis.7.4.1'], 'G_unsetenv2'):
    G_unsetenv2 = _libs['grass_gis.7.4.1'].G_unsetenv2
    G_unsetenv2.restype = None
    G_unsetenv2.argtypes = [String, c_int]

# C:/msys64/usr/src/grass741/dist.x86_64-w64-mingw32/include/grass/defs/gis.h: 297
if hasattr(_libs['grass_gis.7.4.1'], 'G_get_env_name'):
    G_get_env_name = _libs['grass_gis.7.4.1'].G_get_env_name
    G_get_env_name.restype = ReturnString
    G_get_env_name.argtypes = [c_int]

# C:/msys64/usr/src/grass741/dist.x86_64-w64-mingw32/include/grass/defs/gis.h: 298
if hasattr(_libs['grass_gis.7.4.1'], 'G_set_gisrc_mode'):
    G_set_gisrc_mode = _libs['grass_gis.7.4.1'].G_set_gisrc_mode
    G_set_gisrc_mode.restype = None
    G_set_gisrc_mode.argtypes = [c_int]

# C:/msys64/usr/src/grass741/dist.x86_64-w64-mingw32/include/grass/defs/gis.h: 299
if hasattr(_libs['grass_gis.7.4.1'], 'G_get_gisrc_mode'):
    G_get_gisrc_mode = _libs['grass_gis.7.4.1'].G_get_gisrc_mode
    G_get_gisrc_mode.restype = c_int
    G_get_gisrc_mode.argtypes = []

# C:/msys64/usr/src/grass741/dist.x86_64-w64-mingw32/include/grass/defs/gis.h: 300
if hasattr(_libs['grass_gis.7.4.1'], 'G_create_alt_env'):
    G_create_alt_env = _libs['grass_gis.7.4.1'].G_create_alt_env
    G_create_alt_env.restype = None
    G_create_alt_env.argtypes = []

# C:/msys64/usr/src/grass741/dist.x86_64-w64-mingw32/include/grass/defs/gis.h: 301
if hasattr(_libs['grass_gis.7.4.1'], 'G_switch_env'):
    G_switch_env = _libs['grass_gis.7.4.1'].G_switch_env
    G_switch_env.restype = None
    G_switch_env.argtypes = []

# C:/msys64/usr/src/grass741/dist.x86_64-w64-mingw32/include/grass/defs/gis.h: 302
if hasattr(_libs['grass_gis.7.4.1'], 'G__read_mapset_env'):
    G__read_mapset_env = _libs['grass_gis.7.4.1'].G__read_mapset_env
    G__read_mapset_env.restype = None
    G__read_mapset_env.argtypes = []

# C:/msys64/usr/src/grass741/dist.x86_64-w64-mingw32/include/grass/defs/gis.h: 303
if hasattr(_libs['grass_gis.7.4.1'], 'G__read_gisrc_env'):
    G__read_gisrc_env = _libs['grass_gis.7.4.1'].G__read_gisrc_env
    G__read_gisrc_env.restype = None
    G__read_gisrc_env.argtypes = []

# C:/msys64/usr/src/grass741/dist.x86_64-w64-mingw32/include/grass/defs/gis.h: 310
if hasattr(_libs['grass_gis.7.4.1'], 'G_info_format'):
    G_info_format = _libs['grass_gis.7.4.1'].G_info_format
    G_info_format.restype = c_int
    G_info_format.argtypes = []

# C:/msys64/usr/src/grass741/dist.x86_64-w64-mingw32/include/grass/defs/gis.h: 311
if hasattr(_libs['grass_gis.7.4.1'], 'G_message'):
    _func = _libs['grass_gis.7.4.1'].G_message
    _restype = None
    _argtypes = [String]
    G_message = _variadic_function(_func,_restype,_argtypes)

# C:/msys64/usr/src/grass741/dist.x86_64-w64-mingw32/include/grass/defs/gis.h: 312
if hasattr(_libs['grass_gis.7.4.1'], 'G_verbose_message'):
    _func = _libs['grass_gis.7.4.1'].G_verbose_message
    _restype = None
    _argtypes = [String]
    G_verbose_message = _variadic_function(_func,_restype,_argtypes)

# C:/msys64/usr/src/grass741/dist.x86_64-w64-mingw32/include/grass/defs/gis.h: 314
if hasattr(_libs['grass_gis.7.4.1'], 'G_important_message'):
    _func = _libs['grass_gis.7.4.1'].G_important_message
    _restype = None
    _argtypes = [String]
    G_important_message = _variadic_function(_func,_restype,_argtypes)

# C:/msys64/usr/src/grass741/dist.x86_64-w64-mingw32/include/grass/defs/gis.h: 316
if hasattr(_libs['grass_gis.7.4.1'], 'G_fatal_error'):
    _func = _libs['grass_gis.7.4.1'].G_fatal_error
    _restype = None
    _argtypes = [String]
    G_fatal_error = _variadic_function(_func,_restype,_argtypes)

# C:/msys64/usr/src/grass741/dist.x86_64-w64-mingw32/include/grass/defs/gis.h: 318
if hasattr(_libs['grass_gis.7.4.1'], 'G_warning'):
    _func = _libs['grass_gis.7.4.1'].G_warning
    _restype = None
    _argtypes = [String]
    G_warning = _variadic_function(_func,_restype,_argtypes)

# C:/msys64/usr/src/grass741/dist.x86_64-w64-mingw32/include/grass/defs/gis.h: 319
if hasattr(_libs['grass_gis.7.4.1'], 'G_suppress_warnings'):
    G_suppress_warnings = _libs['grass_gis.7.4.1'].G_suppress_warnings
    G_suppress_warnings.restype = c_int
    G_suppress_warnings.argtypes = [c_int]

# C:/msys64/usr/src/grass741/dist.x86_64-w64-mingw32/include/grass/defs/gis.h: 320
if hasattr(_libs['grass_gis.7.4.1'], 'G_sleep_on_error'):
    G_sleep_on_error = _libs['grass_gis.7.4.1'].G_sleep_on_error
    G_sleep_on_error.restype = c_int
    G_sleep_on_error.argtypes = [c_int]

# C:/msys64/usr/src/grass741/dist.x86_64-w64-mingw32/include/grass/defs/gis.h: 321
if hasattr(_libs['grass_gis.7.4.1'], 'G_set_error_routine'):
    G_set_error_routine = _libs['grass_gis.7.4.1'].G_set_error_routine
    G_set_error_routine.restype = None
    G_set_error_routine.argtypes = [CFUNCTYPE(UNCHECKED(c_int), String, c_int)]

# C:/msys64/usr/src/grass741/dist.x86_64-w64-mingw32/include/grass/defs/gis.h: 322
if hasattr(_libs['grass_gis.7.4.1'], 'G_unset_error_routine'):
    G_unset_error_routine = _libs['grass_gis.7.4.1'].G_unset_error_routine
    G_unset_error_routine.restype = None
    G_unset_error_routine.argtypes = []

# C:/msys64/usr/src/grass741/dist.x86_64-w64-mingw32/include/grass/defs/gis.h: 323
if hasattr(_libs['grass_gis.7.4.1'], 'G_init_logging'):
    G_init_logging = _libs['grass_gis.7.4.1'].G_init_logging
    G_init_logging.restype = None
    G_init_logging.argtypes = []

# C:/msys64/usr/src/grass741/dist.x86_64-w64-mingw32/include/grass/defs/gis.h: 326
if hasattr(_libs['grass_gis.7.4.1'], 'G_file_name'):
    G_file_name = _libs['grass_gis.7.4.1'].G_file_name
    G_file_name.restype = ReturnString
    G_file_name.argtypes = [String, String, String, String]

# C:/msys64/usr/src/grass741/dist.x86_64-w64-mingw32/include/grass/defs/gis.h: 327
if hasattr(_libs['grass_gis.7.4.1'], 'G_file_name_misc'):
    G_file_name_misc = _libs['grass_gis.7.4.1'].G_file_name_misc
    G_file_name_misc.restype = ReturnString
    G_file_name_misc.argtypes = [String, String, String, String, String]

# C:/msys64/usr/src/grass741/dist.x86_64-w64-mingw32/include/grass/defs/gis.h: 329
if hasattr(_libs['grass_gis.7.4.1'], 'G_file_name_tmp'):
    G_file_name_tmp = _libs['grass_gis.7.4.1'].G_file_name_tmp
    G_file_name_tmp.restype = ReturnString
    G_file_name_tmp.argtypes = [String, String, String, String]

# C:/msys64/usr/src/grass741/dist.x86_64-w64-mingw32/include/grass/defs/gis.h: 332
if hasattr(_libs['grass_gis.7.4.1'], 'G_find_file'):
    G_find_file = _libs['grass_gis.7.4.1'].G_find_file
    G_find_file.restype = ReturnString
    G_find_file.argtypes = [String, String, String]

# C:/msys64/usr/src/grass741/dist.x86_64-w64-mingw32/include/grass/defs/gis.h: 333
if hasattr(_libs['grass_gis.7.4.1'], 'G_find_file2'):
    G_find_file2 = _libs['grass_gis.7.4.1'].G_find_file2
    G_find_file2.restype = ReturnString
    G_find_file2.argtypes = [String, String, String]

# C:/msys64/usr/src/grass741/dist.x86_64-w64-mingw32/include/grass/defs/gis.h: 334
if hasattr(_libs['grass_gis.7.4.1'], 'G_find_file_misc'):
    G_find_file_misc = _libs['grass_gis.7.4.1'].G_find_file_misc
    G_find_file_misc.restype = ReturnString
    G_find_file_misc.argtypes = [String, String, String, String]

# C:/msys64/usr/src/grass741/dist.x86_64-w64-mingw32/include/grass/defs/gis.h: 335
if hasattr(_libs['grass_gis.7.4.1'], 'G_find_file2_misc'):
    G_find_file2_misc = _libs['grass_gis.7.4.1'].G_find_file2_misc
    G_find_file2_misc.restype = ReturnString
    G_find_file2_misc.argtypes = [String, String, String, String]

# C:/msys64/usr/src/grass741/dist.x86_64-w64-mingw32/include/grass/defs/gis.h: 339
if hasattr(_libs['grass_gis.7.4.1'], 'G_find_etc'):
    G_find_etc = _libs['grass_gis.7.4.1'].G_find_etc
    G_find_etc.restype = ReturnString
    G_find_etc.argtypes = [String]

# C:/msys64/usr/src/grass741/dist.x86_64-w64-mingw32/include/grass/defs/gis.h: 342
if hasattr(_libs['grass_gis.7.4.1'], 'G_find_raster'):
    G_find_raster = _libs['grass_gis.7.4.1'].G_find_raster
    G_find_raster.restype = ReturnString
    G_find_raster.argtypes = [String, String]

# C:/msys64/usr/src/grass741/dist.x86_64-w64-mingw32/include/grass/defs/gis.h: 343
if hasattr(_libs['grass_gis.7.4.1'], 'G_find_raster2'):
    G_find_raster2 = _libs['grass_gis.7.4.1'].G_find_raster2
    G_find_raster2.restype = ReturnString
    G_find_raster2.argtypes = [String, String]

# C:/msys64/usr/src/grass741/dist.x86_64-w64-mingw32/include/grass/defs/gis.h: 346
if hasattr(_libs['grass_gis.7.4.1'], 'G_find_raster3d'):
    G_find_raster3d = _libs['grass_gis.7.4.1'].G_find_raster3d
    G_find_raster3d.restype = ReturnString
    G_find_raster3d.argtypes = [String, String]

# C:/msys64/usr/src/grass741/dist.x86_64-w64-mingw32/include/grass/defs/gis.h: 349
if hasattr(_libs['grass_gis.7.4.1'], 'G_find_vector'):
    G_find_vector = _libs['grass_gis.7.4.1'].G_find_vector
    G_find_vector.restype = ReturnString
    G_find_vector.argtypes = [String, String]

# C:/msys64/usr/src/grass741/dist.x86_64-w64-mingw32/include/grass/defs/gis.h: 350
if hasattr(_libs['grass_gis.7.4.1'], 'G_find_vector2'):
    G_find_vector2 = _libs['grass_gis.7.4.1'].G_find_vector2
    G_find_vector2.restype = ReturnString
    G_find_vector2.argtypes = [String, String]

# C:/msys64/usr/src/grass741/dist.x86_64-w64-mingw32/include/grass/defs/gis.h: 353
if hasattr(_libs['grass_gis.7.4.1'], 'G_begin_geodesic_equation'):
    G_begin_geodesic_equation = _libs['grass_gis.7.4.1'].G_begin_geodesic_equation
    G_begin_geodesic_equation.restype = c_int
    G_begin_geodesic_equation.argtypes = [c_double, c_double, c_double, c_double]

# C:/msys64/usr/src/grass741/dist.x86_64-w64-mingw32/include/grass/defs/gis.h: 354
if hasattr(_libs['grass_gis.7.4.1'], 'G_geodesic_lat_from_lon'):
    G_geodesic_lat_from_lon = _libs['grass_gis.7.4.1'].G_geodesic_lat_from_lon
    G_geodesic_lat_from_lon.restype = c_double
    G_geodesic_lat_from_lon.argtypes = [c_double]

# C:/msys64/usr/src/grass741/dist.x86_64-w64-mingw32/include/grass/defs/gis.h: 357
if hasattr(_libs['grass_gis.7.4.1'], 'G_begin_geodesic_distance'):
    G_begin_geodesic_distance = _libs['grass_gis.7.4.1'].G_begin_geodesic_distance
    G_begin_geodesic_distance.restype = None
    G_begin_geodesic_distance.argtypes = [c_double, c_double]

# C:/msys64/usr/src/grass741/dist.x86_64-w64-mingw32/include/grass/defs/gis.h: 358
if hasattr(_libs['grass_gis.7.4.1'], 'G_set_geodesic_distance_lat1'):
    G_set_geodesic_distance_lat1 = _libs['grass_gis.7.4.1'].G_set_geodesic_distance_lat1
    G_set_geodesic_distance_lat1.restype = None
    G_set_geodesic_distance_lat1.argtypes = [c_double]

# C:/msys64/usr/src/grass741/dist.x86_64-w64-mingw32/include/grass/defs/gis.h: 359
if hasattr(_libs['grass_gis.7.4.1'], 'G_set_geodesic_distance_lat2'):
    G_set_geodesic_distance_lat2 = _libs['grass_gis.7.4.1'].G_set_geodesic_distance_lat2
    G_set_geodesic_distance_lat2.restype = None
    G_set_geodesic_distance_lat2.argtypes = [c_double]

# C:/msys64/usr/src/grass741/dist.x86_64-w64-mingw32/include/grass/defs/gis.h: 360
if hasattr(_libs['grass_gis.7.4.1'], 'G_geodesic_distance_lon_to_lon'):
    G_geodesic_distance_lon_to_lon = _libs['grass_gis.7.4.1'].G_geodesic_distance_lon_to_lon
    G_geodesic_distance_lon_to_lon.restype = c_double
    G_geodesic_distance_lon_to_lon.argtypes = [c_double, c_double]

# C:/msys64/usr/src/grass741/dist.x86_64-w64-mingw32/include/grass/defs/gis.h: 361
if hasattr(_libs['grass_gis.7.4.1'], 'G_geodesic_distance'):
    G_geodesic_distance = _libs['grass_gis.7.4.1'].G_geodesic_distance
    G_geodesic_distance.restype = c_double
    G_geodesic_distance.argtypes = [c_double, c_double, c_double, c_double]

# C:/msys64/usr/src/grass741/dist.x86_64-w64-mingw32/include/grass/defs/gis.h: 364
if hasattr(_libs['grass_gis.7.4.1'], 'G_get_ellipsoid_parameters'):
    G_get_ellipsoid_parameters = _libs['grass_gis.7.4.1'].G_get_ellipsoid_parameters
    G_get_ellipsoid_parameters.restype = c_int
    G_get_ellipsoid_parameters.argtypes = [POINTER(c_double), POINTER(c_double)]

# C:/msys64/usr/src/grass741/dist.x86_64-w64-mingw32/include/grass/defs/gis.h: 365
if hasattr(_libs['grass_gis.7.4.1'], 'G_get_spheroid_by_name'):
    G_get_spheroid_by_name = _libs['grass_gis.7.4.1'].G_get_spheroid_by_name
    G_get_spheroid_by_name.restype = c_int
    G_get_spheroid_by_name.argtypes = [String, POINTER(c_double), POINTER(c_double), POINTER(c_double)]

# C:/msys64/usr/src/grass741/dist.x86_64-w64-mingw32/include/grass/defs/gis.h: 366
if hasattr(_libs['grass_gis.7.4.1'], 'G_get_ellipsoid_by_name'):
    G_get_ellipsoid_by_name = _libs['grass_gis.7.4.1'].G_get_ellipsoid_by_name
    G_get_ellipsoid_by_name.restype = c_int
    G_get_ellipsoid_by_name.argtypes = [String, POINTER(c_double), POINTER(c_double)]

# C:/msys64/usr/src/grass741/dist.x86_64-w64-mingw32/include/grass/defs/gis.h: 367
if hasattr(_libs['grass_gis.7.4.1'], 'G_ellipsoid_name'):
    G_ellipsoid_name = _libs['grass_gis.7.4.1'].G_ellipsoid_name
    G_ellipsoid_name.restype = ReturnString
    G_ellipsoid_name.argtypes = [c_int]

# C:/msys64/usr/src/grass741/dist.x86_64-w64-mingw32/include/grass/defs/gis.h: 368
if hasattr(_libs['grass_gis.7.4.1'], 'G_ellipsoid_description'):
    G_ellipsoid_description = _libs['grass_gis.7.4.1'].G_ellipsoid_description
    G_ellipsoid_description.restype = ReturnString
    G_ellipsoid_description.argtypes = [c_int]

# C:/msys64/usr/src/grass741/dist.x86_64-w64-mingw32/include/grass/defs/gis.h: 369
if hasattr(_libs['grass_gis.7.4.1'], 'G_read_ellipsoid_table'):
    G_read_ellipsoid_table = _libs['grass_gis.7.4.1'].G_read_ellipsoid_table
    G_read_ellipsoid_table.restype = c_int
    G_read_ellipsoid_table.argtypes = [c_int]

# C:/msys64/usr/src/grass741/dist.x86_64-w64-mingw32/include/grass/defs/gis.h: 372
if hasattr(_libs['grass_gis.7.4.1'], 'G_get_projunits'):
    G_get_projunits = _libs['grass_gis.7.4.1'].G_get_projunits
    G_get_projunits.restype = POINTER(struct_Key_Value)
    G_get_projunits.argtypes = []

# C:/msys64/usr/src/grass741/dist.x86_64-w64-mingw32/include/grass/defs/gis.h: 373
if hasattr(_libs['grass_gis.7.4.1'], 'G_get_projinfo'):
    G_get_projinfo = _libs['grass_gis.7.4.1'].G_get_projinfo
    G_get_projinfo.restype = POINTER(struct_Key_Value)
    G_get_projinfo.argtypes = []

# C:/msys64/usr/src/grass741/dist.x86_64-w64-mingw32/include/grass/defs/gis.h: 374
if hasattr(_libs['grass_gis.7.4.1'], 'G_get_projepsg'):
    G_get_projepsg = _libs['grass_gis.7.4.1'].G_get_projepsg
    G_get_projepsg.restype = POINTER(struct_Key_Value)
    G_get_projepsg.argtypes = []

# C:/msys64/usr/src/grass741/dist.x86_64-w64-mingw32/include/grass/defs/gis.h: 377
if hasattr(_libs['grass_gis.7.4.1'], 'G_get_window'):
    G_get_window = _libs['grass_gis.7.4.1'].G_get_window
    G_get_window.restype = None
    G_get_window.argtypes = [POINTER(struct_Cell_head)]

# C:/msys64/usr/src/grass741/dist.x86_64-w64-mingw32/include/grass/defs/gis.h: 378
if hasattr(_libs['grass_gis.7.4.1'], 'G_get_default_window'):
    G_get_default_window = _libs['grass_gis.7.4.1'].G_get_default_window
    G_get_default_window.restype = None
    G_get_default_window.argtypes = [POINTER(struct_Cell_head)]

# C:/msys64/usr/src/grass741/dist.x86_64-w64-mingw32/include/grass/defs/gis.h: 379
if hasattr(_libs['grass_gis.7.4.1'], 'G_get_element_window'):
    G_get_element_window = _libs['grass_gis.7.4.1'].G_get_element_window
    G_get_element_window.restype = None
    G_get_element_window.argtypes = [POINTER(struct_Cell_head), String, String, String]

# C:/msys64/usr/src/grass741/dist.x86_64-w64-mingw32/include/grass/defs/gis.h: 383
if hasattr(_libs['grass_gis.7.4.1'], 'G_getl'):
    G_getl = _libs['grass_gis.7.4.1'].G_getl
    G_getl.restype = c_int
    G_getl.argtypes = [String, c_int, POINTER(FILE)]

# C:/msys64/usr/src/grass741/dist.x86_64-w64-mingw32/include/grass/defs/gis.h: 384
if hasattr(_libs['grass_gis.7.4.1'], 'G_getl2'):
    G_getl2 = _libs['grass_gis.7.4.1'].G_getl2
    G_getl2.restype = c_int
    G_getl2.argtypes = [String, c_int, POINTER(FILE)]

# C:/msys64/usr/src/grass741/dist.x86_64-w64-mingw32/include/grass/defs/gis.h: 387
if hasattr(_libs['grass_gis.7.4.1'], 'G_gisbase'):
    G_gisbase = _libs['grass_gis.7.4.1'].G_gisbase
    G_gisbase.restype = ReturnString
    G_gisbase.argtypes = []

# C:/msys64/usr/src/grass741/dist.x86_64-w64-mingw32/include/grass/defs/gis.h: 390
if hasattr(_libs['grass_gis.7.4.1'], 'G_gisdbase'):
    G_gisdbase = _libs['grass_gis.7.4.1'].G_gisdbase
    G_gisdbase.restype = ReturnString
    G_gisdbase.argtypes = []

# C:/msys64/usr/src/grass741/dist.x86_64-w64-mingw32/include/grass/defs/gis.h: 393
if hasattr(_libs['grass_gis.7.4.1'], 'G__gisinit'):
    G__gisinit = _libs['grass_gis.7.4.1'].G__gisinit
    G__gisinit.restype = None
    G__gisinit.argtypes = [String, String]

# C:/msys64/usr/src/grass741/dist.x86_64-w64-mingw32/include/grass/defs/gis.h: 394
if hasattr(_libs['grass_gis.7.4.1'], 'G__no_gisinit'):
    G__no_gisinit = _libs['grass_gis.7.4.1'].G__no_gisinit
    G__no_gisinit.restype = None
    G__no_gisinit.argtypes = [String]

# C:/msys64/usr/src/grass741/dist.x86_64-w64-mingw32/include/grass/defs/gis.h: 395
if hasattr(_libs['grass_gis.7.4.1'], 'G_init_all'):
    G_init_all = _libs['grass_gis.7.4.1'].G_init_all
    G_init_all.restype = None
    G_init_all.argtypes = []

# C:/msys64/usr/src/grass741/dist.x86_64-w64-mingw32/include/grass/defs/gis.h: 398
if hasattr(_libs['grass_gis.7.4.1'], 'G_add_error_handler'):
    G_add_error_handler = _libs['grass_gis.7.4.1'].G_add_error_handler
    G_add_error_handler.restype = None
    G_add_error_handler.argtypes = [CFUNCTYPE(UNCHECKED(None), POINTER(None)), POINTER(None)]

# C:/msys64/usr/src/grass741/dist.x86_64-w64-mingw32/include/grass/defs/gis.h: 399
if hasattr(_libs['grass_gis.7.4.1'], 'G_remove_error_handler'):
    G_remove_error_handler = _libs['grass_gis.7.4.1'].G_remove_error_handler
    G_remove_error_handler.restype = None
    G_remove_error_handler.argtypes = [CFUNCTYPE(UNCHECKED(None), POINTER(None)), POINTER(None)]

# C:/msys64/usr/src/grass741/dist.x86_64-w64-mingw32/include/grass/defs/gis.h: 402
if hasattr(_libs['grass_gis.7.4.1'], 'G_home'):
    G_home = _libs['grass_gis.7.4.1'].G_home
    G_home.restype = ReturnString
    G_home.argtypes = []

# C:/msys64/usr/src/grass741/dist.x86_64-w64-mingw32/include/grass/defs/gis.h: 403
if hasattr(_libs['grass_gis.7.4.1'], 'G_config_path'):
    G_config_path = _libs['grass_gis.7.4.1'].G_config_path
    G_config_path.restype = ReturnString
    G_config_path.argtypes = []

# C:/msys64/usr/src/grass741/dist.x86_64-w64-mingw32/include/grass/defs/gis.h: 406
if hasattr(_libs['grass_gis.7.4.1'], 'G_init_ilist'):
    G_init_ilist = _libs['grass_gis.7.4.1'].G_init_ilist
    G_init_ilist.restype = None
    G_init_ilist.argtypes = [POINTER(struct_ilist)]

# C:/msys64/usr/src/grass741/dist.x86_64-w64-mingw32/include/grass/defs/gis.h: 407
if hasattr(_libs['grass_gis.7.4.1'], 'G_free_ilist'):
    G_free_ilist = _libs['grass_gis.7.4.1'].G_free_ilist
    G_free_ilist.restype = None
    G_free_ilist.argtypes = [POINTER(struct_ilist)]

# C:/msys64/usr/src/grass741/dist.x86_64-w64-mingw32/include/grass/defs/gis.h: 408
if hasattr(_libs['grass_gis.7.4.1'], 'G_new_ilist'):
    G_new_ilist = _libs['grass_gis.7.4.1'].G_new_ilist
    G_new_ilist.restype = POINTER(struct_ilist)
    G_new_ilist.argtypes = []

# C:/msys64/usr/src/grass741/dist.x86_64-w64-mingw32/include/grass/defs/gis.h: 409
if hasattr(_libs['grass_gis.7.4.1'], 'G_ilist_add'):
    G_ilist_add = _libs['grass_gis.7.4.1'].G_ilist_add
    G_ilist_add.restype = None
    G_ilist_add.argtypes = [POINTER(struct_ilist), c_int]

# C:/msys64/usr/src/grass741/dist.x86_64-w64-mingw32/include/grass/defs/gis.h: 412
if hasattr(_libs['grass_gis.7.4.1'], 'G_intersect_line_segments'):
    G_intersect_line_segments = _libs['grass_gis.7.4.1'].G_intersect_line_segments
    G_intersect_line_segments.restype = c_int
    G_intersect_line_segments.argtypes = [c_double, c_double, c_double, c_double, c_double, c_double, c_double, c_double, POINTER(c_double), POINTER(c_double), POINTER(c_double), POINTER(c_double)]

# C:/msys64/usr/src/grass741/dist.x86_64-w64-mingw32/include/grass/defs/gis.h: 417
if hasattr(_libs['grass_gis.7.4.1'], 'G_is_gisbase'):
    G_is_gisbase = _libs['grass_gis.7.4.1'].G_is_gisbase
    G_is_gisbase.restype = c_int
    G_is_gisbase.argtypes = [String]

# C:/msys64/usr/src/grass741/dist.x86_64-w64-mingw32/include/grass/defs/gis.h: 418
if hasattr(_libs['grass_gis.7.4.1'], 'G_is_location'):
    G_is_location = _libs['grass_gis.7.4.1'].G_is_location
    G_is_location.restype = c_int
    G_is_location.argtypes = [String]

# C:/msys64/usr/src/grass741/dist.x86_64-w64-mingw32/include/grass/defs/gis.h: 419
if hasattr(_libs['grass_gis.7.4.1'], 'G_is_mapset'):
    G_is_mapset = _libs['grass_gis.7.4.1'].G_is_mapset
    G_is_mapset.restype = c_int
    G_is_mapset.argtypes = [String]

# C:/msys64/usr/src/grass741/dist.x86_64-w64-mingw32/include/grass/defs/gis.h: 422
if hasattr(_libs['grass_gis.7.4.1'], 'G_create_key_value'):
    G_create_key_value = _libs['grass_gis.7.4.1'].G_create_key_value
    G_create_key_value.restype = POINTER(struct_Key_Value)
    G_create_key_value.argtypes = []

# C:/msys64/usr/src/grass741/dist.x86_64-w64-mingw32/include/grass/defs/gis.h: 423
if hasattr(_libs['grass_gis.7.4.1'], 'G_set_key_value'):
    G_set_key_value = _libs['grass_gis.7.4.1'].G_set_key_value
    G_set_key_value.restype = None
    G_set_key_value.argtypes = [String, String, POINTER(struct_Key_Value)]

# C:/msys64/usr/src/grass741/dist.x86_64-w64-mingw32/include/grass/defs/gis.h: 424
if hasattr(_libs['grass_gis.7.4.1'], 'G_find_key_value'):
    G_find_key_value = _libs['grass_gis.7.4.1'].G_find_key_value
    G_find_key_value.restype = ReturnString
    G_find_key_value.argtypes = [String, POINTER(struct_Key_Value)]

# C:/msys64/usr/src/grass741/dist.x86_64-w64-mingw32/include/grass/defs/gis.h: 425
if hasattr(_libs['grass_gis.7.4.1'], 'G_free_key_value'):
    G_free_key_value = _libs['grass_gis.7.4.1'].G_free_key_value
    G_free_key_value.restype = None
    G_free_key_value.argtypes = [POINTER(struct_Key_Value)]

# C:/msys64/usr/src/grass741/dist.x86_64-w64-mingw32/include/grass/defs/gis.h: 428
if hasattr(_libs['grass_gis.7.4.1'], 'G_fwrite_key_value'):
    G_fwrite_key_value = _libs['grass_gis.7.4.1'].G_fwrite_key_value
    G_fwrite_key_value.restype = c_int
    G_fwrite_key_value.argtypes = [POINTER(FILE), POINTER(struct_Key_Value)]

# C:/msys64/usr/src/grass741/dist.x86_64-w64-mingw32/include/grass/defs/gis.h: 429
if hasattr(_libs['grass_gis.7.4.1'], 'G_fread_key_value'):
    G_fread_key_value = _libs['grass_gis.7.4.1'].G_fread_key_value
    G_fread_key_value.restype = POINTER(struct_Key_Value)
    G_fread_key_value.argtypes = [POINTER(FILE)]

# C:/msys64/usr/src/grass741/dist.x86_64-w64-mingw32/include/grass/defs/gis.h: 432
if hasattr(_libs['grass_gis.7.4.1'], 'G_write_key_value_file'):
    G_write_key_value_file = _libs['grass_gis.7.4.1'].G_write_key_value_file
    G_write_key_value_file.restype = None
    G_write_key_value_file.argtypes = [String, POINTER(struct_Key_Value)]

# C:/msys64/usr/src/grass741/dist.x86_64-w64-mingw32/include/grass/defs/gis.h: 433
if hasattr(_libs['grass_gis.7.4.1'], 'G_read_key_value_file'):
    G_read_key_value_file = _libs['grass_gis.7.4.1'].G_read_key_value_file
    G_read_key_value_file.restype = POINTER(struct_Key_Value)
    G_read_key_value_file.argtypes = [String]

# C:/msys64/usr/src/grass741/dist.x86_64-w64-mingw32/include/grass/defs/gis.h: 436
if hasattr(_libs['grass_gis.7.4.1'], 'G_update_key_value_file'):
    G_update_key_value_file = _libs['grass_gis.7.4.1'].G_update_key_value_file
    G_update_key_value_file.restype = None
    G_update_key_value_file.argtypes = [String, String, String]

# C:/msys64/usr/src/grass741/dist.x86_64-w64-mingw32/include/grass/defs/gis.h: 437
if hasattr(_libs['grass_gis.7.4.1'], 'G_lookup_key_value_from_file'):
    G_lookup_key_value_from_file = _libs['grass_gis.7.4.1'].G_lookup_key_value_from_file
    G_lookup_key_value_from_file.restype = c_int
    G_lookup_key_value_from_file.argtypes = [String, String, POINTER(c_char), c_int]

# C:/msys64/usr/src/grass741/dist.x86_64-w64-mingw32/include/grass/defs/gis.h: 440
if hasattr(_libs['grass_gis.7.4.1'], 'G_legal_filename'):
    G_legal_filename = _libs['grass_gis.7.4.1'].G_legal_filename
    G_legal_filename.restype = c_int
    G_legal_filename.argtypes = [String]

# C:/msys64/usr/src/grass741/dist.x86_64-w64-mingw32/include/grass/defs/gis.h: 441
if hasattr(_libs['grass_gis.7.4.1'], 'G_check_input_output_name'):
    G_check_input_output_name = _libs['grass_gis.7.4.1'].G_check_input_output_name
    G_check_input_output_name.restype = c_int
    G_check_input_output_name.argtypes = [String, String, c_int]

# C:/msys64/usr/src/grass741/dist.x86_64-w64-mingw32/include/grass/defs/gis.h: 444
if hasattr(_libs['grass_gis.7.4.1'], 'G_set_distance_to_line_tolerance'):
    G_set_distance_to_line_tolerance = _libs['grass_gis.7.4.1'].G_set_distance_to_line_tolerance
    G_set_distance_to_line_tolerance.restype = None
    G_set_distance_to_line_tolerance.argtypes = [c_double]

# C:/msys64/usr/src/grass741/dist.x86_64-w64-mingw32/include/grass/defs/gis.h: 445
if hasattr(_libs['grass_gis.7.4.1'], 'G_distance2_point_to_line'):
    G_distance2_point_to_line = _libs['grass_gis.7.4.1'].G_distance2_point_to_line
    G_distance2_point_to_line.restype = c_double
    G_distance2_point_to_line.argtypes = [c_double, c_double, c_double, c_double, c_double, c_double]

# C:/msys64/usr/src/grass741/dist.x86_64-w64-mingw32/include/grass/defs/gis.h: 449
if hasattr(_libs['grass_gis.7.4.1'], 'G_list_element'):
    G_list_element = _libs['grass_gis.7.4.1'].G_list_element
    G_list_element.restype = None
    G_list_element.argtypes = [String, String, String, CFUNCTYPE(UNCHECKED(c_int), String, String, String)]

# C:/msys64/usr/src/grass741/dist.x86_64-w64-mingw32/include/grass/defs/gis.h: 451
if hasattr(_libs['grass_gis.7.4.1'], 'G_list'):
    G_list = _libs['grass_gis.7.4.1'].G_list
    G_list.restype = POINTER(POINTER(c_char))
    G_list.argtypes = [c_int, String, String, String]

# C:/msys64/usr/src/grass741/dist.x86_64-w64-mingw32/include/grass/defs/gis.h: 452
if hasattr(_libs['grass_gis.7.4.1'], 'G_free_list'):
    G_free_list = _libs['grass_gis.7.4.1'].G_free_list
    G_free_list.restype = None
    G_free_list.argtypes = [POINTER(POINTER(c_char))]

# C:/msys64/usr/src/grass741/dist.x86_64-w64-mingw32/include/grass/defs/gis.h: 455
if hasattr(_libs['grass_gis.7.4.1'], 'G_lat_format'):
    G_lat_format = _libs['grass_gis.7.4.1'].G_lat_format
    G_lat_format.restype = None
    G_lat_format.argtypes = [c_double, String]

# C:/msys64/usr/src/grass741/dist.x86_64-w64-mingw32/include/grass/defs/gis.h: 456
if hasattr(_libs['grass_gis.7.4.1'], 'G_lat_format_string'):
    G_lat_format_string = _libs['grass_gis.7.4.1'].G_lat_format_string
    G_lat_format_string.restype = ReturnString
    G_lat_format_string.argtypes = []

# C:/msys64/usr/src/grass741/dist.x86_64-w64-mingw32/include/grass/defs/gis.h: 457
if hasattr(_libs['grass_gis.7.4.1'], 'G_lon_format'):
    G_lon_format = _libs['grass_gis.7.4.1'].G_lon_format
    G_lon_format.restype = None
    G_lon_format.argtypes = [c_double, String]

# C:/msys64/usr/src/grass741/dist.x86_64-w64-mingw32/include/grass/defs/gis.h: 458
if hasattr(_libs['grass_gis.7.4.1'], 'G_lon_format_string'):
    G_lon_format_string = _libs['grass_gis.7.4.1'].G_lon_format_string
    G_lon_format_string.restype = ReturnString
    G_lon_format_string.argtypes = []

# C:/msys64/usr/src/grass741/dist.x86_64-w64-mingw32/include/grass/defs/gis.h: 459
if hasattr(_libs['grass_gis.7.4.1'], 'G_llres_format'):
    G_llres_format = _libs['grass_gis.7.4.1'].G_llres_format
    G_llres_format.restype = None
    G_llres_format.argtypes = [c_double, String]

# C:/msys64/usr/src/grass741/dist.x86_64-w64-mingw32/include/grass/defs/gis.h: 460
if hasattr(_libs['grass_gis.7.4.1'], 'G_llres_format_string'):
    G_llres_format_string = _libs['grass_gis.7.4.1'].G_llres_format_string
    G_llres_format_string.restype = ReturnString
    G_llres_format_string.argtypes = []

# C:/msys64/usr/src/grass741/dist.x86_64-w64-mingw32/include/grass/defs/gis.h: 461
if hasattr(_libs['grass_gis.7.4.1'], 'G_lat_parts'):
    G_lat_parts = _libs['grass_gis.7.4.1'].G_lat_parts
    G_lat_parts.restype = None
    G_lat_parts.argtypes = [c_double, POINTER(c_int), POINTER(c_int), POINTER(c_double), String]

# C:/msys64/usr/src/grass741/dist.x86_64-w64-mingw32/include/grass/defs/gis.h: 462
if hasattr(_libs['grass_gis.7.4.1'], 'G_lon_parts'):
    G_lon_parts = _libs['grass_gis.7.4.1'].G_lon_parts
    G_lon_parts.restype = None
    G_lon_parts.argtypes = [c_double, POINTER(c_int), POINTER(c_int), POINTER(c_double), String]

# C:/msys64/usr/src/grass741/dist.x86_64-w64-mingw32/include/grass/defs/gis.h: 465
if hasattr(_libs['grass_gis.7.4.1'], 'G_lat_scan'):
    G_lat_scan = _libs['grass_gis.7.4.1'].G_lat_scan
    G_lat_scan.restype = c_int
    G_lat_scan.argtypes = [String, POINTER(c_double)]

# C:/msys64/usr/src/grass741/dist.x86_64-w64-mingw32/include/grass/defs/gis.h: 466
if hasattr(_libs['grass_gis.7.4.1'], 'G_lon_scan'):
    G_lon_scan = _libs['grass_gis.7.4.1'].G_lon_scan
    G_lon_scan.restype = c_int
    G_lon_scan.argtypes = [String, POINTER(c_double)]

# C:/msys64/usr/src/grass741/dist.x86_64-w64-mingw32/include/grass/defs/gis.h: 467
if hasattr(_libs['grass_gis.7.4.1'], 'G_llres_scan'):
    G_llres_scan = _libs['grass_gis.7.4.1'].G_llres_scan
    G_llres_scan.restype = c_int
    G_llres_scan.argtypes = [String, POINTER(c_double)]

# C:/msys64/usr/src/grass741/dist.x86_64-w64-mingw32/include/grass/defs/gis.h: 470
if hasattr(_libs['grass_gis.7.4.1'], 'G_location'):
    G_location = _libs['grass_gis.7.4.1'].G_location
    G_location.restype = ReturnString
    G_location.argtypes = []

# C:/msys64/usr/src/grass741/dist.x86_64-w64-mingw32/include/grass/defs/gis.h: 471
if hasattr(_libs['grass_gis.7.4.1'], 'G_location_path'):
    G_location_path = _libs['grass_gis.7.4.1'].G_location_path
    G_location_path.restype = ReturnString
    G_location_path.argtypes = []

# C:/msys64/usr/src/grass741/dist.x86_64-w64-mingw32/include/grass/defs/gis.h: 474
if hasattr(_libs['grass_gis.7.4.1'], 'G_srand48'):
    G_srand48 = _libs['grass_gis.7.4.1'].G_srand48
    G_srand48.restype = None
    G_srand48.argtypes = [c_long]

# C:/msys64/usr/src/grass741/dist.x86_64-w64-mingw32/include/grass/defs/gis.h: 475
if hasattr(_libs['grass_gis.7.4.1'], 'G_srand48_auto'):
    G_srand48_auto = _libs['grass_gis.7.4.1'].G_srand48_auto
    G_srand48_auto.restype = c_long
    G_srand48_auto.argtypes = []

# C:/msys64/usr/src/grass741/dist.x86_64-w64-mingw32/include/grass/defs/gis.h: 476
if hasattr(_libs['grass_gis.7.4.1'], 'G_lrand48'):
    G_lrand48 = _libs['grass_gis.7.4.1'].G_lrand48
    G_lrand48.restype = c_long
    G_lrand48.argtypes = []

# C:/msys64/usr/src/grass741/dist.x86_64-w64-mingw32/include/grass/defs/gis.h: 477
if hasattr(_libs['grass_gis.7.4.1'], 'G_mrand48'):
    G_mrand48 = _libs['grass_gis.7.4.1'].G_mrand48
    G_mrand48.restype = c_long
    G_mrand48.argtypes = []

# C:/msys64/usr/src/grass741/dist.x86_64-w64-mingw32/include/grass/defs/gis.h: 478
if hasattr(_libs['grass_gis.7.4.1'], 'G_drand48'):
    G_drand48 = _libs['grass_gis.7.4.1'].G_drand48
    G_drand48.restype = c_double
    G_drand48.argtypes = []

# C:/msys64/usr/src/grass741/dist.x86_64-w64-mingw32/include/grass/defs/gis.h: 481
if hasattr(_libs['grass_gis.7.4.1'], 'G_set_ls_filter'):
    G_set_ls_filter = _libs['grass_gis.7.4.1'].G_set_ls_filter
    G_set_ls_filter.restype = None
    G_set_ls_filter.argtypes = [CFUNCTYPE(UNCHECKED(c_int), String, POINTER(None)), POINTER(None)]

# C:/msys64/usr/src/grass741/dist.x86_64-w64-mingw32/include/grass/defs/gis.h: 482
if hasattr(_libs['grass_gis.7.4.1'], 'G_set_ls_exclude_filter'):
    G_set_ls_exclude_filter = _libs['grass_gis.7.4.1'].G_set_ls_exclude_filter
    G_set_ls_exclude_filter.restype = None
    G_set_ls_exclude_filter.argtypes = [CFUNCTYPE(UNCHECKED(c_int), String, POINTER(None)), POINTER(None)]

# C:/msys64/usr/src/grass741/dist.x86_64-w64-mingw32/include/grass/defs/gis.h: 483
if hasattr(_libs['grass_gis.7.4.1'], 'G_ls2'):
    G_ls2 = _libs['grass_gis.7.4.1'].G_ls2
    G_ls2.restype = POINTER(POINTER(c_char))
    G_ls2.argtypes = [String, POINTER(c_int)]

# C:/msys64/usr/src/grass741/dist.x86_64-w64-mingw32/include/grass/defs/gis.h: 484
if hasattr(_libs['grass_gis.7.4.1'], 'G_ls'):
    G_ls = _libs['grass_gis.7.4.1'].G_ls
    G_ls.restype = None
    G_ls.argtypes = [String, POINTER(FILE)]

# C:/msys64/usr/src/grass741/dist.x86_64-w64-mingw32/include/grass/defs/gis.h: 485
if hasattr(_libs['grass_gis.7.4.1'], 'G_ls_format'):
    G_ls_format = _libs['grass_gis.7.4.1'].G_ls_format
    G_ls_format.restype = None
    G_ls_format.argtypes = [POINTER(POINTER(c_char)), c_int, c_int, POINTER(FILE)]

# C:/msys64/usr/src/grass741/dist.x86_64-w64-mingw32/include/grass/defs/gis.h: 489
if hasattr(_libs['grass_gis.7.4.1'], 'G_ls_regex_filter'):
    G_ls_regex_filter = _libs['grass_gis.7.4.1'].G_ls_regex_filter
    G_ls_regex_filter.restype = POINTER(None)
    G_ls_regex_filter.argtypes = [String, c_int, c_int, c_int]

# C:/msys64/usr/src/grass741/dist.x86_64-w64-mingw32/include/grass/defs/gis.h: 490
if hasattr(_libs['grass_gis.7.4.1'], 'G_ls_glob_filter'):
    G_ls_glob_filter = _libs['grass_gis.7.4.1'].G_ls_glob_filter
    G_ls_glob_filter.restype = POINTER(None)
    G_ls_glob_filter.argtypes = [String, c_int, c_int]

# C:/msys64/usr/src/grass741/dist.x86_64-w64-mingw32/include/grass/defs/gis.h: 491
if hasattr(_libs['grass_gis.7.4.1'], 'G_free_ls_filter'):
    G_free_ls_filter = _libs['grass_gis.7.4.1'].G_free_ls_filter
    G_free_ls_filter.restype = None
    G_free_ls_filter.argtypes = [POINTER(None)]

# C:/msys64/usr/src/grass741/dist.x86_64-w64-mingw32/include/grass/defs/gis.h: 495
if hasattr(_libs['grass_gis.7.4.1'], 'G_make_location'):
    G_make_location = _libs['grass_gis.7.4.1'].G_make_location
    G_make_location.restype = c_int
    G_make_location.argtypes = [String, POINTER(struct_Cell_head), POINTER(struct_Key_Value), POINTER(struct_Key_Value)]

# C:/msys64/usr/src/grass741/dist.x86_64-w64-mingw32/include/grass/defs/gis.h: 497
if hasattr(_libs['grass_gis.7.4.1'], 'G_compare_projections'):
    G_compare_projections = _libs['grass_gis.7.4.1'].G_compare_projections
    G_compare_projections.restype = c_int
    G_compare_projections.argtypes = [POINTER(struct_Key_Value), POINTER(struct_Key_Value), POINTER(struct_Key_Value), POINTER(struct_Key_Value)]

# C:/msys64/usr/src/grass741/dist.x86_64-w64-mingw32/include/grass/defs/gis.h: 501
if hasattr(_libs['grass_gis.7.4.1'], 'G_make_mapset'):
    G_make_mapset = _libs['grass_gis.7.4.1'].G_make_mapset
    G_make_mapset.restype = c_int
    G_make_mapset.argtypes = [String, String, String]

# C:/msys64/usr/src/grass741/dist.x86_64-w64-mingw32/include/grass/defs/gis.h: 504
if hasattr(_libs['grass_gis.7.4.1'], 'G_tolcase'):
    G_tolcase = _libs['grass_gis.7.4.1'].G_tolcase
    G_tolcase.restype = ReturnString
    G_tolcase.argtypes = [String]

# C:/msys64/usr/src/grass741/dist.x86_64-w64-mingw32/include/grass/defs/gis.h: 505
if hasattr(_libs['grass_gis.7.4.1'], 'G_toucase'):
    G_toucase = _libs['grass_gis.7.4.1'].G_toucase
    G_toucase.restype = ReturnString
    G_toucase.argtypes = [String]

# C:/msys64/usr/src/grass741/dist.x86_64-w64-mingw32/include/grass/defs/gis.h: 508
if hasattr(_libs['grass_gis.7.4.1'], 'G_mapset'):
    G_mapset = _libs['grass_gis.7.4.1'].G_mapset
    G_mapset.restype = ReturnString
    G_mapset.argtypes = []

# C:/msys64/usr/src/grass741/dist.x86_64-w64-mingw32/include/grass/defs/gis.h: 509
if hasattr(_libs['grass_gis.7.4.1'], 'G_mapset_path'):
    G_mapset_path = _libs['grass_gis.7.4.1'].G_mapset_path
    G_mapset_path.restype = ReturnString
    G_mapset_path.argtypes = []

# C:/msys64/usr/src/grass741/dist.x86_64-w64-mingw32/include/grass/defs/gis.h: 512
if hasattr(_libs['grass_gis.7.4.1'], 'G_make_mapset_element'):
    G_make_mapset_element = _libs['grass_gis.7.4.1'].G_make_mapset_element
    G_make_mapset_element.restype = c_int
    G_make_mapset_element.argtypes = [String]

# C:/msys64/usr/src/grass741/dist.x86_64-w64-mingw32/include/grass/defs/gis.h: 513
if hasattr(_libs['grass_gis.7.4.1'], 'G_make_mapset_element_tmp'):
    G_make_mapset_element_tmp = _libs['grass_gis.7.4.1'].G_make_mapset_element_tmp
    G_make_mapset_element_tmp.restype = c_int
    G_make_mapset_element_tmp.argtypes = [String]

# C:/msys64/usr/src/grass741/dist.x86_64-w64-mingw32/include/grass/defs/gis.h: 514
if hasattr(_libs['grass_gis.7.4.1'], 'G__make_mapset_element_misc'):
    G__make_mapset_element_misc = _libs['grass_gis.7.4.1'].G__make_mapset_element_misc
    G__make_mapset_element_misc.restype = c_int
    G__make_mapset_element_misc.argtypes = [String, String]

# C:/msys64/usr/src/grass741/dist.x86_64-w64-mingw32/include/grass/defs/gis.h: 515
if hasattr(_libs['grass_gis.7.4.1'], 'G_mapset_permissions'):
    G_mapset_permissions = _libs['grass_gis.7.4.1'].G_mapset_permissions
    G_mapset_permissions.restype = c_int
    G_mapset_permissions.argtypes = [String]

# C:/msys64/usr/src/grass741/dist.x86_64-w64-mingw32/include/grass/defs/gis.h: 516
if hasattr(_libs['grass_gis.7.4.1'], 'G_mapset_permissions2'):
    G_mapset_permissions2 = _libs['grass_gis.7.4.1'].G_mapset_permissions2
    G_mapset_permissions2.restype = c_int
    G_mapset_permissions2.argtypes = [String, String, String]

# C:/msys64/usr/src/grass741/dist.x86_64-w64-mingw32/include/grass/defs/gis.h: 519
if hasattr(_libs['grass_gis.7.4.1'], 'G_get_mapset_name'):
    G_get_mapset_name = _libs['grass_gis.7.4.1'].G_get_mapset_name
    G_get_mapset_name.restype = ReturnString
    G_get_mapset_name.argtypes = [c_int]

# C:/msys64/usr/src/grass741/dist.x86_64-w64-mingw32/include/grass/defs/gis.h: 520
if hasattr(_libs['grass_gis.7.4.1'], 'G_create_alt_search_path'):
    G_create_alt_search_path = _libs['grass_gis.7.4.1'].G_create_alt_search_path
    G_create_alt_search_path.restype = None
    G_create_alt_search_path.argtypes = []

# C:/msys64/usr/src/grass741/dist.x86_64-w64-mingw32/include/grass/defs/gis.h: 521
if hasattr(_libs['grass_gis.7.4.1'], 'G_switch_search_path'):
    G_switch_search_path = _libs['grass_gis.7.4.1'].G_switch_search_path
    G_switch_search_path.restype = None
    G_switch_search_path.argtypes = []

# C:/msys64/usr/src/grass741/dist.x86_64-w64-mingw32/include/grass/defs/gis.h: 522
if hasattr(_libs['grass_gis.7.4.1'], 'G_reset_mapsets'):
    G_reset_mapsets = _libs['grass_gis.7.4.1'].G_reset_mapsets
    G_reset_mapsets.restype = None
    G_reset_mapsets.argtypes = []

# C:/msys64/usr/src/grass741/dist.x86_64-w64-mingw32/include/grass/defs/gis.h: 523
if hasattr(_libs['grass_gis.7.4.1'], 'G_get_available_mapsets'):
    G_get_available_mapsets = _libs['grass_gis.7.4.1'].G_get_available_mapsets
    G_get_available_mapsets.restype = POINTER(POINTER(c_char))
    G_get_available_mapsets.argtypes = []

# C:/msys64/usr/src/grass741/dist.x86_64-w64-mingw32/include/grass/defs/gis.h: 524
if hasattr(_libs['grass_gis.7.4.1'], 'G_add_mapset_to_search_path'):
    G_add_mapset_to_search_path = _libs['grass_gis.7.4.1'].G_add_mapset_to_search_path
    G_add_mapset_to_search_path.restype = None
    G_add_mapset_to_search_path.argtypes = [String]

# C:/msys64/usr/src/grass741/dist.x86_64-w64-mingw32/include/grass/defs/gis.h: 525
if hasattr(_libs['grass_gis.7.4.1'], 'G_is_mapset_in_search_path'):
    G_is_mapset_in_search_path = _libs['grass_gis.7.4.1'].G_is_mapset_in_search_path
    G_is_mapset_in_search_path.restype = c_int
    G_is_mapset_in_search_path.argtypes = [String]

# C:/msys64/usr/src/grass741/dist.x86_64-w64-mingw32/include/grass/defs/gis.h: 528
if hasattr(_libs['grass_gis.7.4.1'], 'G_myname'):
    G_myname = _libs['grass_gis.7.4.1'].G_myname
    G_myname.restype = ReturnString
    G_myname.argtypes = []

# C:/msys64/usr/src/grass741/dist.x86_64-w64-mingw32/include/grass/defs/gis.h: 531
if hasattr(_libs['grass_gis.7.4.1'], 'G_color_values'):
    G_color_values = _libs['grass_gis.7.4.1'].G_color_values
    G_color_values.restype = c_int
    G_color_values.argtypes = [String, POINTER(c_float), POINTER(c_float), POINTER(c_float)]

# C:/msys64/usr/src/grass741/dist.x86_64-w64-mingw32/include/grass/defs/gis.h: 532
if hasattr(_libs['grass_gis.7.4.1'], 'G_color_name'):
    G_color_name = _libs['grass_gis.7.4.1'].G_color_name
    G_color_name.restype = ReturnString
    G_color_name.argtypes = [c_int]

# C:/msys64/usr/src/grass741/dist.x86_64-w64-mingw32/include/grass/defs/gis.h: 535
if hasattr(_libs['grass_gis.7.4.1'], 'G_newlines_to_spaces'):
    G_newlines_to_spaces = _libs['grass_gis.7.4.1'].G_newlines_to_spaces
    G_newlines_to_spaces.restype = None
    G_newlines_to_spaces.argtypes = [String]

# C:/msys64/usr/src/grass741/dist.x86_64-w64-mingw32/include/grass/defs/gis.h: 538
if hasattr(_libs['grass_gis.7.4.1'], 'G_name_is_fully_qualified'):
    G_name_is_fully_qualified = _libs['grass_gis.7.4.1'].G_name_is_fully_qualified
    G_name_is_fully_qualified.restype = c_int
    G_name_is_fully_qualified.argtypes = [String, String, String]

# C:/msys64/usr/src/grass741/dist.x86_64-w64-mingw32/include/grass/defs/gis.h: 539
if hasattr(_libs['grass_gis.7.4.1'], 'G_fully_qualified_name'):
    G_fully_qualified_name = _libs['grass_gis.7.4.1'].G_fully_qualified_name
    G_fully_qualified_name.restype = ReturnString
    G_fully_qualified_name.argtypes = [String, String]

# C:/msys64/usr/src/grass741/dist.x86_64-w64-mingw32/include/grass/defs/gis.h: 540
if hasattr(_libs['grass_gis.7.4.1'], 'G_unqualified_name'):
    G_unqualified_name = _libs['grass_gis.7.4.1'].G_unqualified_name
    G_unqualified_name.restype = c_int
    G_unqualified_name.argtypes = [String, String, String, String]

# C:/msys64/usr/src/grass741/dist.x86_64-w64-mingw32/include/grass/defs/gis.h: 543
if hasattr(_libs['grass_gis.7.4.1'], 'G_open_new'):
    G_open_new = _libs['grass_gis.7.4.1'].G_open_new
    G_open_new.restype = c_int
    G_open_new.argtypes = [String, String]

# C:/msys64/usr/src/grass741/dist.x86_64-w64-mingw32/include/grass/defs/gis.h: 544
if hasattr(_libs['grass_gis.7.4.1'], 'G_open_old'):
    G_open_old = _libs['grass_gis.7.4.1'].G_open_old
    G_open_old.restype = c_int
    G_open_old.argtypes = [String, String, String]

# C:/msys64/usr/src/grass741/dist.x86_64-w64-mingw32/include/grass/defs/gis.h: 545
if hasattr(_libs['grass_gis.7.4.1'], 'G_open_update'):
    G_open_update = _libs['grass_gis.7.4.1'].G_open_update
    G_open_update.restype = c_int
    G_open_update.argtypes = [String, String]

# C:/msys64/usr/src/grass741/dist.x86_64-w64-mingw32/include/grass/defs/gis.h: 546
if hasattr(_libs['grass_gis.7.4.1'], 'G_fopen_new'):
    G_fopen_new = _libs['grass_gis.7.4.1'].G_fopen_new
    G_fopen_new.restype = POINTER(FILE)
    G_fopen_new.argtypes = [String, String]

# C:/msys64/usr/src/grass741/dist.x86_64-w64-mingw32/include/grass/defs/gis.h: 547
if hasattr(_libs['grass_gis.7.4.1'], 'G_fopen_old'):
    G_fopen_old = _libs['grass_gis.7.4.1'].G_fopen_old
    G_fopen_old.restype = POINTER(FILE)
    G_fopen_old.argtypes = [String, String, String]

# C:/msys64/usr/src/grass741/dist.x86_64-w64-mingw32/include/grass/defs/gis.h: 548
if hasattr(_libs['grass_gis.7.4.1'], 'G_fopen_append'):
    G_fopen_append = _libs['grass_gis.7.4.1'].G_fopen_append
    G_fopen_append.restype = POINTER(FILE)
    G_fopen_append.argtypes = [String, String]

# C:/msys64/usr/src/grass741/dist.x86_64-w64-mingw32/include/grass/defs/gis.h: 549
if hasattr(_libs['grass_gis.7.4.1'], 'G_fopen_modify'):
    G_fopen_modify = _libs['grass_gis.7.4.1'].G_fopen_modify
    G_fopen_modify.restype = POINTER(FILE)
    G_fopen_modify.argtypes = [String, String]

# C:/msys64/usr/src/grass741/dist.x86_64-w64-mingw32/include/grass/defs/gis.h: 552
if hasattr(_libs['grass_gis.7.4.1'], 'G_open_new_misc'):
    G_open_new_misc = _libs['grass_gis.7.4.1'].G_open_new_misc
    G_open_new_misc.restype = c_int
    G_open_new_misc.argtypes = [String, String, String]

# C:/msys64/usr/src/grass741/dist.x86_64-w64-mingw32/include/grass/defs/gis.h: 553
if hasattr(_libs['grass_gis.7.4.1'], 'G_open_old_misc'):
    G_open_old_misc = _libs['grass_gis.7.4.1'].G_open_old_misc
    G_open_old_misc.restype = c_int
    G_open_old_misc.argtypes = [String, String, String, String]

# C:/msys64/usr/src/grass741/dist.x86_64-w64-mingw32/include/grass/defs/gis.h: 554
if hasattr(_libs['grass_gis.7.4.1'], 'G_open_update_misc'):
    G_open_update_misc = _libs['grass_gis.7.4.1'].G_open_update_misc
    G_open_update_misc.restype = c_int
    G_open_update_misc.argtypes = [String, String, String]

# C:/msys64/usr/src/grass741/dist.x86_64-w64-mingw32/include/grass/defs/gis.h: 555
if hasattr(_libs['grass_gis.7.4.1'], 'G_fopen_new_misc'):
    G_fopen_new_misc = _libs['grass_gis.7.4.1'].G_fopen_new_misc
    G_fopen_new_misc.restype = POINTER(FILE)
    G_fopen_new_misc.argtypes = [String, String, String]

# C:/msys64/usr/src/grass741/dist.x86_64-w64-mingw32/include/grass/defs/gis.h: 556
if hasattr(_libs['grass_gis.7.4.1'], 'G_fopen_old_misc'):
    G_fopen_old_misc = _libs['grass_gis.7.4.1'].G_fopen_old_misc
    G_fopen_old_misc.restype = POINTER(FILE)
    G_fopen_old_misc.argtypes = [String, String, String, String]

# C:/msys64/usr/src/grass741/dist.x86_64-w64-mingw32/include/grass/defs/gis.h: 558
if hasattr(_libs['grass_gis.7.4.1'], 'G_fopen_append_misc'):
    G_fopen_append_misc = _libs['grass_gis.7.4.1'].G_fopen_append_misc
    G_fopen_append_misc.restype = POINTER(FILE)
    G_fopen_append_misc.argtypes = [String, String, String]

# C:/msys64/usr/src/grass741/dist.x86_64-w64-mingw32/include/grass/defs/gis.h: 559
if hasattr(_libs['grass_gis.7.4.1'], 'G_fopen_modify_misc'):
    G_fopen_modify_misc = _libs['grass_gis.7.4.1'].G_fopen_modify_misc
    G_fopen_modify_misc.restype = POINTER(FILE)
    G_fopen_modify_misc.argtypes = [String, String, String]

# C:/msys64/usr/src/grass741/dist.x86_64-w64-mingw32/include/grass/defs/gis.h: 562
if hasattr(_libs['grass_gis.7.4.1'], 'G_check_overwrite'):
    G_check_overwrite = _libs['grass_gis.7.4.1'].G_check_overwrite
    G_check_overwrite.restype = c_int
    G_check_overwrite.argtypes = [c_int, POINTER(POINTER(c_char))]

# C:/msys64/usr/src/grass741/dist.x86_64-w64-mingw32/include/grass/defs/gis.h: 565
if hasattr(_libs['grass_gis.7.4.1'], 'G_open_pager'):
    G_open_pager = _libs['grass_gis.7.4.1'].G_open_pager
    G_open_pager.restype = POINTER(FILE)
    G_open_pager.argtypes = [POINTER(struct_Popen)]

# C:/msys64/usr/src/grass741/dist.x86_64-w64-mingw32/include/grass/defs/gis.h: 566
if hasattr(_libs['grass_gis.7.4.1'], 'G_close_pager'):
    G_close_pager = _libs['grass_gis.7.4.1'].G_close_pager
    G_close_pager.restype = None
    G_close_pager.argtypes = [POINTER(struct_Popen)]

# C:/msys64/usr/src/grass741/dist.x86_64-w64-mingw32/include/grass/defs/gis.h: 567
if hasattr(_libs['grass_gis.7.4.1'], 'G_open_mail'):
    G_open_mail = _libs['grass_gis.7.4.1'].G_open_mail
    G_open_mail.restype = POINTER(FILE)
    G_open_mail.argtypes = [POINTER(struct_Popen)]

# C:/msys64/usr/src/grass741/dist.x86_64-w64-mingw32/include/grass/defs/gis.h: 568
if hasattr(_libs['grass_gis.7.4.1'], 'G_close_mail'):
    G_close_mail = _libs['grass_gis.7.4.1'].G_close_mail
    G_close_mail.restype = None
    G_close_mail.argtypes = [POINTER(struct_Popen)]

# C:/msys64/usr/src/grass741/dist.x86_64-w64-mingw32/include/grass/defs/gis.h: 571
if hasattr(_libs['grass_gis.7.4.1'], 'G_disable_interactive'):
    G_disable_interactive = _libs['grass_gis.7.4.1'].G_disable_interactive
    G_disable_interactive.restype = None
    G_disable_interactive.argtypes = []

# C:/msys64/usr/src/grass741/dist.x86_64-w64-mingw32/include/grass/defs/gis.h: 572
if hasattr(_libs['grass_gis.7.4.1'], 'G_define_module'):
    G_define_module = _libs['grass_gis.7.4.1'].G_define_module
    G_define_module.restype = POINTER(struct_GModule)
    G_define_module.argtypes = []

# C:/msys64/usr/src/grass741/dist.x86_64-w64-mingw32/include/grass/defs/gis.h: 573
if hasattr(_libs['grass_gis.7.4.1'], 'G_define_flag'):
    G_define_flag = _libs['grass_gis.7.4.1'].G_define_flag
    G_define_flag.restype = POINTER(struct_Flag)
    G_define_flag.argtypes = []

# C:/msys64/usr/src/grass741/dist.x86_64-w64-mingw32/include/grass/defs/gis.h: 574
if hasattr(_libs['grass_gis.7.4.1'], 'G_define_option'):
    G_define_option = _libs['grass_gis.7.4.1'].G_define_option
    G_define_option.restype = POINTER(struct_Option)
    G_define_option.argtypes = []

# C:/msys64/usr/src/grass741/dist.x86_64-w64-mingw32/include/grass/defs/gis.h: 575
if hasattr(_libs['grass_gis.7.4.1'], 'G_define_standard_option'):
    G_define_standard_option = _libs['grass_gis.7.4.1'].G_define_standard_option
    G_define_standard_option.restype = POINTER(struct_Option)
    G_define_standard_option.argtypes = [c_int]

# C:/msys64/usr/src/grass741/dist.x86_64-w64-mingw32/include/grass/defs/gis.h: 576
if hasattr(_libs['grass_gis.7.4.1'], 'G_define_standard_flag'):
    G_define_standard_flag = _libs['grass_gis.7.4.1'].G_define_standard_flag
    G_define_standard_flag.restype = POINTER(struct_Flag)
    G_define_standard_flag.argtypes = [c_int]

# C:/msys64/usr/src/grass741/dist.x86_64-w64-mingw32/include/grass/defs/gis.h: 577
if hasattr(_libs['grass_gis.7.4.1'], 'G_parser'):
    G_parser = _libs['grass_gis.7.4.1'].G_parser
    G_parser.restype = c_int
    G_parser.argtypes = [c_int, POINTER(POINTER(c_char))]

# C:/msys64/usr/src/grass741/dist.x86_64-w64-mingw32/include/grass/defs/gis.h: 578
if hasattr(_libs['grass_gis.7.4.1'], 'G_usage'):
    G_usage = _libs['grass_gis.7.4.1'].G_usage
    G_usage.restype = None
    G_usage.argtypes = []

# C:/msys64/usr/src/grass741/dist.x86_64-w64-mingw32/include/grass/defs/gis.h: 579
if hasattr(_libs['grass_gis.7.4.1'], 'G_recreate_command'):
    G_recreate_command = _libs['grass_gis.7.4.1'].G_recreate_command
    G_recreate_command.restype = ReturnString
    G_recreate_command.argtypes = []

# C:/msys64/usr/src/grass741/dist.x86_64-w64-mingw32/include/grass/defs/gis.h: 580
if hasattr(_libs['grass_gis.7.4.1'], 'G_add_keyword'):
    G_add_keyword = _libs['grass_gis.7.4.1'].G_add_keyword
    G_add_keyword.restype = None
    G_add_keyword.argtypes = [String]

# C:/msys64/usr/src/grass741/dist.x86_64-w64-mingw32/include/grass/defs/gis.h: 581
if hasattr(_libs['grass_gis.7.4.1'], 'G_set_keywords'):
    G_set_keywords = _libs['grass_gis.7.4.1'].G_set_keywords
    G_set_keywords.restype = None
    G_set_keywords.argtypes = [String]

# C:/msys64/usr/src/grass741/dist.x86_64-w64-mingw32/include/grass/defs/gis.h: 582
if hasattr(_libs['grass_gis.7.4.1'], 'G_get_overwrite'):
    G_get_overwrite = _libs['grass_gis.7.4.1'].G_get_overwrite
    G_get_overwrite.restype = c_int
    G_get_overwrite.argtypes = []

# C:/msys64/usr/src/grass741/dist.x86_64-w64-mingw32/include/grass/defs/gis.h: 583
if hasattr(_libs['grass_gis.7.4.1'], 'G_option_to_separator'):
    G_option_to_separator = _libs['grass_gis.7.4.1'].G_option_to_separator
    G_option_to_separator.restype = ReturnString
    G_option_to_separator.argtypes = [POINTER(struct_Option)]

# C:/msys64/usr/src/grass741/dist.x86_64-w64-mingw32/include/grass/defs/gis.h: 584
if hasattr(_libs['grass_gis.7.4.1'], 'G_open_option_file'):
    G_open_option_file = _libs['grass_gis.7.4.1'].G_open_option_file
    G_open_option_file.restype = POINTER(FILE)
    G_open_option_file.argtypes = [POINTER(struct_Option)]

# C:/msys64/usr/src/grass741/dist.x86_64-w64-mingw32/include/grass/defs/gis.h: 585
if hasattr(_libs['grass_gis.7.4.1'], 'G_close_option_file'):
    G_close_option_file = _libs['grass_gis.7.4.1'].G_close_option_file
    G_close_option_file.restype = None
    G_close_option_file.argtypes = [POINTER(FILE)]

# C:/msys64/usr/src/grass741/dist.x86_64-w64-mingw32/include/grass/defs/gis.h: 588
if hasattr(_libs['grass_gis.7.4.1'], 'G_option_rule'):
    G_option_rule = _libs['grass_gis.7.4.1'].G_option_rule
    G_option_rule.restype = None
    G_option_rule.argtypes = [c_int, c_int, POINTER(POINTER(None))]

# C:/msys64/usr/src/grass741/dist.x86_64-w64-mingw32/include/grass/defs/gis.h: 589
if hasattr(_libs['grass_gis.7.4.1'], 'G_option_exclusive'):
    _func = _libs['grass_gis.7.4.1'].G_option_exclusive
    _restype = None
    _argtypes = [POINTER(None)]
    G_option_exclusive = _variadic_function(_func,_restype,_argtypes)

# C:/msys64/usr/src/grass741/dist.x86_64-w64-mingw32/include/grass/defs/gis.h: 590
if hasattr(_libs['grass_gis.7.4.1'], 'G_option_required'):
    _func = _libs['grass_gis.7.4.1'].G_option_required
    _restype = None
    _argtypes = [POINTER(None)]
    G_option_required = _variadic_function(_func,_restype,_argtypes)

# C:/msys64/usr/src/grass741/dist.x86_64-w64-mingw32/include/grass/defs/gis.h: 591
if hasattr(_libs['grass_gis.7.4.1'], 'G_option_requires'):
    _func = _libs['grass_gis.7.4.1'].G_option_requires
    _restype = None
    _argtypes = [POINTER(None)]
    G_option_requires = _variadic_function(_func,_restype,_argtypes)

# C:/msys64/usr/src/grass741/dist.x86_64-w64-mingw32/include/grass/defs/gis.h: 592
if hasattr(_libs['grass_gis.7.4.1'], 'G_option_requires_all'):
    _func = _libs['grass_gis.7.4.1'].G_option_requires_all
    _restype = None
    _argtypes = [POINTER(None)]
    G_option_requires_all = _variadic_function(_func,_restype,_argtypes)

# C:/msys64/usr/src/grass741/dist.x86_64-w64-mingw32/include/grass/defs/gis.h: 593
if hasattr(_libs['grass_gis.7.4.1'], 'G_option_excludes'):
    _func = _libs['grass_gis.7.4.1'].G_option_excludes
    _restype = None
    _argtypes = [POINTER(None)]
    G_option_excludes = _variadic_function(_func,_restype,_argtypes)

# C:/msys64/usr/src/grass741/dist.x86_64-w64-mingw32/include/grass/defs/gis.h: 594
if hasattr(_libs['grass_gis.7.4.1'], 'G_option_collective'):
    _func = _libs['grass_gis.7.4.1'].G_option_collective
    _restype = None
    _argtypes = [POINTER(None)]
    G_option_collective = _variadic_function(_func,_restype,_argtypes)

# C:/msys64/usr/src/grass741/dist.x86_64-w64-mingw32/include/grass/defs/gis.h: 597
if hasattr(_libs['grass_gis.7.4.1'], 'G_mkdir'):
    G_mkdir = _libs['grass_gis.7.4.1'].G_mkdir
    G_mkdir.restype = c_int
    G_mkdir.argtypes = [String]

# C:/msys64/usr/src/grass741/dist.x86_64-w64-mingw32/include/grass/defs/gis.h: 598
if hasattr(_libs['grass_gis.7.4.1'], 'G_is_dirsep'):
    G_is_dirsep = _libs['grass_gis.7.4.1'].G_is_dirsep
    G_is_dirsep.restype = c_int
    G_is_dirsep.argtypes = [c_char]

# C:/msys64/usr/src/grass741/dist.x86_64-w64-mingw32/include/grass/defs/gis.h: 599
if hasattr(_libs['grass_gis.7.4.1'], 'G_is_absolute_path'):
    G_is_absolute_path = _libs['grass_gis.7.4.1'].G_is_absolute_path
    G_is_absolute_path.restype = c_int
    G_is_absolute_path.argtypes = [String]

# C:/msys64/usr/src/grass741/dist.x86_64-w64-mingw32/include/grass/defs/gis.h: 600
if hasattr(_libs['grass_gis.7.4.1'], 'G_convert_dirseps_to_host'):
    G_convert_dirseps_to_host = _libs['grass_gis.7.4.1'].G_convert_dirseps_to_host
    G_convert_dirseps_to_host.restype = ReturnString
    G_convert_dirseps_to_host.argtypes = [String]

# C:/msys64/usr/src/grass741/dist.x86_64-w64-mingw32/include/grass/defs/gis.h: 601
if hasattr(_libs['grass_gis.7.4.1'], 'G_convert_dirseps_from_host'):
    G_convert_dirseps_from_host = _libs['grass_gis.7.4.1'].G_convert_dirseps_from_host
    G_convert_dirseps_from_host.restype = ReturnString
    G_convert_dirseps_from_host.argtypes = [String]

# C:/msys64/usr/src/grass741/dist.x86_64-w64-mingw32/include/grass/defs/gis.h: 604
if hasattr(_libs['grass_gis.7.4.1'], 'G_owner'):
    G_owner = _libs['grass_gis.7.4.1'].G_owner
    G_owner.restype = c_int
    G_owner.argtypes = [String]

# C:/msys64/usr/src/grass741/dist.x86_64-w64-mingw32/include/grass/defs/gis.h: 607
if hasattr(_libs['grass_gis.7.4.1'], 'G_percent'):
    G_percent = _libs['grass_gis.7.4.1'].G_percent
    G_percent.restype = None
    G_percent.argtypes = [c_long, c_long, c_int]

# C:/msys64/usr/src/grass741/dist.x86_64-w64-mingw32/include/grass/defs/gis.h: 608
if hasattr(_libs['grass_gis.7.4.1'], 'G_percent_reset'):
    G_percent_reset = _libs['grass_gis.7.4.1'].G_percent_reset
    G_percent_reset.restype = None
    G_percent_reset.argtypes = []

# C:/msys64/usr/src/grass741/dist.x86_64-w64-mingw32/include/grass/defs/gis.h: 609
if hasattr(_libs['grass_gis.7.4.1'], 'G_progress'):
    G_progress = _libs['grass_gis.7.4.1'].G_progress
    G_progress.restype = None
    G_progress.argtypes = [c_long, c_int]

# C:/msys64/usr/src/grass741/dist.x86_64-w64-mingw32/include/grass/defs/gis.h: 610
if hasattr(_libs['grass_gis.7.4.1'], 'G_set_percent_routine'):
    G_set_percent_routine = _libs['grass_gis.7.4.1'].G_set_percent_routine
    G_set_percent_routine.restype = None
    G_set_percent_routine.argtypes = [CFUNCTYPE(UNCHECKED(c_int), c_int)]

# C:/msys64/usr/src/grass741/dist.x86_64-w64-mingw32/include/grass/defs/gis.h: 611
if hasattr(_libs['grass_gis.7.4.1'], 'G_unset_percent_routine'):
    G_unset_percent_routine = _libs['grass_gis.7.4.1'].G_unset_percent_routine
    G_unset_percent_routine.restype = None
    G_unset_percent_routine.argtypes = []

# C:/msys64/usr/src/grass741/dist.x86_64-w64-mingw32/include/grass/defs/gis.h: 614
if hasattr(_libs['grass_gis.7.4.1'], 'G_popen_clear'):
    G_popen_clear = _libs['grass_gis.7.4.1'].G_popen_clear
    G_popen_clear.restype = None
    G_popen_clear.argtypes = [POINTER(struct_Popen)]

# C:/msys64/usr/src/grass741/dist.x86_64-w64-mingw32/include/grass/defs/gis.h: 615
if hasattr(_libs['grass_gis.7.4.1'], 'G_popen_write'):
    G_popen_write = _libs['grass_gis.7.4.1'].G_popen_write
    G_popen_write.restype = POINTER(FILE)
    G_popen_write.argtypes = [POINTER(struct_Popen), String, POINTER(POINTER(c_char))]

# C:/msys64/usr/src/grass741/dist.x86_64-w64-mingw32/include/grass/defs/gis.h: 616
if hasattr(_libs['grass_gis.7.4.1'], 'G_popen_read'):
    G_popen_read = _libs['grass_gis.7.4.1'].G_popen_read
    G_popen_read.restype = POINTER(FILE)
    G_popen_read.argtypes = [POINTER(struct_Popen), String, POINTER(POINTER(c_char))]

# C:/msys64/usr/src/grass741/dist.x86_64-w64-mingw32/include/grass/defs/gis.h: 617
if hasattr(_libs['grass_gis.7.4.1'], 'G_popen_close'):
    G_popen_close = _libs['grass_gis.7.4.1'].G_popen_close
    G_popen_close.restype = None
    G_popen_close.argtypes = [POINTER(struct_Popen)]

# C:/msys64/usr/src/grass741/dist.x86_64-w64-mingw32/include/grass/defs/gis.h: 620
if hasattr(_libs['grass_gis.7.4.1'], 'G_setup_plot'):
    G_setup_plot = _libs['grass_gis.7.4.1'].G_setup_plot
    G_setup_plot.restype = None
    G_setup_plot.argtypes = [c_double, c_double, c_double, c_double, CFUNCTYPE(UNCHECKED(c_int), c_int, c_int), CFUNCTYPE(UNCHECKED(c_int), c_int, c_int)]

# C:/msys64/usr/src/grass741/dist.x86_64-w64-mingw32/include/grass/defs/gis.h: 622
if hasattr(_libs['grass_gis.7.4.1'], 'G_setup_fill'):
    G_setup_fill = _libs['grass_gis.7.4.1'].G_setup_fill
    G_setup_fill.restype = None
    G_setup_fill.argtypes = [c_int]

# C:/msys64/usr/src/grass741/dist.x86_64-w64-mingw32/include/grass/defs/gis.h: 623
if hasattr(_libs['grass_gis.7.4.1'], 'G_plot_where_xy'):
    G_plot_where_xy = _libs['grass_gis.7.4.1'].G_plot_where_xy
    G_plot_where_xy.restype = None
    G_plot_where_xy.argtypes = [c_double, c_double, POINTER(c_int), POINTER(c_int)]

# C:/msys64/usr/src/grass741/dist.x86_64-w64-mingw32/include/grass/defs/gis.h: 624
if hasattr(_libs['grass_gis.7.4.1'], 'G_plot_where_en'):
    G_plot_where_en = _libs['grass_gis.7.4.1'].G_plot_where_en
    G_plot_where_en.restype = None
    G_plot_where_en.argtypes = [c_int, c_int, POINTER(c_double), POINTER(c_double)]

# C:/msys64/usr/src/grass741/dist.x86_64-w64-mingw32/include/grass/defs/gis.h: 625
if hasattr(_libs['grass_gis.7.4.1'], 'G_plot_point'):
    G_plot_point = _libs['grass_gis.7.4.1'].G_plot_point
    G_plot_point.restype = None
    G_plot_point.argtypes = [c_double, c_double]

# C:/msys64/usr/src/grass741/dist.x86_64-w64-mingw32/include/grass/defs/gis.h: 626
if hasattr(_libs['grass_gis.7.4.1'], 'G_plot_line'):
    G_plot_line = _libs['grass_gis.7.4.1'].G_plot_line
    G_plot_line.restype = None
    G_plot_line.argtypes = [c_double, c_double, c_double, c_double]

# C:/msys64/usr/src/grass741/dist.x86_64-w64-mingw32/include/grass/defs/gis.h: 627
if hasattr(_libs['grass_gis.7.4.1'], 'G_plot_line2'):
    G_plot_line2 = _libs['grass_gis.7.4.1'].G_plot_line2
    G_plot_line2.restype = None
    G_plot_line2.argtypes = [c_double, c_double, c_double, c_double]

# C:/msys64/usr/src/grass741/dist.x86_64-w64-mingw32/include/grass/defs/gis.h: 628
if hasattr(_libs['grass_gis.7.4.1'], 'G_plot_polygon'):
    G_plot_polygon = _libs['grass_gis.7.4.1'].G_plot_polygon
    G_plot_polygon.restype = c_int
    G_plot_polygon.argtypes = [POINTER(c_double), POINTER(c_double), c_int]

# C:/msys64/usr/src/grass741/dist.x86_64-w64-mingw32/include/grass/defs/gis.h: 629
if hasattr(_libs['grass_gis.7.4.1'], 'G_plot_area'):
    G_plot_area = _libs['grass_gis.7.4.1'].G_plot_area
    G_plot_area.restype = c_int
    G_plot_area.argtypes = [POINTER(POINTER(c_double)), POINTER(POINTER(c_double)), POINTER(c_int), c_int]

# C:/msys64/usr/src/grass741/dist.x86_64-w64-mingw32/include/grass/defs/gis.h: 630
if hasattr(_libs['grass_gis.7.4.1'], 'G_plot_fx'):
    G_plot_fx = _libs['grass_gis.7.4.1'].G_plot_fx
    G_plot_fx.restype = None
    G_plot_fx.argtypes = [CFUNCTYPE(UNCHECKED(c_double), c_double), c_double, c_double]

# C:/msys64/usr/src/grass741/dist.x86_64-w64-mingw32/include/grass/defs/gis.h: 633
if hasattr(_libs['grass_gis.7.4.1'], 'G_pole_in_polygon'):
    G_pole_in_polygon = _libs['grass_gis.7.4.1'].G_pole_in_polygon
    G_pole_in_polygon.restype = c_int
    G_pole_in_polygon.argtypes = [POINTER(c_double), POINTER(c_double), c_int]

# C:/msys64/usr/src/grass741/dist.x86_64-w64-mingw32/include/grass/defs/gis.h: 636
if hasattr(_libs['grass_gis.7.4.1'], 'G_program_name'):
    G_program_name = _libs['grass_gis.7.4.1'].G_program_name
    G_program_name.restype = ReturnString
    G_program_name.argtypes = []

# C:/msys64/usr/src/grass741/dist.x86_64-w64-mingw32/include/grass/defs/gis.h: 637
if hasattr(_libs['grass_gis.7.4.1'], 'G_original_program_name'):
    G_original_program_name = _libs['grass_gis.7.4.1'].G_original_program_name
    G_original_program_name.restype = ReturnString
    G_original_program_name.argtypes = []

# C:/msys64/usr/src/grass741/dist.x86_64-w64-mingw32/include/grass/defs/gis.h: 638
if hasattr(_libs['grass_gis.7.4.1'], 'G_set_program_name'):
    G_set_program_name = _libs['grass_gis.7.4.1'].G_set_program_name
    G_set_program_name.restype = None
    G_set_program_name.argtypes = [String]

# C:/msys64/usr/src/grass741/dist.x86_64-w64-mingw32/include/grass/defs/gis.h: 641
if hasattr(_libs['grass_gis.7.4.1'], 'G_projection'):
    G_projection = _libs['grass_gis.7.4.1'].G_projection
    G_projection.restype = c_int
    G_projection.argtypes = []

# C:/msys64/usr/src/grass741/dist.x86_64-w64-mingw32/include/grass/defs/gis.h: 644
if hasattr(_libs['grass_gis.7.4.1'], 'G_projection_units'):
    G_projection_units = _libs['grass_gis.7.4.1'].G_projection_units
    G_projection_units.restype = c_int
    G_projection_units.argtypes = [c_int]

# C:/msys64/usr/src/grass741/dist.x86_64-w64-mingw32/include/grass/defs/gis.h: 645
if hasattr(_libs['grass_gis.7.4.1'], 'G_projection_name'):
    G_projection_name = _libs['grass_gis.7.4.1'].G_projection_name
    G_projection_name.restype = ReturnString
    G_projection_name.argtypes = [c_int]

# C:/msys64/usr/src/grass741/dist.x86_64-w64-mingw32/include/grass/defs/gis.h: 648
if hasattr(_libs['grass_gis.7.4.1'], 'G_database_unit_name'):
    G_database_unit_name = _libs['grass_gis.7.4.1'].G_database_unit_name
    G_database_unit_name.restype = ReturnString
    G_database_unit_name.argtypes = [c_int]

# C:/msys64/usr/src/grass741/dist.x86_64-w64-mingw32/include/grass/defs/gis.h: 649
if hasattr(_libs['grass_gis.7.4.1'], 'G_database_unit'):
    G_database_unit = _libs['grass_gis.7.4.1'].G_database_unit
    G_database_unit.restype = c_int
    G_database_unit.argtypes = []

# C:/msys64/usr/src/grass741/dist.x86_64-w64-mingw32/include/grass/defs/gis.h: 650
if hasattr(_libs['grass_gis.7.4.1'], 'G_database_projection_name'):
    G_database_projection_name = _libs['grass_gis.7.4.1'].G_database_projection_name
    G_database_projection_name.restype = ReturnString
    G_database_projection_name.argtypes = []

# C:/msys64/usr/src/grass741/dist.x86_64-w64-mingw32/include/grass/defs/gis.h: 651
if hasattr(_libs['grass_gis.7.4.1'], 'G_database_datum_name'):
    G_database_datum_name = _libs['grass_gis.7.4.1'].G_database_datum_name
    G_database_datum_name.restype = ReturnString
    G_database_datum_name.argtypes = []

# C:/msys64/usr/src/grass741/dist.x86_64-w64-mingw32/include/grass/defs/gis.h: 652
if hasattr(_libs['grass_gis.7.4.1'], 'G_database_ellipse_name'):
    G_database_ellipse_name = _libs['grass_gis.7.4.1'].G_database_ellipse_name
    G_database_ellipse_name.restype = ReturnString
    G_database_ellipse_name.argtypes = []

# C:/msys64/usr/src/grass741/dist.x86_64-w64-mingw32/include/grass/defs/gis.h: 653
if hasattr(_libs['grass_gis.7.4.1'], 'G_database_units_to_meters_factor'):
    G_database_units_to_meters_factor = _libs['grass_gis.7.4.1'].G_database_units_to_meters_factor
    G_database_units_to_meters_factor.restype = c_double
    G_database_units_to_meters_factor.argtypes = []

# C:/msys64/usr/src/grass741/dist.x86_64-w64-mingw32/include/grass/defs/gis.h: 654
if hasattr(_libs['grass_gis.7.4.1'], 'G_database_epsg_code'):
    G_database_epsg_code = _libs['grass_gis.7.4.1'].G_database_epsg_code
    G_database_epsg_code.restype = ReturnString
    G_database_epsg_code.argtypes = []

# C:/msys64/usr/src/grass741/dist.x86_64-w64-mingw32/include/grass/defs/gis.h: 657
if hasattr(_libs['grass_gis.7.4.1'], 'G_put_window'):
    G_put_window = _libs['grass_gis.7.4.1'].G_put_window
    G_put_window.restype = c_int
    G_put_window.argtypes = [POINTER(struct_Cell_head)]

# C:/msys64/usr/src/grass741/dist.x86_64-w64-mingw32/include/grass/defs/gis.h: 658
if hasattr(_libs['grass_gis.7.4.1'], 'G_put_element_window'):
    G_put_element_window = _libs['grass_gis.7.4.1'].G_put_element_window
    G_put_element_window.restype = c_int
    G_put_element_window.argtypes = [POINTER(struct_Cell_head), String, String]

# C:/msys64/usr/src/grass741/dist.x86_64-w64-mingw32/include/grass/defs/gis.h: 661
if hasattr(_libs['grass_gis.7.4.1'], 'G_putenv'):
    G_putenv = _libs['grass_gis.7.4.1'].G_putenv
    G_putenv.restype = None
    G_putenv.argtypes = [String, String]

# C:/msys64/usr/src/grass741/dist.x86_64-w64-mingw32/include/grass/defs/gis.h: 664
if hasattr(_libs['grass_gis.7.4.1'], 'G_meridional_radius_of_curvature'):
    G_meridional_radius_of_curvature = _libs['grass_gis.7.4.1'].G_meridional_radius_of_curvature
    G_meridional_radius_of_curvature.restype = c_double
    G_meridional_radius_of_curvature.argtypes = [c_double, c_double, c_double]

# C:/msys64/usr/src/grass741/dist.x86_64-w64-mingw32/include/grass/defs/gis.h: 665
if hasattr(_libs['grass_gis.7.4.1'], 'G_transverse_radius_of_curvature'):
    G_transverse_radius_of_curvature = _libs['grass_gis.7.4.1'].G_transverse_radius_of_curvature
    G_transverse_radius_of_curvature.restype = c_double
    G_transverse_radius_of_curvature.argtypes = [c_double, c_double, c_double]

# C:/msys64/usr/src/grass741/dist.x86_64-w64-mingw32/include/grass/defs/gis.h: 666
if hasattr(_libs['grass_gis.7.4.1'], 'G_radius_of_conformal_tangent_sphere'):
    G_radius_of_conformal_tangent_sphere = _libs['grass_gis.7.4.1'].G_radius_of_conformal_tangent_sphere
    G_radius_of_conformal_tangent_sphere.restype = c_double
    G_radius_of_conformal_tangent_sphere.argtypes = [c_double, c_double, c_double]

# C:/msys64/usr/src/grass741/dist.x86_64-w64-mingw32/include/grass/defs/gis.h: 669
if hasattr(_libs['grass_gis.7.4.1'], 'G__read_Cell_head'):
    G__read_Cell_head = _libs['grass_gis.7.4.1'].G__read_Cell_head
    G__read_Cell_head.restype = None
    G__read_Cell_head.argtypes = [POINTER(FILE), POINTER(struct_Cell_head), c_int]

# C:/msys64/usr/src/grass741/dist.x86_64-w64-mingw32/include/grass/defs/gis.h: 670
if hasattr(_libs['grass_gis.7.4.1'], 'G__read_Cell_head_array'):
    G__read_Cell_head_array = _libs['grass_gis.7.4.1'].G__read_Cell_head_array
    G__read_Cell_head_array.restype = None
    G__read_Cell_head_array.argtypes = [POINTER(POINTER(c_char)), POINTER(struct_Cell_head), c_int]

# C:/msys64/usr/src/grass741/dist.x86_64-w64-mingw32/include/grass/defs/gis.h: 673
if hasattr(_libs['grass_gis.7.4.1'], 'G_remove'):
    G_remove = _libs['grass_gis.7.4.1'].G_remove
    G_remove.restype = c_int
    G_remove.argtypes = [String, String]

# C:/msys64/usr/src/grass741/dist.x86_64-w64-mingw32/include/grass/defs/gis.h: 674
if hasattr(_libs['grass_gis.7.4.1'], 'G_remove_misc'):
    G_remove_misc = _libs['grass_gis.7.4.1'].G_remove_misc
    G_remove_misc.restype = c_int
    G_remove_misc.argtypes = [String, String, String]

# C:/msys64/usr/src/grass741/dist.x86_64-w64-mingw32/include/grass/defs/gis.h: 675
if hasattr(_libs['grass_gis.7.4.1'], 'G_recursive_remove'):
    G_recursive_remove = _libs['grass_gis.7.4.1'].G_recursive_remove
    G_recursive_remove.restype = c_int
    G_recursive_remove.argtypes = [String]

# C:/msys64/usr/src/grass741/dist.x86_64-w64-mingw32/include/grass/defs/gis.h: 678
if hasattr(_libs['grass_gis.7.4.1'], 'G_rename_file'):
    G_rename_file = _libs['grass_gis.7.4.1'].G_rename_file
    G_rename_file.restype = c_int
    G_rename_file.argtypes = [String, String]

# C:/msys64/usr/src/grass741/dist.x86_64-w64-mingw32/include/grass/defs/gis.h: 679
if hasattr(_libs['grass_gis.7.4.1'], 'G_rename'):
    G_rename = _libs['grass_gis.7.4.1'].G_rename
    G_rename.restype = c_int
    G_rename.argtypes = [String, String, String]

# C:/msys64/usr/src/grass741/dist.x86_64-w64-mingw32/include/grass/defs/gis.h: 682
if hasattr(_libs['grass_gis.7.4.1'], 'G_begin_rhumbline_equation'):
    G_begin_rhumbline_equation = _libs['grass_gis.7.4.1'].G_begin_rhumbline_equation
    G_begin_rhumbline_equation.restype = c_int
    G_begin_rhumbline_equation.argtypes = [c_double, c_double, c_double, c_double]

# C:/msys64/usr/src/grass741/dist.x86_64-w64-mingw32/include/grass/defs/gis.h: 683
if hasattr(_libs['grass_gis.7.4.1'], 'G_rhumbline_lat_from_lon'):
    G_rhumbline_lat_from_lon = _libs['grass_gis.7.4.1'].G_rhumbline_lat_from_lon
    G_rhumbline_lat_from_lon.restype = c_double
    G_rhumbline_lat_from_lon.argtypes = [c_double]

# C:/msys64/usr/src/grass741/dist.x86_64-w64-mingw32/include/grass/defs/gis.h: 686
if hasattr(_libs['grass_gis.7.4.1'], 'G_rotate_around_point'):
    G_rotate_around_point = _libs['grass_gis.7.4.1'].G_rotate_around_point
    G_rotate_around_point.restype = None
    G_rotate_around_point.argtypes = [c_double, c_double, POINTER(c_double), POINTER(c_double), c_double]

# C:/msys64/usr/src/grass741/dist.x86_64-w64-mingw32/include/grass/defs/gis.h: 687
if hasattr(_libs['grass_gis.7.4.1'], 'G_rotate_around_point_int'):
    G_rotate_around_point_int = _libs['grass_gis.7.4.1'].G_rotate_around_point_int
    G_rotate_around_point_int.restype = None
    G_rotate_around_point_int.argtypes = [c_int, c_int, POINTER(c_int), POINTER(c_int), c_double]

# C:/msys64/usr/src/grass741/dist.x86_64-w64-mingw32/include/grass/defs/gis.h: 690
if hasattr(_libs['grass_gis.7.4.1'], 'G_ftell'):
    G_ftell = _libs['grass_gis.7.4.1'].G_ftell
    G_ftell.restype = off_t
    G_ftell.argtypes = [POINTER(FILE)]

# C:/msys64/usr/src/grass741/dist.x86_64-w64-mingw32/include/grass/defs/gis.h: 691
if hasattr(_libs['grass_gis.7.4.1'], 'G_fseek'):
    G_fseek = _libs['grass_gis.7.4.1'].G_fseek
    G_fseek.restype = None
    G_fseek.argtypes = [POINTER(FILE), off_t, c_int]

# C:/msys64/usr/src/grass741/dist.x86_64-w64-mingw32/include/grass/defs/gis.h: 694
if hasattr(_libs['grass_gis.7.4.1'], 'G_get_set_window'):
    G_get_set_window = _libs['grass_gis.7.4.1'].G_get_set_window
    G_get_set_window.restype = None
    G_get_set_window.argtypes = [POINTER(struct_Cell_head)]

# C:/msys64/usr/src/grass741/dist.x86_64-w64-mingw32/include/grass/defs/gis.h: 695
if hasattr(_libs['grass_gis.7.4.1'], 'G_set_window'):
    G_set_window = _libs['grass_gis.7.4.1'].G_set_window
    G_set_window.restype = None
    G_set_window.argtypes = [POINTER(struct_Cell_head)]

# C:/msys64/usr/src/grass741/dist.x86_64-w64-mingw32/include/grass/defs/gis.h: 696
if hasattr(_libs['grass_gis.7.4.1'], 'G_unset_window'):
    G_unset_window = _libs['grass_gis.7.4.1'].G_unset_window
    G_unset_window.restype = None
    G_unset_window.argtypes = []

# C:/msys64/usr/src/grass741/dist.x86_64-w64-mingw32/include/grass/defs/gis.h: 699
if hasattr(_libs['grass_gis.7.4.1'], 'G_shortest_way'):
    G_shortest_way = _libs['grass_gis.7.4.1'].G_shortest_way
    G_shortest_way.restype = None
    G_shortest_way.argtypes = [POINTER(c_double), POINTER(c_double)]

# C:/msys64/usr/src/grass741/dist.x86_64-w64-mingw32/include/grass/defs/gis.h: 702
if hasattr(_libs['grass_gis.7.4.1'], 'G_sleep'):
    G_sleep = _libs['grass_gis.7.4.1'].G_sleep
    G_sleep.restype = None
    G_sleep.argtypes = [c_uint]

# C:/msys64/usr/src/grass741/dist.x86_64-w64-mingw32/include/grass/defs/gis.h: 705
if hasattr(_libs['grass_gis.7.4.1'], 'G_snprintf'):
    _func = _libs['grass_gis.7.4.1'].G_snprintf
    _restype = c_int
    _argtypes = [String, c_size_t, String]
    G_snprintf = _variadic_function(_func,_restype,_argtypes)

# C:/msys64/usr/src/grass741/dist.x86_64-w64-mingw32/include/grass/defs/gis.h: 709
if hasattr(_libs['grass_gis.7.4.1'], 'G_strcasecmp'):
    G_strcasecmp = _libs['grass_gis.7.4.1'].G_strcasecmp
    G_strcasecmp.restype = c_int
    G_strcasecmp.argtypes = [String, String]

# C:/msys64/usr/src/grass741/dist.x86_64-w64-mingw32/include/grass/defs/gis.h: 710
if hasattr(_libs['grass_gis.7.4.1'], 'G_strncasecmp'):
    G_strncasecmp = _libs['grass_gis.7.4.1'].G_strncasecmp
    G_strncasecmp.restype = c_int
    G_strncasecmp.argtypes = [String, String, c_int]

# C:/msys64/usr/src/grass741/dist.x86_64-w64-mingw32/include/grass/defs/gis.h: 711
if hasattr(_libs['grass_gis.7.4.1'], 'G_store'):
    G_store = _libs['grass_gis.7.4.1'].G_store
    G_store.restype = ReturnString
    G_store.argtypes = [String]

# C:/msys64/usr/src/grass741/dist.x86_64-w64-mingw32/include/grass/defs/gis.h: 712
if hasattr(_libs['grass_gis.7.4.1'], 'G_store_upper'):
    G_store_upper = _libs['grass_gis.7.4.1'].G_store_upper
    G_store_upper.restype = ReturnString
    G_store_upper.argtypes = [String]

# C:/msys64/usr/src/grass741/dist.x86_64-w64-mingw32/include/grass/defs/gis.h: 713
if hasattr(_libs['grass_gis.7.4.1'], 'G_store_lower'):
    G_store_lower = _libs['grass_gis.7.4.1'].G_store_lower
    G_store_lower.restype = ReturnString
    G_store_lower.argtypes = [String]

# C:/msys64/usr/src/grass741/dist.x86_64-w64-mingw32/include/grass/defs/gis.h: 714
if hasattr(_libs['grass_gis.7.4.1'], 'G_strchg'):
    G_strchg = _libs['grass_gis.7.4.1'].G_strchg
    G_strchg.restype = ReturnString
    G_strchg.argtypes = [String, c_char, c_char]

# C:/msys64/usr/src/grass741/dist.x86_64-w64-mingw32/include/grass/defs/gis.h: 715
if hasattr(_libs['grass_gis.7.4.1'], 'G_str_replace'):
    G_str_replace = _libs['grass_gis.7.4.1'].G_str_replace
    G_str_replace.restype = ReturnString
    G_str_replace.argtypes = [String, String, String]

# C:/msys64/usr/src/grass741/dist.x86_64-w64-mingw32/include/grass/defs/gis.h: 716
if hasattr(_libs['grass_gis.7.4.1'], 'G_strip'):
    G_strip = _libs['grass_gis.7.4.1'].G_strip
    G_strip.restype = None
    G_strip.argtypes = [String]

# C:/msys64/usr/src/grass741/dist.x86_64-w64-mingw32/include/grass/defs/gis.h: 717
if hasattr(_libs['grass_gis.7.4.1'], 'G_chop'):
    G_chop = _libs['grass_gis.7.4.1'].G_chop
    G_chop.restype = ReturnString
    G_chop.argtypes = [String]

# C:/msys64/usr/src/grass741/dist.x86_64-w64-mingw32/include/grass/defs/gis.h: 718
if hasattr(_libs['grass_gis.7.4.1'], 'G_str_to_upper'):
    G_str_to_upper = _libs['grass_gis.7.4.1'].G_str_to_upper
    G_str_to_upper.restype = None
    G_str_to_upper.argtypes = [String]

# C:/msys64/usr/src/grass741/dist.x86_64-w64-mingw32/include/grass/defs/gis.h: 719
if hasattr(_libs['grass_gis.7.4.1'], 'G_str_to_lower'):
    G_str_to_lower = _libs['grass_gis.7.4.1'].G_str_to_lower
    G_str_to_lower.restype = None
    G_str_to_lower.argtypes = [String]

# C:/msys64/usr/src/grass741/dist.x86_64-w64-mingw32/include/grass/defs/gis.h: 720
if hasattr(_libs['grass_gis.7.4.1'], 'G_str_to_sql'):
    G_str_to_sql = _libs['grass_gis.7.4.1'].G_str_to_sql
    G_str_to_sql.restype = c_int
    G_str_to_sql.argtypes = [String]

# C:/msys64/usr/src/grass741/dist.x86_64-w64-mingw32/include/grass/defs/gis.h: 721
if hasattr(_libs['grass_gis.7.4.1'], 'G_squeeze'):
    G_squeeze = _libs['grass_gis.7.4.1'].G_squeeze
    G_squeeze.restype = None
    G_squeeze.argtypes = [String]

# C:/msys64/usr/src/grass741/dist.x86_64-w64-mingw32/include/grass/defs/gis.h: 722
if hasattr(_libs['grass_gis.7.4.1'], 'G_strcasestr'):
    G_strcasestr = _libs['grass_gis.7.4.1'].G_strcasestr
    G_strcasestr.restype = ReturnString
    G_strcasestr.argtypes = [String, String]

# C:/msys64/usr/src/grass741/dist.x86_64-w64-mingw32/include/grass/defs/gis.h: 725
if hasattr(_libs['grass_gis.7.4.1'], 'G_init_tempfile'):
    G_init_tempfile = _libs['grass_gis.7.4.1'].G_init_tempfile
    G_init_tempfile.restype = None
    G_init_tempfile.argtypes = []

# C:/msys64/usr/src/grass741/dist.x86_64-w64-mingw32/include/grass/defs/gis.h: 726
if hasattr(_libs['grass_gis.7.4.1'], 'G_tempfile'):
    G_tempfile = _libs['grass_gis.7.4.1'].G_tempfile
    G_tempfile.restype = ReturnString
    G_tempfile.argtypes = []

# C:/msys64/usr/src/grass741/dist.x86_64-w64-mingw32/include/grass/defs/gis.h: 727
if hasattr(_libs['grass_gis.7.4.1'], 'G_tempfile_pid'):
    G_tempfile_pid = _libs['grass_gis.7.4.1'].G_tempfile_pid
    G_tempfile_pid.restype = ReturnString
    G_tempfile_pid.argtypes = [c_int]

# C:/msys64/usr/src/grass741/dist.x86_64-w64-mingw32/include/grass/defs/gis.h: 728
if hasattr(_libs['grass_gis.7.4.1'], 'G_temp_element'):
    G_temp_element = _libs['grass_gis.7.4.1'].G_temp_element
    G_temp_element.restype = None
    G_temp_element.argtypes = [String]

# C:/msys64/usr/src/grass741/dist.x86_64-w64-mingw32/include/grass/defs/gis.h: 729
if hasattr(_libs['grass_gis.7.4.1'], 'G__temp_element'):
    G__temp_element = _libs['grass_gis.7.4.1'].G__temp_element
    G__temp_element.restype = None
    G__temp_element.argtypes = [String, c_int]

# C:/msys64/usr/src/grass741/dist.x86_64-w64-mingw32/include/grass/defs/gis.h: 732
if hasattr(_libs['grass_gis.7.4.1'], 'G_mktemp'):
    G_mktemp = _libs['grass_gis.7.4.1'].G_mktemp
    G_mktemp.restype = ReturnString
    G_mktemp.argtypes = [String]

# C:/msys64/usr/src/grass741/dist.x86_64-w64-mingw32/include/grass/defs/gis.h: 733
if hasattr(_libs['grass_gis.7.4.1'], 'G_mkstemp'):
    G_mkstemp = _libs['grass_gis.7.4.1'].G_mkstemp
    G_mkstemp.restype = c_int
    G_mkstemp.argtypes = [String, c_int, c_int]

# C:/msys64/usr/src/grass741/dist.x86_64-w64-mingw32/include/grass/defs/gis.h: 734
if hasattr(_libs['grass_gis.7.4.1'], 'G_mkstemp_fp'):
    G_mkstemp_fp = _libs['grass_gis.7.4.1'].G_mkstemp_fp
    G_mkstemp_fp.restype = POINTER(FILE)
    G_mkstemp_fp.argtypes = [String, c_int, c_int]

# C:/msys64/usr/src/grass741/dist.x86_64-w64-mingw32/include/grass/defs/gis.h: 737
if hasattr(_libs['grass_gis.7.4.1'], 'G_init_timestamp'):
    G_init_timestamp = _libs['grass_gis.7.4.1'].G_init_timestamp
    G_init_timestamp.restype = None
    G_init_timestamp.argtypes = [POINTER(struct_TimeStamp)]

# C:/msys64/usr/src/grass741/dist.x86_64-w64-mingw32/include/grass/defs/gis.h: 738
if hasattr(_libs['grass_gis.7.4.1'], 'G_set_timestamp'):
    G_set_timestamp = _libs['grass_gis.7.4.1'].G_set_timestamp
    G_set_timestamp.restype = None
    G_set_timestamp.argtypes = [POINTER(struct_TimeStamp), POINTER(struct_DateTime)]

# C:/msys64/usr/src/grass741/dist.x86_64-w64-mingw32/include/grass/defs/gis.h: 739
if hasattr(_libs['grass_gis.7.4.1'], 'G_set_timestamp_range'):
    G_set_timestamp_range = _libs['grass_gis.7.4.1'].G_set_timestamp_range
    G_set_timestamp_range.restype = None
    G_set_timestamp_range.argtypes = [POINTER(struct_TimeStamp), POINTER(struct_DateTime), POINTER(struct_DateTime)]

# C:/msys64/usr/src/grass741/dist.x86_64-w64-mingw32/include/grass/defs/gis.h: 741
if hasattr(_libs['grass_gis.7.4.1'], 'G_write_timestamp'):
    G_write_timestamp = _libs['grass_gis.7.4.1'].G_write_timestamp
    G_write_timestamp.restype = c_int
    G_write_timestamp.argtypes = [POINTER(FILE), POINTER(struct_TimeStamp)]

# C:/msys64/usr/src/grass741/dist.x86_64-w64-mingw32/include/grass/defs/gis.h: 742
if hasattr(_libs['grass_gis.7.4.1'], 'G_get_timestamps'):
    G_get_timestamps = _libs['grass_gis.7.4.1'].G_get_timestamps
    G_get_timestamps.restype = None
    G_get_timestamps.argtypes = [POINTER(struct_TimeStamp), POINTER(struct_DateTime), POINTER(struct_DateTime), POINTER(c_int)]

# C:/msys64/usr/src/grass741/dist.x86_64-w64-mingw32/include/grass/defs/gis.h: 743
if hasattr(_libs['grass_gis.7.4.1'], 'G_format_timestamp'):
    G_format_timestamp = _libs['grass_gis.7.4.1'].G_format_timestamp
    G_format_timestamp.restype = c_int
    G_format_timestamp.argtypes = [POINTER(struct_TimeStamp), String]

# C:/msys64/usr/src/grass741/dist.x86_64-w64-mingw32/include/grass/defs/gis.h: 744
if hasattr(_libs['grass_gis.7.4.1'], 'G_scan_timestamp'):
    G_scan_timestamp = _libs['grass_gis.7.4.1'].G_scan_timestamp
    G_scan_timestamp.restype = c_int
    G_scan_timestamp.argtypes = [POINTER(struct_TimeStamp), String]

# C:/msys64/usr/src/grass741/dist.x86_64-w64-mingw32/include/grass/defs/gis.h: 745
if hasattr(_libs['grass_gis.7.4.1'], 'G_has_raster_timestamp'):
    G_has_raster_timestamp = _libs['grass_gis.7.4.1'].G_has_raster_timestamp
    G_has_raster_timestamp.restype = c_int
    G_has_raster_timestamp.argtypes = [String, String]

# C:/msys64/usr/src/grass741/dist.x86_64-w64-mingw32/include/grass/defs/gis.h: 746
if hasattr(_libs['grass_gis.7.4.1'], 'G_read_raster_timestamp'):
    G_read_raster_timestamp = _libs['grass_gis.7.4.1'].G_read_raster_timestamp
    G_read_raster_timestamp.restype = c_int
    G_read_raster_timestamp.argtypes = [String, String, POINTER(struct_TimeStamp)]

# C:/msys64/usr/src/grass741/dist.x86_64-w64-mingw32/include/grass/defs/gis.h: 747
if hasattr(_libs['grass_gis.7.4.1'], 'G_write_raster_timestamp'):
    G_write_raster_timestamp = _libs['grass_gis.7.4.1'].G_write_raster_timestamp
    G_write_raster_timestamp.restype = c_int
    G_write_raster_timestamp.argtypes = [String, POINTER(struct_TimeStamp)]

# C:/msys64/usr/src/grass741/dist.x86_64-w64-mingw32/include/grass/defs/gis.h: 748
if hasattr(_libs['grass_gis.7.4.1'], 'G_remove_raster_timestamp'):
    G_remove_raster_timestamp = _libs['grass_gis.7.4.1'].G_remove_raster_timestamp
    G_remove_raster_timestamp.restype = c_int
    G_remove_raster_timestamp.argtypes = [String]

# C:/msys64/usr/src/grass741/dist.x86_64-w64-mingw32/include/grass/defs/gis.h: 749
if hasattr(_libs['grass_gis.7.4.1'], 'G_has_vector_timestamp'):
    G_has_vector_timestamp = _libs['grass_gis.7.4.1'].G_has_vector_timestamp
    G_has_vector_timestamp.restype = c_int
    G_has_vector_timestamp.argtypes = [String, String, String]

# C:/msys64/usr/src/grass741/dist.x86_64-w64-mingw32/include/grass/defs/gis.h: 750
if hasattr(_libs['grass_gis.7.4.1'], 'G_read_vector_timestamp'):
    G_read_vector_timestamp = _libs['grass_gis.7.4.1'].G_read_vector_timestamp
    G_read_vector_timestamp.restype = c_int
    G_read_vector_timestamp.argtypes = [String, String, String, POINTER(struct_TimeStamp)]

# C:/msys64/usr/src/grass741/dist.x86_64-w64-mingw32/include/grass/defs/gis.h: 751
if hasattr(_libs['grass_gis.7.4.1'], 'G_write_vector_timestamp'):
    G_write_vector_timestamp = _libs['grass_gis.7.4.1'].G_write_vector_timestamp
    G_write_vector_timestamp.restype = c_int
    G_write_vector_timestamp.argtypes = [String, String, POINTER(struct_TimeStamp)]

# C:/msys64/usr/src/grass741/dist.x86_64-w64-mingw32/include/grass/defs/gis.h: 752
if hasattr(_libs['grass_gis.7.4.1'], 'G_remove_vector_timestamp'):
    G_remove_vector_timestamp = _libs['grass_gis.7.4.1'].G_remove_vector_timestamp
    G_remove_vector_timestamp.restype = c_int
    G_remove_vector_timestamp.argtypes = [String, String]

# C:/msys64/usr/src/grass741/dist.x86_64-w64-mingw32/include/grass/defs/gis.h: 753
if hasattr(_libs['grass_gis.7.4.1'], 'G_has_raster3d_timestamp'):
    G_has_raster3d_timestamp = _libs['grass_gis.7.4.1'].G_has_raster3d_timestamp
    G_has_raster3d_timestamp.restype = c_int
    G_has_raster3d_timestamp.argtypes = [String, String]

# C:/msys64/usr/src/grass741/dist.x86_64-w64-mingw32/include/grass/defs/gis.h: 754
if hasattr(_libs['grass_gis.7.4.1'], 'G_read_raster3d_timestamp'):
    G_read_raster3d_timestamp = _libs['grass_gis.7.4.1'].G_read_raster3d_timestamp
    G_read_raster3d_timestamp.restype = c_int
    G_read_raster3d_timestamp.argtypes = [String, String, POINTER(struct_TimeStamp)]

# C:/msys64/usr/src/grass741/dist.x86_64-w64-mingw32/include/grass/defs/gis.h: 755
if hasattr(_libs['grass_gis.7.4.1'], 'G_remove_raster3d_timestamp'):
    G_remove_raster3d_timestamp = _libs['grass_gis.7.4.1'].G_remove_raster3d_timestamp
    G_remove_raster3d_timestamp.restype = c_int
    G_remove_raster3d_timestamp.argtypes = [String]

# C:/msys64/usr/src/grass741/dist.x86_64-w64-mingw32/include/grass/defs/gis.h: 756
if hasattr(_libs['grass_gis.7.4.1'], 'G_write_raster3d_timestamp'):
    G_write_raster3d_timestamp = _libs['grass_gis.7.4.1'].G_write_raster3d_timestamp
    G_write_raster3d_timestamp.restype = c_int
    G_write_raster3d_timestamp.argtypes = [String, POINTER(struct_TimeStamp)]

# C:/msys64/usr/src/grass741/dist.x86_64-w64-mingw32/include/grass/defs/gis.h: 759
if hasattr(_libs['grass_gis.7.4.1'], 'G_tokenize'):
    G_tokenize = _libs['grass_gis.7.4.1'].G_tokenize
    G_tokenize.restype = POINTER(POINTER(c_char))
    G_tokenize.argtypes = [String, String]

# C:/msys64/usr/src/grass741/dist.x86_64-w64-mingw32/include/grass/defs/gis.h: 760
if hasattr(_libs['grass_gis.7.4.1'], 'G_tokenize2'):
    G_tokenize2 = _libs['grass_gis.7.4.1'].G_tokenize2
    G_tokenize2.restype = POINTER(POINTER(c_char))
    G_tokenize2.argtypes = [String, String, String]

# C:/msys64/usr/src/grass741/dist.x86_64-w64-mingw32/include/grass/defs/gis.h: 761
if hasattr(_libs['grass_gis.7.4.1'], 'G_number_of_tokens'):
    G_number_of_tokens = _libs['grass_gis.7.4.1'].G_number_of_tokens
    G_number_of_tokens.restype = c_int
    G_number_of_tokens.argtypes = [POINTER(POINTER(c_char))]

# C:/msys64/usr/src/grass741/dist.x86_64-w64-mingw32/include/grass/defs/gis.h: 762
if hasattr(_libs['grass_gis.7.4.1'], 'G_free_tokens'):
    G_free_tokens = _libs['grass_gis.7.4.1'].G_free_tokens
    G_free_tokens.restype = None
    G_free_tokens.argtypes = [POINTER(POINTER(c_char))]

# C:/msys64/usr/src/grass741/dist.x86_64-w64-mingw32/include/grass/defs/gis.h: 765
if hasattr(_libs['grass_gis.7.4.1'], 'G_trim_decimal'):
    G_trim_decimal = _libs['grass_gis.7.4.1'].G_trim_decimal
    G_trim_decimal.restype = None
    G_trim_decimal.argtypes = [String]

# C:/msys64/usr/src/grass741/dist.x86_64-w64-mingw32/include/grass/defs/gis.h: 768
if hasattr(_libs['grass_gis.7.4.1'], 'G_meters_to_units_factor'):
    G_meters_to_units_factor = _libs['grass_gis.7.4.1'].G_meters_to_units_factor
    G_meters_to_units_factor.restype = c_double
    G_meters_to_units_factor.argtypes = [c_int]

# C:/msys64/usr/src/grass741/dist.x86_64-w64-mingw32/include/grass/defs/gis.h: 769
if hasattr(_libs['grass_gis.7.4.1'], 'G_meters_to_units_factor_sq'):
    G_meters_to_units_factor_sq = _libs['grass_gis.7.4.1'].G_meters_to_units_factor_sq
    G_meters_to_units_factor_sq.restype = c_double
    G_meters_to_units_factor_sq.argtypes = [c_int]

# C:/msys64/usr/src/grass741/dist.x86_64-w64-mingw32/include/grass/defs/gis.h: 770
if hasattr(_libs['grass_gis.7.4.1'], 'G_get_units_name'):
    G_get_units_name = _libs['grass_gis.7.4.1'].G_get_units_name
    G_get_units_name.restype = ReturnString
    G_get_units_name.argtypes = [c_int, c_int, c_int]

# C:/msys64/usr/src/grass741/dist.x86_64-w64-mingw32/include/grass/defs/gis.h: 771
if hasattr(_libs['grass_gis.7.4.1'], 'G_units'):
    G_units = _libs['grass_gis.7.4.1'].G_units
    G_units.restype = c_int
    G_units.argtypes = [String]

# C:/msys64/usr/src/grass741/dist.x86_64-w64-mingw32/include/grass/defs/gis.h: 772
if hasattr(_libs['grass_gis.7.4.1'], 'G_is_units_type_spatial'):
    G_is_units_type_spatial = _libs['grass_gis.7.4.1'].G_is_units_type_spatial
    G_is_units_type_spatial.restype = c_int
    G_is_units_type_spatial.argtypes = [c_int]

# C:/msys64/usr/src/grass741/dist.x86_64-w64-mingw32/include/grass/defs/gis.h: 773
if hasattr(_libs['grass_gis.7.4.1'], 'G_is_units_type_temporal'):
    G_is_units_type_temporal = _libs['grass_gis.7.4.1'].G_is_units_type_temporal
    G_is_units_type_temporal.restype = c_int
    G_is_units_type_temporal.argtypes = [c_int]

# C:/msys64/usr/src/grass741/dist.x86_64-w64-mingw32/include/grass/defs/gis.h: 781
if hasattr(_libs['grass_gis.7.4.1'], 'G_verbose'):
    G_verbose = _libs['grass_gis.7.4.1'].G_verbose
    G_verbose.restype = c_int
    G_verbose.argtypes = []

# C:/msys64/usr/src/grass741/dist.x86_64-w64-mingw32/include/grass/defs/gis.h: 782
if hasattr(_libs['grass_gis.7.4.1'], 'G_verbose_min'):
    G_verbose_min = _libs['grass_gis.7.4.1'].G_verbose_min
    G_verbose_min.restype = c_int
    G_verbose_min.argtypes = []

# C:/msys64/usr/src/grass741/dist.x86_64-w64-mingw32/include/grass/defs/gis.h: 783
if hasattr(_libs['grass_gis.7.4.1'], 'G_verbose_std'):
    G_verbose_std = _libs['grass_gis.7.4.1'].G_verbose_std
    G_verbose_std.restype = c_int
    G_verbose_std.argtypes = []

# C:/msys64/usr/src/grass741/dist.x86_64-w64-mingw32/include/grass/defs/gis.h: 784
if hasattr(_libs['grass_gis.7.4.1'], 'G_verbose_max'):
    G_verbose_max = _libs['grass_gis.7.4.1'].G_verbose_max
    G_verbose_max.restype = c_int
    G_verbose_max.argtypes = []

# C:/msys64/usr/src/grass741/dist.x86_64-w64-mingw32/include/grass/defs/gis.h: 785
if hasattr(_libs['grass_gis.7.4.1'], 'G_set_verbose'):
    G_set_verbose = _libs['grass_gis.7.4.1'].G_set_verbose
    G_set_verbose.restype = c_int
    G_set_verbose.argtypes = [c_int]

# C:/msys64/usr/src/grass741/dist.x86_64-w64-mingw32/include/grass/defs/gis.h: 788
if hasattr(_libs['grass_gis.7.4.1'], 'G_3dview_warning'):
    G_3dview_warning = _libs['grass_gis.7.4.1'].G_3dview_warning
    G_3dview_warning.restype = None
    G_3dview_warning.argtypes = [c_int]

# C:/msys64/usr/src/grass741/dist.x86_64-w64-mingw32/include/grass/defs/gis.h: 789
if hasattr(_libs['grass_gis.7.4.1'], 'G_get_3dview_defaults'):
    G_get_3dview_defaults = _libs['grass_gis.7.4.1'].G_get_3dview_defaults
    G_get_3dview_defaults.restype = c_int
    G_get_3dview_defaults.argtypes = [POINTER(struct_G_3dview), POINTER(struct_Cell_head)]

# C:/msys64/usr/src/grass741/dist.x86_64-w64-mingw32/include/grass/defs/gis.h: 790
if hasattr(_libs['grass_gis.7.4.1'], 'G_put_3dview'):
    G_put_3dview = _libs['grass_gis.7.4.1'].G_put_3dview
    G_put_3dview.restype = c_int
    G_put_3dview.argtypes = [String, String, POINTER(struct_G_3dview), POINTER(struct_Cell_head)]

# C:/msys64/usr/src/grass741/dist.x86_64-w64-mingw32/include/grass/defs/gis.h: 792
if hasattr(_libs['grass_gis.7.4.1'], 'G_get_3dview'):
    G_get_3dview = _libs['grass_gis.7.4.1'].G_get_3dview
    G_get_3dview.restype = c_int
    G_get_3dview.argtypes = [String, String, POINTER(struct_G_3dview)]

# C:/msys64/usr/src/grass741/dist.x86_64-w64-mingw32/include/grass/defs/gis.h: 795
if hasattr(_libs['grass_gis.7.4.1'], 'G_whoami'):
    G_whoami = _libs['grass_gis.7.4.1'].G_whoami
    G_whoami.restype = ReturnString
    G_whoami.argtypes = []

# C:/msys64/usr/src/grass741/dist.x86_64-w64-mingw32/include/grass/defs/gis.h: 798
if hasattr(_libs['grass_gis.7.4.1'], 'G_adjust_window_to_box'):
    G_adjust_window_to_box = _libs['grass_gis.7.4.1'].G_adjust_window_to_box
    G_adjust_window_to_box.restype = None
    G_adjust_window_to_box.argtypes = [POINTER(struct_Cell_head), POINTER(struct_Cell_head), c_int, c_int]

# C:/msys64/usr/src/grass741/dist.x86_64-w64-mingw32/include/grass/defs/gis.h: 802
if hasattr(_libs['grass_gis.7.4.1'], 'G_format_northing'):
    G_format_northing = _libs['grass_gis.7.4.1'].G_format_northing
    G_format_northing.restype = None
    G_format_northing.argtypes = [c_double, String, c_int]

# C:/msys64/usr/src/grass741/dist.x86_64-w64-mingw32/include/grass/defs/gis.h: 803
if hasattr(_libs['grass_gis.7.4.1'], 'G_format_easting'):
    G_format_easting = _libs['grass_gis.7.4.1'].G_format_easting
    G_format_easting.restype = None
    G_format_easting.argtypes = [c_double, String, c_int]

# C:/msys64/usr/src/grass741/dist.x86_64-w64-mingw32/include/grass/defs/gis.h: 804
if hasattr(_libs['grass_gis.7.4.1'], 'G_format_resolution'):
    G_format_resolution = _libs['grass_gis.7.4.1'].G_format_resolution
    G_format_resolution.restype = None
    G_format_resolution.argtypes = [c_double, String, c_int]

# C:/msys64/usr/src/grass741/dist.x86_64-w64-mingw32/include/grass/defs/gis.h: 807
if hasattr(_libs['grass_gis.7.4.1'], 'G_point_in_region'):
    G_point_in_region = _libs['grass_gis.7.4.1'].G_point_in_region
    G_point_in_region.restype = c_int
    G_point_in_region.argtypes = [c_double, c_double]

# C:/msys64/usr/src/grass741/dist.x86_64-w64-mingw32/include/grass/defs/gis.h: 808
if hasattr(_libs['grass_gis.7.4.1'], 'G_point_in_window'):
    G_point_in_window = _libs['grass_gis.7.4.1'].G_point_in_window
    G_point_in_window.restype = c_int
    G_point_in_window.argtypes = [c_double, c_double, POINTER(struct_Cell_head)]

# C:/msys64/usr/src/grass741/dist.x86_64-w64-mingw32/include/grass/defs/gis.h: 811
if hasattr(_libs['grass_gis.7.4.1'], 'G_limit_east'):
    G_limit_east = _libs['grass_gis.7.4.1'].G_limit_east
    G_limit_east.restype = c_int
    G_limit_east.argtypes = [POINTER(c_double), c_int]

# C:/msys64/usr/src/grass741/dist.x86_64-w64-mingw32/include/grass/defs/gis.h: 812
if hasattr(_libs['grass_gis.7.4.1'], 'G_limit_west'):
    G_limit_west = _libs['grass_gis.7.4.1'].G_limit_west
    G_limit_west.restype = c_int
    G_limit_west.argtypes = [POINTER(c_double), c_int]

# C:/msys64/usr/src/grass741/dist.x86_64-w64-mingw32/include/grass/defs/gis.h: 813
if hasattr(_libs['grass_gis.7.4.1'], 'G_limit_north'):
    G_limit_north = _libs['grass_gis.7.4.1'].G_limit_north
    G_limit_north.restype = c_int
    G_limit_north.argtypes = [POINTER(c_double), c_int]

# C:/msys64/usr/src/grass741/dist.x86_64-w64-mingw32/include/grass/defs/gis.h: 814
if hasattr(_libs['grass_gis.7.4.1'], 'G_limit_south'):
    G_limit_south = _libs['grass_gis.7.4.1'].G_limit_south
    G_limit_south.restype = c_int
    G_limit_south.argtypes = [POINTER(c_double), c_int]

# C:/msys64/usr/src/grass741/dist.x86_64-w64-mingw32/include/grass/defs/gis.h: 817
if hasattr(_libs['grass_gis.7.4.1'], 'G_window_overlap'):
    G_window_overlap = _libs['grass_gis.7.4.1'].G_window_overlap
    G_window_overlap.restype = c_int
    G_window_overlap.argtypes = [POINTER(struct_Cell_head), c_double, c_double, c_double, c_double]

# C:/msys64/usr/src/grass741/dist.x86_64-w64-mingw32/include/grass/defs/gis.h: 819
if hasattr(_libs['grass_gis.7.4.1'], 'G_window_percentage_overlap'):
    G_window_percentage_overlap = _libs['grass_gis.7.4.1'].G_window_percentage_overlap
    G_window_percentage_overlap.restype = c_double
    G_window_percentage_overlap.argtypes = [POINTER(struct_Cell_head), c_double, c_double, c_double, c_double]

# C:/msys64/usr/src/grass741/dist.x86_64-w64-mingw32/include/grass/defs/gis.h: 823
if hasattr(_libs['grass_gis.7.4.1'], 'G_scan_northing'):
    G_scan_northing = _libs['grass_gis.7.4.1'].G_scan_northing
    G_scan_northing.restype = c_int
    G_scan_northing.argtypes = [String, POINTER(c_double), c_int]

# C:/msys64/usr/src/grass741/dist.x86_64-w64-mingw32/include/grass/defs/gis.h: 824
if hasattr(_libs['grass_gis.7.4.1'], 'G_scan_easting'):
    G_scan_easting = _libs['grass_gis.7.4.1'].G_scan_easting
    G_scan_easting.restype = c_int
    G_scan_easting.argtypes = [String, POINTER(c_double), c_int]

# C:/msys64/usr/src/grass741/dist.x86_64-w64-mingw32/include/grass/defs/gis.h: 825
if hasattr(_libs['grass_gis.7.4.1'], 'G_scan_resolution'):
    G_scan_resolution = _libs['grass_gis.7.4.1'].G_scan_resolution
    G_scan_resolution.restype = c_int
    G_scan_resolution.argtypes = [String, POINTER(c_double), c_int]

# C:/msys64/usr/src/grass741/dist.x86_64-w64-mingw32/include/grass/defs/gis.h: 828
if hasattr(_libs['grass_gis.7.4.1'], 'G_adjust_east_longitude'):
    G_adjust_east_longitude = _libs['grass_gis.7.4.1'].G_adjust_east_longitude
    G_adjust_east_longitude.restype = c_double
    G_adjust_east_longitude.argtypes = [c_double, c_double]

# C:/msys64/usr/src/grass741/dist.x86_64-w64-mingw32/include/grass/defs/gis.h: 829
if hasattr(_libs['grass_gis.7.4.1'], 'G_adjust_easting'):
    G_adjust_easting = _libs['grass_gis.7.4.1'].G_adjust_easting
    G_adjust_easting.restype = c_double
    G_adjust_easting.argtypes = [c_double, POINTER(struct_Cell_head)]

# C:/msys64/usr/src/grass741/dist.x86_64-w64-mingw32/include/grass/defs/gis.h: 830
if hasattr(_libs['grass_gis.7.4.1'], 'G__init_window'):
    G__init_window = _libs['grass_gis.7.4.1'].G__init_window
    G__init_window.restype = None
    G__init_window.argtypes = []

# C:/msys64/usr/src/grass741/dist.x86_64-w64-mingw32/include/grass/defs/gis.h: 833
if hasattr(_libs['grass_gis.7.4.1'], 'G_begin_execute'):
    G_begin_execute = _libs['grass_gis.7.4.1'].G_begin_execute
    G_begin_execute.restype = None
    G_begin_execute.argtypes = [CFUNCTYPE(UNCHECKED(None), POINTER(None)), POINTER(None), POINTER(POINTER(None)), c_int]

# C:/msys64/usr/src/grass741/dist.x86_64-w64-mingw32/include/grass/defs/gis.h: 834
if hasattr(_libs['grass_gis.7.4.1'], 'G_end_execute'):
    G_end_execute = _libs['grass_gis.7.4.1'].G_end_execute
    G_end_execute.restype = None
    G_end_execute.argtypes = [POINTER(POINTER(None))]

# C:/msys64/usr/src/grass741/dist.x86_64-w64-mingw32/include/grass/defs/gis.h: 835
if hasattr(_libs['grass_gis.7.4.1'], 'G_init_workers'):
    G_init_workers = _libs['grass_gis.7.4.1'].G_init_workers
    G_init_workers.restype = None
    G_init_workers.argtypes = []

# C:/msys64/usr/src/grass741/dist.x86_64-w64-mingw32/include/grass/defs/gis.h: 836
if hasattr(_libs['grass_gis.7.4.1'], 'G_finish_workers'):
    G_finish_workers = _libs['grass_gis.7.4.1'].G_finish_workers
    G_finish_workers.restype = None
    G_finish_workers.argtypes = []

# C:/msys64/usr/src/grass741/dist.x86_64-w64-mingw32/include/grass/defs/gis.h: 839
if hasattr(_libs['grass_gis.7.4.1'], 'G__write_Cell_head'):
    G__write_Cell_head = _libs['grass_gis.7.4.1'].G__write_Cell_head
    G__write_Cell_head.restype = None
    G__write_Cell_head.argtypes = [POINTER(FILE), POINTER(struct_Cell_head), c_int]

# C:/msys64/usr/src/grass741/dist.x86_64-w64-mingw32/include/grass/defs/gis.h: 840
if hasattr(_libs['grass_gis.7.4.1'], 'G__write_Cell_head3'):
    G__write_Cell_head3 = _libs['grass_gis.7.4.1'].G__write_Cell_head3
    G__write_Cell_head3.restype = None
    G__write_Cell_head3.argtypes = [POINTER(FILE), POINTER(struct_Cell_head), c_int]

# C:/msys64/usr/src/grass741/dist.x86_64-w64-mingw32/include/grass/defs/gis.h: 843
if hasattr(_libs['grass_gis.7.4.1'], 'G_write_zeros'):
    G_write_zeros = _libs['grass_gis.7.4.1'].G_write_zeros
    G_write_zeros.restype = None
    G_write_zeros.argtypes = [c_int, c_size_t]

# C:/msys64/usr/src/grass741/dist.x86_64-w64-mingw32/include/grass/defs/gis.h: 846
if hasattr(_libs['grass_gis.7.4.1'], 'G_xdr_get_int'):
    G_xdr_get_int = _libs['grass_gis.7.4.1'].G_xdr_get_int
    G_xdr_get_int.restype = None
    G_xdr_get_int.argtypes = [POINTER(c_int), POINTER(None)]

# C:/msys64/usr/src/grass741/dist.x86_64-w64-mingw32/include/grass/defs/gis.h: 847
if hasattr(_libs['grass_gis.7.4.1'], 'G_xdr_put_int'):
    G_xdr_put_int = _libs['grass_gis.7.4.1'].G_xdr_put_int
    G_xdr_put_int.restype = None
    G_xdr_put_int.argtypes = [POINTER(None), POINTER(c_int)]

# C:/msys64/usr/src/grass741/dist.x86_64-w64-mingw32/include/grass/defs/gis.h: 848
if hasattr(_libs['grass_gis.7.4.1'], 'G_xdr_get_float'):
    G_xdr_get_float = _libs['grass_gis.7.4.1'].G_xdr_get_float
    G_xdr_get_float.restype = None
    G_xdr_get_float.argtypes = [POINTER(c_float), POINTER(None)]

# C:/msys64/usr/src/grass741/dist.x86_64-w64-mingw32/include/grass/defs/gis.h: 849
if hasattr(_libs['grass_gis.7.4.1'], 'G_xdr_put_float'):
    G_xdr_put_float = _libs['grass_gis.7.4.1'].G_xdr_put_float
    G_xdr_put_float.restype = None
    G_xdr_put_float.argtypes = [POINTER(None), POINTER(c_float)]

# C:/msys64/usr/src/grass741/dist.x86_64-w64-mingw32/include/grass/defs/gis.h: 850
if hasattr(_libs['grass_gis.7.4.1'], 'G_xdr_get_double'):
    G_xdr_get_double = _libs['grass_gis.7.4.1'].G_xdr_get_double
    G_xdr_get_double.restype = None
    G_xdr_get_double.argtypes = [POINTER(c_double), POINTER(None)]

# C:/msys64/usr/src/grass741/dist.x86_64-w64-mingw32/include/grass/defs/gis.h: 851
if hasattr(_libs['grass_gis.7.4.1'], 'G_xdr_put_double'):
    G_xdr_put_double = _libs['grass_gis.7.4.1'].G_xdr_put_double
    G_xdr_put_double.restype = None
    G_xdr_put_double.argtypes = [POINTER(None), POINTER(c_double)]

# C:/msys64/usr/src/grass741/dist.x86_64-w64-mingw32/include/grass/defs/gis.h: 854
if hasattr(_libs['grass_gis.7.4.1'], 'G_zero'):
    G_zero = _libs['grass_gis.7.4.1'].G_zero
    G_zero.restype = None
    G_zero.argtypes = [POINTER(None), c_int]

# C:/msys64/usr/src/grass741/dist.x86_64-w64-mingw32/include/grass/defs/gis.h: 857
if hasattr(_libs['grass_gis.7.4.1'], 'G_zone'):
    G_zone = _libs['grass_gis.7.4.1'].G_zone
    G_zone.restype = c_int
    G_zone.argtypes = []

# C:\\msys64\\usr\\src\\grass741\\dist.x86_64-w64-mingw32\\include\\grass\\colors.h: 33
class struct_color_rgb(Structure):
    pass

struct_color_rgb.__slots__ = [
    'r',
    'g',
    'b',
]
struct_color_rgb._fields_ = [
    ('r', c_ubyte),
    ('g', c_ubyte),
    ('b', c_ubyte),
]

# C:\\msys64\\usr\\src\\grass741\\dist.x86_64-w64-mingw32\\include\\grass\\colors.h: 38
class struct_color_name(Structure):
    pass

struct_color_name.__slots__ = [
    'name',
    'number',
]
struct_color_name._fields_ = [
    ('name', String),
    ('number', c_int),
]

# C:/msys64/usr/src/grass741/dist.x86_64-w64-mingw32/include/grass/defs/colors.h: 4
if hasattr(_libs['grass_gis.7.4.1'], 'G_num_standard_colors'):
    G_num_standard_colors = _libs['grass_gis.7.4.1'].G_num_standard_colors
    G_num_standard_colors.restype = c_int
    G_num_standard_colors.argtypes = []

# C:/msys64/usr/src/grass741/dist.x86_64-w64-mingw32/include/grass/defs/colors.h: 5
if hasattr(_libs['grass_gis.7.4.1'], 'G_standard_color_rgb'):
    G_standard_color_rgb = _libs['grass_gis.7.4.1'].G_standard_color_rgb
    G_standard_color_rgb.restype = struct_color_rgb
    G_standard_color_rgb.argtypes = [c_int]

# C:/msys64/usr/src/grass741/dist.x86_64-w64-mingw32/include/grass/defs/colors.h: 6
if hasattr(_libs['grass_gis.7.4.1'], 'G_num_standard_color_names'):
    G_num_standard_color_names = _libs['grass_gis.7.4.1'].G_num_standard_color_names
    G_num_standard_color_names.restype = c_int
    G_num_standard_color_names.argtypes = []

# C:/msys64/usr/src/grass741/dist.x86_64-w64-mingw32/include/grass/defs/colors.h: 7
if hasattr(_libs['grass_gis.7.4.1'], 'G_standard_color_name'):
    G_standard_color_name = _libs['grass_gis.7.4.1'].G_standard_color_name
    G_standard_color_name.restype = POINTER(struct_color_name)
    G_standard_color_name.argtypes = [c_int]

# C:/msys64/usr/src/grass741/dist.x86_64-w64-mingw32/include/grass/defs/colors.h: 8
if hasattr(_libs['grass_gis.7.4.1'], 'G_str_to_color'):
    G_str_to_color = _libs['grass_gis.7.4.1'].G_str_to_color
    G_str_to_color.restype = c_int
    G_str_to_color.argtypes = [String, POINTER(c_int), POINTER(c_int), POINTER(c_int)]

# C:/msys64/usr/src/grass741/dist.x86_64-w64-mingw32/include/grass/datetime.h: 7
try:
    DATETIME_YEAR = 101
except:
    pass

# C:/msys64/usr/src/grass741/dist.x86_64-w64-mingw32/include/grass/datetime.h: 7
try:
    DATETIME_MONTH = 102
except:
    pass

# C:/msys64/usr/src/grass741/dist.x86_64-w64-mingw32/include/grass/datetime.h: 7
try:
    DATETIME_DAY = 103
except:
    pass

# C:/msys64/usr/src/grass741/dist.x86_64-w64-mingw32/include/grass/datetime.h: 7
try:
    DATETIME_HOUR = 104
except:
    pass

# C:/msys64/usr/src/grass741/dist.x86_64-w64-mingw32/include/grass/datetime.h: 7
try:
    DATETIME_MINUTE = 105
except:
    pass

# C:/msys64/usr/src/grass741/dist.x86_64-w64-mingw32/include/grass/datetime.h: 7
try:
    DATETIME_SECOND = 106
except:
    pass

# C:\\msys64\\usr\\src\\grass741\\dist.x86_64-w64-mingw32\\include\\grass\\gis.h: 40
try:
    GIS_H_VERSION = '$Revision: 70829 $'
except:
    pass

# C:\\msys64\\usr\\src\\grass741\\dist.x86_64-w64-mingw32\\include\\grass\\gis.h: 40
try:
    GIS_H_DATE = '$Date: 2017-04-04 09:43:02 +0200 (Tue, 04 Apr 2017) $'
except:
    pass

# C:\\msys64\\usr\\src\\grass741\\dist.x86_64-w64-mingw32\\include\\grass\\gis.h: 41
def G_gisinit(pgm):
    return (G__gisinit (GIS_H_VERSION, pgm))

# C:\\msys64\\usr\\src\\grass741\\dist.x86_64-w64-mingw32\\include\\grass\\gis.h: 41
try:
    G_no_gisinit = (G__no_gisinit (GIS_H_VERSION))
except:
    pass

# C:\\msys64\\usr\\src\\grass741\\dist.x86_64-w64-mingw32\\include\\grass\\gis.h: 44
try:
    TRUE = 1
except:
    pass

# C:\\msys64\\usr\\src\\grass741\\dist.x86_64-w64-mingw32\\include\\grass\\gis.h: 47
try:
    FALSE = 0
except:
    pass

# C:\\msys64\\usr\\src\\grass741\\dist.x86_64-w64-mingw32\\include\\grass\\gis.h: 50
try:
    PRI_OFF_T = 'lld'
except:
    pass

# C:\\msys64\\usr\\src\\grass741\\dist.x86_64-w64-mingw32\\include\\grass\\gis.h: 55
try:
    NEWLINE = '\\n'
except:
    pass

# C:\\msys64\\usr\\src\\grass741\\dist.x86_64-w64-mingw32\\include\\grass\\gis.h: 56
try:
    HOST_NEWLINE = '\r\n'
except:
    pass

# C:\\msys64\\usr\\src\\grass741\\dist.x86_64-w64-mingw32\\include\\grass\\gis.h: 63
try:
    U_UNDEFINED = (-1)
except:
    pass

# C:\\msys64\\usr\\src\\grass741\\dist.x86_64-w64-mingw32\\include\\grass\\gis.h: 63
try:
    U_UNKNOWN = 0
except:
    pass

# C:\\msys64\\usr\\src\\grass741\\dist.x86_64-w64-mingw32\\include\\grass\\gis.h: 63
try:
    U_ACRES = 1
except:
    pass

# C:\\msys64\\usr\\src\\grass741\\dist.x86_64-w64-mingw32\\include\\grass\\gis.h: 63
try:
    U_HECTARES = 2
except:
    pass

# C:\\msys64\\usr\\src\\grass741\\dist.x86_64-w64-mingw32\\include\\grass\\gis.h: 63
try:
    U_KILOMETERS = 3
except:
    pass

# C:\\msys64\\usr\\src\\grass741\\dist.x86_64-w64-mingw32\\include\\grass\\gis.h: 63
try:
    U_METERS = 4
except:
    pass

# C:\\msys64\\usr\\src\\grass741\\dist.x86_64-w64-mingw32\\include\\grass\\gis.h: 63
try:
    U_MILES = 5
except:
    pass

# C:\\msys64\\usr\\src\\grass741\\dist.x86_64-w64-mingw32\\include\\grass\\gis.h: 63
try:
    U_FEET = 6
except:
    pass

# C:\\msys64\\usr\\src\\grass741\\dist.x86_64-w64-mingw32\\include\\grass\\gis.h: 63
try:
    U_RADIANS = 7
except:
    pass

# C:\\msys64\\usr\\src\\grass741\\dist.x86_64-w64-mingw32\\include\\grass\\gis.h: 63
try:
    U_DEGREES = 8
except:
    pass

# C:\\msys64\\usr\\src\\grass741\\dist.x86_64-w64-mingw32\\include\\grass\\gis.h: 63
try:
    U_USFEET = 9
except:
    pass

# C:\\msys64\\usr\\src\\grass741\\dist.x86_64-w64-mingw32\\include\\grass\\gis.h: 64
try:
    U_YEARS = DATETIME_YEAR
except:
    pass

# C:\\msys64\\usr\\src\\grass741\\dist.x86_64-w64-mingw32\\include\\grass\\gis.h: 64
try:
    U_MONTHS = DATETIME_MONTH
except:
    pass

# C:\\msys64\\usr\\src\\grass741\\dist.x86_64-w64-mingw32\\include\\grass\\gis.h: 64
try:
    U_DAYS = DATETIME_DAY
except:
    pass

# C:\\msys64\\usr\\src\\grass741\\dist.x86_64-w64-mingw32\\include\\grass\\gis.h: 64
try:
    U_HOURS = DATETIME_HOUR
except:
    pass

# C:\\msys64\\usr\\src\\grass741\\dist.x86_64-w64-mingw32\\include\\grass\\gis.h: 64
try:
    U_MINUTES = DATETIME_MINUTE
except:
    pass

# C:\\msys64\\usr\\src\\grass741\\dist.x86_64-w64-mingw32\\include\\grass\\gis.h: 64
try:
    U_SECONDS = DATETIME_SECOND
except:
    pass

# C:\\msys64\\usr\\src\\grass741\\dist.x86_64-w64-mingw32\\include\\grass\\gis.h: 66
try:
    PROJECTION_XY = 0
except:
    pass

# C:\\msys64\\usr\\src\\grass741\\dist.x86_64-w64-mingw32\\include\\grass\\gis.h: 67
try:
    PROJECTION_UTM = 1
except:
    pass

# C:\\msys64\\usr\\src\\grass741\\dist.x86_64-w64-mingw32\\include\\grass\\gis.h: 68
try:
    PROJECTION_SP = 2
except:
    pass

# C:\\msys64\\usr\\src\\grass741\\dist.x86_64-w64-mingw32\\include\\grass\\gis.h: 69
try:
    PROJECTION_LL = 3
except:
    pass

# C:\\msys64\\usr\\src\\grass741\\dist.x86_64-w64-mingw32\\include\\grass\\gis.h: 70
try:
    PROJECTION_OTHER = 99
except:
    pass

# C:\\msys64\\usr\\src\\grass741\\dist.x86_64-w64-mingw32\\include\\grass\\gis.h: 71
try:
    PROJECTION_FILE = 'PROJ_INFO'
except:
    pass

# C:\\msys64\\usr\\src\\grass741\\dist.x86_64-w64-mingw32\\include\\grass\\gis.h: 71
try:
    UNIT_FILE = 'PROJ_UNITS'
except:
    pass

# C:\\msys64\\usr\\src\\grass741\\dist.x86_64-w64-mingw32\\include\\grass\\gis.h: 71
try:
    EPSG_FILE = 'PROJ_EPSG'
except:
    pass

# C:\\msys64\\usr\\src\\grass741\\dist.x86_64-w64-mingw32\\include\\grass\\gis.h: 73
try:
    CONFIG_DIR = 'GRASS7'
except:
    pass

# C:\\msys64\\usr\\src\\grass741\\dist.x86_64-w64-mingw32\\include\\grass\\gis.h: 79
try:
    M_PI = 3.141592653589793
except:
    pass

# C:\\msys64\\usr\\src\\grass741\\dist.x86_64-w64-mingw32\\include\\grass\\gis.h: 81
try:
    M_PI_2 = 1.5707963267948966
except:
    pass

# C:\\msys64\\usr\\src\\grass741\\dist.x86_64-w64-mingw32\\include\\grass\\gis.h: 83
try:
    M_PI_4 = 0.7853981633974483
except:
    pass

# C:\\msys64\\usr\\src\\grass741\\dist.x86_64-w64-mingw32\\include\\grass\\gis.h: 85
try:
    M_R2D = 57.29577951308232
except:
    pass

# C:\\msys64\\usr\\src\\grass741\\dist.x86_64-w64-mingw32\\include\\grass\\gis.h: 87
try:
    M_D2R = 0.017453292519943295
except:
    pass

# C:\\msys64\\usr\\src\\grass741\\dist.x86_64-w64-mingw32\\include\\grass\\gis.h: 89
try:
    GRASS_EPSILON = 1e-15
except:
    pass

# C:\\msys64\\usr\\src\\grass741\\dist.x86_64-w64-mingw32\\include\\grass\\gis.h: 91
try:
    G_VAR_GISRC = 0
except:
    pass

# C:\\msys64\\usr\\src\\grass741\\dist.x86_64-w64-mingw32\\include\\grass\\gis.h: 91
try:
    G_VAR_MAPSET = 1
except:
    pass

# C:\\msys64\\usr\\src\\grass741\\dist.x86_64-w64-mingw32\\include\\grass\\gis.h: 93
try:
    G_GISRC_MODE_FILE = 0
except:
    pass

# C:\\msys64\\usr\\src\\grass741\\dist.x86_64-w64-mingw32\\include\\grass\\gis.h: 93
try:
    G_GISRC_MODE_MEMORY = 1
except:
    pass

# C:\\msys64\\usr\\src\\grass741\\dist.x86_64-w64-mingw32\\include\\grass\\gis.h: 95
try:
    TYPE_INTEGER = 1
except:
    pass

# C:\\msys64\\usr\\src\\grass741\\dist.x86_64-w64-mingw32\\include\\grass\\gis.h: 95
try:
    TYPE_DOUBLE = 2
except:
    pass

# C:\\msys64\\usr\\src\\grass741\\dist.x86_64-w64-mingw32\\include\\grass\\gis.h: 95
try:
    TYPE_STRING = 3
except:
    pass

# C:\\msys64\\usr\\src\\grass741\\dist.x86_64-w64-mingw32\\include\\grass\\gis.h: 95
try:
    YES = 1
except:
    pass

# C:\\msys64\\usr\\src\\grass741\\dist.x86_64-w64-mingw32\\include\\grass\\gis.h: 95
try:
    NO = 0
except:
    pass

# C:\\msys64\\usr\\src\\grass741\\dist.x86_64-w64-mingw32\\include\\grass\\gis.h: 97
try:
    GNAME_MAX = 256
except:
    pass

# C:\\msys64\\usr\\src\\grass741\\dist.x86_64-w64-mingw32\\include\\grass\\gis.h: 97
try:
    GMAPSET_MAX = 256
except:
    pass

# C:\\msys64\\usr\\src\\grass741\\dist.x86_64-w64-mingw32\\include\\grass\\gis.h: 98
try:
    GPATH_MAX = 4096
except:
    pass

# C:\\msys64\\usr\\src\\grass741\\dist.x86_64-w64-mingw32\\include\\grass\\gis.h: 100
try:
    GBASENAME_SEP = '_'
except:
    pass

# C:\\msys64\\usr\\src\\grass741\\dist.x86_64-w64-mingw32\\include\\grass\\gis.h: 113
def deserialize_int32_le(buf):
    return (((((buf [0]) << 0) | ((buf [1]) << 8)) | ((buf [2]) << 16)) | ((buf [3]) << 24))

# C:\\msys64\\usr\\src\\grass741\\dist.x86_64-w64-mingw32\\include\\grass\\gis.h: 125
def deserialize_int32_be(buf):
    return (((((buf [0]) << 24) | ((buf [1]) << 16)) | ((buf [2]) << 8)) | ((buf [3]) << 0))

# C:\\msys64\\usr\\src\\grass741\\dist.x86_64-w64-mingw32\\include\\grass\\gis.h: 130
try:
    GRASS_DIRSEP = '/'
except:
    pass

# C:\\msys64\\usr\\src\\grass741\\dist.x86_64-w64-mingw32\\include\\grass\\gis.h: 131
try:
    HOST_DIRSEP = '\\\\'
except:
    pass

# C:\\msys64\\usr\\src\\grass741\\dist.x86_64-w64-mingw32\\include\\grass\\gis.h: 131
try:
    G_DEV_NULL = 'NUL:'
except:
    pass

# C:\\msys64\\usr\\src\\grass741\\dist.x86_64-w64-mingw32\\include\\grass\\gis.h: 337
try:
    G_INFO_FORMAT_STANDARD = 0
except:
    pass

# C:\\msys64\\usr\\src\\grass741\\dist.x86_64-w64-mingw32\\include\\grass\\gis.h: 337
try:
    G_INFO_FORMAT_GUI = 1
except:
    pass

# C:\\msys64\\usr\\src\\grass741\\dist.x86_64-w64-mingw32\\include\\grass\\gis.h: 337
try:
    G_INFO_FORMAT_SILENT = 2
except:
    pass

# C:\\msys64\\usr\\src\\grass741\\dist.x86_64-w64-mingw32\\include\\grass\\gis.h: 337
try:
    G_INFO_FORMAT_PLAIN = 3
except:
    pass

# C:\\msys64\\usr\\src\\grass741\\dist.x86_64-w64-mingw32\\include\\grass\\gis.h: 339
try:
    G_ICON_CROSS = 0
except:
    pass

# C:\\msys64\\usr\\src\\grass741\\dist.x86_64-w64-mingw32\\include\\grass\\gis.h: 339
try:
    G_ICON_BOX = 1
except:
    pass

# C:\\msys64\\usr\\src\\grass741\\dist.x86_64-w64-mingw32\\include\\grass\\gis.h: 339
try:
    G_ICON_ARROW = 2
except:
    pass

# C:\\msys64\\usr\\src\\grass741\\dist.x86_64-w64-mingw32\\include\\grass\\gis.h: 341
try:
    DEFAULT_FG_COLOR = 'black'
except:
    pass

# C:\\msys64\\usr\\src\\grass741\\dist.x86_64-w64-mingw32\\include\\grass\\gis.h: 341
try:
    DEFAULT_BG_COLOR = 'white'
except:
    pass

# C:\\msys64\\usr\\src\\grass741\\dist.x86_64-w64-mingw32\\include\\grass\\gis.h: 341
try:
    DEFAULT_COLOR_TABLE = 'viridis'
except:
    pass

# C:\\msys64\\usr\\src\\grass741\\dist.x86_64-w64-mingw32\\include\\grass\\gis.h: 343
try:
    G_FATAL_EXIT = 0
except:
    pass

# C:\\msys64\\usr\\src\\grass741\\dist.x86_64-w64-mingw32\\include\\grass\\gis.h: 343
try:
    G_FATAL_PRINT = 1
except:
    pass

# C:\\msys64\\usr\\src\\grass741\\dist.x86_64-w64-mingw32\\include\\grass\\gis.h: 343
try:
    G_FATAL_RETURN = 2
except:
    pass

# C:\\msys64\\usr\\src\\grass741\\dist.x86_64-w64-mingw32\\include\\grass\\gis.h: 345
try:
    ENDIAN_LITTLE = 0
except:
    pass

# C:\\msys64\\usr\\src\\grass741\\dist.x86_64-w64-mingw32\\include\\grass\\gis.h: 345
try:
    ENDIAN_BIG = 1
except:
    pass

# C:\\msys64\\usr\\src\\grass741\\dist.x86_64-w64-mingw32\\include\\grass\\gis.h: 345
try:
    ENDIAN_OTHER = 2
except:
    pass

# C:\\msys64\\usr\\src\\grass741\\dist.x86_64-w64-mingw32\\include\\grass\\gis.h: 350
try:
    GV_KEY_COLUMN = 'cat'
except:
    pass

# C:/msys64/usr/src/grass741/dist.x86_64-w64-mingw32/include/grass/defs/gis.h: 57
def G_alloca(n):
    return (G_malloc (n))

# C:/msys64/usr/src/grass741/dist.x86_64-w64-mingw32/include/grass/defs/gis.h: 57
def G_freea(p):
    return (G_free (p))

# C:/msys64/usr/src/grass741/dist.x86_64-w64-mingw32/include/grass/defs/gis.h: 72
try:
    RELDIR = '?'
except:
    pass

# C:/msys64/usr/src/grass741/dist.x86_64-w64-mingw32/include/grass/defs/gis.h: 89
try:
    HAVE_LONG_LONG = 1
except:
    pass

# C:/msys64/usr/src/grass741/dist.x86_64-w64-mingw32/include/grass/defs/gis.h: 100
def G_incr_void_ptr(ptr, size):
    return (ptr + size)

# C:/msys64/usr/src/grass741/dist.x86_64-w64-mingw32/include/grass/defs/gis.h: 116
def G_malloc(n):
    return (G__malloc ('<ctypesgen>', 0, n))

# C:/msys64/usr/src/grass741/dist.x86_64-w64-mingw32/include/grass/defs/gis.h: 116
def G_calloc(m, n):
    return (G__calloc ('<ctypesgen>', 0, m, n))

# C:/msys64/usr/src/grass741/dist.x86_64-w64-mingw32/include/grass/defs/gis.h: 116
def G_realloc(p, n):
    return (G__realloc ('<ctypesgen>', 0, p, n))

# C:\\msys64\\usr\\src\\grass741\\dist.x86_64-w64-mingw32\\include\\grass\\colors.h: 8
try:
    BLACK = 1
except:
    pass

# C:\\msys64\\usr\\src\\grass741\\dist.x86_64-w64-mingw32\\include\\grass\\colors.h: 8
try:
    RED = 2
except:
    pass

# C:\\msys64\\usr\\src\\grass741\\dist.x86_64-w64-mingw32\\include\\grass\\colors.h: 8
try:
    GREEN = 3
except:
    pass

# C:\\msys64\\usr\\src\\grass741\\dist.x86_64-w64-mingw32\\include\\grass\\colors.h: 8
try:
    BLUE = 4
except:
    pass

# C:\\msys64\\usr\\src\\grass741\\dist.x86_64-w64-mingw32\\include\\grass\\colors.h: 8
try:
    YELLOW = 5
except:
    pass

# C:\\msys64\\usr\\src\\grass741\\dist.x86_64-w64-mingw32\\include\\grass\\colors.h: 8
try:
    CYAN = 6
except:
    pass

# C:\\msys64\\usr\\src\\grass741\\dist.x86_64-w64-mingw32\\include\\grass\\colors.h: 8
try:
    MAGENTA = 7
except:
    pass

# C:\\msys64\\usr\\src\\grass741\\dist.x86_64-w64-mingw32\\include\\grass\\colors.h: 8
try:
    WHITE = 8
except:
    pass

# C:\\msys64\\usr\\src\\grass741\\dist.x86_64-w64-mingw32\\include\\grass\\colors.h: 8
try:
    GRAY = 9
except:
    pass

# C:\\msys64\\usr\\src\\grass741\\dist.x86_64-w64-mingw32\\include\\grass\\colors.h: 8
try:
    ORANGE = 10
except:
    pass

# C:\\msys64\\usr\\src\\grass741\\dist.x86_64-w64-mingw32\\include\\grass\\colors.h: 8
try:
    AQUA = 11
except:
    pass

# C:\\msys64\\usr\\src\\grass741\\dist.x86_64-w64-mingw32\\include\\grass\\colors.h: 8
try:
    INDIGO = 12
except:
    pass

# C:\\msys64\\usr\\src\\grass741\\dist.x86_64-w64-mingw32\\include\\grass\\colors.h: 8
try:
    VIOLET = 13
except:
    pass

# C:\\msys64\\usr\\src\\grass741\\dist.x86_64-w64-mingw32\\include\\grass\\colors.h: 8
try:
    BROWN = 14
except:
    pass

# C:\\msys64\\usr\\src\\grass741\\dist.x86_64-w64-mingw32\\include\\grass\\colors.h: 9
try:
    GREY = GRAY
except:
    pass

# C:\\msys64\\usr\\src\\grass741\\dist.x86_64-w64-mingw32\\include\\grass\\colors.h: 9
try:
    PURPLE = VIOLET
except:
    pass

# C:\\msys64\\usr\\src\\grass741\\dist.x86_64-w64-mingw32\\include\\grass\\colors.h: 11
try:
    D_COLOR_LIST = 'red,orange,yellow,green,blue,indigo,violet,white,black,gray,brown,magenta,aqua,grey,cyan,purple'
except:
    pass

# C:\\msys64\\usr\\src\\grass741\\dist.x86_64-w64-mingw32\\include\\grass\\colors.h: 13
try:
    MAX_COLOR_LEN = 32
except:
    pass

Cell_head = struct_Cell_head # C:\\msys64\\usr\\src\\grass741\\dist.x86_64-w64-mingw32\\include\\grass\\gis.h: 390

G_3dview = struct_G_3dview # C:\\msys64\\usr\\src\\grass741\\dist.x86_64-w64-mingw32\\include\\grass\\gis.h: 452

Key_Value = struct_Key_Value # C:\\msys64\\usr\\src\\grass741\\dist.x86_64-w64-mingw32\\include\\grass\\gis.h: 479

Option = struct_Option # C:\\msys64\\usr\\src\\grass741\\dist.x86_64-w64-mingw32\\include\\grass\\gis.h: 509

Flag = struct_Flag # C:\\msys64\\usr\\src\\grass741\\dist.x86_64-w64-mingw32\\include\\grass\\gis.h: 538

GModule = struct_GModule # C:\\msys64\\usr\\src\\grass741\\dist.x86_64-w64-mingw32\\include\\grass\\gis.h: 555

TimeStamp = struct_TimeStamp # C:\\msys64\\usr\\src\\grass741\\dist.x86_64-w64-mingw32\\include\\grass\\gis.h: 565

Counter = struct_Counter # C:\\msys64\\usr\\src\\grass741\\dist.x86_64-w64-mingw32\\include\\grass\\gis.h: 571

Popen = struct_Popen # C:\\msys64\\usr\\src\\grass741\\dist.x86_64-w64-mingw32\\include\\grass\\gis.h: 575

_Color_Value_ = struct__Color_Value_ # C:\\msys64\\usr\\src\\grass741\\dist.x86_64-w64-mingw32\\include\\grass\\gis.h: 584

_Color_Rule_ = struct__Color_Rule_ # C:\\msys64\\usr\\src\\grass741\\dist.x86_64-w64-mingw32\\include\\grass\\gis.h: 592

_Color_Info_ = struct__Color_Info_ # C:\\msys64\\usr\\src\\grass741\\dist.x86_64-w64-mingw32\\include\\grass\\gis.h: 599

Colors = struct_Colors # C:\\msys64\\usr\\src\\grass741\\dist.x86_64-w64-mingw32\\include\\grass\\gis.h: 626

ilist = struct_ilist # C:\\msys64\\usr\\src\\grass741\\dist.x86_64-w64-mingw32\\include\\grass\\gis.h: 650

color_rgb = struct_color_rgb # C:\\msys64\\usr\\src\\grass741\\dist.x86_64-w64-mingw32\\include\\grass\\colors.h: 33

color_name = struct_color_name # C:\\msys64\\usr\\src\\grass741\\dist.x86_64-w64-mingw32\\include\\grass\\colors.h: 38

# No inserted files

