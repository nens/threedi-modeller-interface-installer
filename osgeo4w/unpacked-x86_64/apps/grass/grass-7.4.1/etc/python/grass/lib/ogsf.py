'''Wrapper for ogsf.h

Generated with:
./ctypesgen.py --cpp gcc -E -I/c/OSGeo4W64/include -D_FILE_OFFSET_BITS=64     -I/c/msys64/usr/src/grass741/dist.x86_64-w64-mingw32/include -I/c/msys64/usr/src/grass741/dist.x86_64-w64-mingw32/include -D__GLIBC_HAVE_LONG_LONG -lgrass_ogsf.7.4.1 C:/msys64/usr/src/grass741/dist.x86_64-w64-mingw32/include/grass/ogsf.h C:/msys64/usr/src/grass741/dist.x86_64-w64-mingw32/include/grass/defs/ogsf.h -o OBJ.x86_64-w64-mingw32/ogsf.py

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

_libs["grass_ogsf.7.4.1"] = load_library("grass_ogsf.7.4.1")

# 1 libraries
# End libraries

# No modules

# C:/msys64/usr/src/grass741/dist.x86_64-w64-mingw32/include/grass/linkm.h: 12
class struct_link_head(Structure):
    pass

struct_link_head.__slots__ = [
    'ptr_array',
    'max_ptr',
    'alloced',
    'chunk_size',
    'unit_size',
    'Unused',
    'exit_flag',
]
struct_link_head._fields_ = [
    ('ptr_array', POINTER(POINTER(c_char))),
    ('max_ptr', c_int),
    ('alloced', c_int),
    ('chunk_size', c_int),
    ('unit_size', c_int),
    ('Unused', String),
    ('exit_flag', c_int),
]

# C:/msys64/usr/src/grass741/dist.x86_64-w64-mingw32/include/grass/bitmap.h: 17
class struct_BM(Structure):
    pass

struct_BM.__slots__ = [
    'rows',
    'cols',
    'bytes',
    'data',
    'sparse',
    'token',
]
struct_BM._fields_ = [
    ('rows', c_int),
    ('cols', c_int),
    ('bytes', c_size_t),
    ('data', POINTER(c_ubyte)),
    ('sparse', c_int),
    ('token', POINTER(struct_link_head)),
]

GLint = c_int # C:/msys64/mingw64/x86_64-w64-mingw32/include/GL/gl.h: 27

GLuint = c_uint # C:/msys64/mingw64/x86_64-w64-mingw32/include/GL/gl.h: 31

GLdouble = c_double # C:/msys64/mingw64/x86_64-w64-mingw32/include/GL/gl.h: 34

# C:/msys64/usr/src/grass741/dist.x86_64-w64-mingw32/include/grass/gis.h: 390
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

DCELL = c_double # C:/msys64/usr/src/grass741/dist.x86_64-w64-mingw32/include/grass/gis.h: 581

# C:/msys64/usr/src/grass741/dist.x86_64-w64-mingw32/include/grass/gis.h: 584
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

# C:/msys64/usr/src/grass741/dist.x86_64-w64-mingw32/include/grass/gis.h: 592
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

# C:/msys64/usr/src/grass741/dist.x86_64-w64-mingw32/include/grass/gis.h: 604
class struct_anon_368(Structure):
    pass

struct_anon_368.__slots__ = [
    'red',
    'grn',
    'blu',
    'set',
    'nalloc',
    'active',
]
struct_anon_368._fields_ = [
    ('red', POINTER(c_ubyte)),
    ('grn', POINTER(c_ubyte)),
    ('blu', POINTER(c_ubyte)),
    ('set', POINTER(c_ubyte)),
    ('nalloc', c_int),
    ('active', c_int),
]

# C:/msys64/usr/src/grass741/dist.x86_64-w64-mingw32/include/grass/gis.h: 614
class struct_anon_369(Structure):
    pass

struct_anon_369.__slots__ = [
    'vals',
    'rules',
    'nalloc',
    'active',
]
struct_anon_369._fields_ = [
    ('vals', POINTER(DCELL)),
    ('rules', POINTER(POINTER(struct__Color_Rule_))),
    ('nalloc', c_int),
    ('active', c_int),
]

# C:/msys64/usr/src/grass741/dist.x86_64-w64-mingw32/include/grass/gis.h: 599
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
    ('lookup', struct_anon_368),
    ('fp_lookup', struct_anon_369),
    ('min', DCELL),
    ('max', DCELL),
]

# C:/msys64/usr/src/grass741/dist.x86_64-w64-mingw32/include/grass/gis.h: 626
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

Point4 = c_float * 4 # C:\\msys64\\usr\\src\\grass741\\dist.x86_64-w64-mingw32\\include\\grass\\ogsf.h: 200

Point3 = c_float * 3 # C:\\msys64\\usr\\src\\grass741\\dist.x86_64-w64-mingw32\\include\\grass\\ogsf.h: 201

Point2 = c_float * 2 # C:\\msys64\\usr\\src\\grass741\\dist.x86_64-w64-mingw32\\include\\grass\\ogsf.h: 202

# C:\\msys64\\usr\\src\\grass741\\dist.x86_64-w64-mingw32\\include\\grass\\ogsf.h: 214
class struct_anon_370(Structure):
    pass

struct_anon_370.__slots__ = [
    'fb',
    'ib',
    'sb',
    'cb',
    'bm',
    'nm',
    'tfunc',
    'k',
]
struct_anon_370._fields_ = [
    ('fb', POINTER(c_float)),
    ('ib', POINTER(c_int)),
    ('sb', POINTER(c_short)),
    ('cb', POINTER(c_ubyte)),
    ('bm', POINTER(struct_BM)),
    ('nm', POINTER(struct_BM)),
    ('tfunc', CFUNCTYPE(UNCHECKED(c_float), c_float, c_int)),
    ('k', c_float),
]

typbuff = struct_anon_370 # C:\\msys64\\usr\\src\\grass741\\dist.x86_64-w64-mingw32\\include\\grass\\ogsf.h: 214

# C:\\msys64\\usr\\src\\grass741\\dist.x86_64-w64-mingw32\\include\\grass\\ogsf.h: 221
class struct_anon_371(Structure):
    pass

struct_anon_371.__slots__ = [
    'n_elem',
    'index',
    'value',
]
struct_anon_371._fields_ = [
    ('n_elem', c_int),
    ('index', String),
    ('value', POINTER(c_int)),
]

table256 = struct_anon_371 # C:\\msys64\\usr\\src\\grass741\\dist.x86_64-w64-mingw32\\include\\grass\\ogsf.h: 221

# C:\\msys64\\usr\\src\\grass741\\dist.x86_64-w64-mingw32\\include\\grass\\ogsf.h: 229
class struct_anon_372(Structure):
    pass

struct_anon_372.__slots__ = [
    'offset',
    'mult',
    'use_lookup',
    'lookup',
]
struct_anon_372._fields_ = [
    ('offset', c_float),
    ('mult', c_float),
    ('use_lookup', c_int),
    ('lookup', table256),
]

transform = struct_anon_372 # C:\\msys64\\usr\\src\\grass741\\dist.x86_64-w64-mingw32\\include\\grass\\ogsf.h: 229

# C:\\msys64\\usr\\src\\grass741\\dist.x86_64-w64-mingw32\\include\\grass\\ogsf.h: 242
class struct_anon_373(Structure):
    pass

struct_anon_373.__slots__ = [
    'data_id',
    'dims',
    'ndims',
    'numbytes',
    'unique_name',
    'databuff',
    'changed',
    'need_reload',
]
struct_anon_373._fields_ = [
    ('data_id', c_int),
    ('dims', c_int * 4),
    ('ndims', c_int),
    ('numbytes', c_size_t),
    ('unique_name', String),
    ('databuff', typbuff),
    ('changed', c_uint),
    ('need_reload', c_int),
]

dataset = struct_anon_373 # C:\\msys64\\usr\\src\\grass741\\dist.x86_64-w64-mingw32\\include\\grass\\ogsf.h: 242

# C:\\msys64\\usr\\src\\grass741\\dist.x86_64-w64-mingw32\\include\\grass\\ogsf.h: 255
class struct_anon_374(Structure):
    pass

struct_anon_374.__slots__ = [
    'att_src',
    'att_type',
    'hdata',
    'user_func',
    'constant',
    'lookup',
    'min_nz',
    'max_nz',
    'range_nz',
    'default_null',
]
struct_anon_374._fields_ = [
    ('att_src', c_uint),
    ('att_type', c_uint),
    ('hdata', c_int),
    ('user_func', CFUNCTYPE(UNCHECKED(c_int), )),
    ('constant', c_float),
    ('lookup', POINTER(c_int)),
    ('min_nz', c_float),
    ('max_nz', c_float),
    ('range_nz', c_float),
    ('default_null', c_float),
]

gsurf_att = struct_anon_374 # C:\\msys64\\usr\\src\\grass741\\dist.x86_64-w64-mingw32\\include\\grass\\ogsf.h: 255

# C:\\msys64\\usr\\src\\grass741\\dist.x86_64-w64-mingw32\\include\\grass\\ogsf.h: 257
class struct_g_surf(Structure):
    pass

struct_g_surf.__slots__ = [
    'gsurf_id',
    'cols',
    'rows',
    'att',
    'draw_mode',
    'wire_color',
    'ox',
    'oy',
    'xres',
    'yres',
    'z_exag',
    'x_trans',
    'y_trans',
    'z_trans',
    'xmin',
    'xmax',
    'ymin',
    'ymax',
    'zmin',
    'zmax',
    'zminmasked',
    'xrange',
    'yrange',
    'zrange',
    'zmin_nz',
    'zmax_nz',
    'zrange_nz',
    'x_mod',
    'y_mod',
    'x_modw',
    'y_modw',
    'nz_topo',
    'nz_color',
    'mask_needupdate',
    'norm_needupdate',
    'norms',
    'curmask',
    'next',
    'clientdata',
]
struct_g_surf._fields_ = [
    ('gsurf_id', c_int),
    ('cols', c_int),
    ('rows', c_int),
    ('att', gsurf_att * 7),
    ('draw_mode', c_uint),
    ('wire_color', c_long),
    ('ox', c_double),
    ('oy', c_double),
    ('xres', c_double),
    ('yres', c_double),
    ('z_exag', c_float),
    ('x_trans', c_float),
    ('y_trans', c_float),
    ('z_trans', c_float),
    ('xmin', c_float),
    ('xmax', c_float),
    ('ymin', c_float),
    ('ymax', c_float),
    ('zmin', c_float),
    ('zmax', c_float),
    ('zminmasked', c_float),
    ('xrange', c_float),
    ('yrange', c_float),
    ('zrange', c_float),
    ('zmin_nz', c_float),
    ('zmax_nz', c_float),
    ('zrange_nz', c_float),
    ('x_mod', c_int),
    ('y_mod', c_int),
    ('x_modw', c_int),
    ('y_modw', c_int),
    ('nz_topo', c_int),
    ('nz_color', c_int),
    ('mask_needupdate', c_int),
    ('norm_needupdate', c_int),
    ('norms', POINTER(c_ulong)),
    ('curmask', POINTER(struct_BM)),
    ('next', POINTER(struct_g_surf)),
    ('clientdata', POINTER(None)),
]

geosurf = struct_g_surf # C:\\msys64\\usr\\src\\grass741\\dist.x86_64-w64-mingw32\\include\\grass\\ogsf.h: 278

# C:\\msys64\\usr\\src\\grass741\\dist.x86_64-w64-mingw32\\include\\grass\\ogsf.h: 286
class struct_g_vect_style(Structure):
    pass

struct_g_vect_style.__slots__ = [
    'color',
    'symbol',
    'size',
    'width',
    'next',
]
struct_g_vect_style._fields_ = [
    ('color', c_int),
    ('symbol', c_int),
    ('size', c_float),
    ('width', c_int),
    ('next', POINTER(struct_g_vect_style)),
]

gvstyle = struct_g_vect_style # C:\\msys64\\usr\\src\\grass741\\dist.x86_64-w64-mingw32\\include\\grass\\ogsf.h: 299

# C:\\msys64\\usr\\src\\grass741\\dist.x86_64-w64-mingw32\\include\\grass\\ogsf.h: 311
class struct_g_vect_style_thematic(Structure):
    pass

struct_g_vect_style_thematic.__slots__ = [
    'active',
    'layer',
    'color_column',
    'symbol_column',
    'size_column',
    'width_column',
]
struct_g_vect_style_thematic._fields_ = [
    ('active', c_int),
    ('layer', c_int),
    ('color_column', String),
    ('symbol_column', String),
    ('size_column', String),
    ('width_column', String),
]

gvstyle_thematic = struct_g_vect_style_thematic # C:\\msys64\\usr\\src\\grass741\\dist.x86_64-w64-mingw32\\include\\grass\\ogsf.h: 311

# C:\\msys64\\usr\\src\\grass741\\dist.x86_64-w64-mingw32\\include\\grass\\ogsf.h: 322
class struct_line_cats(Structure):
    pass

# C:\\msys64\\usr\\src\\grass741\\dist.x86_64-w64-mingw32\\include\\grass\\ogsf.h: 314
class struct_g_line(Structure):
    pass

struct_g_line.__slots__ = [
    'type',
    'norm',
    'dims',
    'npts',
    'p3',
    'p2',
    'cats',
    'style',
    'highlighted',
    'next',
]
struct_g_line._fields_ = [
    ('type', c_int),
    ('norm', c_float * 3),
    ('dims', c_int),
    ('npts', c_int),
    ('p3', POINTER(Point3)),
    ('p2', POINTER(Point2)),
    ('cats', POINTER(struct_line_cats)),
    ('style', POINTER(gvstyle)),
    ('highlighted', c_char),
    ('next', POINTER(struct_g_line)),
]

geoline = struct_g_line # C:\\msys64\\usr\\src\\grass741\\dist.x86_64-w64-mingw32\\include\\grass\\ogsf.h: 327

# C:\\msys64\\usr\\src\\grass741\\dist.x86_64-w64-mingw32\\include\\grass\\ogsf.h: 330
class struct_g_vect(Structure):
    pass

struct_g_vect.__slots__ = [
    'gvect_id',
    'use_mem',
    'n_lines',
    'drape_surf_id',
    'use_z',
    'n_surfs',
    'filename',
    'x_trans',
    'y_trans',
    'z_trans',
    'lines',
    'fastlines',
    'bgn_read',
    'end_read',
    'nxt_line',
    'next',
    'clientdata',
    'tstyle',
    'style',
    'hstyle',
]
struct_g_vect._fields_ = [
    ('gvect_id', c_int),
    ('use_mem', c_int),
    ('n_lines', c_int),
    ('drape_surf_id', c_int * 12),
    ('use_z', c_int),
    ('n_surfs', c_int),
    ('filename', String),
    ('x_trans', c_float),
    ('y_trans', c_float),
    ('z_trans', c_float),
    ('lines', POINTER(geoline)),
    ('fastlines', POINTER(geoline)),
    ('bgn_read', CFUNCTYPE(UNCHECKED(c_int), )),
    ('end_read', CFUNCTYPE(UNCHECKED(c_int), )),
    ('nxt_line', CFUNCTYPE(UNCHECKED(c_int), )),
    ('next', POINTER(struct_g_vect)),
    ('clientdata', POINTER(None)),
    ('tstyle', POINTER(gvstyle_thematic)),
    ('style', POINTER(gvstyle)),
    ('hstyle', POINTER(gvstyle)),
]

geovect = struct_g_vect # C:\\msys64\\usr\\src\\grass741\\dist.x86_64-w64-mingw32\\include\\grass\\ogsf.h: 349

# C:\\msys64\\usr\\src\\grass741\\dist.x86_64-w64-mingw32\\include\\grass\\ogsf.h: 352
class struct_g_point(Structure):
    pass

struct_g_point.__slots__ = [
    'dims',
    'p3',
    'cats',
    'style',
    'highlighted',
    'next',
]
struct_g_point._fields_ = [
    ('dims', c_int),
    ('p3', Point3),
    ('cats', POINTER(struct_line_cats)),
    ('style', POINTER(gvstyle)),
    ('highlighted', c_char),
    ('next', POINTER(struct_g_point)),
]

geopoint = struct_g_point # C:\\msys64\\usr\\src\\grass741\\dist.x86_64-w64-mingw32\\include\\grass\\ogsf.h: 362

# C:\\msys64\\usr\\src\\grass741\\dist.x86_64-w64-mingw32\\include\\grass\\ogsf.h: 365
class struct_g_site(Structure):
    pass

struct_g_site.__slots__ = [
    'gsite_id',
    'drape_surf_id',
    'n_surfs',
    'n_sites',
    'use_z',
    'use_mem',
    'has_z',
    'filename',
    'attr_trans',
    'x_trans',
    'y_trans',
    'z_trans',
    'points',
    'bgn_read',
    'end_read',
    'nxt_site',
    'next',
    'clientdata',
    'tstyle',
    'style',
    'hstyle',
]
struct_g_site._fields_ = [
    ('gsite_id', c_int),
    ('drape_surf_id', c_int * 12),
    ('n_surfs', c_int),
    ('n_sites', c_int),
    ('use_z', c_int),
    ('use_mem', c_int),
    ('has_z', c_int),
    ('filename', String),
    ('attr_trans', transform),
    ('x_trans', c_float),
    ('y_trans', c_float),
    ('z_trans', c_float),
    ('points', POINTER(geopoint)),
    ('bgn_read', CFUNCTYPE(UNCHECKED(c_int), )),
    ('end_read', CFUNCTYPE(UNCHECKED(c_int), )),
    ('nxt_site', CFUNCTYPE(UNCHECKED(c_int), )),
    ('next', POINTER(struct_g_site)),
    ('clientdata', POINTER(None)),
    ('tstyle', POINTER(gvstyle_thematic)),
    ('style', POINTER(gvstyle)),
    ('hstyle', POINTER(gvstyle)),
]

geosite = struct_g_site # C:\\msys64\\usr\\src\\grass741\\dist.x86_64-w64-mingw32\\include\\grass\\ogsf.h: 384

# C:\\msys64\\usr\\src\\grass741\\dist.x86_64-w64-mingw32\\include\\grass\\ogsf.h: 401
class struct_anon_375(Structure):
    pass

struct_anon_375.__slots__ = [
    'data_id',
    'file_type',
    'count',
    'file_name',
    'data_type',
    'map',
    'min',
    'max',
    'status',
    'mode',
    'buff',
]
struct_anon_375._fields_ = [
    ('data_id', c_int),
    ('file_type', c_uint),
    ('count', c_uint),
    ('file_name', String),
    ('data_type', c_uint),
    ('map', POINTER(None)),
    ('min', c_double),
    ('max', c_double),
    ('status', c_uint),
    ('mode', c_uint),
    ('buff', POINTER(None)),
]

geovol_file = struct_anon_375 # C:\\msys64\\usr\\src\\grass741\\dist.x86_64-w64-mingw32\\include\\grass\\ogsf.h: 401

# C:\\msys64\\usr\\src\\grass741\\dist.x86_64-w64-mingw32\\include\\grass\\ogsf.h: 413
class struct_anon_376(Structure):
    pass

struct_anon_376.__slots__ = [
    'att_src',
    'hfile',
    'user_func',
    'constant',
    'att_data',
    'changed',
]
struct_anon_376._fields_ = [
    ('att_src', c_uint),
    ('hfile', c_int),
    ('user_func', CFUNCTYPE(UNCHECKED(c_int), )),
    ('constant', c_float),
    ('att_data', POINTER(None)),
    ('changed', c_int),
]

geovol_isosurf_att = struct_anon_376 # C:\\msys64\\usr\\src\\grass741\\dist.x86_64-w64-mingw32\\include\\grass\\ogsf.h: 413

# C:\\msys64\\usr\\src\\grass741\\dist.x86_64-w64-mingw32\\include\\grass\\ogsf.h: 422
class struct_anon_377(Structure):
    pass

struct_anon_377.__slots__ = [
    'inout_mode',
    'att',
    'data_desc',
    'data',
]
struct_anon_377._fields_ = [
    ('inout_mode', c_int),
    ('att', geovol_isosurf_att * 7),
    ('data_desc', c_int),
    ('data', POINTER(c_ubyte)),
]

geovol_isosurf = struct_anon_377 # C:\\msys64\\usr\\src\\grass741\\dist.x86_64-w64-mingw32\\include\\grass\\ogsf.h: 422

# C:\\msys64\\usr\\src\\grass741\\dist.x86_64-w64-mingw32\\include\\grass\\ogsf.h: 432
class struct_anon_378(Structure):
    pass

struct_anon_378.__slots__ = [
    'dir',
    'x1',
    'x2',
    'y1',
    'y2',
    'z1',
    'z2',
    'data',
    'changed',
    'mode',
    'transp',
]
struct_anon_378._fields_ = [
    ('dir', c_int),
    ('x1', c_float),
    ('x2', c_float),
    ('y1', c_float),
    ('y2', c_float),
    ('z1', c_float),
    ('z2', c_float),
    ('data', POINTER(c_ubyte)),
    ('changed', c_int),
    ('mode', c_int),
    ('transp', c_int),
]

geovol_slice = struct_anon_378 # C:\\msys64\\usr\\src\\grass741\\dist.x86_64-w64-mingw32\\include\\grass\\ogsf.h: 432

# C:\\msys64\\usr\\src\\grass741\\dist.x86_64-w64-mingw32\\include\\grass\\ogsf.h: 434
class struct_g_vol(Structure):
    pass

struct_g_vol.__slots__ = [
    'gvol_id',
    'next',
    'hfile',
    'cols',
    'rows',
    'depths',
    'ox',
    'oy',
    'oz',
    'xres',
    'yres',
    'zres',
    'xmin',
    'xmax',
    'ymin',
    'ymax',
    'zmin',
    'zmax',
    'xrange',
    'yrange',
    'zrange',
    'x_trans',
    'y_trans',
    'z_trans',
    'draw_wire',
    'n_isosurfs',
    'isosurf',
    'isosurf_x_mod',
    'isosurf_y_mod',
    'isosurf_z_mod',
    'isosurf_draw_mode',
    'n_slices',
    'slice',
    'slice_x_mod',
    'slice_y_mod',
    'slice_z_mod',
    'slice_draw_mode',
    'clientdata',
]
struct_g_vol._fields_ = [
    ('gvol_id', c_int),
    ('next', POINTER(struct_g_vol)),
    ('hfile', c_int),
    ('cols', c_int),
    ('rows', c_int),
    ('depths', c_int),
    ('ox', c_double),
    ('oy', c_double),
    ('oz', c_double),
    ('xres', c_double),
    ('yres', c_double),
    ('zres', c_double),
    ('xmin', c_double),
    ('xmax', c_double),
    ('ymin', c_double),
    ('ymax', c_double),
    ('zmin', c_double),
    ('zmax', c_double),
    ('xrange', c_double),
    ('yrange', c_double),
    ('zrange', c_double),
    ('x_trans', c_float),
    ('y_trans', c_float),
    ('z_trans', c_float),
    ('draw_wire', c_int),
    ('n_isosurfs', c_int),
    ('isosurf', POINTER(geovol_isosurf) * 12),
    ('isosurf_x_mod', c_int),
    ('isosurf_y_mod', c_int),
    ('isosurf_z_mod', c_int),
    ('isosurf_draw_mode', c_uint),
    ('n_slices', c_int),
    ('slice', POINTER(geovol_slice) * 12),
    ('slice_x_mod', c_int),
    ('slice_y_mod', c_int),
    ('slice_z_mod', c_int),
    ('slice_draw_mode', c_uint),
    ('clientdata', POINTER(None)),
]

geovol = struct_g_vol # C:\\msys64\\usr\\src\\grass741\\dist.x86_64-w64-mingw32\\include\\grass\\ogsf.h: 459

# C:\\msys64\\usr\\src\\grass741\\dist.x86_64-w64-mingw32\\include\\grass\\ogsf.h: 461
class struct_lightdefs(Structure):
    pass

struct_lightdefs.__slots__ = [
    'position',
    'color',
    'ambient',
    'emission',
    'shine',
]
struct_lightdefs._fields_ = [
    ('position', c_float * 4),
    ('color', c_float * 3),
    ('ambient', c_float * 3),
    ('emission', c_float * 3),
    ('shine', c_float),
]

# C:\\msys64\\usr\\src\\grass741\\dist.x86_64-w64-mingw32\\include\\grass\\ogsf.h: 470
class struct_georot(Structure):
    pass

struct_georot.__slots__ = [
    'do_rot',
    'rot_angle',
    'rot_axes',
    'rotMatrix',
]
struct_georot._fields_ = [
    ('do_rot', c_int),
    ('rot_angle', c_double),
    ('rot_axes', c_double * 3),
    ('rotMatrix', GLdouble * 16),
]

# C:\\msys64\\usr\\src\\grass741\\dist.x86_64-w64-mingw32\\include\\grass\\ogsf.h: 489
class struct_anon_379(Structure):
    pass

struct_anon_379.__slots__ = [
    'coord_sys',
    'view_proj',
    'infocus',
    'from_to',
    'rotate',
    'twist',
    'fov',
    'incl',
    'look',
    'real_to',
    'vert_exag',
    'scale',
    'lights',
]
struct_anon_379._fields_ = [
    ('coord_sys', c_int),
    ('view_proj', c_int),
    ('infocus', c_int),
    ('from_to', (c_float * 4) * 2),
    ('rotate', struct_georot),
    ('twist', c_int),
    ('fov', c_int),
    ('incl', c_int),
    ('look', c_int),
    ('real_to', c_float * 4),
    ('vert_exag', c_float),
    ('scale', c_float),
    ('lights', struct_lightdefs * 3),
]

geoview = struct_anon_379 # C:\\msys64\\usr\\src\\grass741\\dist.x86_64-w64-mingw32\\include\\grass\\ogsf.h: 489

# C:\\msys64\\usr\\src\\grass741\\dist.x86_64-w64-mingw32\\include\\grass\\ogsf.h: 496
class struct_anon_380(Structure):
    pass

struct_anon_380.__slots__ = [
    'nearclip',
    'farclip',
    'aspect',
    'left',
    'right',
    'bottom',
    'top',
    'bgcol',
]
struct_anon_380._fields_ = [
    ('nearclip', c_float),
    ('farclip', c_float),
    ('aspect', c_float),
    ('left', c_short),
    ('right', c_short),
    ('bottom', c_short),
    ('top', c_short),
    ('bgcol', c_int),
]

geodisplay = struct_anon_380 # C:\\msys64\\usr\\src\\grass741\\dist.x86_64-w64-mingw32\\include\\grass\\ogsf.h: 496

# C:\\msys64\\usr\\src\\grass741\\dist.x86_64-w64-mingw32\\include\\grass\\ogsf.h: 498
try:
    Cxl_func = (POINTER(CFUNCTYPE(UNCHECKED(None), ))).in_dll(_libs['grass_ogsf.7.4.1'], 'Cxl_func')
except:
    pass

# C:\\msys64\\usr\\src\\grass741\\dist.x86_64-w64-mingw32\\include\\grass\\ogsf.h: 499
try:
    Swap_func = (POINTER(CFUNCTYPE(UNCHECKED(None), ))).in_dll(_libs['grass_ogsf.7.4.1'], 'Swap_func')
except:
    pass

# C:\\msys64\\usr\\src\\grass741\\dist.x86_64-w64-mingw32\\include\\grass\\ogsf.h: 543
class struct_view_node(Structure):
    pass

struct_view_node.__slots__ = [
    'fields',
]
struct_view_node._fields_ = [
    ('fields', c_float * 8),
]

Viewnode = struct_view_node # C:\\msys64\\usr\\src\\grass741\\dist.x86_64-w64-mingw32\\include\\grass\\ogsf.h: 543

# C:\\msys64\\usr\\src\\grass741\\dist.x86_64-w64-mingw32\\include\\grass\\ogsf.h: 545
class struct_key_node(Structure):
    pass

struct_key_node.__slots__ = [
    'pos',
    'fields',
    'look_ahead',
    'fieldmask',
    'next',
    'prior',
]
struct_key_node._fields_ = [
    ('pos', c_float),
    ('fields', c_float * 8),
    ('look_ahead', c_int),
    ('fieldmask', c_ulong),
    ('next', POINTER(struct_key_node)),
    ('prior', POINTER(struct_key_node)),
]

Keylist = struct_key_node # C:\\msys64\\usr\\src\\grass741\\dist.x86_64-w64-mingw32\\include\\grass\\ogsf.h: 551

# C:/msys64/usr/src/grass741/dist.x86_64-w64-mingw32/include/grass/defs/ogsf.h: 5
if hasattr(_libs['grass_ogsf.7.4.1'], 'GK_set_interpmode'):
    GK_set_interpmode = _libs['grass_ogsf.7.4.1'].GK_set_interpmode
    GK_set_interpmode.restype = c_int
    GK_set_interpmode.argtypes = [c_int]

# C:/msys64/usr/src/grass741/dist.x86_64-w64-mingw32/include/grass/defs/ogsf.h: 6
if hasattr(_libs['grass_ogsf.7.4.1'], 'GK_set_tension'):
    GK_set_tension = _libs['grass_ogsf.7.4.1'].GK_set_tension
    GK_set_tension.restype = None
    GK_set_tension.argtypes = [c_float]

# C:/msys64/usr/src/grass741/dist.x86_64-w64-mingw32/include/grass/defs/ogsf.h: 7
if hasattr(_libs['grass_ogsf.7.4.1'], 'GK_showtension_start'):
    GK_showtension_start = _libs['grass_ogsf.7.4.1'].GK_showtension_start
    GK_showtension_start.restype = None
    GK_showtension_start.argtypes = []

# C:/msys64/usr/src/grass741/dist.x86_64-w64-mingw32/include/grass/defs/ogsf.h: 8
if hasattr(_libs['grass_ogsf.7.4.1'], 'GK_showtension_stop'):
    GK_showtension_stop = _libs['grass_ogsf.7.4.1'].GK_showtension_stop
    GK_showtension_stop.restype = None
    GK_showtension_stop.argtypes = []

# C:/msys64/usr/src/grass741/dist.x86_64-w64-mingw32/include/grass/defs/ogsf.h: 9
if hasattr(_libs['grass_ogsf.7.4.1'], 'GK_update_tension'):
    GK_update_tension = _libs['grass_ogsf.7.4.1'].GK_update_tension
    GK_update_tension.restype = None
    GK_update_tension.argtypes = []

# C:/msys64/usr/src/grass741/dist.x86_64-w64-mingw32/include/grass/defs/ogsf.h: 10
if hasattr(_libs['grass_ogsf.7.4.1'], 'GK_update_frames'):
    GK_update_frames = _libs['grass_ogsf.7.4.1'].GK_update_frames
    GK_update_frames.restype = None
    GK_update_frames.argtypes = []

# C:/msys64/usr/src/grass741/dist.x86_64-w64-mingw32/include/grass/defs/ogsf.h: 11
if hasattr(_libs['grass_ogsf.7.4.1'], 'GK_set_numsteps'):
    GK_set_numsteps = _libs['grass_ogsf.7.4.1'].GK_set_numsteps
    GK_set_numsteps.restype = None
    GK_set_numsteps.argtypes = [c_int]

# C:/msys64/usr/src/grass741/dist.x86_64-w64-mingw32/include/grass/defs/ogsf.h: 12
if hasattr(_libs['grass_ogsf.7.4.1'], 'GK_clear_keys'):
    GK_clear_keys = _libs['grass_ogsf.7.4.1'].GK_clear_keys
    GK_clear_keys.restype = None
    GK_clear_keys.argtypes = []

# C:/msys64/usr/src/grass741/dist.x86_64-w64-mingw32/include/grass/defs/ogsf.h: 13
if hasattr(_libs['grass_ogsf.7.4.1'], 'GK_print_keys'):
    GK_print_keys = _libs['grass_ogsf.7.4.1'].GK_print_keys
    GK_print_keys.restype = None
    GK_print_keys.argtypes = [String]

# C:/msys64/usr/src/grass741/dist.x86_64-w64-mingw32/include/grass/defs/ogsf.h: 14
if hasattr(_libs['grass_ogsf.7.4.1'], 'GK_move_key'):
    GK_move_key = _libs['grass_ogsf.7.4.1'].GK_move_key
    GK_move_key.restype = c_int
    GK_move_key.argtypes = [c_float, c_float, c_float]

# C:/msys64/usr/src/grass741/dist.x86_64-w64-mingw32/include/grass/defs/ogsf.h: 15
if hasattr(_libs['grass_ogsf.7.4.1'], 'GK_delete_key'):
    GK_delete_key = _libs['grass_ogsf.7.4.1'].GK_delete_key
    GK_delete_key.restype = c_int
    GK_delete_key.argtypes = [c_float, c_float, c_int]

# C:/msys64/usr/src/grass741/dist.x86_64-w64-mingw32/include/grass/defs/ogsf.h: 16
if hasattr(_libs['grass_ogsf.7.4.1'], 'GK_add_key'):
    GK_add_key = _libs['grass_ogsf.7.4.1'].GK_add_key
    GK_add_key.restype = c_int
    GK_add_key.argtypes = [c_float, c_ulong, c_int, c_float]

# C:/msys64/usr/src/grass741/dist.x86_64-w64-mingw32/include/grass/defs/ogsf.h: 17
if hasattr(_libs['grass_ogsf.7.4.1'], 'GK_do_framestep'):
    GK_do_framestep = _libs['grass_ogsf.7.4.1'].GK_do_framestep
    GK_do_framestep.restype = None
    GK_do_framestep.argtypes = [c_int, c_int]

# C:/msys64/usr/src/grass741/dist.x86_64-w64-mingw32/include/grass/defs/ogsf.h: 18
if hasattr(_libs['grass_ogsf.7.4.1'], 'GK_show_path'):
    GK_show_path = _libs['grass_ogsf.7.4.1'].GK_show_path
    GK_show_path.restype = None
    GK_show_path.argtypes = [c_int]

# C:/msys64/usr/src/grass741/dist.x86_64-w64-mingw32/include/grass/defs/ogsf.h: 19
if hasattr(_libs['grass_ogsf.7.4.1'], 'GK_show_vect'):
    GK_show_vect = _libs['grass_ogsf.7.4.1'].GK_show_vect
    GK_show_vect.restype = None
    GK_show_vect.argtypes = [c_int]

# C:/msys64/usr/src/grass741/dist.x86_64-w64-mingw32/include/grass/defs/ogsf.h: 20
if hasattr(_libs['grass_ogsf.7.4.1'], 'GK_show_site'):
    GK_show_site = _libs['grass_ogsf.7.4.1'].GK_show_site
    GK_show_site.restype = None
    GK_show_site.argtypes = [c_int]

# C:/msys64/usr/src/grass741/dist.x86_64-w64-mingw32/include/grass/defs/ogsf.h: 21
if hasattr(_libs['grass_ogsf.7.4.1'], 'GK_show_vol'):
    GK_show_vol = _libs['grass_ogsf.7.4.1'].GK_show_vol
    GK_show_vol.restype = None
    GK_show_vol.argtypes = [c_int]

# C:/msys64/usr/src/grass741/dist.x86_64-w64-mingw32/include/grass/defs/ogsf.h: 22
if hasattr(_libs['grass_ogsf.7.4.1'], 'GK_show_list'):
    GK_show_list = _libs['grass_ogsf.7.4.1'].GK_show_list
    GK_show_list.restype = None
    GK_show_list.argtypes = [c_int]

# C:/msys64/usr/src/grass741/dist.x86_64-w64-mingw32/include/grass/defs/ogsf.h: 25
if hasattr(_libs['grass_ogsf.7.4.1'], 'GP_site_exists'):
    GP_site_exists = _libs['grass_ogsf.7.4.1'].GP_site_exists
    GP_site_exists.restype = c_int
    GP_site_exists.argtypes = [c_int]

# C:/msys64/usr/src/grass741/dist.x86_64-w64-mingw32/include/grass/defs/ogsf.h: 26
if hasattr(_libs['grass_ogsf.7.4.1'], 'GP_new_site'):
    GP_new_site = _libs['grass_ogsf.7.4.1'].GP_new_site
    GP_new_site.restype = c_int
    GP_new_site.argtypes = []

# C:/msys64/usr/src/grass741/dist.x86_64-w64-mingw32/include/grass/defs/ogsf.h: 27
if hasattr(_libs['grass_ogsf.7.4.1'], 'GP_num_sites'):
    GP_num_sites = _libs['grass_ogsf.7.4.1'].GP_num_sites
    GP_num_sites.restype = c_int
    GP_num_sites.argtypes = []

# C:/msys64/usr/src/grass741/dist.x86_64-w64-mingw32/include/grass/defs/ogsf.h: 28
if hasattr(_libs['grass_ogsf.7.4.1'], 'GP_get_site_list'):
    GP_get_site_list = _libs['grass_ogsf.7.4.1'].GP_get_site_list
    GP_get_site_list.restype = POINTER(c_int)
    GP_get_site_list.argtypes = [POINTER(c_int)]

# C:/msys64/usr/src/grass741/dist.x86_64-w64-mingw32/include/grass/defs/ogsf.h: 29
if hasattr(_libs['grass_ogsf.7.4.1'], 'GP_delete_site'):
    GP_delete_site = _libs['grass_ogsf.7.4.1'].GP_delete_site
    GP_delete_site.restype = c_int
    GP_delete_site.argtypes = [c_int]

# C:/msys64/usr/src/grass741/dist.x86_64-w64-mingw32/include/grass/defs/ogsf.h: 30
if hasattr(_libs['grass_ogsf.7.4.1'], 'GP_load_site'):
    GP_load_site = _libs['grass_ogsf.7.4.1'].GP_load_site
    GP_load_site.restype = c_int
    GP_load_site.argtypes = [c_int, String]

# C:/msys64/usr/src/grass741/dist.x86_64-w64-mingw32/include/grass/defs/ogsf.h: 31
if hasattr(_libs['grass_ogsf.7.4.1'], 'GP_get_sitename'):
    GP_get_sitename = _libs['grass_ogsf.7.4.1'].GP_get_sitename
    GP_get_sitename.restype = c_int
    GP_get_sitename.argtypes = [c_int, POINTER(POINTER(c_char))]

# C:/msys64/usr/src/grass741/dist.x86_64-w64-mingw32/include/grass/defs/ogsf.h: 32
if hasattr(_libs['grass_ogsf.7.4.1'], 'GP_get_style'):
    GP_get_style = _libs['grass_ogsf.7.4.1'].GP_get_style
    GP_get_style.restype = c_int
    GP_get_style.argtypes = [c_int, POINTER(c_int), POINTER(c_int), POINTER(c_float), POINTER(c_int)]

# C:/msys64/usr/src/grass741/dist.x86_64-w64-mingw32/include/grass/defs/ogsf.h: 33
if hasattr(_libs['grass_ogsf.7.4.1'], 'GP_set_style'):
    GP_set_style = _libs['grass_ogsf.7.4.1'].GP_set_style
    GP_set_style.restype = c_int
    GP_set_style.argtypes = [c_int, c_int, c_int, c_float, c_int]

# C:/msys64/usr/src/grass741/dist.x86_64-w64-mingw32/include/grass/defs/ogsf.h: 34
if hasattr(_libs['grass_ogsf.7.4.1'], 'GP_set_style_thematic'):
    GP_set_style_thematic = _libs['grass_ogsf.7.4.1'].GP_set_style_thematic
    GP_set_style_thematic.restype = c_int
    GP_set_style_thematic.argtypes = [c_int, c_int, String, String, String, String, POINTER(struct_Colors)]

# C:/msys64/usr/src/grass741/dist.x86_64-w64-mingw32/include/grass/defs/ogsf.h: 36
if hasattr(_libs['grass_ogsf.7.4.1'], 'GP_unset_style_thematic'):
    GP_unset_style_thematic = _libs['grass_ogsf.7.4.1'].GP_unset_style_thematic
    GP_unset_style_thematic.restype = c_int
    GP_unset_style_thematic.argtypes = [c_int]

# C:/msys64/usr/src/grass741/dist.x86_64-w64-mingw32/include/grass/defs/ogsf.h: 37
for _lib in _libs.values():
    if hasattr(_lib, 'GP_attmode_color'):
        GP_attmode_color = _lib.GP_attmode_color
        GP_attmode_color.restype = c_int
        GP_attmode_color.argtypes = [c_int, String]
        break

# C:/msys64/usr/src/grass741/dist.x86_64-w64-mingw32/include/grass/defs/ogsf.h: 38
for _lib in _libs.values():
    if hasattr(_lib, 'GP_attmode_none'):
        GP_attmode_none = _lib.GP_attmode_none
        GP_attmode_none.restype = c_int
        GP_attmode_none.argtypes = [c_int]
        break

# C:/msys64/usr/src/grass741/dist.x86_64-w64-mingw32/include/grass/defs/ogsf.h: 39
if hasattr(_libs['grass_ogsf.7.4.1'], 'GP_set_zmode'):
    GP_set_zmode = _libs['grass_ogsf.7.4.1'].GP_set_zmode
    GP_set_zmode.restype = c_int
    GP_set_zmode.argtypes = [c_int, c_int]

# C:/msys64/usr/src/grass741/dist.x86_64-w64-mingw32/include/grass/defs/ogsf.h: 40
if hasattr(_libs['grass_ogsf.7.4.1'], 'GP_get_zmode'):
    GP_get_zmode = _libs['grass_ogsf.7.4.1'].GP_get_zmode
    GP_get_zmode.restype = c_int
    GP_get_zmode.argtypes = [c_int, POINTER(c_int)]

# C:/msys64/usr/src/grass741/dist.x86_64-w64-mingw32/include/grass/defs/ogsf.h: 41
if hasattr(_libs['grass_ogsf.7.4.1'], 'GP_set_trans'):
    GP_set_trans = _libs['grass_ogsf.7.4.1'].GP_set_trans
    GP_set_trans.restype = None
    GP_set_trans.argtypes = [c_int, c_float, c_float, c_float]

# C:/msys64/usr/src/grass741/dist.x86_64-w64-mingw32/include/grass/defs/ogsf.h: 42
if hasattr(_libs['grass_ogsf.7.4.1'], 'GP_get_trans'):
    GP_get_trans = _libs['grass_ogsf.7.4.1'].GP_get_trans
    GP_get_trans.restype = None
    GP_get_trans.argtypes = [c_int, POINTER(c_float), POINTER(c_float), POINTER(c_float)]

# C:/msys64/usr/src/grass741/dist.x86_64-w64-mingw32/include/grass/defs/ogsf.h: 43
if hasattr(_libs['grass_ogsf.7.4.1'], 'GP_select_surf'):
    GP_select_surf = _libs['grass_ogsf.7.4.1'].GP_select_surf
    GP_select_surf.restype = c_int
    GP_select_surf.argtypes = [c_int, c_int]

# C:/msys64/usr/src/grass741/dist.x86_64-w64-mingw32/include/grass/defs/ogsf.h: 44
if hasattr(_libs['grass_ogsf.7.4.1'], 'GP_unselect_surf'):
    GP_unselect_surf = _libs['grass_ogsf.7.4.1'].GP_unselect_surf
    GP_unselect_surf.restype = c_int
    GP_unselect_surf.argtypes = [c_int, c_int]

# C:/msys64/usr/src/grass741/dist.x86_64-w64-mingw32/include/grass/defs/ogsf.h: 45
if hasattr(_libs['grass_ogsf.7.4.1'], 'GP_surf_is_selected'):
    GP_surf_is_selected = _libs['grass_ogsf.7.4.1'].GP_surf_is_selected
    GP_surf_is_selected.restype = c_int
    GP_surf_is_selected.argtypes = [c_int, c_int]

# C:/msys64/usr/src/grass741/dist.x86_64-w64-mingw32/include/grass/defs/ogsf.h: 46
if hasattr(_libs['grass_ogsf.7.4.1'], 'GP_draw_site'):
    GP_draw_site = _libs['grass_ogsf.7.4.1'].GP_draw_site
    GP_draw_site.restype = None
    GP_draw_site.argtypes = [c_int]

# C:/msys64/usr/src/grass741/dist.x86_64-w64-mingw32/include/grass/defs/ogsf.h: 47
if hasattr(_libs['grass_ogsf.7.4.1'], 'GP_alldraw_site'):
    GP_alldraw_site = _libs['grass_ogsf.7.4.1'].GP_alldraw_site
    GP_alldraw_site.restype = None
    GP_alldraw_site.argtypes = []

# C:/msys64/usr/src/grass741/dist.x86_64-w64-mingw32/include/grass/defs/ogsf.h: 48
if hasattr(_libs['grass_ogsf.7.4.1'], 'GP_Set_ClientData'):
    GP_Set_ClientData = _libs['grass_ogsf.7.4.1'].GP_Set_ClientData
    GP_Set_ClientData.restype = c_int
    GP_Set_ClientData.argtypes = [c_int, POINTER(None)]

# C:/msys64/usr/src/grass741/dist.x86_64-w64-mingw32/include/grass/defs/ogsf.h: 49
if hasattr(_libs['grass_ogsf.7.4.1'], 'GP_Get_ClientData'):
    GP_Get_ClientData = _libs['grass_ogsf.7.4.1'].GP_Get_ClientData
    GP_Get_ClientData.restype = POINTER(None)
    GP_Get_ClientData.argtypes = [c_int]

# C:/msys64/usr/src/grass741/dist.x86_64-w64-mingw32/include/grass/defs/ogsf.h: 50
if hasattr(_libs['grass_ogsf.7.4.1'], 'GP_str_to_marker'):
    GP_str_to_marker = _libs['grass_ogsf.7.4.1'].GP_str_to_marker
    GP_str_to_marker.restype = c_int
    GP_str_to_marker.argtypes = [String]

# C:/msys64/usr/src/grass741/dist.x86_64-w64-mingw32/include/grass/defs/ogsf.h: 53
if hasattr(_libs['grass_ogsf.7.4.1'], 'void_func'):
    void_func = _libs['grass_ogsf.7.4.1'].void_func
    void_func.restype = None
    void_func.argtypes = []

# C:/msys64/usr/src/grass741/dist.x86_64-w64-mingw32/include/grass/defs/ogsf.h: 54
if hasattr(_libs['grass_ogsf.7.4.1'], 'GS_libinit'):
    GS_libinit = _libs['grass_ogsf.7.4.1'].GS_libinit
    GS_libinit.restype = None
    GS_libinit.argtypes = []

# C:/msys64/usr/src/grass741/dist.x86_64-w64-mingw32/include/grass/defs/ogsf.h: 55
if hasattr(_libs['grass_ogsf.7.4.1'], 'GS_get_longdim'):
    GS_get_longdim = _libs['grass_ogsf.7.4.1'].GS_get_longdim
    GS_get_longdim.restype = c_int
    GS_get_longdim.argtypes = [POINTER(c_float)]

# C:/msys64/usr/src/grass741/dist.x86_64-w64-mingw32/include/grass/defs/ogsf.h: 56
if hasattr(_libs['grass_ogsf.7.4.1'], 'GS_get_region'):
    GS_get_region = _libs['grass_ogsf.7.4.1'].GS_get_region
    GS_get_region.restype = c_int
    GS_get_region.argtypes = [POINTER(c_float), POINTER(c_float), POINTER(c_float), POINTER(c_float)]

# C:/msys64/usr/src/grass741/dist.x86_64-w64-mingw32/include/grass/defs/ogsf.h: 57
if hasattr(_libs['grass_ogsf.7.4.1'], 'GS_set_att_defaults'):
    GS_set_att_defaults = _libs['grass_ogsf.7.4.1'].GS_set_att_defaults
    GS_set_att_defaults.restype = None
    GS_set_att_defaults.argtypes = [POINTER(c_float), POINTER(c_float)]

# C:/msys64/usr/src/grass741/dist.x86_64-w64-mingw32/include/grass/defs/ogsf.h: 58
if hasattr(_libs['grass_ogsf.7.4.1'], 'GS_surf_exists'):
    GS_surf_exists = _libs['grass_ogsf.7.4.1'].GS_surf_exists
    GS_surf_exists.restype = c_int
    GS_surf_exists.argtypes = [c_int]

# C:/msys64/usr/src/grass741/dist.x86_64-w64-mingw32/include/grass/defs/ogsf.h: 59
if hasattr(_libs['grass_ogsf.7.4.1'], 'GS_new_surface'):
    GS_new_surface = _libs['grass_ogsf.7.4.1'].GS_new_surface
    GS_new_surface.restype = c_int
    GS_new_surface.argtypes = []

# C:/msys64/usr/src/grass741/dist.x86_64-w64-mingw32/include/grass/defs/ogsf.h: 60
if hasattr(_libs['grass_ogsf.7.4.1'], 'GS_new_light'):
    GS_new_light = _libs['grass_ogsf.7.4.1'].GS_new_light
    GS_new_light.restype = c_int
    GS_new_light.argtypes = []

# C:/msys64/usr/src/grass741/dist.x86_64-w64-mingw32/include/grass/defs/ogsf.h: 61
if hasattr(_libs['grass_ogsf.7.4.1'], 'GS_set_light_reset'):
    GS_set_light_reset = _libs['grass_ogsf.7.4.1'].GS_set_light_reset
    GS_set_light_reset.restype = None
    GS_set_light_reset.argtypes = [c_int]

# C:/msys64/usr/src/grass741/dist.x86_64-w64-mingw32/include/grass/defs/ogsf.h: 62
if hasattr(_libs['grass_ogsf.7.4.1'], 'GS_get_light_reset'):
    GS_get_light_reset = _libs['grass_ogsf.7.4.1'].GS_get_light_reset
    GS_get_light_reset.restype = c_int
    GS_get_light_reset.argtypes = []

# C:/msys64/usr/src/grass741/dist.x86_64-w64-mingw32/include/grass/defs/ogsf.h: 63
if hasattr(_libs['grass_ogsf.7.4.1'], 'GS_setlight_position'):
    GS_setlight_position = _libs['grass_ogsf.7.4.1'].GS_setlight_position
    GS_setlight_position.restype = None
    GS_setlight_position.argtypes = [c_int, c_float, c_float, c_float, c_int]

# C:/msys64/usr/src/grass741/dist.x86_64-w64-mingw32/include/grass/defs/ogsf.h: 64
if hasattr(_libs['grass_ogsf.7.4.1'], 'GS_setlight_color'):
    GS_setlight_color = _libs['grass_ogsf.7.4.1'].GS_setlight_color
    GS_setlight_color.restype = None
    GS_setlight_color.argtypes = [c_int, c_float, c_float, c_float]

# C:/msys64/usr/src/grass741/dist.x86_64-w64-mingw32/include/grass/defs/ogsf.h: 65
if hasattr(_libs['grass_ogsf.7.4.1'], 'GS_setlight_ambient'):
    GS_setlight_ambient = _libs['grass_ogsf.7.4.1'].GS_setlight_ambient
    GS_setlight_ambient.restype = None
    GS_setlight_ambient.argtypes = [c_int, c_float, c_float, c_float]

# C:/msys64/usr/src/grass741/dist.x86_64-w64-mingw32/include/grass/defs/ogsf.h: 66
if hasattr(_libs['grass_ogsf.7.4.1'], 'GS_lights_off'):
    GS_lights_off = _libs['grass_ogsf.7.4.1'].GS_lights_off
    GS_lights_off.restype = None
    GS_lights_off.argtypes = []

# C:/msys64/usr/src/grass741/dist.x86_64-w64-mingw32/include/grass/defs/ogsf.h: 67
if hasattr(_libs['grass_ogsf.7.4.1'], 'GS_lights_on'):
    GS_lights_on = _libs['grass_ogsf.7.4.1'].GS_lights_on
    GS_lights_on.restype = None
    GS_lights_on.argtypes = []

# C:/msys64/usr/src/grass741/dist.x86_64-w64-mingw32/include/grass/defs/ogsf.h: 68
if hasattr(_libs['grass_ogsf.7.4.1'], 'GS_switchlight'):
    GS_switchlight = _libs['grass_ogsf.7.4.1'].GS_switchlight
    GS_switchlight.restype = None
    GS_switchlight.argtypes = [c_int, c_int]

# C:/msys64/usr/src/grass741/dist.x86_64-w64-mingw32/include/grass/defs/ogsf.h: 69
if hasattr(_libs['grass_ogsf.7.4.1'], 'GS_transp_is_set'):
    GS_transp_is_set = _libs['grass_ogsf.7.4.1'].GS_transp_is_set
    GS_transp_is_set.restype = c_int
    GS_transp_is_set.argtypes = []

# C:/msys64/usr/src/grass741/dist.x86_64-w64-mingw32/include/grass/defs/ogsf.h: 70
if hasattr(_libs['grass_ogsf.7.4.1'], 'GS_get_modelposition1'):
    GS_get_modelposition1 = _libs['grass_ogsf.7.4.1'].GS_get_modelposition1
    GS_get_modelposition1.restype = None
    GS_get_modelposition1.argtypes = [POINTER(c_float)]

# C:/msys64/usr/src/grass741/dist.x86_64-w64-mingw32/include/grass/defs/ogsf.h: 71
if hasattr(_libs['grass_ogsf.7.4.1'], 'GS_get_modelposition'):
    GS_get_modelposition = _libs['grass_ogsf.7.4.1'].GS_get_modelposition
    GS_get_modelposition.restype = None
    GS_get_modelposition.argtypes = [POINTER(c_float), POINTER(c_float)]

# C:/msys64/usr/src/grass741/dist.x86_64-w64-mingw32/include/grass/defs/ogsf.h: 72
if hasattr(_libs['grass_ogsf.7.4.1'], 'GS_draw_X'):
    GS_draw_X = _libs['grass_ogsf.7.4.1'].GS_draw_X
    GS_draw_X.restype = None
    GS_draw_X.argtypes = [c_int, POINTER(c_float)]

# C:/msys64/usr/src/grass741/dist.x86_64-w64-mingw32/include/grass/defs/ogsf.h: 73
if hasattr(_libs['grass_ogsf.7.4.1'], 'GS_set_Narrow'):
    GS_set_Narrow = _libs['grass_ogsf.7.4.1'].GS_set_Narrow
    GS_set_Narrow.restype = None
    GS_set_Narrow.argtypes = [POINTER(c_int), c_int, POINTER(c_float)]

# C:/msys64/usr/src/grass741/dist.x86_64-w64-mingw32/include/grass/defs/ogsf.h: 74
if hasattr(_libs['grass_ogsf.7.4.1'], 'GS_draw_line_onsurf'):
    GS_draw_line_onsurf = _libs['grass_ogsf.7.4.1'].GS_draw_line_onsurf
    GS_draw_line_onsurf.restype = None
    GS_draw_line_onsurf.argtypes = [c_int, c_float, c_float, c_float, c_float]

# C:/msys64/usr/src/grass741/dist.x86_64-w64-mingw32/include/grass/defs/ogsf.h: 75
if hasattr(_libs['grass_ogsf.7.4.1'], 'GS_draw_nline_onsurf'):
    GS_draw_nline_onsurf = _libs['grass_ogsf.7.4.1'].GS_draw_nline_onsurf
    GS_draw_nline_onsurf.restype = c_int
    GS_draw_nline_onsurf.argtypes = [c_int, c_float, c_float, c_float, c_float, POINTER(c_float), c_int]

# C:/msys64/usr/src/grass741/dist.x86_64-w64-mingw32/include/grass/defs/ogsf.h: 76
if hasattr(_libs['grass_ogsf.7.4.1'], 'GS_draw_flowline_at_xy'):
    GS_draw_flowline_at_xy = _libs['grass_ogsf.7.4.1'].GS_draw_flowline_at_xy
    GS_draw_flowline_at_xy.restype = None
    GS_draw_flowline_at_xy.argtypes = [c_int, c_float, c_float]

# C:/msys64/usr/src/grass741/dist.x86_64-w64-mingw32/include/grass/defs/ogsf.h: 77
if hasattr(_libs['grass_ogsf.7.4.1'], 'GS_draw_lighting_model1'):
    GS_draw_lighting_model1 = _libs['grass_ogsf.7.4.1'].GS_draw_lighting_model1
    GS_draw_lighting_model1.restype = None
    GS_draw_lighting_model1.argtypes = []

# C:/msys64/usr/src/grass741/dist.x86_64-w64-mingw32/include/grass/defs/ogsf.h: 78
if hasattr(_libs['grass_ogsf.7.4.1'], 'GS_draw_lighting_model'):
    GS_draw_lighting_model = _libs['grass_ogsf.7.4.1'].GS_draw_lighting_model
    GS_draw_lighting_model.restype = None
    GS_draw_lighting_model.argtypes = []

# C:/msys64/usr/src/grass741/dist.x86_64-w64-mingw32/include/grass/defs/ogsf.h: 79
if hasattr(_libs['grass_ogsf.7.4.1'], 'GS_update_curmask'):
    GS_update_curmask = _libs['grass_ogsf.7.4.1'].GS_update_curmask
    GS_update_curmask.restype = c_int
    GS_update_curmask.argtypes = [c_int]

# C:/msys64/usr/src/grass741/dist.x86_64-w64-mingw32/include/grass/defs/ogsf.h: 80
if hasattr(_libs['grass_ogsf.7.4.1'], 'GS_is_masked'):
    GS_is_masked = _libs['grass_ogsf.7.4.1'].GS_is_masked
    GS_is_masked.restype = c_int
    GS_is_masked.argtypes = [c_int, POINTER(c_float)]

# C:/msys64/usr/src/grass741/dist.x86_64-w64-mingw32/include/grass/defs/ogsf.h: 81
if hasattr(_libs['grass_ogsf.7.4.1'], 'GS_unset_SDsurf'):
    GS_unset_SDsurf = _libs['grass_ogsf.7.4.1'].GS_unset_SDsurf
    GS_unset_SDsurf.restype = None
    GS_unset_SDsurf.argtypes = []

# C:/msys64/usr/src/grass741/dist.x86_64-w64-mingw32/include/grass/defs/ogsf.h: 82
if hasattr(_libs['grass_ogsf.7.4.1'], 'GS_set_SDsurf'):
    GS_set_SDsurf = _libs['grass_ogsf.7.4.1'].GS_set_SDsurf
    GS_set_SDsurf.restype = c_int
    GS_set_SDsurf.argtypes = [c_int]

# C:/msys64/usr/src/grass741/dist.x86_64-w64-mingw32/include/grass/defs/ogsf.h: 83
if hasattr(_libs['grass_ogsf.7.4.1'], 'GS_set_SDscale'):
    GS_set_SDscale = _libs['grass_ogsf.7.4.1'].GS_set_SDscale
    GS_set_SDscale.restype = c_int
    GS_set_SDscale.argtypes = [c_float]

# C:/msys64/usr/src/grass741/dist.x86_64-w64-mingw32/include/grass/defs/ogsf.h: 84
if hasattr(_libs['grass_ogsf.7.4.1'], 'GS_get_SDsurf'):
    GS_get_SDsurf = _libs['grass_ogsf.7.4.1'].GS_get_SDsurf
    GS_get_SDsurf.restype = c_int
    GS_get_SDsurf.argtypes = [POINTER(c_int)]

# C:/msys64/usr/src/grass741/dist.x86_64-w64-mingw32/include/grass/defs/ogsf.h: 85
if hasattr(_libs['grass_ogsf.7.4.1'], 'GS_get_SDscale'):
    GS_get_SDscale = _libs['grass_ogsf.7.4.1'].GS_get_SDscale
    GS_get_SDscale.restype = c_int
    GS_get_SDscale.argtypes = [POINTER(c_float)]

# C:/msys64/usr/src/grass741/dist.x86_64-w64-mingw32/include/grass/defs/ogsf.h: 86
if hasattr(_libs['grass_ogsf.7.4.1'], 'GS_update_normals'):
    GS_update_normals = _libs['grass_ogsf.7.4.1'].GS_update_normals
    GS_update_normals.restype = c_int
    GS_update_normals.argtypes = [c_int]

# C:/msys64/usr/src/grass741/dist.x86_64-w64-mingw32/include/grass/defs/ogsf.h: 87
if hasattr(_libs['grass_ogsf.7.4.1'], 'GS_get_att'):
    GS_get_att = _libs['grass_ogsf.7.4.1'].GS_get_att
    GS_get_att.restype = c_int
    GS_get_att.argtypes = [c_int, c_int, POINTER(c_int), POINTER(c_float), String]

# C:/msys64/usr/src/grass741/dist.x86_64-w64-mingw32/include/grass/defs/ogsf.h: 88
if hasattr(_libs['grass_ogsf.7.4.1'], 'GS_get_cat_at_xy'):
    GS_get_cat_at_xy = _libs['grass_ogsf.7.4.1'].GS_get_cat_at_xy
    GS_get_cat_at_xy.restype = c_int
    GS_get_cat_at_xy.argtypes = [c_int, c_int, String, c_float, c_float]

# C:/msys64/usr/src/grass741/dist.x86_64-w64-mingw32/include/grass/defs/ogsf.h: 89
if hasattr(_libs['grass_ogsf.7.4.1'], 'GS_get_norm_at_xy'):
    GS_get_norm_at_xy = _libs['grass_ogsf.7.4.1'].GS_get_norm_at_xy
    GS_get_norm_at_xy.restype = c_int
    GS_get_norm_at_xy.argtypes = [c_int, c_float, c_float, POINTER(c_float)]

# C:/msys64/usr/src/grass741/dist.x86_64-w64-mingw32/include/grass/defs/ogsf.h: 90
if hasattr(_libs['grass_ogsf.7.4.1'], 'GS_get_val_at_xy'):
    GS_get_val_at_xy = _libs['grass_ogsf.7.4.1'].GS_get_val_at_xy
    GS_get_val_at_xy.restype = c_int
    GS_get_val_at_xy.argtypes = [c_int, c_int, String, c_float, c_float]

# C:/msys64/usr/src/grass741/dist.x86_64-w64-mingw32/include/grass/defs/ogsf.h: 91
if hasattr(_libs['grass_ogsf.7.4.1'], 'GS_unset_att'):
    GS_unset_att = _libs['grass_ogsf.7.4.1'].GS_unset_att
    GS_unset_att.restype = c_int
    GS_unset_att.argtypes = [c_int, c_int]

# C:/msys64/usr/src/grass741/dist.x86_64-w64-mingw32/include/grass/defs/ogsf.h: 92
if hasattr(_libs['grass_ogsf.7.4.1'], 'GS_set_att_const'):
    GS_set_att_const = _libs['grass_ogsf.7.4.1'].GS_set_att_const
    GS_set_att_const.restype = c_int
    GS_set_att_const.argtypes = [c_int, c_int, c_float]

# C:/msys64/usr/src/grass741/dist.x86_64-w64-mingw32/include/grass/defs/ogsf.h: 93
if hasattr(_libs['grass_ogsf.7.4.1'], 'GS_set_maskmode'):
    GS_set_maskmode = _libs['grass_ogsf.7.4.1'].GS_set_maskmode
    GS_set_maskmode.restype = c_int
    GS_set_maskmode.argtypes = [c_int, c_int]

# C:/msys64/usr/src/grass741/dist.x86_64-w64-mingw32/include/grass/defs/ogsf.h: 94
if hasattr(_libs['grass_ogsf.7.4.1'], 'GS_get_maskmode'):
    GS_get_maskmode = _libs['grass_ogsf.7.4.1'].GS_get_maskmode
    GS_get_maskmode.restype = c_int
    GS_get_maskmode.argtypes = [c_int, POINTER(c_int)]

# C:/msys64/usr/src/grass741/dist.x86_64-w64-mingw32/include/grass/defs/ogsf.h: 95
if hasattr(_libs['grass_ogsf.7.4.1'], 'GS_Set_ClientData'):
    GS_Set_ClientData = _libs['grass_ogsf.7.4.1'].GS_Set_ClientData
    GS_Set_ClientData.restype = c_int
    GS_Set_ClientData.argtypes = [c_int, POINTER(None)]

# C:/msys64/usr/src/grass741/dist.x86_64-w64-mingw32/include/grass/defs/ogsf.h: 96
if hasattr(_libs['grass_ogsf.7.4.1'], 'GS_Get_ClientData'):
    GS_Get_ClientData = _libs['grass_ogsf.7.4.1'].GS_Get_ClientData
    GS_Get_ClientData.restype = POINTER(None)
    GS_Get_ClientData.argtypes = [c_int]

# C:/msys64/usr/src/grass741/dist.x86_64-w64-mingw32/include/grass/defs/ogsf.h: 97
if hasattr(_libs['grass_ogsf.7.4.1'], 'GS_num_surfs'):
    GS_num_surfs = _libs['grass_ogsf.7.4.1'].GS_num_surfs
    GS_num_surfs.restype = c_int
    GS_num_surfs.argtypes = []

# C:/msys64/usr/src/grass741/dist.x86_64-w64-mingw32/include/grass/defs/ogsf.h: 98
if hasattr(_libs['grass_ogsf.7.4.1'], 'GS_get_surf_list'):
    GS_get_surf_list = _libs['grass_ogsf.7.4.1'].GS_get_surf_list
    GS_get_surf_list.restype = POINTER(c_int)
    GS_get_surf_list.argtypes = [POINTER(c_int)]

# C:/msys64/usr/src/grass741/dist.x86_64-w64-mingw32/include/grass/defs/ogsf.h: 99
if hasattr(_libs['grass_ogsf.7.4.1'], 'GS_delete_surface'):
    GS_delete_surface = _libs['grass_ogsf.7.4.1'].GS_delete_surface
    GS_delete_surface.restype = c_int
    GS_delete_surface.argtypes = [c_int]

# C:/msys64/usr/src/grass741/dist.x86_64-w64-mingw32/include/grass/defs/ogsf.h: 100
if hasattr(_libs['grass_ogsf.7.4.1'], 'GS_load_att_map'):
    GS_load_att_map = _libs['grass_ogsf.7.4.1'].GS_load_att_map
    GS_load_att_map.restype = c_int
    GS_load_att_map.argtypes = [c_int, String, c_int]

# C:/msys64/usr/src/grass741/dist.x86_64-w64-mingw32/include/grass/defs/ogsf.h: 101
if hasattr(_libs['grass_ogsf.7.4.1'], 'GS_draw_surf'):
    GS_draw_surf = _libs['grass_ogsf.7.4.1'].GS_draw_surf
    GS_draw_surf.restype = None
    GS_draw_surf.argtypes = [c_int]

# C:/msys64/usr/src/grass741/dist.x86_64-w64-mingw32/include/grass/defs/ogsf.h: 102
if hasattr(_libs['grass_ogsf.7.4.1'], 'GS_draw_wire'):
    GS_draw_wire = _libs['grass_ogsf.7.4.1'].GS_draw_wire
    GS_draw_wire.restype = None
    GS_draw_wire.argtypes = [c_int]

# C:/msys64/usr/src/grass741/dist.x86_64-w64-mingw32/include/grass/defs/ogsf.h: 103
if hasattr(_libs['grass_ogsf.7.4.1'], 'GS_alldraw_wire'):
    GS_alldraw_wire = _libs['grass_ogsf.7.4.1'].GS_alldraw_wire
    GS_alldraw_wire.restype = None
    GS_alldraw_wire.argtypes = []

# C:/msys64/usr/src/grass741/dist.x86_64-w64-mingw32/include/grass/defs/ogsf.h: 104
if hasattr(_libs['grass_ogsf.7.4.1'], 'GS_alldraw_surf'):
    GS_alldraw_surf = _libs['grass_ogsf.7.4.1'].GS_alldraw_surf
    GS_alldraw_surf.restype = None
    GS_alldraw_surf.argtypes = []

# C:/msys64/usr/src/grass741/dist.x86_64-w64-mingw32/include/grass/defs/ogsf.h: 105
if hasattr(_libs['grass_ogsf.7.4.1'], 'GS_set_exag'):
    GS_set_exag = _libs['grass_ogsf.7.4.1'].GS_set_exag
    GS_set_exag.restype = None
    GS_set_exag.argtypes = [c_int, c_float]

# C:/msys64/usr/src/grass741/dist.x86_64-w64-mingw32/include/grass/defs/ogsf.h: 106
if hasattr(_libs['grass_ogsf.7.4.1'], 'GS_set_global_exag'):
    GS_set_global_exag = _libs['grass_ogsf.7.4.1'].GS_set_global_exag
    GS_set_global_exag.restype = None
    GS_set_global_exag.argtypes = [c_float]

# C:/msys64/usr/src/grass741/dist.x86_64-w64-mingw32/include/grass/defs/ogsf.h: 107
if hasattr(_libs['grass_ogsf.7.4.1'], 'GS_global_exag'):
    GS_global_exag = _libs['grass_ogsf.7.4.1'].GS_global_exag
    GS_global_exag.restype = c_float
    GS_global_exag.argtypes = []

# C:/msys64/usr/src/grass741/dist.x86_64-w64-mingw32/include/grass/defs/ogsf.h: 108
if hasattr(_libs['grass_ogsf.7.4.1'], 'GS_set_wire_color'):
    GS_set_wire_color = _libs['grass_ogsf.7.4.1'].GS_set_wire_color
    GS_set_wire_color.restype = None
    GS_set_wire_color.argtypes = [c_int, c_int]

# C:/msys64/usr/src/grass741/dist.x86_64-w64-mingw32/include/grass/defs/ogsf.h: 109
if hasattr(_libs['grass_ogsf.7.4.1'], 'GS_get_wire_color'):
    GS_get_wire_color = _libs['grass_ogsf.7.4.1'].GS_get_wire_color
    GS_get_wire_color.restype = c_int
    GS_get_wire_color.argtypes = [c_int, POINTER(c_int)]

# C:/msys64/usr/src/grass741/dist.x86_64-w64-mingw32/include/grass/defs/ogsf.h: 110
if hasattr(_libs['grass_ogsf.7.4.1'], 'GS_setall_drawmode'):
    GS_setall_drawmode = _libs['grass_ogsf.7.4.1'].GS_setall_drawmode
    GS_setall_drawmode.restype = c_int
    GS_setall_drawmode.argtypes = [c_int]

# C:/msys64/usr/src/grass741/dist.x86_64-w64-mingw32/include/grass/defs/ogsf.h: 111
if hasattr(_libs['grass_ogsf.7.4.1'], 'GS_set_drawmode'):
    GS_set_drawmode = _libs['grass_ogsf.7.4.1'].GS_set_drawmode
    GS_set_drawmode.restype = c_int
    GS_set_drawmode.argtypes = [c_int, c_int]

# C:/msys64/usr/src/grass741/dist.x86_64-w64-mingw32/include/grass/defs/ogsf.h: 112
if hasattr(_libs['grass_ogsf.7.4.1'], 'GS_get_drawmode'):
    GS_get_drawmode = _libs['grass_ogsf.7.4.1'].GS_get_drawmode
    GS_get_drawmode.restype = c_int
    GS_get_drawmode.argtypes = [c_int, POINTER(c_int)]

# C:/msys64/usr/src/grass741/dist.x86_64-w64-mingw32/include/grass/defs/ogsf.h: 113
if hasattr(_libs['grass_ogsf.7.4.1'], 'GS_set_nozero'):
    GS_set_nozero = _libs['grass_ogsf.7.4.1'].GS_set_nozero
    GS_set_nozero.restype = None
    GS_set_nozero.argtypes = [c_int, c_int, c_int]

# C:/msys64/usr/src/grass741/dist.x86_64-w64-mingw32/include/grass/defs/ogsf.h: 114
if hasattr(_libs['grass_ogsf.7.4.1'], 'GS_get_nozero'):
    GS_get_nozero = _libs['grass_ogsf.7.4.1'].GS_get_nozero
    GS_get_nozero.restype = c_int
    GS_get_nozero.argtypes = [c_int, c_int, POINTER(c_int)]

# C:/msys64/usr/src/grass741/dist.x86_64-w64-mingw32/include/grass/defs/ogsf.h: 115
if hasattr(_libs['grass_ogsf.7.4.1'], 'GS_setall_drawres'):
    GS_setall_drawres = _libs['grass_ogsf.7.4.1'].GS_setall_drawres
    GS_setall_drawres.restype = c_int
    GS_setall_drawres.argtypes = [c_int, c_int, c_int, c_int]

# C:/msys64/usr/src/grass741/dist.x86_64-w64-mingw32/include/grass/defs/ogsf.h: 116
if hasattr(_libs['grass_ogsf.7.4.1'], 'GS_set_drawres'):
    GS_set_drawres = _libs['grass_ogsf.7.4.1'].GS_set_drawres
    GS_set_drawres.restype = c_int
    GS_set_drawres.argtypes = [c_int, c_int, c_int, c_int, c_int]

# C:/msys64/usr/src/grass741/dist.x86_64-w64-mingw32/include/grass/defs/ogsf.h: 117
if hasattr(_libs['grass_ogsf.7.4.1'], 'GS_get_drawres'):
    GS_get_drawres = _libs['grass_ogsf.7.4.1'].GS_get_drawres
    GS_get_drawres.restype = None
    GS_get_drawres.argtypes = [c_int, POINTER(c_int), POINTER(c_int), POINTER(c_int), POINTER(c_int)]

# C:/msys64/usr/src/grass741/dist.x86_64-w64-mingw32/include/grass/defs/ogsf.h: 118
if hasattr(_libs['grass_ogsf.7.4.1'], 'GS_get_dims'):
    GS_get_dims = _libs['grass_ogsf.7.4.1'].GS_get_dims
    GS_get_dims.restype = None
    GS_get_dims.argtypes = [c_int, POINTER(c_int), POINTER(c_int)]

# C:/msys64/usr/src/grass741/dist.x86_64-w64-mingw32/include/grass/defs/ogsf.h: 119
if hasattr(_libs['grass_ogsf.7.4.1'], 'GS_get_exag_guess'):
    GS_get_exag_guess = _libs['grass_ogsf.7.4.1'].GS_get_exag_guess
    GS_get_exag_guess.restype = c_int
    GS_get_exag_guess.argtypes = [c_int, POINTER(c_float)]

# C:/msys64/usr/src/grass741/dist.x86_64-w64-mingw32/include/grass/defs/ogsf.h: 120
if hasattr(_libs['grass_ogsf.7.4.1'], 'GS_get_zrange_nz'):
    GS_get_zrange_nz = _libs['grass_ogsf.7.4.1'].GS_get_zrange_nz
    GS_get_zrange_nz.restype = None
    GS_get_zrange_nz.argtypes = [POINTER(c_float), POINTER(c_float)]

# C:/msys64/usr/src/grass741/dist.x86_64-w64-mingw32/include/grass/defs/ogsf.h: 121
if hasattr(_libs['grass_ogsf.7.4.1'], 'GS_set_trans'):
    GS_set_trans = _libs['grass_ogsf.7.4.1'].GS_set_trans
    GS_set_trans.restype = None
    GS_set_trans.argtypes = [c_int, c_float, c_float, c_float]

# C:/msys64/usr/src/grass741/dist.x86_64-w64-mingw32/include/grass/defs/ogsf.h: 122
if hasattr(_libs['grass_ogsf.7.4.1'], 'GS_get_trans'):
    GS_get_trans = _libs['grass_ogsf.7.4.1'].GS_get_trans
    GS_get_trans.restype = None
    GS_get_trans.argtypes = [c_int, POINTER(c_float), POINTER(c_float), POINTER(c_float)]

# C:/msys64/usr/src/grass741/dist.x86_64-w64-mingw32/include/grass/defs/ogsf.h: 123
if hasattr(_libs['grass_ogsf.7.4.1'], 'GS_default_draw_color'):
    GS_default_draw_color = _libs['grass_ogsf.7.4.1'].GS_default_draw_color
    GS_default_draw_color.restype = c_uint
    GS_default_draw_color.argtypes = []

# C:/msys64/usr/src/grass741/dist.x86_64-w64-mingw32/include/grass/defs/ogsf.h: 124
if hasattr(_libs['grass_ogsf.7.4.1'], 'GS_background_color'):
    GS_background_color = _libs['grass_ogsf.7.4.1'].GS_background_color
    GS_background_color.restype = c_uint
    GS_background_color.argtypes = []

# C:/msys64/usr/src/grass741/dist.x86_64-w64-mingw32/include/grass/defs/ogsf.h: 125
if hasattr(_libs['grass_ogsf.7.4.1'], 'GS_set_draw'):
    GS_set_draw = _libs['grass_ogsf.7.4.1'].GS_set_draw
    GS_set_draw.restype = None
    GS_set_draw.argtypes = [c_int]

# C:/msys64/usr/src/grass741/dist.x86_64-w64-mingw32/include/grass/defs/ogsf.h: 126
if hasattr(_libs['grass_ogsf.7.4.1'], 'GS_ready_draw'):
    GS_ready_draw = _libs['grass_ogsf.7.4.1'].GS_ready_draw
    GS_ready_draw.restype = None
    GS_ready_draw.argtypes = []

# C:/msys64/usr/src/grass741/dist.x86_64-w64-mingw32/include/grass/defs/ogsf.h: 127
if hasattr(_libs['grass_ogsf.7.4.1'], 'GS_done_draw'):
    GS_done_draw = _libs['grass_ogsf.7.4.1'].GS_done_draw
    GS_done_draw.restype = None
    GS_done_draw.argtypes = []

# C:/msys64/usr/src/grass741/dist.x86_64-w64-mingw32/include/grass/defs/ogsf.h: 128
if hasattr(_libs['grass_ogsf.7.4.1'], 'GS_set_focus'):
    GS_set_focus = _libs['grass_ogsf.7.4.1'].GS_set_focus
    GS_set_focus.restype = None
    GS_set_focus.argtypes = [POINTER(c_float)]

# C:/msys64/usr/src/grass741/dist.x86_64-w64-mingw32/include/grass/defs/ogsf.h: 129
if hasattr(_libs['grass_ogsf.7.4.1'], 'GS_get_focus'):
    GS_get_focus = _libs['grass_ogsf.7.4.1'].GS_get_focus
    GS_get_focus.restype = c_int
    GS_get_focus.argtypes = [POINTER(c_float)]

# C:/msys64/usr/src/grass741/dist.x86_64-w64-mingw32/include/grass/defs/ogsf.h: 130
if hasattr(_libs['grass_ogsf.7.4.1'], 'GS_set_focus_center_map'):
    GS_set_focus_center_map = _libs['grass_ogsf.7.4.1'].GS_set_focus_center_map
    GS_set_focus_center_map.restype = None
    GS_set_focus_center_map.argtypes = [c_int]

# C:/msys64/usr/src/grass741/dist.x86_64-w64-mingw32/include/grass/defs/ogsf.h: 131
if hasattr(_libs['grass_ogsf.7.4.1'], 'GS_moveto'):
    GS_moveto = _libs['grass_ogsf.7.4.1'].GS_moveto
    GS_moveto.restype = None
    GS_moveto.argtypes = [POINTER(c_float)]

# C:/msys64/usr/src/grass741/dist.x86_64-w64-mingw32/include/grass/defs/ogsf.h: 132
if hasattr(_libs['grass_ogsf.7.4.1'], 'GS_moveto_real'):
    GS_moveto_real = _libs['grass_ogsf.7.4.1'].GS_moveto_real
    GS_moveto_real.restype = None
    GS_moveto_real.argtypes = [POINTER(c_float)]

# C:/msys64/usr/src/grass741/dist.x86_64-w64-mingw32/include/grass/defs/ogsf.h: 133
if hasattr(_libs['grass_ogsf.7.4.1'], 'GS_set_focus_real'):
    GS_set_focus_real = _libs['grass_ogsf.7.4.1'].GS_set_focus_real
    GS_set_focus_real.restype = None
    GS_set_focus_real.argtypes = [POINTER(c_float)]

# C:/msys64/usr/src/grass741/dist.x86_64-w64-mingw32/include/grass/defs/ogsf.h: 134
if hasattr(_libs['grass_ogsf.7.4.1'], 'GS_get_to_real'):
    GS_get_to_real = _libs['grass_ogsf.7.4.1'].GS_get_to_real
    GS_get_to_real.restype = None
    GS_get_to_real.argtypes = [POINTER(c_float)]

# C:/msys64/usr/src/grass741/dist.x86_64-w64-mingw32/include/grass/defs/ogsf.h: 135
if hasattr(_libs['grass_ogsf.7.4.1'], 'GS_get_zextents'):
    GS_get_zextents = _libs['grass_ogsf.7.4.1'].GS_get_zextents
    GS_get_zextents.restype = c_int
    GS_get_zextents.argtypes = [c_int, POINTER(c_float), POINTER(c_float), POINTER(c_float)]

# C:/msys64/usr/src/grass741/dist.x86_64-w64-mingw32/include/grass/defs/ogsf.h: 136
if hasattr(_libs['grass_ogsf.7.4.1'], 'GS_get_zrange'):
    GS_get_zrange = _libs['grass_ogsf.7.4.1'].GS_get_zrange
    GS_get_zrange.restype = c_int
    GS_get_zrange.argtypes = [POINTER(c_float), POINTER(c_float), c_int]

# C:/msys64/usr/src/grass741/dist.x86_64-w64-mingw32/include/grass/defs/ogsf.h: 137
if hasattr(_libs['grass_ogsf.7.4.1'], 'GS_get_from'):
    GS_get_from = _libs['grass_ogsf.7.4.1'].GS_get_from
    GS_get_from.restype = None
    GS_get_from.argtypes = [POINTER(c_float)]

# C:/msys64/usr/src/grass741/dist.x86_64-w64-mingw32/include/grass/defs/ogsf.h: 138
if hasattr(_libs['grass_ogsf.7.4.1'], 'GS_get_from_real'):
    GS_get_from_real = _libs['grass_ogsf.7.4.1'].GS_get_from_real
    GS_get_from_real.restype = None
    GS_get_from_real.argtypes = [POINTER(c_float)]

# C:/msys64/usr/src/grass741/dist.x86_64-w64-mingw32/include/grass/defs/ogsf.h: 139
if hasattr(_libs['grass_ogsf.7.4.1'], 'GS_get_to'):
    GS_get_to = _libs['grass_ogsf.7.4.1'].GS_get_to
    GS_get_to.restype = None
    GS_get_to.argtypes = [POINTER(c_float)]

# C:/msys64/usr/src/grass741/dist.x86_64-w64-mingw32/include/grass/defs/ogsf.h: 140
if hasattr(_libs['grass_ogsf.7.4.1'], 'GS_get_viewdir'):
    GS_get_viewdir = _libs['grass_ogsf.7.4.1'].GS_get_viewdir
    GS_get_viewdir.restype = None
    GS_get_viewdir.argtypes = [POINTER(c_float)]

# C:/msys64/usr/src/grass741/dist.x86_64-w64-mingw32/include/grass/defs/ogsf.h: 141
if hasattr(_libs['grass_ogsf.7.4.1'], 'GS_set_viewdir'):
    GS_set_viewdir = _libs['grass_ogsf.7.4.1'].GS_set_viewdir
    GS_set_viewdir.restype = None
    GS_set_viewdir.argtypes = [POINTER(c_float)]

# C:/msys64/usr/src/grass741/dist.x86_64-w64-mingw32/include/grass/defs/ogsf.h: 142
if hasattr(_libs['grass_ogsf.7.4.1'], 'GS_set_fov'):
    GS_set_fov = _libs['grass_ogsf.7.4.1'].GS_set_fov
    GS_set_fov.restype = None
    GS_set_fov.argtypes = [c_int]

# C:/msys64/usr/src/grass741/dist.x86_64-w64-mingw32/include/grass/defs/ogsf.h: 143
if hasattr(_libs['grass_ogsf.7.4.1'], 'GS_set_rotation'):
    GS_set_rotation = _libs['grass_ogsf.7.4.1'].GS_set_rotation
    GS_set_rotation.restype = None
    GS_set_rotation.argtypes = [c_double, c_double, c_double, c_double]

# C:/msys64/usr/src/grass741/dist.x86_64-w64-mingw32/include/grass/defs/ogsf.h: 144
if hasattr(_libs['grass_ogsf.7.4.1'], 'GS_get_rotation_matrix'):
    GS_get_rotation_matrix = _libs['grass_ogsf.7.4.1'].GS_get_rotation_matrix
    GS_get_rotation_matrix.restype = None
    GS_get_rotation_matrix.argtypes = [POINTER(c_double)]

# C:/msys64/usr/src/grass741/dist.x86_64-w64-mingw32/include/grass/defs/ogsf.h: 145
if hasattr(_libs['grass_ogsf.7.4.1'], 'GS_set_rotation_matrix'):
    GS_set_rotation_matrix = _libs['grass_ogsf.7.4.1'].GS_set_rotation_matrix
    GS_set_rotation_matrix.restype = None
    GS_set_rotation_matrix.argtypes = [POINTER(c_double)]

# C:/msys64/usr/src/grass741/dist.x86_64-w64-mingw32/include/grass/defs/ogsf.h: 146
if hasattr(_libs['grass_ogsf.7.4.1'], 'GS_init_rotation'):
    GS_init_rotation = _libs['grass_ogsf.7.4.1'].GS_init_rotation
    GS_init_rotation.restype = None
    GS_init_rotation.argtypes = []

# C:/msys64/usr/src/grass741/dist.x86_64-w64-mingw32/include/grass/defs/ogsf.h: 147
if hasattr(_libs['grass_ogsf.7.4.1'], 'GS_unset_rotation'):
    GS_unset_rotation = _libs['grass_ogsf.7.4.1'].GS_unset_rotation
    GS_unset_rotation.restype = None
    GS_unset_rotation.argtypes = []

# C:/msys64/usr/src/grass741/dist.x86_64-w64-mingw32/include/grass/defs/ogsf.h: 148
if hasattr(_libs['grass_ogsf.7.4.1'], 'GS_get_fov'):
    GS_get_fov = _libs['grass_ogsf.7.4.1'].GS_get_fov
    GS_get_fov.restype = c_int
    GS_get_fov.argtypes = []

# C:/msys64/usr/src/grass741/dist.x86_64-w64-mingw32/include/grass/defs/ogsf.h: 149
if hasattr(_libs['grass_ogsf.7.4.1'], 'GS_get_twist'):
    GS_get_twist = _libs['grass_ogsf.7.4.1'].GS_get_twist
    GS_get_twist.restype = c_int
    GS_get_twist.argtypes = []

# C:/msys64/usr/src/grass741/dist.x86_64-w64-mingw32/include/grass/defs/ogsf.h: 150
if hasattr(_libs['grass_ogsf.7.4.1'], 'GS_set_twist'):
    GS_set_twist = _libs['grass_ogsf.7.4.1'].GS_set_twist
    GS_set_twist.restype = None
    GS_set_twist.argtypes = [c_int]

# C:/msys64/usr/src/grass741/dist.x86_64-w64-mingw32/include/grass/defs/ogsf.h: 151
if hasattr(_libs['grass_ogsf.7.4.1'], 'GS_set_nofocus'):
    GS_set_nofocus = _libs['grass_ogsf.7.4.1'].GS_set_nofocus
    GS_set_nofocus.restype = None
    GS_set_nofocus.argtypes = []

# C:/msys64/usr/src/grass741/dist.x86_64-w64-mingw32/include/grass/defs/ogsf.h: 152
if hasattr(_libs['grass_ogsf.7.4.1'], 'GS_set_infocus'):
    GS_set_infocus = _libs['grass_ogsf.7.4.1'].GS_set_infocus
    GS_set_infocus.restype = None
    GS_set_infocus.argtypes = []

# C:/msys64/usr/src/grass741/dist.x86_64-w64-mingw32/include/grass/defs/ogsf.h: 153
if hasattr(_libs['grass_ogsf.7.4.1'], 'GS_set_viewport'):
    GS_set_viewport = _libs['grass_ogsf.7.4.1'].GS_set_viewport
    GS_set_viewport.restype = None
    GS_set_viewport.argtypes = [c_int, c_int, c_int, c_int]

# C:/msys64/usr/src/grass741/dist.x86_64-w64-mingw32/include/grass/defs/ogsf.h: 154
if hasattr(_libs['grass_ogsf.7.4.1'], 'GS_look_here'):
    GS_look_here = _libs['grass_ogsf.7.4.1'].GS_look_here
    GS_look_here.restype = c_int
    GS_look_here.argtypes = [c_int, c_int]

# C:/msys64/usr/src/grass741/dist.x86_64-w64-mingw32/include/grass/defs/ogsf.h: 155
if hasattr(_libs['grass_ogsf.7.4.1'], 'GS_get_selected_point_on_surface'):
    GS_get_selected_point_on_surface = _libs['grass_ogsf.7.4.1'].GS_get_selected_point_on_surface
    GS_get_selected_point_on_surface.restype = c_int
    GS_get_selected_point_on_surface.argtypes = [c_int, c_int, POINTER(c_int), POINTER(c_float), POINTER(c_float), POINTER(c_float)]

# C:/msys64/usr/src/grass741/dist.x86_64-w64-mingw32/include/grass/defs/ogsf.h: 157
if hasattr(_libs['grass_ogsf.7.4.1'], 'GS_set_cplane_rot'):
    GS_set_cplane_rot = _libs['grass_ogsf.7.4.1'].GS_set_cplane_rot
    GS_set_cplane_rot.restype = None
    GS_set_cplane_rot.argtypes = [c_int, c_float, c_float, c_float]

# C:/msys64/usr/src/grass741/dist.x86_64-w64-mingw32/include/grass/defs/ogsf.h: 158
if hasattr(_libs['grass_ogsf.7.4.1'], 'GS_set_cplane_trans'):
    GS_set_cplane_trans = _libs['grass_ogsf.7.4.1'].GS_set_cplane_trans
    GS_set_cplane_trans.restype = None
    GS_set_cplane_trans.argtypes = [c_int, c_float, c_float, c_float]

# C:/msys64/usr/src/grass741/dist.x86_64-w64-mingw32/include/grass/defs/ogsf.h: 159
if hasattr(_libs['grass_ogsf.7.4.1'], 'GS_draw_cplane'):
    GS_draw_cplane = _libs['grass_ogsf.7.4.1'].GS_draw_cplane
    GS_draw_cplane.restype = None
    GS_draw_cplane.argtypes = [c_int]

# C:/msys64/usr/src/grass741/dist.x86_64-w64-mingw32/include/grass/defs/ogsf.h: 160
if hasattr(_libs['grass_ogsf.7.4.1'], 'GS_draw_cplane_fence'):
    GS_draw_cplane_fence = _libs['grass_ogsf.7.4.1'].GS_draw_cplane_fence
    GS_draw_cplane_fence.restype = c_int
    GS_draw_cplane_fence.argtypes = [c_int, c_int, c_int]

# C:/msys64/usr/src/grass741/dist.x86_64-w64-mingw32/include/grass/defs/ogsf.h: 161
if hasattr(_libs['grass_ogsf.7.4.1'], 'GS_alldraw_cplane_fences'):
    GS_alldraw_cplane_fences = _libs['grass_ogsf.7.4.1'].GS_alldraw_cplane_fences
    GS_alldraw_cplane_fences.restype = None
    GS_alldraw_cplane_fences.argtypes = []

# C:/msys64/usr/src/grass741/dist.x86_64-w64-mingw32/include/grass/defs/ogsf.h: 162
if hasattr(_libs['grass_ogsf.7.4.1'], 'GS_set_cplane'):
    GS_set_cplane = _libs['grass_ogsf.7.4.1'].GS_set_cplane
    GS_set_cplane.restype = None
    GS_set_cplane.argtypes = [c_int]

# C:/msys64/usr/src/grass741/dist.x86_64-w64-mingw32/include/grass/defs/ogsf.h: 163
if hasattr(_libs['grass_ogsf.7.4.1'], 'GS_unset_cplane'):
    GS_unset_cplane = _libs['grass_ogsf.7.4.1'].GS_unset_cplane
    GS_unset_cplane.restype = None
    GS_unset_cplane.argtypes = [c_int]

# C:/msys64/usr/src/grass741/dist.x86_64-w64-mingw32/include/grass/defs/ogsf.h: 164
if hasattr(_libs['grass_ogsf.7.4.1'], 'GS_get_scale'):
    GS_get_scale = _libs['grass_ogsf.7.4.1'].GS_get_scale
    GS_get_scale.restype = None
    GS_get_scale.argtypes = [POINTER(c_float), POINTER(c_float), POINTER(c_float), c_int]

# C:/msys64/usr/src/grass741/dist.x86_64-w64-mingw32/include/grass/defs/ogsf.h: 165
if hasattr(_libs['grass_ogsf.7.4.1'], 'GS_set_fencecolor'):
    GS_set_fencecolor = _libs['grass_ogsf.7.4.1'].GS_set_fencecolor
    GS_set_fencecolor.restype = None
    GS_set_fencecolor.argtypes = [c_int]

# C:/msys64/usr/src/grass741/dist.x86_64-w64-mingw32/include/grass/defs/ogsf.h: 166
if hasattr(_libs['grass_ogsf.7.4.1'], 'GS_get_fencecolor'):
    GS_get_fencecolor = _libs['grass_ogsf.7.4.1'].GS_get_fencecolor
    GS_get_fencecolor.restype = c_int
    GS_get_fencecolor.argtypes = []

# C:/msys64/usr/src/grass741/dist.x86_64-w64-mingw32/include/grass/defs/ogsf.h: 167
if hasattr(_libs['grass_ogsf.7.4.1'], 'GS_get_distance_alongsurf'):
    GS_get_distance_alongsurf = _libs['grass_ogsf.7.4.1'].GS_get_distance_alongsurf
    GS_get_distance_alongsurf.restype = c_int
    GS_get_distance_alongsurf.argtypes = [c_int, c_float, c_float, c_float, c_float, POINTER(c_float), c_int]

# C:/msys64/usr/src/grass741/dist.x86_64-w64-mingw32/include/grass/defs/ogsf.h: 168
if hasattr(_libs['grass_ogsf.7.4.1'], 'GS_save_3dview'):
    GS_save_3dview = _libs['grass_ogsf.7.4.1'].GS_save_3dview
    GS_save_3dview.restype = c_int
    GS_save_3dview.argtypes = [String, c_int]

# C:/msys64/usr/src/grass741/dist.x86_64-w64-mingw32/include/grass/defs/ogsf.h: 169
if hasattr(_libs['grass_ogsf.7.4.1'], 'GS_load_3dview'):
    GS_load_3dview = _libs['grass_ogsf.7.4.1'].GS_load_3dview
    GS_load_3dview.restype = c_int
    GS_load_3dview.argtypes = [String, c_int]

# C:/msys64/usr/src/grass741/dist.x86_64-w64-mingw32/include/grass/defs/ogsf.h: 170
if hasattr(_libs['grass_ogsf.7.4.1'], 'GS_init_view'):
    GS_init_view = _libs['grass_ogsf.7.4.1'].GS_init_view
    GS_init_view.restype = None
    GS_init_view.argtypes = []

# C:/msys64/usr/src/grass741/dist.x86_64-w64-mingw32/include/grass/defs/ogsf.h: 171
if hasattr(_libs['grass_ogsf.7.4.1'], 'GS_clear'):
    GS_clear = _libs['grass_ogsf.7.4.1'].GS_clear
    GS_clear.restype = None
    GS_clear.argtypes = [c_int]

# C:/msys64/usr/src/grass741/dist.x86_64-w64-mingw32/include/grass/defs/ogsf.h: 172
if hasattr(_libs['grass_ogsf.7.4.1'], 'GS_get_aspect'):
    GS_get_aspect = _libs['grass_ogsf.7.4.1'].GS_get_aspect
    GS_get_aspect.restype = c_double
    GS_get_aspect.argtypes = []

# C:/msys64/usr/src/grass741/dist.x86_64-w64-mingw32/include/grass/defs/ogsf.h: 173
if hasattr(_libs['grass_ogsf.7.4.1'], 'GS_has_transparency'):
    GS_has_transparency = _libs['grass_ogsf.7.4.1'].GS_has_transparency
    GS_has_transparency.restype = c_int
    GS_has_transparency.argtypes = []

# C:/msys64/usr/src/grass741/dist.x86_64-w64-mingw32/include/grass/defs/ogsf.h: 174
if hasattr(_libs['grass_ogsf.7.4.1'], 'GS_zoom_setup'):
    GS_zoom_setup = _libs['grass_ogsf.7.4.1'].GS_zoom_setup
    GS_zoom_setup.restype = None
    GS_zoom_setup.argtypes = [POINTER(c_int), POINTER(c_int), POINTER(c_int), POINTER(c_int), POINTER(c_int), POINTER(c_int)]

# C:/msys64/usr/src/grass741/dist.x86_64-w64-mingw32/include/grass/defs/ogsf.h: 175
if hasattr(_libs['grass_ogsf.7.4.1'], 'GS_write_zoom'):
    GS_write_zoom = _libs['grass_ogsf.7.4.1'].GS_write_zoom
    GS_write_zoom.restype = c_int
    GS_write_zoom.argtypes = [String, c_uint, c_uint]

# C:/msys64/usr/src/grass741/dist.x86_64-w64-mingw32/include/grass/defs/ogsf.h: 176
if hasattr(_libs['grass_ogsf.7.4.1'], 'GS_draw_all_list'):
    GS_draw_all_list = _libs['grass_ogsf.7.4.1'].GS_draw_all_list
    GS_draw_all_list.restype = None
    GS_draw_all_list.argtypes = []

# C:/msys64/usr/src/grass741/dist.x86_64-w64-mingw32/include/grass/defs/ogsf.h: 177
if hasattr(_libs['grass_ogsf.7.4.1'], 'GS_delete_list'):
    GS_delete_list = _libs['grass_ogsf.7.4.1'].GS_delete_list
    GS_delete_list.restype = None
    GS_delete_list.argtypes = [GLuint]

# C:/msys64/usr/src/grass741/dist.x86_64-w64-mingw32/include/grass/defs/ogsf.h: 178
if hasattr(_libs['grass_ogsf.7.4.1'], 'GS_draw_legend'):
    GS_draw_legend = _libs['grass_ogsf.7.4.1'].GS_draw_legend
    GS_draw_legend.restype = c_int
    GS_draw_legend.argtypes = [String, GLuint, c_int, POINTER(c_int), POINTER(c_float), POINTER(c_int)]

# C:/msys64/usr/src/grass741/dist.x86_64-w64-mingw32/include/grass/defs/ogsf.h: 179
if hasattr(_libs['grass_ogsf.7.4.1'], 'GS_draw_fringe'):
    GS_draw_fringe = _libs['grass_ogsf.7.4.1'].GS_draw_fringe
    GS_draw_fringe.restype = None
    GS_draw_fringe.argtypes = [c_int, c_ulong, c_float, POINTER(c_int)]

# C:/msys64/usr/src/grass741/dist.x86_64-w64-mingw32/include/grass/defs/ogsf.h: 180
if hasattr(_libs['grass_ogsf.7.4.1'], 'GS_getlight_position'):
    GS_getlight_position = _libs['grass_ogsf.7.4.1'].GS_getlight_position
    GS_getlight_position.restype = None
    GS_getlight_position.argtypes = [c_int, POINTER(c_float), POINTER(c_float), POINTER(c_float), POINTER(c_int)]

# C:/msys64/usr/src/grass741/dist.x86_64-w64-mingw32/include/grass/defs/ogsf.h: 181
if hasattr(_libs['grass_ogsf.7.4.1'], 'GS_getlight_color'):
    GS_getlight_color = _libs['grass_ogsf.7.4.1'].GS_getlight_color
    GS_getlight_color.restype = None
    GS_getlight_color.argtypes = [c_int, POINTER(c_float), POINTER(c_float), POINTER(c_float)]

# C:/msys64/usr/src/grass741/dist.x86_64-w64-mingw32/include/grass/defs/ogsf.h: 182
if hasattr(_libs['grass_ogsf.7.4.1'], 'GS_getlight_ambient'):
    GS_getlight_ambient = _libs['grass_ogsf.7.4.1'].GS_getlight_ambient
    GS_getlight_ambient.restype = None
    GS_getlight_ambient.argtypes = [c_int, POINTER(c_float), POINTER(c_float), POINTER(c_float)]

# C:/msys64/usr/src/grass741/dist.x86_64-w64-mingw32/include/grass/defs/ogsf.h: 185
if hasattr(_libs['grass_ogsf.7.4.1'], 'GS_check_cancel'):
    GS_check_cancel = _libs['grass_ogsf.7.4.1'].GS_check_cancel
    GS_check_cancel.restype = c_int
    GS_check_cancel.argtypes = []

# C:/msys64/usr/src/grass741/dist.x86_64-w64-mingw32/include/grass/defs/ogsf.h: 186
if hasattr(_libs['grass_ogsf.7.4.1'], 'GS_set_cancel'):
    GS_set_cancel = _libs['grass_ogsf.7.4.1'].GS_set_cancel
    GS_set_cancel.restype = None
    GS_set_cancel.argtypes = [c_int]

# C:/msys64/usr/src/grass741/dist.x86_64-w64-mingw32/include/grass/defs/ogsf.h: 187
if hasattr(_libs['grass_ogsf.7.4.1'], 'GS_set_cxl_func'):
    GS_set_cxl_func = _libs['grass_ogsf.7.4.1'].GS_set_cxl_func
    GS_set_cxl_func.restype = None
    GS_set_cxl_func.argtypes = [CFUNCTYPE(UNCHECKED(None), )]

# C:/msys64/usr/src/grass741/dist.x86_64-w64-mingw32/include/grass/defs/ogsf.h: 188
if hasattr(_libs['grass_ogsf.7.4.1'], 'GS_set_swap_func'):
    GS_set_swap_func = _libs['grass_ogsf.7.4.1'].GS_set_swap_func
    GS_set_swap_func.restype = None
    GS_set_swap_func.argtypes = [CFUNCTYPE(UNCHECKED(None), )]

# C:/msys64/usr/src/grass741/dist.x86_64-w64-mingw32/include/grass/defs/ogsf.h: 191
if hasattr(_libs['grass_ogsf.7.4.1'], 'GS_geodistance'):
    GS_geodistance = _libs['grass_ogsf.7.4.1'].GS_geodistance
    GS_geodistance.restype = c_double
    GS_geodistance.argtypes = [POINTER(c_double), POINTER(c_double), String]

# C:/msys64/usr/src/grass741/dist.x86_64-w64-mingw32/include/grass/defs/ogsf.h: 192
if hasattr(_libs['grass_ogsf.7.4.1'], 'GS_distance'):
    GS_distance = _libs['grass_ogsf.7.4.1'].GS_distance
    GS_distance.restype = c_float
    GS_distance.argtypes = [POINTER(c_float), POINTER(c_float)]

# C:/msys64/usr/src/grass741/dist.x86_64-w64-mingw32/include/grass/defs/ogsf.h: 193
if hasattr(_libs['grass_ogsf.7.4.1'], 'GS_P2distance'):
    GS_P2distance = _libs['grass_ogsf.7.4.1'].GS_P2distance
    GS_P2distance.restype = c_float
    GS_P2distance.argtypes = [POINTER(c_float), POINTER(c_float)]

# C:/msys64/usr/src/grass741/dist.x86_64-w64-mingw32/include/grass/defs/ogsf.h: 194
if hasattr(_libs['grass_ogsf.7.4.1'], 'GS_v3eq'):
    GS_v3eq = _libs['grass_ogsf.7.4.1'].GS_v3eq
    GS_v3eq.restype = None
    GS_v3eq.argtypes = [POINTER(c_float), POINTER(c_float)]

# C:/msys64/usr/src/grass741/dist.x86_64-w64-mingw32/include/grass/defs/ogsf.h: 195
if hasattr(_libs['grass_ogsf.7.4.1'], 'GS_v3add'):
    GS_v3add = _libs['grass_ogsf.7.4.1'].GS_v3add
    GS_v3add.restype = None
    GS_v3add.argtypes = [POINTER(c_float), POINTER(c_float)]

# C:/msys64/usr/src/grass741/dist.x86_64-w64-mingw32/include/grass/defs/ogsf.h: 196
if hasattr(_libs['grass_ogsf.7.4.1'], 'GS_v3sub'):
    GS_v3sub = _libs['grass_ogsf.7.4.1'].GS_v3sub
    GS_v3sub.restype = None
    GS_v3sub.argtypes = [POINTER(c_float), POINTER(c_float)]

# C:/msys64/usr/src/grass741/dist.x86_64-w64-mingw32/include/grass/defs/ogsf.h: 197
if hasattr(_libs['grass_ogsf.7.4.1'], 'GS_v3mult'):
    GS_v3mult = _libs['grass_ogsf.7.4.1'].GS_v3mult
    GS_v3mult.restype = None
    GS_v3mult.argtypes = [POINTER(c_float), c_float]

# C:/msys64/usr/src/grass741/dist.x86_64-w64-mingw32/include/grass/defs/ogsf.h: 198
if hasattr(_libs['grass_ogsf.7.4.1'], 'GS_v3norm'):
    GS_v3norm = _libs['grass_ogsf.7.4.1'].GS_v3norm
    GS_v3norm.restype = c_int
    GS_v3norm.argtypes = [POINTER(c_float)]

# C:/msys64/usr/src/grass741/dist.x86_64-w64-mingw32/include/grass/defs/ogsf.h: 199
if hasattr(_libs['grass_ogsf.7.4.1'], 'GS_v2norm'):
    GS_v2norm = _libs['grass_ogsf.7.4.1'].GS_v2norm
    GS_v2norm.restype = c_int
    GS_v2norm.argtypes = [POINTER(c_float)]

# C:/msys64/usr/src/grass741/dist.x86_64-w64-mingw32/include/grass/defs/ogsf.h: 200
if hasattr(_libs['grass_ogsf.7.4.1'], 'GS_dv3norm'):
    GS_dv3norm = _libs['grass_ogsf.7.4.1'].GS_dv3norm
    GS_dv3norm.restype = c_int
    GS_dv3norm.argtypes = [POINTER(c_double)]

# C:/msys64/usr/src/grass741/dist.x86_64-w64-mingw32/include/grass/defs/ogsf.h: 201
if hasattr(_libs['grass_ogsf.7.4.1'], 'GS_v3normalize'):
    GS_v3normalize = _libs['grass_ogsf.7.4.1'].GS_v3normalize
    GS_v3normalize.restype = c_int
    GS_v3normalize.argtypes = [POINTER(c_float), POINTER(c_float)]

# C:/msys64/usr/src/grass741/dist.x86_64-w64-mingw32/include/grass/defs/ogsf.h: 202
if hasattr(_libs['grass_ogsf.7.4.1'], 'GS_v3dir'):
    GS_v3dir = _libs['grass_ogsf.7.4.1'].GS_v3dir
    GS_v3dir.restype = c_int
    GS_v3dir.argtypes = [POINTER(c_float), POINTER(c_float), POINTER(c_float)]

# C:/msys64/usr/src/grass741/dist.x86_64-w64-mingw32/include/grass/defs/ogsf.h: 203
if hasattr(_libs['grass_ogsf.7.4.1'], 'GS_v2dir'):
    GS_v2dir = _libs['grass_ogsf.7.4.1'].GS_v2dir
    GS_v2dir.restype = None
    GS_v2dir.argtypes = [POINTER(c_float), POINTER(c_float), POINTER(c_float)]

# C:/msys64/usr/src/grass741/dist.x86_64-w64-mingw32/include/grass/defs/ogsf.h: 204
if hasattr(_libs['grass_ogsf.7.4.1'], 'GS_v3cross'):
    GS_v3cross = _libs['grass_ogsf.7.4.1'].GS_v3cross
    GS_v3cross.restype = None
    GS_v3cross.argtypes = [POINTER(c_float), POINTER(c_float), POINTER(c_float)]

# C:/msys64/usr/src/grass741/dist.x86_64-w64-mingw32/include/grass/defs/ogsf.h: 205
if hasattr(_libs['grass_ogsf.7.4.1'], 'GS_v3mag'):
    GS_v3mag = _libs['grass_ogsf.7.4.1'].GS_v3mag
    GS_v3mag.restype = None
    GS_v3mag.argtypes = [POINTER(c_float), POINTER(c_float)]

# C:/msys64/usr/src/grass741/dist.x86_64-w64-mingw32/include/grass/defs/ogsf.h: 206
if hasattr(_libs['grass_ogsf.7.4.1'], 'GS_coordpair_repeats'):
    GS_coordpair_repeats = _libs['grass_ogsf.7.4.1'].GS_coordpair_repeats
    GS_coordpair_repeats.restype = c_int
    GS_coordpair_repeats.argtypes = [POINTER(c_float), POINTER(c_float), c_int]

# C:/msys64/usr/src/grass741/dist.x86_64-w64-mingw32/include/grass/defs/ogsf.h: 209
if hasattr(_libs['grass_ogsf.7.4.1'], 'GV_vect_exists'):
    GV_vect_exists = _libs['grass_ogsf.7.4.1'].GV_vect_exists
    GV_vect_exists.restype = c_int
    GV_vect_exists.argtypes = [c_int]

# C:/msys64/usr/src/grass741/dist.x86_64-w64-mingw32/include/grass/defs/ogsf.h: 210
if hasattr(_libs['grass_ogsf.7.4.1'], 'GV_new_vector'):
    GV_new_vector = _libs['grass_ogsf.7.4.1'].GV_new_vector
    GV_new_vector.restype = c_int
    GV_new_vector.argtypes = []

# C:/msys64/usr/src/grass741/dist.x86_64-w64-mingw32/include/grass/defs/ogsf.h: 211
if hasattr(_libs['grass_ogsf.7.4.1'], 'GV_num_vects'):
    GV_num_vects = _libs['grass_ogsf.7.4.1'].GV_num_vects
    GV_num_vects.restype = c_int
    GV_num_vects.argtypes = []

# C:/msys64/usr/src/grass741/dist.x86_64-w64-mingw32/include/grass/defs/ogsf.h: 212
if hasattr(_libs['grass_ogsf.7.4.1'], 'GV_get_vect_list'):
    GV_get_vect_list = _libs['grass_ogsf.7.4.1'].GV_get_vect_list
    GV_get_vect_list.restype = POINTER(c_int)
    GV_get_vect_list.argtypes = [POINTER(c_int)]

# C:/msys64/usr/src/grass741/dist.x86_64-w64-mingw32/include/grass/defs/ogsf.h: 213
if hasattr(_libs['grass_ogsf.7.4.1'], 'GV_delete_vector'):
    GV_delete_vector = _libs['grass_ogsf.7.4.1'].GV_delete_vector
    GV_delete_vector.restype = c_int
    GV_delete_vector.argtypes = [c_int]

# C:/msys64/usr/src/grass741/dist.x86_64-w64-mingw32/include/grass/defs/ogsf.h: 214
if hasattr(_libs['grass_ogsf.7.4.1'], 'GV_load_vector'):
    GV_load_vector = _libs['grass_ogsf.7.4.1'].GV_load_vector
    GV_load_vector.restype = c_int
    GV_load_vector.argtypes = [c_int, String]

# C:/msys64/usr/src/grass741/dist.x86_64-w64-mingw32/include/grass/defs/ogsf.h: 215
if hasattr(_libs['grass_ogsf.7.4.1'], 'GV_get_vectname'):
    GV_get_vectname = _libs['grass_ogsf.7.4.1'].GV_get_vectname
    GV_get_vectname.restype = c_int
    GV_get_vectname.argtypes = [c_int, POINTER(POINTER(c_char))]

# C:/msys64/usr/src/grass741/dist.x86_64-w64-mingw32/include/grass/defs/ogsf.h: 216
if hasattr(_libs['grass_ogsf.7.4.1'], 'GV_set_style'):
    GV_set_style = _libs['grass_ogsf.7.4.1'].GV_set_style
    GV_set_style.restype = c_int
    GV_set_style.argtypes = [c_int, c_int, c_int, c_int, c_int]

# C:/msys64/usr/src/grass741/dist.x86_64-w64-mingw32/include/grass/defs/ogsf.h: 217
if hasattr(_libs['grass_ogsf.7.4.1'], 'GV_get_style'):
    GV_get_style = _libs['grass_ogsf.7.4.1'].GV_get_style
    GV_get_style.restype = c_int
    GV_get_style.argtypes = [c_int, POINTER(c_int), POINTER(c_int), POINTER(c_int), POINTER(c_int)]

# C:/msys64/usr/src/grass741/dist.x86_64-w64-mingw32/include/grass/defs/ogsf.h: 218
if hasattr(_libs['grass_ogsf.7.4.1'], 'GV_set_style_thematic'):
    GV_set_style_thematic = _libs['grass_ogsf.7.4.1'].GV_set_style_thematic
    GV_set_style_thematic.restype = c_int
    GV_set_style_thematic.argtypes = [c_int, c_int, String, String, POINTER(struct_Colors)]

# C:/msys64/usr/src/grass741/dist.x86_64-w64-mingw32/include/grass/defs/ogsf.h: 219
if hasattr(_libs['grass_ogsf.7.4.1'], 'GV_unset_style_thematic'):
    GV_unset_style_thematic = _libs['grass_ogsf.7.4.1'].GV_unset_style_thematic
    GV_unset_style_thematic.restype = c_int
    GV_unset_style_thematic.argtypes = [c_int]

# C:/msys64/usr/src/grass741/dist.x86_64-w64-mingw32/include/grass/defs/ogsf.h: 220
if hasattr(_libs['grass_ogsf.7.4.1'], 'GV_set_trans'):
    GV_set_trans = _libs['grass_ogsf.7.4.1'].GV_set_trans
    GV_set_trans.restype = None
    GV_set_trans.argtypes = [c_int, c_float, c_float, c_float]

# C:/msys64/usr/src/grass741/dist.x86_64-w64-mingw32/include/grass/defs/ogsf.h: 221
if hasattr(_libs['grass_ogsf.7.4.1'], 'GV_get_trans'):
    GV_get_trans = _libs['grass_ogsf.7.4.1'].GV_get_trans
    GV_get_trans.restype = c_int
    GV_get_trans.argtypes = [c_int, POINTER(c_float), POINTER(c_float), POINTER(c_float)]

# C:/msys64/usr/src/grass741/dist.x86_64-w64-mingw32/include/grass/defs/ogsf.h: 222
if hasattr(_libs['grass_ogsf.7.4.1'], 'GV_select_surf'):
    GV_select_surf = _libs['grass_ogsf.7.4.1'].GV_select_surf
    GV_select_surf.restype = c_int
    GV_select_surf.argtypes = [c_int, c_int]

# C:/msys64/usr/src/grass741/dist.x86_64-w64-mingw32/include/grass/defs/ogsf.h: 223
if hasattr(_libs['grass_ogsf.7.4.1'], 'GV_unselect_surf'):
    GV_unselect_surf = _libs['grass_ogsf.7.4.1'].GV_unselect_surf
    GV_unselect_surf.restype = c_int
    GV_unselect_surf.argtypes = [c_int, c_int]

# C:/msys64/usr/src/grass741/dist.x86_64-w64-mingw32/include/grass/defs/ogsf.h: 224
if hasattr(_libs['grass_ogsf.7.4.1'], 'GV_surf_is_selected'):
    GV_surf_is_selected = _libs['grass_ogsf.7.4.1'].GV_surf_is_selected
    GV_surf_is_selected.restype = c_int
    GV_surf_is_selected.argtypes = [c_int, c_int]

# C:/msys64/usr/src/grass741/dist.x86_64-w64-mingw32/include/grass/defs/ogsf.h: 225
if hasattr(_libs['grass_ogsf.7.4.1'], 'GV_draw_vect'):
    GV_draw_vect = _libs['grass_ogsf.7.4.1'].GV_draw_vect
    GV_draw_vect.restype = None
    GV_draw_vect.argtypes = [c_int]

# C:/msys64/usr/src/grass741/dist.x86_64-w64-mingw32/include/grass/defs/ogsf.h: 226
if hasattr(_libs['grass_ogsf.7.4.1'], 'GV_alldraw_vect'):
    GV_alldraw_vect = _libs['grass_ogsf.7.4.1'].GV_alldraw_vect
    GV_alldraw_vect.restype = None
    GV_alldraw_vect.argtypes = []

# C:/msys64/usr/src/grass741/dist.x86_64-w64-mingw32/include/grass/defs/ogsf.h: 227
if hasattr(_libs['grass_ogsf.7.4.1'], 'GV_alldraw_fastvect'):
    GV_alldraw_fastvect = _libs['grass_ogsf.7.4.1'].GV_alldraw_fastvect
    GV_alldraw_fastvect.restype = None
    GV_alldraw_fastvect.argtypes = []

# C:/msys64/usr/src/grass741/dist.x86_64-w64-mingw32/include/grass/defs/ogsf.h: 228
if hasattr(_libs['grass_ogsf.7.4.1'], 'GV_draw_fastvect'):
    GV_draw_fastvect = _libs['grass_ogsf.7.4.1'].GV_draw_fastvect
    GV_draw_fastvect.restype = None
    GV_draw_fastvect.argtypes = [c_int]

# C:/msys64/usr/src/grass741/dist.x86_64-w64-mingw32/include/grass/defs/ogsf.h: 229
if hasattr(_libs['grass_ogsf.7.4.1'], 'GV_Set_ClientData'):
    GV_Set_ClientData = _libs['grass_ogsf.7.4.1'].GV_Set_ClientData
    GV_Set_ClientData.restype = c_int
    GV_Set_ClientData.argtypes = [c_int, POINTER(None)]

# C:/msys64/usr/src/grass741/dist.x86_64-w64-mingw32/include/grass/defs/ogsf.h: 230
if hasattr(_libs['grass_ogsf.7.4.1'], 'GV_Get_ClientData'):
    GV_Get_ClientData = _libs['grass_ogsf.7.4.1'].GV_Get_ClientData
    GV_Get_ClientData.restype = POINTER(None)
    GV_Get_ClientData.argtypes = [c_int]

# C:/msys64/usr/src/grass741/dist.x86_64-w64-mingw32/include/grass/defs/ogsf.h: 233
if hasattr(_libs['grass_ogsf.7.4.1'], 'GVL_libinit'):
    GVL_libinit = _libs['grass_ogsf.7.4.1'].GVL_libinit
    GVL_libinit.restype = None
    GVL_libinit.argtypes = []

# C:/msys64/usr/src/grass741/dist.x86_64-w64-mingw32/include/grass/defs/ogsf.h: 234
if hasattr(_libs['grass_ogsf.7.4.1'], 'GVL_init_region'):
    GVL_init_region = _libs['grass_ogsf.7.4.1'].GVL_init_region
    GVL_init_region.restype = None
    GVL_init_region.argtypes = []

# C:/msys64/usr/src/grass741/dist.x86_64-w64-mingw32/include/grass/defs/ogsf.h: 235
if hasattr(_libs['grass_ogsf.7.4.1'], 'GVL_get_region'):
    GVL_get_region = _libs['grass_ogsf.7.4.1'].GVL_get_region
    GVL_get_region.restype = c_int
    GVL_get_region.argtypes = [POINTER(c_float), POINTER(c_float), POINTER(c_float), POINTER(c_float), POINTER(c_float), POINTER(c_float)]

# C:/msys64/usr/src/grass741/dist.x86_64-w64-mingw32/include/grass/defs/ogsf.h: 236
if hasattr(_libs['grass_ogsf.7.4.1'], 'GVL_get_window'):
    GVL_get_window = _libs['grass_ogsf.7.4.1'].GVL_get_window
    GVL_get_window.restype = POINTER(None)
    GVL_get_window.argtypes = []

# C:/msys64/usr/src/grass741/dist.x86_64-w64-mingw32/include/grass/defs/ogsf.h: 237
if hasattr(_libs['grass_ogsf.7.4.1'], 'GVL_vol_exists'):
    GVL_vol_exists = _libs['grass_ogsf.7.4.1'].GVL_vol_exists
    GVL_vol_exists.restype = c_int
    GVL_vol_exists.argtypes = [c_int]

# C:/msys64/usr/src/grass741/dist.x86_64-w64-mingw32/include/grass/defs/ogsf.h: 238
if hasattr(_libs['grass_ogsf.7.4.1'], 'GVL_new_vol'):
    GVL_new_vol = _libs['grass_ogsf.7.4.1'].GVL_new_vol
    GVL_new_vol.restype = c_int
    GVL_new_vol.argtypes = []

# C:/msys64/usr/src/grass741/dist.x86_64-w64-mingw32/include/grass/defs/ogsf.h: 239
if hasattr(_libs['grass_ogsf.7.4.1'], 'GVL_num_vols'):
    GVL_num_vols = _libs['grass_ogsf.7.4.1'].GVL_num_vols
    GVL_num_vols.restype = c_int
    GVL_num_vols.argtypes = []

# C:/msys64/usr/src/grass741/dist.x86_64-w64-mingw32/include/grass/defs/ogsf.h: 240
if hasattr(_libs['grass_ogsf.7.4.1'], 'GVL_get_vol_list'):
    GVL_get_vol_list = _libs['grass_ogsf.7.4.1'].GVL_get_vol_list
    GVL_get_vol_list.restype = POINTER(c_int)
    GVL_get_vol_list.argtypes = [POINTER(c_int)]

# C:/msys64/usr/src/grass741/dist.x86_64-w64-mingw32/include/grass/defs/ogsf.h: 241
if hasattr(_libs['grass_ogsf.7.4.1'], 'GVL_delete_vol'):
    GVL_delete_vol = _libs['grass_ogsf.7.4.1'].GVL_delete_vol
    GVL_delete_vol.restype = c_int
    GVL_delete_vol.argtypes = [c_int]

# C:/msys64/usr/src/grass741/dist.x86_64-w64-mingw32/include/grass/defs/ogsf.h: 242
if hasattr(_libs['grass_ogsf.7.4.1'], 'GVL_load_vol'):
    GVL_load_vol = _libs['grass_ogsf.7.4.1'].GVL_load_vol
    GVL_load_vol.restype = c_int
    GVL_load_vol.argtypes = [c_int, String]

# C:/msys64/usr/src/grass741/dist.x86_64-w64-mingw32/include/grass/defs/ogsf.h: 243
if hasattr(_libs['grass_ogsf.7.4.1'], 'GVL_get_volname'):
    GVL_get_volname = _libs['grass_ogsf.7.4.1'].GVL_get_volname
    GVL_get_volname.restype = c_int
    GVL_get_volname.argtypes = [c_int, String]

# C:/msys64/usr/src/grass741/dist.x86_64-w64-mingw32/include/grass/defs/ogsf.h: 244
if hasattr(_libs['grass_ogsf.7.4.1'], 'GVL_set_trans'):
    GVL_set_trans = _libs['grass_ogsf.7.4.1'].GVL_set_trans
    GVL_set_trans.restype = None
    GVL_set_trans.argtypes = [c_int, c_float, c_float, c_float]

# C:/msys64/usr/src/grass741/dist.x86_64-w64-mingw32/include/grass/defs/ogsf.h: 245
if hasattr(_libs['grass_ogsf.7.4.1'], 'GVL_get_trans'):
    GVL_get_trans = _libs['grass_ogsf.7.4.1'].GVL_get_trans
    GVL_get_trans.restype = c_int
    GVL_get_trans.argtypes = [c_int, POINTER(c_float), POINTER(c_float), POINTER(c_float)]

# C:/msys64/usr/src/grass741/dist.x86_64-w64-mingw32/include/grass/defs/ogsf.h: 246
if hasattr(_libs['grass_ogsf.7.4.1'], 'GVL_set_draw_wire'):
    GVL_set_draw_wire = _libs['grass_ogsf.7.4.1'].GVL_set_draw_wire
    GVL_set_draw_wire.restype = None
    GVL_set_draw_wire.argtypes = [c_int, c_int]

# C:/msys64/usr/src/grass741/dist.x86_64-w64-mingw32/include/grass/defs/ogsf.h: 247
if hasattr(_libs['grass_ogsf.7.4.1'], 'GVL_draw_vol'):
    GVL_draw_vol = _libs['grass_ogsf.7.4.1'].GVL_draw_vol
    GVL_draw_vol.restype = None
    GVL_draw_vol.argtypes = [c_int]

# C:/msys64/usr/src/grass741/dist.x86_64-w64-mingw32/include/grass/defs/ogsf.h: 248
if hasattr(_libs['grass_ogsf.7.4.1'], 'GVL_draw_wire'):
    GVL_draw_wire = _libs['grass_ogsf.7.4.1'].GVL_draw_wire
    GVL_draw_wire.restype = None
    GVL_draw_wire.argtypes = [c_int]

# C:/msys64/usr/src/grass741/dist.x86_64-w64-mingw32/include/grass/defs/ogsf.h: 249
if hasattr(_libs['grass_ogsf.7.4.1'], 'GVL_alldraw_vol'):
    GVL_alldraw_vol = _libs['grass_ogsf.7.4.1'].GVL_alldraw_vol
    GVL_alldraw_vol.restype = None
    GVL_alldraw_vol.argtypes = []

# C:/msys64/usr/src/grass741/dist.x86_64-w64-mingw32/include/grass/defs/ogsf.h: 250
if hasattr(_libs['grass_ogsf.7.4.1'], 'GVL_alldraw_wire'):
    GVL_alldraw_wire = _libs['grass_ogsf.7.4.1'].GVL_alldraw_wire
    GVL_alldraw_wire.restype = None
    GVL_alldraw_wire.argtypes = []

# C:/msys64/usr/src/grass741/dist.x86_64-w64-mingw32/include/grass/defs/ogsf.h: 251
if hasattr(_libs['grass_ogsf.7.4.1'], 'GVL_Set_ClientData'):
    GVL_Set_ClientData = _libs['grass_ogsf.7.4.1'].GVL_Set_ClientData
    GVL_Set_ClientData.restype = c_int
    GVL_Set_ClientData.argtypes = [c_int, POINTER(None)]

# C:/msys64/usr/src/grass741/dist.x86_64-w64-mingw32/include/grass/defs/ogsf.h: 252
if hasattr(_libs['grass_ogsf.7.4.1'], 'GVL_Get_ClientData'):
    GVL_Get_ClientData = _libs['grass_ogsf.7.4.1'].GVL_Get_ClientData
    GVL_Get_ClientData.restype = POINTER(None)
    GVL_Get_ClientData.argtypes = [c_int]

# C:/msys64/usr/src/grass741/dist.x86_64-w64-mingw32/include/grass/defs/ogsf.h: 253
if hasattr(_libs['grass_ogsf.7.4.1'], 'GVL_get_dims'):
    GVL_get_dims = _libs['grass_ogsf.7.4.1'].GVL_get_dims
    GVL_get_dims.restype = None
    GVL_get_dims.argtypes = [c_int, POINTER(c_int), POINTER(c_int), POINTER(c_int)]

# C:/msys64/usr/src/grass741/dist.x86_64-w64-mingw32/include/grass/defs/ogsf.h: 254
if hasattr(_libs['grass_ogsf.7.4.1'], 'GVL_set_focus_center_map'):
    GVL_set_focus_center_map = _libs['grass_ogsf.7.4.1'].GVL_set_focus_center_map
    GVL_set_focus_center_map.restype = None
    GVL_set_focus_center_map.argtypes = [c_int]

# C:/msys64/usr/src/grass741/dist.x86_64-w64-mingw32/include/grass/defs/ogsf.h: 256
if hasattr(_libs['grass_ogsf.7.4.1'], 'GVL_isosurf_move_up'):
    GVL_isosurf_move_up = _libs['grass_ogsf.7.4.1'].GVL_isosurf_move_up
    GVL_isosurf_move_up.restype = c_int
    GVL_isosurf_move_up.argtypes = [c_int, c_int]

# C:/msys64/usr/src/grass741/dist.x86_64-w64-mingw32/include/grass/defs/ogsf.h: 257
if hasattr(_libs['grass_ogsf.7.4.1'], 'GVL_isosurf_move_down'):
    GVL_isosurf_move_down = _libs['grass_ogsf.7.4.1'].GVL_isosurf_move_down
    GVL_isosurf_move_down.restype = c_int
    GVL_isosurf_move_down.argtypes = [c_int, c_int]

# C:/msys64/usr/src/grass741/dist.x86_64-w64-mingw32/include/grass/defs/ogsf.h: 258
if hasattr(_libs['grass_ogsf.7.4.1'], 'GVL_isosurf_get_drawres'):
    GVL_isosurf_get_drawres = _libs['grass_ogsf.7.4.1'].GVL_isosurf_get_drawres
    GVL_isosurf_get_drawres.restype = None
    GVL_isosurf_get_drawres.argtypes = [c_int, POINTER(c_int), POINTER(c_int), POINTER(c_int)]

# C:/msys64/usr/src/grass741/dist.x86_64-w64-mingw32/include/grass/defs/ogsf.h: 259
if hasattr(_libs['grass_ogsf.7.4.1'], 'GVL_isosurf_set_drawres'):
    GVL_isosurf_set_drawres = _libs['grass_ogsf.7.4.1'].GVL_isosurf_set_drawres
    GVL_isosurf_set_drawres.restype = c_int
    GVL_isosurf_set_drawres.argtypes = [c_int, c_int, c_int, c_int]

# C:/msys64/usr/src/grass741/dist.x86_64-w64-mingw32/include/grass/defs/ogsf.h: 260
if hasattr(_libs['grass_ogsf.7.4.1'], 'GVL_isosurf_get_drawmode'):
    GVL_isosurf_get_drawmode = _libs['grass_ogsf.7.4.1'].GVL_isosurf_get_drawmode
    GVL_isosurf_get_drawmode.restype = c_int
    GVL_isosurf_get_drawmode.argtypes = [c_int, POINTER(c_int)]

# C:/msys64/usr/src/grass741/dist.x86_64-w64-mingw32/include/grass/defs/ogsf.h: 261
if hasattr(_libs['grass_ogsf.7.4.1'], 'GVL_isosurf_set_drawmode'):
    GVL_isosurf_set_drawmode = _libs['grass_ogsf.7.4.1'].GVL_isosurf_set_drawmode
    GVL_isosurf_set_drawmode.restype = c_int
    GVL_isosurf_set_drawmode.argtypes = [c_int, c_int]

# C:/msys64/usr/src/grass741/dist.x86_64-w64-mingw32/include/grass/defs/ogsf.h: 262
if hasattr(_libs['grass_ogsf.7.4.1'], 'GVL_isosurf_add'):
    GVL_isosurf_add = _libs['grass_ogsf.7.4.1'].GVL_isosurf_add
    GVL_isosurf_add.restype = c_int
    GVL_isosurf_add.argtypes = [c_int]

# C:/msys64/usr/src/grass741/dist.x86_64-w64-mingw32/include/grass/defs/ogsf.h: 263
if hasattr(_libs['grass_ogsf.7.4.1'], 'GVL_isosurf_del'):
    GVL_isosurf_del = _libs['grass_ogsf.7.4.1'].GVL_isosurf_del
    GVL_isosurf_del.restype = c_int
    GVL_isosurf_del.argtypes = [c_int, c_int]

# C:/msys64/usr/src/grass741/dist.x86_64-w64-mingw32/include/grass/defs/ogsf.h: 264
if hasattr(_libs['grass_ogsf.7.4.1'], 'GVL_isosurf_get_att'):
    GVL_isosurf_get_att = _libs['grass_ogsf.7.4.1'].GVL_isosurf_get_att
    GVL_isosurf_get_att.restype = c_int
    GVL_isosurf_get_att.argtypes = [c_int, c_int, c_int, POINTER(c_int), POINTER(c_float), String]

# C:/msys64/usr/src/grass741/dist.x86_64-w64-mingw32/include/grass/defs/ogsf.h: 265
if hasattr(_libs['grass_ogsf.7.4.1'], 'GVL_isosurf_unset_att'):
    GVL_isosurf_unset_att = _libs['grass_ogsf.7.4.1'].GVL_isosurf_unset_att
    GVL_isosurf_unset_att.restype = c_int
    GVL_isosurf_unset_att.argtypes = [c_int, c_int, c_int]

# C:/msys64/usr/src/grass741/dist.x86_64-w64-mingw32/include/grass/defs/ogsf.h: 266
if hasattr(_libs['grass_ogsf.7.4.1'], 'GVL_isosurf_set_att_const'):
    GVL_isosurf_set_att_const = _libs['grass_ogsf.7.4.1'].GVL_isosurf_set_att_const
    GVL_isosurf_set_att_const.restype = c_int
    GVL_isosurf_set_att_const.argtypes = [c_int, c_int, c_int, c_float]

# C:/msys64/usr/src/grass741/dist.x86_64-w64-mingw32/include/grass/defs/ogsf.h: 267
if hasattr(_libs['grass_ogsf.7.4.1'], 'GVL_isosurf_set_att_map'):
    GVL_isosurf_set_att_map = _libs['grass_ogsf.7.4.1'].GVL_isosurf_set_att_map
    GVL_isosurf_set_att_map.restype = c_int
    GVL_isosurf_set_att_map.argtypes = [c_int, c_int, c_int, String]

# C:/msys64/usr/src/grass741/dist.x86_64-w64-mingw32/include/grass/defs/ogsf.h: 268
if hasattr(_libs['grass_ogsf.7.4.1'], 'GVL_isosurf_get_flags'):
    GVL_isosurf_get_flags = _libs['grass_ogsf.7.4.1'].GVL_isosurf_get_flags
    GVL_isosurf_get_flags.restype = c_int
    GVL_isosurf_get_flags.argtypes = [c_int, c_int, POINTER(c_int)]

# C:/msys64/usr/src/grass741/dist.x86_64-w64-mingw32/include/grass/defs/ogsf.h: 269
if hasattr(_libs['grass_ogsf.7.4.1'], 'GVL_isosurf_set_flags'):
    GVL_isosurf_set_flags = _libs['grass_ogsf.7.4.1'].GVL_isosurf_set_flags
    GVL_isosurf_set_flags.restype = c_int
    GVL_isosurf_set_flags.argtypes = [c_int, c_int, c_int]

# C:/msys64/usr/src/grass741/dist.x86_64-w64-mingw32/include/grass/defs/ogsf.h: 270
if hasattr(_libs['grass_ogsf.7.4.1'], 'GVL_isosurf_num_isosurfs'):
    GVL_isosurf_num_isosurfs = _libs['grass_ogsf.7.4.1'].GVL_isosurf_num_isosurfs
    GVL_isosurf_num_isosurfs.restype = c_int
    GVL_isosurf_num_isosurfs.argtypes = [c_int]

# C:/msys64/usr/src/grass741/dist.x86_64-w64-mingw32/include/grass/defs/ogsf.h: 271
if hasattr(_libs['grass_ogsf.7.4.1'], 'GVL_isosurf_set_maskmode'):
    GVL_isosurf_set_maskmode = _libs['grass_ogsf.7.4.1'].GVL_isosurf_set_maskmode
    GVL_isosurf_set_maskmode.restype = c_int
    GVL_isosurf_set_maskmode.argtypes = [c_int, c_int, c_int]

# C:/msys64/usr/src/grass741/dist.x86_64-w64-mingw32/include/grass/defs/ogsf.h: 272
if hasattr(_libs['grass_ogsf.7.4.1'], 'GVL_isosurf_get_maskmode'):
    GVL_isosurf_get_maskmode = _libs['grass_ogsf.7.4.1'].GVL_isosurf_get_maskmode
    GVL_isosurf_get_maskmode.restype = c_int
    GVL_isosurf_get_maskmode.argtypes = [c_int, c_int, POINTER(c_int)]

# C:/msys64/usr/src/grass741/dist.x86_64-w64-mingw32/include/grass/defs/ogsf.h: 274
if hasattr(_libs['grass_ogsf.7.4.1'], 'GVL_slice_move_up'):
    GVL_slice_move_up = _libs['grass_ogsf.7.4.1'].GVL_slice_move_up
    GVL_slice_move_up.restype = c_int
    GVL_slice_move_up.argtypes = [c_int, c_int]

# C:/msys64/usr/src/grass741/dist.x86_64-w64-mingw32/include/grass/defs/ogsf.h: 275
if hasattr(_libs['grass_ogsf.7.4.1'], 'GVL_slice_move_down'):
    GVL_slice_move_down = _libs['grass_ogsf.7.4.1'].GVL_slice_move_down
    GVL_slice_move_down.restype = c_int
    GVL_slice_move_down.argtypes = [c_int, c_int]

# C:/msys64/usr/src/grass741/dist.x86_64-w64-mingw32/include/grass/defs/ogsf.h: 276
if hasattr(_libs['grass_ogsf.7.4.1'], 'GVL_slice_get_drawres'):
    GVL_slice_get_drawres = _libs['grass_ogsf.7.4.1'].GVL_slice_get_drawres
    GVL_slice_get_drawres.restype = None
    GVL_slice_get_drawres.argtypes = [c_int, POINTER(c_int), POINTER(c_int), POINTER(c_int)]

# C:/msys64/usr/src/grass741/dist.x86_64-w64-mingw32/include/grass/defs/ogsf.h: 277
if hasattr(_libs['grass_ogsf.7.4.1'], 'GVL_slice_get_transp'):
    GVL_slice_get_transp = _libs['grass_ogsf.7.4.1'].GVL_slice_get_transp
    GVL_slice_get_transp.restype = c_int
    GVL_slice_get_transp.argtypes = [c_int, c_int, POINTER(c_int)]

# C:/msys64/usr/src/grass741/dist.x86_64-w64-mingw32/include/grass/defs/ogsf.h: 278
if hasattr(_libs['grass_ogsf.7.4.1'], 'GVL_slice_set_transp'):
    GVL_slice_set_transp = _libs['grass_ogsf.7.4.1'].GVL_slice_set_transp
    GVL_slice_set_transp.restype = c_int
    GVL_slice_set_transp.argtypes = [c_int, c_int, c_int]

# C:/msys64/usr/src/grass741/dist.x86_64-w64-mingw32/include/grass/defs/ogsf.h: 279
if hasattr(_libs['grass_ogsf.7.4.1'], 'GVL_slice_set_drawres'):
    GVL_slice_set_drawres = _libs['grass_ogsf.7.4.1'].GVL_slice_set_drawres
    GVL_slice_set_drawres.restype = c_int
    GVL_slice_set_drawres.argtypes = [c_int, c_int, c_int, c_int]

# C:/msys64/usr/src/grass741/dist.x86_64-w64-mingw32/include/grass/defs/ogsf.h: 280
if hasattr(_libs['grass_ogsf.7.4.1'], 'GVL_slice_get_drawmode'):
    GVL_slice_get_drawmode = _libs['grass_ogsf.7.4.1'].GVL_slice_get_drawmode
    GVL_slice_get_drawmode.restype = c_int
    GVL_slice_get_drawmode.argtypes = [c_int, POINTER(c_int)]

# C:/msys64/usr/src/grass741/dist.x86_64-w64-mingw32/include/grass/defs/ogsf.h: 281
if hasattr(_libs['grass_ogsf.7.4.1'], 'GVL_slice_set_drawmode'):
    GVL_slice_set_drawmode = _libs['grass_ogsf.7.4.1'].GVL_slice_set_drawmode
    GVL_slice_set_drawmode.restype = c_int
    GVL_slice_set_drawmode.argtypes = [c_int, c_int]

# C:/msys64/usr/src/grass741/dist.x86_64-w64-mingw32/include/grass/defs/ogsf.h: 282
if hasattr(_libs['grass_ogsf.7.4.1'], 'GVL_slice_add'):
    GVL_slice_add = _libs['grass_ogsf.7.4.1'].GVL_slice_add
    GVL_slice_add.restype = c_int
    GVL_slice_add.argtypes = [c_int]

# C:/msys64/usr/src/grass741/dist.x86_64-w64-mingw32/include/grass/defs/ogsf.h: 283
if hasattr(_libs['grass_ogsf.7.4.1'], 'GVL_slice_del'):
    GVL_slice_del = _libs['grass_ogsf.7.4.1'].GVL_slice_del
    GVL_slice_del.restype = c_int
    GVL_slice_del.argtypes = [c_int, c_int]

# C:/msys64/usr/src/grass741/dist.x86_64-w64-mingw32/include/grass/defs/ogsf.h: 284
if hasattr(_libs['grass_ogsf.7.4.1'], 'GVL_slice_num_slices'):
    GVL_slice_num_slices = _libs['grass_ogsf.7.4.1'].GVL_slice_num_slices
    GVL_slice_num_slices.restype = c_int
    GVL_slice_num_slices.argtypes = [c_int]

# C:/msys64/usr/src/grass741/dist.x86_64-w64-mingw32/include/grass/defs/ogsf.h: 285
if hasattr(_libs['grass_ogsf.7.4.1'], 'GVL_slice_get_pos'):
    GVL_slice_get_pos = _libs['grass_ogsf.7.4.1'].GVL_slice_get_pos
    GVL_slice_get_pos.restype = c_int
    GVL_slice_get_pos.argtypes = [c_int, c_int, POINTER(c_float), POINTER(c_float), POINTER(c_float), POINTER(c_float), POINTER(c_float), POINTER(c_float), POINTER(c_int)]

# C:/msys64/usr/src/grass741/dist.x86_64-w64-mingw32/include/grass/defs/ogsf.h: 287
if hasattr(_libs['grass_ogsf.7.4.1'], 'GVL_slice_set_pos'):
    GVL_slice_set_pos = _libs['grass_ogsf.7.4.1'].GVL_slice_set_pos
    GVL_slice_set_pos.restype = c_int
    GVL_slice_set_pos.argtypes = [c_int, c_int, c_float, c_float, c_float, c_float, c_float, c_float, c_int]

# C:/msys64/usr/src/grass741/dist.x86_64-w64-mingw32/include/grass/defs/ogsf.h: 291
for _lib in _libs.values():
    if hasattr(_lib, 'Gp_set_color'):
        Gp_set_color = _lib.Gp_set_color
        Gp_set_color.restype = c_int
        Gp_set_color.argtypes = [String, POINTER(geopoint)]
        break

# C:/msys64/usr/src/grass741/dist.x86_64-w64-mingw32/include/grass/defs/ogsf.h: 292
if hasattr(_libs['grass_ogsf.7.4.1'], 'Gp_load_sites'):
    Gp_load_sites = _libs['grass_ogsf.7.4.1'].Gp_load_sites
    Gp_load_sites.restype = POINTER(geopoint)
    Gp_load_sites.argtypes = [String, POINTER(c_int), POINTER(c_int)]

# C:/msys64/usr/src/grass741/dist.x86_64-w64-mingw32/include/grass/defs/ogsf.h: 293
if hasattr(_libs['grass_ogsf.7.4.1'], 'Gp_load_sites_thematic'):
    Gp_load_sites_thematic = _libs['grass_ogsf.7.4.1'].Gp_load_sites_thematic
    Gp_load_sites_thematic.restype = c_int
    Gp_load_sites_thematic.argtypes = [POINTER(geosite), POINTER(struct_Colors)]

# C:/msys64/usr/src/grass741/dist.x86_64-w64-mingw32/include/grass/defs/ogsf.h: 296
if hasattr(_libs['grass_ogsf.7.4.1'], 'Gs_distance'):
    Gs_distance = _libs['grass_ogsf.7.4.1'].Gs_distance
    Gs_distance.restype = c_double
    Gs_distance.argtypes = [POINTER(c_double), POINTER(c_double)]

# C:/msys64/usr/src/grass741/dist.x86_64-w64-mingw32/include/grass/defs/ogsf.h: 297
if hasattr(_libs['grass_ogsf.7.4.1'], 'Gs_loadmap_as_float'):
    Gs_loadmap_as_float = _libs['grass_ogsf.7.4.1'].Gs_loadmap_as_float
    Gs_loadmap_as_float.restype = c_int
    Gs_loadmap_as_float.argtypes = [POINTER(struct_Cell_head), String, POINTER(c_float), POINTER(struct_BM), POINTER(c_int)]

# C:/msys64/usr/src/grass741/dist.x86_64-w64-mingw32/include/grass/defs/ogsf.h: 299
if hasattr(_libs['grass_ogsf.7.4.1'], 'Gs_loadmap_as_int'):
    Gs_loadmap_as_int = _libs['grass_ogsf.7.4.1'].Gs_loadmap_as_int
    Gs_loadmap_as_int.restype = c_int
    Gs_loadmap_as_int.argtypes = [POINTER(struct_Cell_head), String, POINTER(c_int), POINTER(struct_BM), POINTER(c_int)]

# C:/msys64/usr/src/grass741/dist.x86_64-w64-mingw32/include/grass/defs/ogsf.h: 301
if hasattr(_libs['grass_ogsf.7.4.1'], 'Gs_numtype'):
    Gs_numtype = _libs['grass_ogsf.7.4.1'].Gs_numtype
    Gs_numtype.restype = c_int
    Gs_numtype.argtypes = [String, POINTER(c_int)]

# C:/msys64/usr/src/grass741/dist.x86_64-w64-mingw32/include/grass/defs/ogsf.h: 302
if hasattr(_libs['grass_ogsf.7.4.1'], 'Gs_loadmap_as_short'):
    Gs_loadmap_as_short = _libs['grass_ogsf.7.4.1'].Gs_loadmap_as_short
    Gs_loadmap_as_short.restype = c_int
    Gs_loadmap_as_short.argtypes = [POINTER(struct_Cell_head), String, POINTER(c_short), POINTER(struct_BM), POINTER(c_int)]

# C:/msys64/usr/src/grass741/dist.x86_64-w64-mingw32/include/grass/defs/ogsf.h: 304
if hasattr(_libs['grass_ogsf.7.4.1'], 'Gs_loadmap_as_char'):
    Gs_loadmap_as_char = _libs['grass_ogsf.7.4.1'].Gs_loadmap_as_char
    Gs_loadmap_as_char.restype = c_int
    Gs_loadmap_as_char.argtypes = [POINTER(struct_Cell_head), String, POINTER(c_ubyte), POINTER(struct_BM), POINTER(c_int)]

# C:/msys64/usr/src/grass741/dist.x86_64-w64-mingw32/include/grass/defs/ogsf.h: 306
if hasattr(_libs['grass_ogsf.7.4.1'], 'Gs_loadmap_as_bitmap'):
    Gs_loadmap_as_bitmap = _libs['grass_ogsf.7.4.1'].Gs_loadmap_as_bitmap
    Gs_loadmap_as_bitmap.restype = c_int
    Gs_loadmap_as_bitmap.argtypes = [POINTER(struct_Cell_head), String, POINTER(struct_BM)]

# C:/msys64/usr/src/grass741/dist.x86_64-w64-mingw32/include/grass/defs/ogsf.h: 307
if hasattr(_libs['grass_ogsf.7.4.1'], 'Gs_build_256lookup'):
    Gs_build_256lookup = _libs['grass_ogsf.7.4.1'].Gs_build_256lookup
    Gs_build_256lookup.restype = c_int
    Gs_build_256lookup.argtypes = [String, POINTER(c_int)]

# C:/msys64/usr/src/grass741/dist.x86_64-w64-mingw32/include/grass/defs/ogsf.h: 308
if hasattr(_libs['grass_ogsf.7.4.1'], 'Gs_pack_colors'):
    Gs_pack_colors = _libs['grass_ogsf.7.4.1'].Gs_pack_colors
    Gs_pack_colors.restype = None
    Gs_pack_colors.argtypes = [String, POINTER(c_int), c_int, c_int]

# C:/msys64/usr/src/grass741/dist.x86_64-w64-mingw32/include/grass/defs/ogsf.h: 309
if hasattr(_libs['grass_ogsf.7.4.1'], 'Gs_pack_colors_float'):
    Gs_pack_colors_float = _libs['grass_ogsf.7.4.1'].Gs_pack_colors_float
    Gs_pack_colors_float.restype = None
    Gs_pack_colors_float.argtypes = [String, POINTER(c_float), POINTER(c_int), c_int, c_int]

# C:/msys64/usr/src/grass741/dist.x86_64-w64-mingw32/include/grass/defs/ogsf.h: 310
if hasattr(_libs['grass_ogsf.7.4.1'], 'Gs_get_cat_label'):
    Gs_get_cat_label = _libs['grass_ogsf.7.4.1'].Gs_get_cat_label
    Gs_get_cat_label.restype = c_int
    Gs_get_cat_label.argtypes = [String, c_int, c_int, String]

# C:/msys64/usr/src/grass741/dist.x86_64-w64-mingw32/include/grass/defs/ogsf.h: 311
if hasattr(_libs['grass_ogsf.7.4.1'], 'Gs_save_3dview'):
    Gs_save_3dview = _libs['grass_ogsf.7.4.1'].Gs_save_3dview
    Gs_save_3dview.restype = c_int
    Gs_save_3dview.argtypes = [String, POINTER(geoview), POINTER(geodisplay), POINTER(struct_Cell_head), POINTER(geosurf)]

# C:/msys64/usr/src/grass741/dist.x86_64-w64-mingw32/include/grass/defs/ogsf.h: 313
if hasattr(_libs['grass_ogsf.7.4.1'], 'Gs_load_3dview'):
    Gs_load_3dview = _libs['grass_ogsf.7.4.1'].Gs_load_3dview
    Gs_load_3dview.restype = c_int
    Gs_load_3dview.argtypes = [String, POINTER(geoview), POINTER(geodisplay), POINTER(struct_Cell_head), POINTER(geosurf)]

# C:/msys64/usr/src/grass741/dist.x86_64-w64-mingw32/include/grass/defs/ogsf.h: 315
if hasattr(_libs['grass_ogsf.7.4.1'], 'Gs_update_attrange'):
    Gs_update_attrange = _libs['grass_ogsf.7.4.1'].Gs_update_attrange
    Gs_update_attrange.restype = c_int
    Gs_update_attrange.argtypes = [POINTER(geosurf), c_int]

# C:/msys64/usr/src/grass741/dist.x86_64-w64-mingw32/include/grass/defs/ogsf.h: 318
if hasattr(_libs['grass_ogsf.7.4.1'], 'Gv_load_vect'):
    Gv_load_vect = _libs['grass_ogsf.7.4.1'].Gv_load_vect
    Gv_load_vect.restype = POINTER(geoline)
    Gv_load_vect.argtypes = [String, POINTER(c_int)]

# C:/msys64/usr/src/grass741/dist.x86_64-w64-mingw32/include/grass/defs/ogsf.h: 319
if hasattr(_libs['grass_ogsf.7.4.1'], 'Gv_load_vect_thematic'):
    Gv_load_vect_thematic = _libs['grass_ogsf.7.4.1'].Gv_load_vect_thematic
    Gv_load_vect_thematic.restype = c_int
    Gv_load_vect_thematic.argtypes = [POINTER(geovect), POINTER(struct_Colors)]

# C:/msys64/usr/src/grass741/dist.x86_64-w64-mingw32/include/grass/defs/ogsf.h: 320
if hasattr(_libs['grass_ogsf.7.4.1'], 'sub_Vectmem'):
    sub_Vectmem = _libs['grass_ogsf.7.4.1'].sub_Vectmem
    sub_Vectmem.restype = None
    sub_Vectmem.argtypes = [c_int]

# C:/msys64/usr/src/grass741/dist.x86_64-w64-mingw32/include/grass/defs/ogsf.h: 323
if hasattr(_libs['grass_ogsf.7.4.1'], 'gk_copy_key'):
    gk_copy_key = _libs['grass_ogsf.7.4.1'].gk_copy_key
    gk_copy_key.restype = POINTER(Keylist)
    gk_copy_key.argtypes = [POINTER(Keylist)]

# C:/msys64/usr/src/grass741/dist.x86_64-w64-mingw32/include/grass/defs/ogsf.h: 324
if hasattr(_libs['grass_ogsf.7.4.1'], 'gk_get_mask_sofar'):
    gk_get_mask_sofar = _libs['grass_ogsf.7.4.1'].gk_get_mask_sofar
    gk_get_mask_sofar.restype = c_ulong
    gk_get_mask_sofar.argtypes = [c_float, POINTER(Keylist)]

# C:/msys64/usr/src/grass741/dist.x86_64-w64-mingw32/include/grass/defs/ogsf.h: 325
if hasattr(_libs['grass_ogsf.7.4.1'], 'gk_viable_keys_for_mask'):
    gk_viable_keys_for_mask = _libs['grass_ogsf.7.4.1'].gk_viable_keys_for_mask
    gk_viable_keys_for_mask.restype = c_int
    gk_viable_keys_for_mask.argtypes = [c_ulong, POINTER(Keylist), POINTER(POINTER(Keylist))]

# C:/msys64/usr/src/grass741/dist.x86_64-w64-mingw32/include/grass/defs/ogsf.h: 326
if hasattr(_libs['grass_ogsf.7.4.1'], 'gk_follow_frames'):
    gk_follow_frames = _libs['grass_ogsf.7.4.1'].gk_follow_frames
    gk_follow_frames.restype = None
    gk_follow_frames.argtypes = [POINTER(Viewnode), c_int, POINTER(Keylist), c_int, c_int, c_int, c_ulong]

# C:/msys64/usr/src/grass741/dist.x86_64-w64-mingw32/include/grass/defs/ogsf.h: 328
if hasattr(_libs['grass_ogsf.7.4.1'], 'gk_free_key'):
    gk_free_key = _libs['grass_ogsf.7.4.1'].gk_free_key
    gk_free_key.restype = None
    gk_free_key.argtypes = [POINTER(Keylist)]

# C:/msys64/usr/src/grass741/dist.x86_64-w64-mingw32/include/grass/defs/ogsf.h: 329
if hasattr(_libs['grass_ogsf.7.4.1'], 'gk_make_framesfromkeys'):
    gk_make_framesfromkeys = _libs['grass_ogsf.7.4.1'].gk_make_framesfromkeys
    gk_make_framesfromkeys.restype = POINTER(Viewnode)
    gk_make_framesfromkeys.argtypes = [POINTER(Keylist), c_int, c_int, c_int, c_float]

# C:/msys64/usr/src/grass741/dist.x86_64-w64-mingw32/include/grass/defs/ogsf.h: 330
if hasattr(_libs['grass_ogsf.7.4.1'], 'get_key_neighbors'):
    get_key_neighbors = _libs['grass_ogsf.7.4.1'].get_key_neighbors
    get_key_neighbors.restype = c_double
    get_key_neighbors.argtypes = [c_int, c_double, c_double, c_int, POINTER(POINTER(Keylist)), POINTER(POINTER(Keylist)), POINTER(POINTER(Keylist)), POINTER(POINTER(Keylist)), POINTER(POINTER(Keylist)), POINTER(c_double), POINTER(c_double)]

# C:/msys64/usr/src/grass741/dist.x86_64-w64-mingw32/include/grass/defs/ogsf.h: 333
if hasattr(_libs['grass_ogsf.7.4.1'], 'lin_interp'):
    lin_interp = _libs['grass_ogsf.7.4.1'].lin_interp
    lin_interp.restype = c_double
    lin_interp.argtypes = [c_float, c_float, c_float]

# C:/msys64/usr/src/grass741/dist.x86_64-w64-mingw32/include/grass/defs/ogsf.h: 334
if hasattr(_libs['grass_ogsf.7.4.1'], 'get_2key_neighbors'):
    get_2key_neighbors = _libs['grass_ogsf.7.4.1'].get_2key_neighbors
    get_2key_neighbors.restype = c_double
    get_2key_neighbors.argtypes = [c_int, c_float, c_float, c_int, POINTER(POINTER(Keylist)), POINTER(POINTER(Keylist)), POINTER(POINTER(Keylist))]

# C:/msys64/usr/src/grass741/dist.x86_64-w64-mingw32/include/grass/defs/ogsf.h: 336
if hasattr(_libs['grass_ogsf.7.4.1'], 'gk_make_linear_framesfromkeys'):
    gk_make_linear_framesfromkeys = _libs['grass_ogsf.7.4.1'].gk_make_linear_framesfromkeys
    gk_make_linear_framesfromkeys.restype = POINTER(Viewnode)
    gk_make_linear_framesfromkeys.argtypes = [POINTER(Keylist), c_int, c_int, c_int]

# C:/msys64/usr/src/grass741/dist.x86_64-w64-mingw32/include/grass/defs/ogsf.h: 337
if hasattr(_libs['grass_ogsf.7.4.1'], 'correct_twist'):
    correct_twist = _libs['grass_ogsf.7.4.1'].correct_twist
    correct_twist.restype = None
    correct_twist.argtypes = [POINTER(Keylist)]

# C:/msys64/usr/src/grass741/dist.x86_64-w64-mingw32/include/grass/defs/ogsf.h: 338
if hasattr(_libs['grass_ogsf.7.4.1'], 'gk_draw_path'):
    gk_draw_path = _libs['grass_ogsf.7.4.1'].gk_draw_path
    gk_draw_path.restype = c_int
    gk_draw_path.argtypes = [POINTER(Viewnode), c_int, POINTER(Keylist)]

# C:/msys64/usr/src/grass741/dist.x86_64-w64-mingw32/include/grass/defs/ogsf.h: 341
if hasattr(_libs['grass_ogsf.7.4.1'], 'gp_get_site'):
    gp_get_site = _libs['grass_ogsf.7.4.1'].gp_get_site
    gp_get_site.restype = POINTER(geosite)
    gp_get_site.argtypes = [c_int]

# C:/msys64/usr/src/grass741/dist.x86_64-w64-mingw32/include/grass/defs/ogsf.h: 342
if hasattr(_libs['grass_ogsf.7.4.1'], 'gp_get_prev_site'):
    gp_get_prev_site = _libs['grass_ogsf.7.4.1'].gp_get_prev_site
    gp_get_prev_site.restype = POINTER(geosite)
    gp_get_prev_site.argtypes = [c_int]

# C:/msys64/usr/src/grass741/dist.x86_64-w64-mingw32/include/grass/defs/ogsf.h: 343
if hasattr(_libs['grass_ogsf.7.4.1'], 'gp_num_sites'):
    gp_num_sites = _libs['grass_ogsf.7.4.1'].gp_num_sites
    gp_num_sites.restype = c_int
    gp_num_sites.argtypes = []

# C:/msys64/usr/src/grass741/dist.x86_64-w64-mingw32/include/grass/defs/ogsf.h: 344
if hasattr(_libs['grass_ogsf.7.4.1'], 'gp_get_last_site'):
    gp_get_last_site = _libs['grass_ogsf.7.4.1'].gp_get_last_site
    gp_get_last_site.restype = POINTER(geosite)
    gp_get_last_site.argtypes = []

# C:/msys64/usr/src/grass741/dist.x86_64-w64-mingw32/include/grass/defs/ogsf.h: 345
if hasattr(_libs['grass_ogsf.7.4.1'], 'gp_get_new_site'):
    gp_get_new_site = _libs['grass_ogsf.7.4.1'].gp_get_new_site
    gp_get_new_site.restype = POINTER(geosite)
    gp_get_new_site.argtypes = []

# C:/msys64/usr/src/grass741/dist.x86_64-w64-mingw32/include/grass/defs/ogsf.h: 346
if hasattr(_libs['grass_ogsf.7.4.1'], 'gp_update_drapesurfs'):
    gp_update_drapesurfs = _libs['grass_ogsf.7.4.1'].gp_update_drapesurfs
    gp_update_drapesurfs.restype = None
    gp_update_drapesurfs.argtypes = []

# C:/msys64/usr/src/grass741/dist.x86_64-w64-mingw32/include/grass/defs/ogsf.h: 347
if hasattr(_libs['grass_ogsf.7.4.1'], 'gp_set_defaults'):
    gp_set_defaults = _libs['grass_ogsf.7.4.1'].gp_set_defaults
    gp_set_defaults.restype = c_int
    gp_set_defaults.argtypes = [POINTER(geosite)]

# C:/msys64/usr/src/grass741/dist.x86_64-w64-mingw32/include/grass/defs/ogsf.h: 348
for _lib in _libs.values():
    if hasattr(_lib, 'print_site_fields'):
        print_site_fields = _lib.print_site_fields
        print_site_fields.restype = None
        print_site_fields.argtypes = [POINTER(geosite)]
        break

# C:/msys64/usr/src/grass741/dist.x86_64-w64-mingw32/include/grass/defs/ogsf.h: 349
if hasattr(_libs['grass_ogsf.7.4.1'], 'gp_init_site'):
    gp_init_site = _libs['grass_ogsf.7.4.1'].gp_init_site
    gp_init_site.restype = c_int
    gp_init_site.argtypes = [POINTER(geosite)]

# C:/msys64/usr/src/grass741/dist.x86_64-w64-mingw32/include/grass/defs/ogsf.h: 350
if hasattr(_libs['grass_ogsf.7.4.1'], 'gp_delete_site'):
    gp_delete_site = _libs['grass_ogsf.7.4.1'].gp_delete_site
    gp_delete_site.restype = None
    gp_delete_site.argtypes = [c_int]

# C:/msys64/usr/src/grass741/dist.x86_64-w64-mingw32/include/grass/defs/ogsf.h: 351
if hasattr(_libs['grass_ogsf.7.4.1'], 'gp_free_site'):
    gp_free_site = _libs['grass_ogsf.7.4.1'].gp_free_site
    gp_free_site.restype = c_int
    gp_free_site.argtypes = [POINTER(geosite)]

# C:/msys64/usr/src/grass741/dist.x86_64-w64-mingw32/include/grass/defs/ogsf.h: 352
if hasattr(_libs['grass_ogsf.7.4.1'], 'gp_free_sitemem'):
    gp_free_sitemem = _libs['grass_ogsf.7.4.1'].gp_free_sitemem
    gp_free_sitemem.restype = None
    gp_free_sitemem.argtypes = [POINTER(geosite)]

# C:/msys64/usr/src/grass741/dist.x86_64-w64-mingw32/include/grass/defs/ogsf.h: 353
if hasattr(_libs['grass_ogsf.7.4.1'], 'gp_set_drapesurfs'):
    gp_set_drapesurfs = _libs['grass_ogsf.7.4.1'].gp_set_drapesurfs
    gp_set_drapesurfs.restype = None
    gp_set_drapesurfs.argtypes = [POINTER(geosite), POINTER(c_int), c_int]

# C:/msys64/usr/src/grass741/dist.x86_64-w64-mingw32/include/grass/defs/ogsf.h: 356
if hasattr(_libs['grass_ogsf.7.4.1'], 'gs_point_in_region'):
    gs_point_in_region = _libs['grass_ogsf.7.4.1'].gs_point_in_region
    gs_point_in_region.restype = c_int
    gs_point_in_region.argtypes = [POINTER(geosurf), POINTER(c_float), POINTER(c_float)]

# C:/msys64/usr/src/grass741/dist.x86_64-w64-mingw32/include/grass/defs/ogsf.h: 357
if hasattr(_libs['grass_ogsf.7.4.1'], 'gpd_obj'):
    gpd_obj = _libs['grass_ogsf.7.4.1'].gpd_obj
    gpd_obj.restype = None
    gpd_obj.argtypes = [POINTER(geosurf), POINTER(gvstyle), Point3]

# C:/msys64/usr/src/grass741/dist.x86_64-w64-mingw32/include/grass/defs/ogsf.h: 358
if hasattr(_libs['grass_ogsf.7.4.1'], 'gpd_2dsite'):
    gpd_2dsite = _libs['grass_ogsf.7.4.1'].gpd_2dsite
    gpd_2dsite.restype = c_int
    gpd_2dsite.argtypes = [POINTER(geosite), POINTER(geosurf), c_int]

# C:/msys64/usr/src/grass741/dist.x86_64-w64-mingw32/include/grass/defs/ogsf.h: 359
if hasattr(_libs['grass_ogsf.7.4.1'], 'gpd_3dsite'):
    gpd_3dsite = _libs['grass_ogsf.7.4.1'].gpd_3dsite
    gpd_3dsite.restype = c_int
    gpd_3dsite.argtypes = [POINTER(geosite), c_float, c_float, c_int]

# C:/msys64/usr/src/grass741/dist.x86_64-w64-mingw32/include/grass/defs/ogsf.h: 362
if hasattr(_libs['grass_ogsf.7.4.1'], 'gs_err'):
    gs_err = _libs['grass_ogsf.7.4.1'].gs_err
    gs_err.restype = None
    gs_err.argtypes = [String]

# C:/msys64/usr/src/grass741/dist.x86_64-w64-mingw32/include/grass/defs/ogsf.h: 363
if hasattr(_libs['grass_ogsf.7.4.1'], 'gs_init'):
    gs_init = _libs['grass_ogsf.7.4.1'].gs_init
    gs_init.restype = None
    gs_init.argtypes = []

# C:/msys64/usr/src/grass741/dist.x86_64-w64-mingw32/include/grass/defs/ogsf.h: 364
if hasattr(_libs['grass_ogsf.7.4.1'], 'gs_get_surf'):
    gs_get_surf = _libs['grass_ogsf.7.4.1'].gs_get_surf
    gs_get_surf.restype = POINTER(geosurf)
    gs_get_surf.argtypes = [c_int]

# C:/msys64/usr/src/grass741/dist.x86_64-w64-mingw32/include/grass/defs/ogsf.h: 365
if hasattr(_libs['grass_ogsf.7.4.1'], 'gs_get_prev_surface'):
    gs_get_prev_surface = _libs['grass_ogsf.7.4.1'].gs_get_prev_surface
    gs_get_prev_surface.restype = POINTER(geosurf)
    gs_get_prev_surface.argtypes = [c_int]

# C:/msys64/usr/src/grass741/dist.x86_64-w64-mingw32/include/grass/defs/ogsf.h: 366
if hasattr(_libs['grass_ogsf.7.4.1'], 'gs_getall_surfaces'):
    gs_getall_surfaces = _libs['grass_ogsf.7.4.1'].gs_getall_surfaces
    gs_getall_surfaces.restype = c_int
    gs_getall_surfaces.argtypes = [POINTER(POINTER(geosurf))]

# C:/msys64/usr/src/grass741/dist.x86_64-w64-mingw32/include/grass/defs/ogsf.h: 367
if hasattr(_libs['grass_ogsf.7.4.1'], 'gs_num_surfaces'):
    gs_num_surfaces = _libs['grass_ogsf.7.4.1'].gs_num_surfaces
    gs_num_surfaces.restype = c_int
    gs_num_surfaces.argtypes = []

# C:/msys64/usr/src/grass741/dist.x86_64-w64-mingw32/include/grass/defs/ogsf.h: 368
if hasattr(_libs['grass_ogsf.7.4.1'], 'gs_att_is_set'):
    gs_att_is_set = _libs['grass_ogsf.7.4.1'].gs_att_is_set
    gs_att_is_set.restype = c_int
    gs_att_is_set.argtypes = [POINTER(geosurf), c_uint]

# C:/msys64/usr/src/grass741/dist.x86_64-w64-mingw32/include/grass/defs/ogsf.h: 369
if hasattr(_libs['grass_ogsf.7.4.1'], 'gs_get_last_surface'):
    gs_get_last_surface = _libs['grass_ogsf.7.4.1'].gs_get_last_surface
    gs_get_last_surface.restype = POINTER(geosurf)
    gs_get_last_surface.argtypes = []

# C:/msys64/usr/src/grass741/dist.x86_64-w64-mingw32/include/grass/defs/ogsf.h: 370
if hasattr(_libs['grass_ogsf.7.4.1'], 'gs_get_new_surface'):
    gs_get_new_surface = _libs['grass_ogsf.7.4.1'].gs_get_new_surface
    gs_get_new_surface.restype = POINTER(geosurf)
    gs_get_new_surface.argtypes = []

# C:/msys64/usr/src/grass741/dist.x86_64-w64-mingw32/include/grass/defs/ogsf.h: 371
if hasattr(_libs['grass_ogsf.7.4.1'], 'gs_init_surf'):
    gs_init_surf = _libs['grass_ogsf.7.4.1'].gs_init_surf
    gs_init_surf.restype = c_int
    gs_init_surf.argtypes = [POINTER(geosurf), c_double, c_double, c_int, c_int, c_double, c_double]

# C:/msys64/usr/src/grass741/dist.x86_64-w64-mingw32/include/grass/defs/ogsf.h: 372
if hasattr(_libs['grass_ogsf.7.4.1'], 'gs_init_normbuff'):
    gs_init_normbuff = _libs['grass_ogsf.7.4.1'].gs_init_normbuff
    gs_init_normbuff.restype = c_int
    gs_init_normbuff.argtypes = [POINTER(geosurf)]

# C:/msys64/usr/src/grass741/dist.x86_64-w64-mingw32/include/grass/defs/ogsf.h: 373
if hasattr(_libs['grass_ogsf.7.4.1'], 'print_frto'):
    print_frto = _libs['grass_ogsf.7.4.1'].print_frto
    print_frto.restype = None
    print_frto.argtypes = [POINTER(c_float * 4)]

# C:/msys64/usr/src/grass741/dist.x86_64-w64-mingw32/include/grass/defs/ogsf.h: 374
if hasattr(_libs['grass_ogsf.7.4.1'], 'print_realto'):
    print_realto = _libs['grass_ogsf.7.4.1'].print_realto
    print_realto.restype = None
    print_realto.argtypes = [POINTER(c_float)]

# C:/msys64/usr/src/grass741/dist.x86_64-w64-mingw32/include/grass/defs/ogsf.h: 375
if hasattr(_libs['grass_ogsf.7.4.1'], 'print_256lookup'):
    print_256lookup = _libs['grass_ogsf.7.4.1'].print_256lookup
    print_256lookup.restype = None
    print_256lookup.argtypes = [POINTER(c_int)]

# C:/msys64/usr/src/grass741/dist.x86_64-w64-mingw32/include/grass/defs/ogsf.h: 376
if hasattr(_libs['grass_ogsf.7.4.1'], 'print_surf_fields'):
    print_surf_fields = _libs['grass_ogsf.7.4.1'].print_surf_fields
    print_surf_fields.restype = None
    print_surf_fields.argtypes = [POINTER(geosurf)]

# C:/msys64/usr/src/grass741/dist.x86_64-w64-mingw32/include/grass/defs/ogsf.h: 377
if hasattr(_libs['grass_ogsf.7.4.1'], 'print_view_fields'):
    print_view_fields = _libs['grass_ogsf.7.4.1'].print_view_fields
    print_view_fields.restype = None
    print_view_fields.argtypes = [POINTER(geoview)]

# C:/msys64/usr/src/grass741/dist.x86_64-w64-mingw32/include/grass/defs/ogsf.h: 378
if hasattr(_libs['grass_ogsf.7.4.1'], 'gs_set_defaults'):
    gs_set_defaults = _libs['grass_ogsf.7.4.1'].gs_set_defaults
    gs_set_defaults.restype = None
    gs_set_defaults.argtypes = [POINTER(geosurf), POINTER(c_float), POINTER(c_float)]

# C:/msys64/usr/src/grass741/dist.x86_64-w64-mingw32/include/grass/defs/ogsf.h: 379
if hasattr(_libs['grass_ogsf.7.4.1'], 'gs_delete_surf'):
    gs_delete_surf = _libs['grass_ogsf.7.4.1'].gs_delete_surf
    gs_delete_surf.restype = None
    gs_delete_surf.argtypes = [c_int]

# C:/msys64/usr/src/grass741/dist.x86_64-w64-mingw32/include/grass/defs/ogsf.h: 380
if hasattr(_libs['grass_ogsf.7.4.1'], 'gs_free_surf'):
    gs_free_surf = _libs['grass_ogsf.7.4.1'].gs_free_surf
    gs_free_surf.restype = c_int
    gs_free_surf.argtypes = [POINTER(geosurf)]

# C:/msys64/usr/src/grass741/dist.x86_64-w64-mingw32/include/grass/defs/ogsf.h: 381
if hasattr(_libs['grass_ogsf.7.4.1'], 'gs_free_unshared_buffs'):
    gs_free_unshared_buffs = _libs['grass_ogsf.7.4.1'].gs_free_unshared_buffs
    gs_free_unshared_buffs.restype = None
    gs_free_unshared_buffs.argtypes = [POINTER(geosurf)]

# C:/msys64/usr/src/grass741/dist.x86_64-w64-mingw32/include/grass/defs/ogsf.h: 382
if hasattr(_libs['grass_ogsf.7.4.1'], 'gs_num_datah_reused'):
    gs_num_datah_reused = _libs['grass_ogsf.7.4.1'].gs_num_datah_reused
    gs_num_datah_reused.restype = c_int
    gs_num_datah_reused.argtypes = [c_int]

# C:/msys64/usr/src/grass741/dist.x86_64-w64-mingw32/include/grass/defs/ogsf.h: 383
if hasattr(_libs['grass_ogsf.7.4.1'], 'gs_get_att_type'):
    gs_get_att_type = _libs['grass_ogsf.7.4.1'].gs_get_att_type
    gs_get_att_type.restype = c_int
    gs_get_att_type.argtypes = [POINTER(geosurf), c_int]

# C:/msys64/usr/src/grass741/dist.x86_64-w64-mingw32/include/grass/defs/ogsf.h: 384
if hasattr(_libs['grass_ogsf.7.4.1'], 'gs_get_att_src'):
    gs_get_att_src = _libs['grass_ogsf.7.4.1'].gs_get_att_src
    gs_get_att_src.restype = c_int
    gs_get_att_src.argtypes = [POINTER(geosurf), c_int]

# C:/msys64/usr/src/grass741/dist.x86_64-w64-mingw32/include/grass/defs/ogsf.h: 385
if hasattr(_libs['grass_ogsf.7.4.1'], 'gs_get_att_typbuff'):
    gs_get_att_typbuff = _libs['grass_ogsf.7.4.1'].gs_get_att_typbuff
    gs_get_att_typbuff.restype = POINTER(typbuff)
    gs_get_att_typbuff.argtypes = [POINTER(geosurf), c_int, c_int]

# C:/msys64/usr/src/grass741/dist.x86_64-w64-mingw32/include/grass/defs/ogsf.h: 386
if hasattr(_libs['grass_ogsf.7.4.1'], 'gs_malloc_att_buff'):
    gs_malloc_att_buff = _libs['grass_ogsf.7.4.1'].gs_malloc_att_buff
    gs_malloc_att_buff.restype = c_size_t
    gs_malloc_att_buff.argtypes = [POINTER(geosurf), c_int, c_int]

# C:/msys64/usr/src/grass741/dist.x86_64-w64-mingw32/include/grass/defs/ogsf.h: 387
if hasattr(_libs['grass_ogsf.7.4.1'], 'gs_malloc_lookup'):
    gs_malloc_lookup = _libs['grass_ogsf.7.4.1'].gs_malloc_lookup
    gs_malloc_lookup.restype = c_int
    gs_malloc_lookup.argtypes = [POINTER(geosurf), c_int]

# C:/msys64/usr/src/grass741/dist.x86_64-w64-mingw32/include/grass/defs/ogsf.h: 388
if hasattr(_libs['grass_ogsf.7.4.1'], 'gs_set_att_type'):
    gs_set_att_type = _libs['grass_ogsf.7.4.1'].gs_set_att_type
    gs_set_att_type.restype = c_int
    gs_set_att_type.argtypes = [POINTER(geosurf), c_int, c_int]

# C:/msys64/usr/src/grass741/dist.x86_64-w64-mingw32/include/grass/defs/ogsf.h: 389
if hasattr(_libs['grass_ogsf.7.4.1'], 'gs_set_att_src'):
    gs_set_att_src = _libs['grass_ogsf.7.4.1'].gs_set_att_src
    gs_set_att_src.restype = c_int
    gs_set_att_src.argtypes = [POINTER(geosurf), c_int, c_int]

# C:/msys64/usr/src/grass741/dist.x86_64-w64-mingw32/include/grass/defs/ogsf.h: 390
if hasattr(_libs['grass_ogsf.7.4.1'], 'gs_set_att_const'):
    gs_set_att_const = _libs['grass_ogsf.7.4.1'].gs_set_att_const
    gs_set_att_const.restype = c_int
    gs_set_att_const.argtypes = [POINTER(geosurf), c_int, c_float]

# C:/msys64/usr/src/grass741/dist.x86_64-w64-mingw32/include/grass/defs/ogsf.h: 391
if hasattr(_libs['grass_ogsf.7.4.1'], 'gs_set_maskmode'):
    gs_set_maskmode = _libs['grass_ogsf.7.4.1'].gs_set_maskmode
    gs_set_maskmode.restype = None
    gs_set_maskmode.argtypes = [c_int]

# C:/msys64/usr/src/grass741/dist.x86_64-w64-mingw32/include/grass/defs/ogsf.h: 392
if hasattr(_libs['grass_ogsf.7.4.1'], 'gs_mask_defined'):
    gs_mask_defined = _libs['grass_ogsf.7.4.1'].gs_mask_defined
    gs_mask_defined.restype = c_int
    gs_mask_defined.argtypes = [POINTER(geosurf)]

# C:/msys64/usr/src/grass741/dist.x86_64-w64-mingw32/include/grass/defs/ogsf.h: 393
if hasattr(_libs['grass_ogsf.7.4.1'], 'gs_masked'):
    gs_masked = _libs['grass_ogsf.7.4.1'].gs_masked
    gs_masked.restype = c_int
    gs_masked.argtypes = [POINTER(typbuff), c_int, c_int, c_int]

# C:/msys64/usr/src/grass741/dist.x86_64-w64-mingw32/include/grass/defs/ogsf.h: 394
if hasattr(_libs['grass_ogsf.7.4.1'], 'gs_mapcolor'):
    gs_mapcolor = _libs['grass_ogsf.7.4.1'].gs_mapcolor
    gs_mapcolor.restype = c_int
    gs_mapcolor.argtypes = [POINTER(typbuff), POINTER(gsurf_att), c_int]

# C:/msys64/usr/src/grass741/dist.x86_64-w64-mingw32/include/grass/defs/ogsf.h: 395
if hasattr(_libs['grass_ogsf.7.4.1'], 'gs_get_zextents'):
    gs_get_zextents = _libs['grass_ogsf.7.4.1'].gs_get_zextents
    gs_get_zextents.restype = c_int
    gs_get_zextents.argtypes = [POINTER(geosurf), POINTER(c_float), POINTER(c_float), POINTER(c_float)]

# C:/msys64/usr/src/grass741/dist.x86_64-w64-mingw32/include/grass/defs/ogsf.h: 396
if hasattr(_libs['grass_ogsf.7.4.1'], 'gs_get_xextents'):
    gs_get_xextents = _libs['grass_ogsf.7.4.1'].gs_get_xextents
    gs_get_xextents.restype = c_int
    gs_get_xextents.argtypes = [POINTER(geosurf), POINTER(c_float), POINTER(c_float)]

# C:/msys64/usr/src/grass741/dist.x86_64-w64-mingw32/include/grass/defs/ogsf.h: 397
if hasattr(_libs['grass_ogsf.7.4.1'], 'gs_get_yextents'):
    gs_get_yextents = _libs['grass_ogsf.7.4.1'].gs_get_yextents
    gs_get_yextents.restype = c_int
    gs_get_yextents.argtypes = [POINTER(geosurf), POINTER(c_float), POINTER(c_float)]

# C:/msys64/usr/src/grass741/dist.x86_64-w64-mingw32/include/grass/defs/ogsf.h: 398
if hasattr(_libs['grass_ogsf.7.4.1'], 'gs_get_zrange0'):
    gs_get_zrange0 = _libs['grass_ogsf.7.4.1'].gs_get_zrange0
    gs_get_zrange0.restype = c_int
    gs_get_zrange0.argtypes = [POINTER(c_float), POINTER(c_float)]

# C:/msys64/usr/src/grass741/dist.x86_64-w64-mingw32/include/grass/defs/ogsf.h: 399
if hasattr(_libs['grass_ogsf.7.4.1'], 'gs_get_zrange'):
    gs_get_zrange = _libs['grass_ogsf.7.4.1'].gs_get_zrange
    gs_get_zrange.restype = c_int
    gs_get_zrange.argtypes = [POINTER(c_float), POINTER(c_float)]

# C:/msys64/usr/src/grass741/dist.x86_64-w64-mingw32/include/grass/defs/ogsf.h: 400
if hasattr(_libs['grass_ogsf.7.4.1'], 'gs_get_xrange'):
    gs_get_xrange = _libs['grass_ogsf.7.4.1'].gs_get_xrange
    gs_get_xrange.restype = c_int
    gs_get_xrange.argtypes = [POINTER(c_float), POINTER(c_float)]

# C:/msys64/usr/src/grass741/dist.x86_64-w64-mingw32/include/grass/defs/ogsf.h: 401
if hasattr(_libs['grass_ogsf.7.4.1'], 'gs_get_yrange'):
    gs_get_yrange = _libs['grass_ogsf.7.4.1'].gs_get_yrange
    gs_get_yrange.restype = c_int
    gs_get_yrange.argtypes = [POINTER(c_float), POINTER(c_float)]

# C:/msys64/usr/src/grass741/dist.x86_64-w64-mingw32/include/grass/defs/ogsf.h: 402
if hasattr(_libs['grass_ogsf.7.4.1'], 'gs_get_data_avg_zmax'):
    gs_get_data_avg_zmax = _libs['grass_ogsf.7.4.1'].gs_get_data_avg_zmax
    gs_get_data_avg_zmax.restype = c_int
    gs_get_data_avg_zmax.argtypes = [POINTER(c_float)]

# C:/msys64/usr/src/grass741/dist.x86_64-w64-mingw32/include/grass/defs/ogsf.h: 403
if hasattr(_libs['grass_ogsf.7.4.1'], 'gs_get_datacenter'):
    gs_get_datacenter = _libs['grass_ogsf.7.4.1'].gs_get_datacenter
    gs_get_datacenter.restype = c_int
    gs_get_datacenter.argtypes = [POINTER(c_float)]

# C:/msys64/usr/src/grass741/dist.x86_64-w64-mingw32/include/grass/defs/ogsf.h: 404
if hasattr(_libs['grass_ogsf.7.4.1'], 'gs_setall_norm_needupdate'):
    gs_setall_norm_needupdate = _libs['grass_ogsf.7.4.1'].gs_setall_norm_needupdate
    gs_setall_norm_needupdate.restype = c_int
    gs_setall_norm_needupdate.argtypes = []

# C:/msys64/usr/src/grass741/dist.x86_64-w64-mingw32/include/grass/defs/ogsf.h: 405
if hasattr(_libs['grass_ogsf.7.4.1'], 'gs_point_is_masked'):
    gs_point_is_masked = _libs['grass_ogsf.7.4.1'].gs_point_is_masked
    gs_point_is_masked.restype = c_int
    gs_point_is_masked.argtypes = [POINTER(geosurf), POINTER(c_float)]

# C:/msys64/usr/src/grass741/dist.x86_64-w64-mingw32/include/grass/defs/ogsf.h: 406
if hasattr(_libs['grass_ogsf.7.4.1'], 'gs_distance_onsurf'):
    gs_distance_onsurf = _libs['grass_ogsf.7.4.1'].gs_distance_onsurf
    gs_distance_onsurf.restype = c_int
    gs_distance_onsurf.argtypes = [POINTER(geosurf), POINTER(c_float), POINTER(c_float), POINTER(c_float), c_int]

# C:/msys64/usr/src/grass741/dist.x86_64-w64-mingw32/include/grass/defs/ogsf.h: 409
if hasattr(_libs['grass_ogsf.7.4.1'], 'gsbm_make_mask'):
    gsbm_make_mask = _libs['grass_ogsf.7.4.1'].gsbm_make_mask
    gsbm_make_mask.restype = POINTER(struct_BM)
    gsbm_make_mask.argtypes = [POINTER(typbuff), c_float, c_int, c_int]

# C:/msys64/usr/src/grass741/dist.x86_64-w64-mingw32/include/grass/defs/ogsf.h: 410
if hasattr(_libs['grass_ogsf.7.4.1'], 'gsbm_zero_mask'):
    gsbm_zero_mask = _libs['grass_ogsf.7.4.1'].gsbm_zero_mask
    gsbm_zero_mask.restype = None
    gsbm_zero_mask.argtypes = [POINTER(struct_BM)]

# C:/msys64/usr/src/grass741/dist.x86_64-w64-mingw32/include/grass/defs/ogsf.h: 411
if hasattr(_libs['grass_ogsf.7.4.1'], 'gsbm_or_masks'):
    gsbm_or_masks = _libs['grass_ogsf.7.4.1'].gsbm_or_masks
    gsbm_or_masks.restype = c_int
    gsbm_or_masks.argtypes = [POINTER(struct_BM), POINTER(struct_BM)]

# C:/msys64/usr/src/grass741/dist.x86_64-w64-mingw32/include/grass/defs/ogsf.h: 412
if hasattr(_libs['grass_ogsf.7.4.1'], 'gsbm_ornot_masks'):
    gsbm_ornot_masks = _libs['grass_ogsf.7.4.1'].gsbm_ornot_masks
    gsbm_ornot_masks.restype = c_int
    gsbm_ornot_masks.argtypes = [POINTER(struct_BM), POINTER(struct_BM)]

# C:/msys64/usr/src/grass741/dist.x86_64-w64-mingw32/include/grass/defs/ogsf.h: 413
if hasattr(_libs['grass_ogsf.7.4.1'], 'gsbm_and_masks'):
    gsbm_and_masks = _libs['grass_ogsf.7.4.1'].gsbm_and_masks
    gsbm_and_masks.restype = c_int
    gsbm_and_masks.argtypes = [POINTER(struct_BM), POINTER(struct_BM)]

# C:/msys64/usr/src/grass741/dist.x86_64-w64-mingw32/include/grass/defs/ogsf.h: 414
if hasattr(_libs['grass_ogsf.7.4.1'], 'gsbm_xor_masks'):
    gsbm_xor_masks = _libs['grass_ogsf.7.4.1'].gsbm_xor_masks
    gsbm_xor_masks.restype = c_int
    gsbm_xor_masks.argtypes = [POINTER(struct_BM), POINTER(struct_BM)]

# C:/msys64/usr/src/grass741/dist.x86_64-w64-mingw32/include/grass/defs/ogsf.h: 415
if hasattr(_libs['grass_ogsf.7.4.1'], 'gs_update_curmask'):
    gs_update_curmask = _libs['grass_ogsf.7.4.1'].gs_update_curmask
    gs_update_curmask.restype = c_int
    gs_update_curmask.argtypes = [POINTER(geosurf)]

# C:/msys64/usr/src/grass741/dist.x86_64-w64-mingw32/include/grass/defs/ogsf.h: 416
if hasattr(_libs['grass_ogsf.7.4.1'], 'print_bm'):
    print_bm = _libs['grass_ogsf.7.4.1'].print_bm
    print_bm.restype = None
    print_bm.argtypes = [POINTER(struct_BM)]

# C:/msys64/usr/src/grass741/dist.x86_64-w64-mingw32/include/grass/defs/ogsf.h: 419
if hasattr(_libs['grass_ogsf.7.4.1'], 'init_vars'):
    init_vars = _libs['grass_ogsf.7.4.1'].init_vars
    init_vars.restype = None
    init_vars.argtypes = [POINTER(geosurf)]

# C:/msys64/usr/src/grass741/dist.x86_64-w64-mingw32/include/grass/defs/ogsf.h: 420
if hasattr(_libs['grass_ogsf.7.4.1'], 'gs_calc_normals'):
    gs_calc_normals = _libs['grass_ogsf.7.4.1'].gs_calc_normals
    gs_calc_normals.restype = c_int
    gs_calc_normals.argtypes = [POINTER(geosurf)]

# C:/msys64/usr/src/grass741/dist.x86_64-w64-mingw32/include/grass/defs/ogsf.h: 421
if hasattr(_libs['grass_ogsf.7.4.1'], 'calc_norm'):
    calc_norm = _libs['grass_ogsf.7.4.1'].calc_norm
    calc_norm.restype = c_int
    calc_norm.argtypes = [POINTER(geosurf), c_int, c_int, c_uint]

# C:/msys64/usr/src/grass741/dist.x86_64-w64-mingw32/include/grass/defs/ogsf.h: 424
if hasattr(_libs['grass_ogsf.7.4.1'], 'gs_los_intersect1'):
    gs_los_intersect1 = _libs['grass_ogsf.7.4.1'].gs_los_intersect1
    gs_los_intersect1.restype = c_int
    gs_los_intersect1.argtypes = [c_int, POINTER(c_float * 3), POINTER(c_float)]

# C:/msys64/usr/src/grass741/dist.x86_64-w64-mingw32/include/grass/defs/ogsf.h: 425
if hasattr(_libs['grass_ogsf.7.4.1'], 'gs_los_intersect'):
    gs_los_intersect = _libs['grass_ogsf.7.4.1'].gs_los_intersect
    gs_los_intersect.restype = c_int
    gs_los_intersect.argtypes = [c_int, POINTER(POINTER(c_float)), POINTER(c_float)]

# C:/msys64/usr/src/grass741/dist.x86_64-w64-mingw32/include/grass/defs/ogsf.h: 426
if hasattr(_libs['grass_ogsf.7.4.1'], 'RayCvxPolyhedronInt'):
    RayCvxPolyhedronInt = _libs['grass_ogsf.7.4.1'].RayCvxPolyhedronInt
    RayCvxPolyhedronInt.restype = c_int
    RayCvxPolyhedronInt.argtypes = [Point3, Point3, c_double, POINTER(Point4), c_int, POINTER(c_double), POINTER(c_int)]

# C:/msys64/usr/src/grass741/dist.x86_64-w64-mingw32/include/grass/defs/ogsf.h: 428
if hasattr(_libs['grass_ogsf.7.4.1'], 'gs_get_databounds_planes'):
    gs_get_databounds_planes = _libs['grass_ogsf.7.4.1'].gs_get_databounds_planes
    gs_get_databounds_planes.restype = None
    gs_get_databounds_planes.argtypes = [POINTER(Point4)]

# C:/msys64/usr/src/grass741/dist.x86_64-w64-mingw32/include/grass/defs/ogsf.h: 429
if hasattr(_libs['grass_ogsf.7.4.1'], 'gs_setlos_enterdata'):
    gs_setlos_enterdata = _libs['grass_ogsf.7.4.1'].gs_setlos_enterdata
    gs_setlos_enterdata.restype = c_int
    gs_setlos_enterdata.argtypes = [POINTER(Point3)]

# C:/msys64/usr/src/grass741/dist.x86_64-w64-mingw32/include/grass/defs/ogsf.h: 432
if hasattr(_libs['grass_ogsf.7.4.1'], 'gsd_def_cplane'):
    gsd_def_cplane = _libs['grass_ogsf.7.4.1'].gsd_def_cplane
    gsd_def_cplane.restype = None
    gsd_def_cplane.argtypes = [c_int, POINTER(c_float), POINTER(c_float)]

# C:/msys64/usr/src/grass741/dist.x86_64-w64-mingw32/include/grass/defs/ogsf.h: 433
if hasattr(_libs['grass_ogsf.7.4.1'], 'gsd_update_cplanes'):
    gsd_update_cplanes = _libs['grass_ogsf.7.4.1'].gsd_update_cplanes
    gsd_update_cplanes.restype = None
    gsd_update_cplanes.argtypes = []

# C:/msys64/usr/src/grass741/dist.x86_64-w64-mingw32/include/grass/defs/ogsf.h: 434
if hasattr(_libs['grass_ogsf.7.4.1'], 'gsd_cplane_on'):
    gsd_cplane_on = _libs['grass_ogsf.7.4.1'].gsd_cplane_on
    gsd_cplane_on.restype = None
    gsd_cplane_on.argtypes = [c_int]

# C:/msys64/usr/src/grass741/dist.x86_64-w64-mingw32/include/grass/defs/ogsf.h: 435
if hasattr(_libs['grass_ogsf.7.4.1'], 'gsd_cplane_off'):
    gsd_cplane_off = _libs['grass_ogsf.7.4.1'].gsd_cplane_off
    gsd_cplane_off.restype = None
    gsd_cplane_off.argtypes = [c_int]

# C:/msys64/usr/src/grass741/dist.x86_64-w64-mingw32/include/grass/defs/ogsf.h: 436
if hasattr(_libs['grass_ogsf.7.4.1'], 'gsd_get_cplanes_state'):
    gsd_get_cplanes_state = _libs['grass_ogsf.7.4.1'].gsd_get_cplanes_state
    gsd_get_cplanes_state.restype = None
    gsd_get_cplanes_state.argtypes = [POINTER(c_int)]

# C:/msys64/usr/src/grass741/dist.x86_64-w64-mingw32/include/grass/defs/ogsf.h: 437
if hasattr(_libs['grass_ogsf.7.4.1'], 'gsd_get_cplanes'):
    gsd_get_cplanes = _libs['grass_ogsf.7.4.1'].gsd_get_cplanes
    gsd_get_cplanes.restype = c_int
    gsd_get_cplanes.argtypes = [POINTER(Point4)]

# C:/msys64/usr/src/grass741/dist.x86_64-w64-mingw32/include/grass/defs/ogsf.h: 438
if hasattr(_libs['grass_ogsf.7.4.1'], 'gsd_update_cpnorm'):
    gsd_update_cpnorm = _libs['grass_ogsf.7.4.1'].gsd_update_cpnorm
    gsd_update_cpnorm.restype = None
    gsd_update_cpnorm.argtypes = [c_int]

# C:/msys64/usr/src/grass741/dist.x86_64-w64-mingw32/include/grass/defs/ogsf.h: 439
if hasattr(_libs['grass_ogsf.7.4.1'], 'gsd_cplane_setrot'):
    gsd_cplane_setrot = _libs['grass_ogsf.7.4.1'].gsd_cplane_setrot
    gsd_cplane_setrot.restype = None
    gsd_cplane_setrot.argtypes = [c_int, c_float, c_float, c_float]

# C:/msys64/usr/src/grass741/dist.x86_64-w64-mingw32/include/grass/defs/ogsf.h: 440
if hasattr(_libs['grass_ogsf.7.4.1'], 'gsd_cplane_settrans'):
    gsd_cplane_settrans = _libs['grass_ogsf.7.4.1'].gsd_cplane_settrans
    gsd_cplane_settrans.restype = None
    gsd_cplane_settrans.argtypes = [c_int, c_float, c_float, c_float]

# C:/msys64/usr/src/grass741/dist.x86_64-w64-mingw32/include/grass/defs/ogsf.h: 441
if hasattr(_libs['grass_ogsf.7.4.1'], 'gsd_draw_cplane_fence'):
    gsd_draw_cplane_fence = _libs['grass_ogsf.7.4.1'].gsd_draw_cplane_fence
    gsd_draw_cplane_fence.restype = None
    gsd_draw_cplane_fence.argtypes = [POINTER(geosurf), POINTER(geosurf), c_int]

# C:/msys64/usr/src/grass741/dist.x86_64-w64-mingw32/include/grass/defs/ogsf.h: 442
if hasattr(_libs['grass_ogsf.7.4.1'], 'gsd_draw_cplane'):
    gsd_draw_cplane = _libs['grass_ogsf.7.4.1'].gsd_draw_cplane
    gsd_draw_cplane.restype = None
    gsd_draw_cplane.argtypes = [c_int]

# C:/msys64/usr/src/grass741/dist.x86_64-w64-mingw32/include/grass/defs/ogsf.h: 445
for _lib in _libs.values():
    if hasattr(_lib, 'gsd_set_font'):
        gsd_set_font = _lib.gsd_set_font
        gsd_set_font.restype = GLuint
        gsd_set_font.argtypes = [String]
        break

# C:/msys64/usr/src/grass741/dist.x86_64-w64-mingw32/include/grass/defs/ogsf.h: 446
if hasattr(_libs['grass_ogsf.7.4.1'], 'gsd_get_txtwidth'):
    gsd_get_txtwidth = _libs['grass_ogsf.7.4.1'].gsd_get_txtwidth
    gsd_get_txtwidth.restype = c_int
    gsd_get_txtwidth.argtypes = [String, c_int]

# C:/msys64/usr/src/grass741/dist.x86_64-w64-mingw32/include/grass/defs/ogsf.h: 447
if hasattr(_libs['grass_ogsf.7.4.1'], 'gsd_get_txtheight'):
    gsd_get_txtheight = _libs['grass_ogsf.7.4.1'].gsd_get_txtheight
    gsd_get_txtheight.restype = c_int
    gsd_get_txtheight.argtypes = [c_int]

# C:/msys64/usr/src/grass741/dist.x86_64-w64-mingw32/include/grass/defs/ogsf.h: 448
if hasattr(_libs['grass_ogsf.7.4.1'], 'do_label_display'):
    do_label_display = _libs['grass_ogsf.7.4.1'].do_label_display
    do_label_display.restype = None
    do_label_display.argtypes = [GLuint, POINTER(c_float), String]

# C:/msys64/usr/src/grass741/dist.x86_64-w64-mingw32/include/grass/defs/ogsf.h: 449
if hasattr(_libs['grass_ogsf.7.4.1'], 'get_txtdescender'):
    get_txtdescender = _libs['grass_ogsf.7.4.1'].get_txtdescender
    get_txtdescender.restype = c_int
    get_txtdescender.argtypes = []

# C:/msys64/usr/src/grass741/dist.x86_64-w64-mingw32/include/grass/defs/ogsf.h: 450
if hasattr(_libs['grass_ogsf.7.4.1'], 'get_txtxoffset'):
    get_txtxoffset = _libs['grass_ogsf.7.4.1'].get_txtxoffset
    get_txtxoffset.restype = c_int
    get_txtxoffset.argtypes = []

# C:/msys64/usr/src/grass741/dist.x86_64-w64-mingw32/include/grass/defs/ogsf.h: 453
if hasattr(_libs['grass_ogsf.7.4.1'], 'GS_write_ppm'):
    GS_write_ppm = _libs['grass_ogsf.7.4.1'].GS_write_ppm
    GS_write_ppm.restype = c_int
    GS_write_ppm.argtypes = [String]

# C:/msys64/usr/src/grass741/dist.x86_64-w64-mingw32/include/grass/defs/ogsf.h: 456
if hasattr(_libs['grass_ogsf.7.4.1'], 'GS_write_tif'):
    GS_write_tif = _libs['grass_ogsf.7.4.1'].GS_write_tif
    GS_write_tif.restype = c_int
    GS_write_tif.argtypes = [String]

# C:/msys64/usr/src/grass741/dist.x86_64-w64-mingw32/include/grass/defs/ogsf.h: 459
if hasattr(_libs['grass_ogsf.7.4.1'], 'gs_put_label'):
    gs_put_label = _libs['grass_ogsf.7.4.1'].gs_put_label
    gs_put_label.restype = None
    gs_put_label.argtypes = [String, GLuint, c_int, c_ulong, POINTER(c_int)]

# C:/msys64/usr/src/grass741/dist.x86_64-w64-mingw32/include/grass/defs/ogsf.h: 460
if hasattr(_libs['grass_ogsf.7.4.1'], 'gsd_remove_curr'):
    gsd_remove_curr = _libs['grass_ogsf.7.4.1'].gsd_remove_curr
    gsd_remove_curr.restype = None
    gsd_remove_curr.argtypes = []

# C:/msys64/usr/src/grass741/dist.x86_64-w64-mingw32/include/grass/defs/ogsf.h: 461
if hasattr(_libs['grass_ogsf.7.4.1'], 'gsd_remove_all'):
    gsd_remove_all = _libs['grass_ogsf.7.4.1'].gsd_remove_all
    gsd_remove_all.restype = None
    gsd_remove_all.argtypes = []

# C:/msys64/usr/src/grass741/dist.x86_64-w64-mingw32/include/grass/defs/ogsf.h: 462
if hasattr(_libs['grass_ogsf.7.4.1'], 'gsd_call_label'):
    gsd_call_label = _libs['grass_ogsf.7.4.1'].gsd_call_label
    gsd_call_label.restype = None
    gsd_call_label.argtypes = []

# C:/msys64/usr/src/grass741/dist.x86_64-w64-mingw32/include/grass/defs/ogsf.h: 465
if hasattr(_libs['grass_ogsf.7.4.1'], 'gsd_box'):
    gsd_box = _libs['grass_ogsf.7.4.1'].gsd_box
    gsd_box.restype = None
    gsd_box.argtypes = [POINTER(c_float), c_int, POINTER(c_float)]

# C:/msys64/usr/src/grass741/dist.x86_64-w64-mingw32/include/grass/defs/ogsf.h: 466
if hasattr(_libs['grass_ogsf.7.4.1'], 'gsd_plus'):
    gsd_plus = _libs['grass_ogsf.7.4.1'].gsd_plus
    gsd_plus.restype = None
    gsd_plus.argtypes = [POINTER(c_float), c_int, c_float]

# C:/msys64/usr/src/grass741/dist.x86_64-w64-mingw32/include/grass/defs/ogsf.h: 467
if hasattr(_libs['grass_ogsf.7.4.1'], 'gsd_line_onsurf'):
    gsd_line_onsurf = _libs['grass_ogsf.7.4.1'].gsd_line_onsurf
    gsd_line_onsurf.restype = None
    gsd_line_onsurf.argtypes = [POINTER(geosurf), POINTER(c_float), POINTER(c_float)]

# C:/msys64/usr/src/grass741/dist.x86_64-w64-mingw32/include/grass/defs/ogsf.h: 468
if hasattr(_libs['grass_ogsf.7.4.1'], 'gsd_nline_onsurf'):
    gsd_nline_onsurf = _libs['grass_ogsf.7.4.1'].gsd_nline_onsurf
    gsd_nline_onsurf.restype = c_int
    gsd_nline_onsurf.argtypes = [POINTER(geosurf), POINTER(c_float), POINTER(c_float), POINTER(c_float), c_int]

# C:/msys64/usr/src/grass741/dist.x86_64-w64-mingw32/include/grass/defs/ogsf.h: 469
if hasattr(_libs['grass_ogsf.7.4.1'], 'gsd_x'):
    gsd_x = _libs['grass_ogsf.7.4.1'].gsd_x
    gsd_x.restype = None
    gsd_x.argtypes = [POINTER(geosurf), POINTER(c_float), c_int, c_float]

# C:/msys64/usr/src/grass741/dist.x86_64-w64-mingw32/include/grass/defs/ogsf.h: 470
if hasattr(_libs['grass_ogsf.7.4.1'], 'gsd_diamond'):
    gsd_diamond = _libs['grass_ogsf.7.4.1'].gsd_diamond
    gsd_diamond.restype = None
    gsd_diamond.argtypes = [POINTER(c_float), c_ulong, c_float]

# C:/msys64/usr/src/grass741/dist.x86_64-w64-mingw32/include/grass/defs/ogsf.h: 471
if hasattr(_libs['grass_ogsf.7.4.1'], 'gsd_diamond_lines'):
    gsd_diamond_lines = _libs['grass_ogsf.7.4.1'].gsd_diamond_lines
    gsd_diamond_lines.restype = None
    gsd_diamond_lines.argtypes = []

# C:/msys64/usr/src/grass741/dist.x86_64-w64-mingw32/include/grass/defs/ogsf.h: 472
if hasattr(_libs['grass_ogsf.7.4.1'], 'gsd_cube'):
    gsd_cube = _libs['grass_ogsf.7.4.1'].gsd_cube
    gsd_cube.restype = None
    gsd_cube.argtypes = [POINTER(c_float), c_ulong, c_float]

# C:/msys64/usr/src/grass741/dist.x86_64-w64-mingw32/include/grass/defs/ogsf.h: 473
if hasattr(_libs['grass_ogsf.7.4.1'], 'gsd_draw_box'):
    gsd_draw_box = _libs['grass_ogsf.7.4.1'].gsd_draw_box
    gsd_draw_box.restype = None
    gsd_draw_box.argtypes = [POINTER(c_float), c_ulong, c_float]

# C:/msys64/usr/src/grass741/dist.x86_64-w64-mingw32/include/grass/defs/ogsf.h: 474
if hasattr(_libs['grass_ogsf.7.4.1'], 'gsd_drawsphere'):
    gsd_drawsphere = _libs['grass_ogsf.7.4.1'].gsd_drawsphere
    gsd_drawsphere.restype = None
    gsd_drawsphere.argtypes = [POINTER(c_float), c_ulong, c_float]

# C:/msys64/usr/src/grass741/dist.x86_64-w64-mingw32/include/grass/defs/ogsf.h: 475
if hasattr(_libs['grass_ogsf.7.4.1'], 'gsd_draw_asterisk'):
    gsd_draw_asterisk = _libs['grass_ogsf.7.4.1'].gsd_draw_asterisk
    gsd_draw_asterisk.restype = None
    gsd_draw_asterisk.argtypes = [POINTER(c_float), c_ulong, c_float]

# C:/msys64/usr/src/grass741/dist.x86_64-w64-mingw32/include/grass/defs/ogsf.h: 476
if hasattr(_libs['grass_ogsf.7.4.1'], 'gsd_draw_gyro'):
    gsd_draw_gyro = _libs['grass_ogsf.7.4.1'].gsd_draw_gyro
    gsd_draw_gyro.restype = None
    gsd_draw_gyro.argtypes = [POINTER(c_float), c_ulong, c_float]

# C:/msys64/usr/src/grass741/dist.x86_64-w64-mingw32/include/grass/defs/ogsf.h: 477
if hasattr(_libs['grass_ogsf.7.4.1'], 'gsd_3dcursor'):
    gsd_3dcursor = _libs['grass_ogsf.7.4.1'].gsd_3dcursor
    gsd_3dcursor.restype = None
    gsd_3dcursor.argtypes = [POINTER(c_float)]

# C:/msys64/usr/src/grass741/dist.x86_64-w64-mingw32/include/grass/defs/ogsf.h: 478
if hasattr(_libs['grass_ogsf.7.4.1'], 'dir_to_slope_aspect'):
    dir_to_slope_aspect = _libs['grass_ogsf.7.4.1'].dir_to_slope_aspect
    dir_to_slope_aspect.restype = None
    dir_to_slope_aspect.argtypes = [POINTER(c_float), POINTER(c_float), POINTER(c_float), c_int]

# C:/msys64/usr/src/grass741/dist.x86_64-w64-mingw32/include/grass/defs/ogsf.h: 479
if hasattr(_libs['grass_ogsf.7.4.1'], 'gsd_north_arrow'):
    gsd_north_arrow = _libs['grass_ogsf.7.4.1'].gsd_north_arrow
    gsd_north_arrow.restype = c_int
    gsd_north_arrow.argtypes = [POINTER(c_float), c_float, GLuint, c_ulong, c_ulong]

# C:/msys64/usr/src/grass741/dist.x86_64-w64-mingw32/include/grass/defs/ogsf.h: 480
if hasattr(_libs['grass_ogsf.7.4.1'], 'gsd_arrow'):
    gsd_arrow = _libs['grass_ogsf.7.4.1'].gsd_arrow
    gsd_arrow.restype = c_int
    gsd_arrow.argtypes = [POINTER(c_float), c_ulong, c_float, POINTER(c_float), c_float, POINTER(geosurf)]

# C:/msys64/usr/src/grass741/dist.x86_64-w64-mingw32/include/grass/defs/ogsf.h: 481
if hasattr(_libs['grass_ogsf.7.4.1'], 'gsd_arrow_onsurf'):
    gsd_arrow_onsurf = _libs['grass_ogsf.7.4.1'].gsd_arrow_onsurf
    gsd_arrow_onsurf.restype = c_int
    gsd_arrow_onsurf.argtypes = [POINTER(c_float), POINTER(c_float), c_ulong, c_int, POINTER(geosurf)]

# C:/msys64/usr/src/grass741/dist.x86_64-w64-mingw32/include/grass/defs/ogsf.h: 482
if hasattr(_libs['grass_ogsf.7.4.1'], 'gsd_3darrow'):
    gsd_3darrow = _libs['grass_ogsf.7.4.1'].gsd_3darrow
    gsd_3darrow.restype = None
    gsd_3darrow.argtypes = [POINTER(c_float), c_ulong, c_float, c_float, POINTER(c_float), c_float]

# C:/msys64/usr/src/grass741/dist.x86_64-w64-mingw32/include/grass/defs/ogsf.h: 483
if hasattr(_libs['grass_ogsf.7.4.1'], 'gsd_scalebar'):
    gsd_scalebar = _libs['grass_ogsf.7.4.1'].gsd_scalebar
    gsd_scalebar.restype = c_int
    gsd_scalebar.argtypes = [POINTER(c_float), c_float, GLuint, c_ulong, c_ulong]

# C:/msys64/usr/src/grass741/dist.x86_64-w64-mingw32/include/grass/defs/ogsf.h: 484
if hasattr(_libs['grass_ogsf.7.4.1'], 'gsd_scalebar_v2'):
    gsd_scalebar_v2 = _libs['grass_ogsf.7.4.1'].gsd_scalebar_v2
    gsd_scalebar_v2.restype = c_int
    gsd_scalebar_v2.argtypes = [POINTER(c_float), c_float, GLuint, c_ulong, c_ulong]

# C:/msys64/usr/src/grass741/dist.x86_64-w64-mingw32/include/grass/defs/ogsf.h: 485
if hasattr(_libs['grass_ogsf.7.4.1'], 'primitive_cone'):
    primitive_cone = _libs['grass_ogsf.7.4.1'].primitive_cone
    primitive_cone.restype = None
    primitive_cone.argtypes = [c_ulong]

# C:/msys64/usr/src/grass741/dist.x86_64-w64-mingw32/include/grass/defs/ogsf.h: 486
if hasattr(_libs['grass_ogsf.7.4.1'], 'primitive_cylinder'):
    primitive_cylinder = _libs['grass_ogsf.7.4.1'].primitive_cylinder
    primitive_cylinder.restype = None
    primitive_cylinder.argtypes = [c_ulong, c_int]

# C:/msys64/usr/src/grass741/dist.x86_64-w64-mingw32/include/grass/defs/ogsf.h: 489
if hasattr(_libs['grass_ogsf.7.4.1'], 'gsd_flush'):
    gsd_flush = _libs['grass_ogsf.7.4.1'].gsd_flush
    gsd_flush.restype = None
    gsd_flush.argtypes = []

# C:/msys64/usr/src/grass741/dist.x86_64-w64-mingw32/include/grass/defs/ogsf.h: 490
if hasattr(_libs['grass_ogsf.7.4.1'], 'gsd_colormode'):
    gsd_colormode = _libs['grass_ogsf.7.4.1'].gsd_colormode
    gsd_colormode.restype = None
    gsd_colormode.argtypes = [c_int]

# C:/msys64/usr/src/grass741/dist.x86_64-w64-mingw32/include/grass/defs/ogsf.h: 491
if hasattr(_libs['grass_ogsf.7.4.1'], 'show_colormode'):
    show_colormode = _libs['grass_ogsf.7.4.1'].show_colormode
    show_colormode.restype = None
    show_colormode.argtypes = []

# C:/msys64/usr/src/grass741/dist.x86_64-w64-mingw32/include/grass/defs/ogsf.h: 492
if hasattr(_libs['grass_ogsf.7.4.1'], 'gsd_circ'):
    gsd_circ = _libs['grass_ogsf.7.4.1'].gsd_circ
    gsd_circ.restype = None
    gsd_circ.argtypes = [c_float, c_float, c_float]

# C:/msys64/usr/src/grass741/dist.x86_64-w64-mingw32/include/grass/defs/ogsf.h: 493
if hasattr(_libs['grass_ogsf.7.4.1'], 'gsd_disc'):
    gsd_disc = _libs['grass_ogsf.7.4.1'].gsd_disc
    gsd_disc.restype = None
    gsd_disc.argtypes = [c_float, c_float, c_float, c_float]

# C:/msys64/usr/src/grass741/dist.x86_64-w64-mingw32/include/grass/defs/ogsf.h: 494
if hasattr(_libs['grass_ogsf.7.4.1'], 'gsd_sphere'):
    gsd_sphere = _libs['grass_ogsf.7.4.1'].gsd_sphere
    gsd_sphere.restype = None
    gsd_sphere.argtypes = [POINTER(c_float), c_float]

# C:/msys64/usr/src/grass741/dist.x86_64-w64-mingw32/include/grass/defs/ogsf.h: 495
if hasattr(_libs['grass_ogsf.7.4.1'], 'gsd_zwritemask'):
    gsd_zwritemask = _libs['grass_ogsf.7.4.1'].gsd_zwritemask
    gsd_zwritemask.restype = None
    gsd_zwritemask.argtypes = [c_ulong]

# C:/msys64/usr/src/grass741/dist.x86_64-w64-mingw32/include/grass/defs/ogsf.h: 496
if hasattr(_libs['grass_ogsf.7.4.1'], 'gsd_backface'):
    gsd_backface = _libs['grass_ogsf.7.4.1'].gsd_backface
    gsd_backface.restype = None
    gsd_backface.argtypes = [c_int]

# C:/msys64/usr/src/grass741/dist.x86_64-w64-mingw32/include/grass/defs/ogsf.h: 497
if hasattr(_libs['grass_ogsf.7.4.1'], 'gsd_linewidth'):
    gsd_linewidth = _libs['grass_ogsf.7.4.1'].gsd_linewidth
    gsd_linewidth.restype = None
    gsd_linewidth.argtypes = [c_short]

# C:/msys64/usr/src/grass741/dist.x86_64-w64-mingw32/include/grass/defs/ogsf.h: 498
if hasattr(_libs['grass_ogsf.7.4.1'], 'gsd_bgnqstrip'):
    gsd_bgnqstrip = _libs['grass_ogsf.7.4.1'].gsd_bgnqstrip
    gsd_bgnqstrip.restype = None
    gsd_bgnqstrip.argtypes = []

# C:/msys64/usr/src/grass741/dist.x86_64-w64-mingw32/include/grass/defs/ogsf.h: 499
if hasattr(_libs['grass_ogsf.7.4.1'], 'gsd_endqstrip'):
    gsd_endqstrip = _libs['grass_ogsf.7.4.1'].gsd_endqstrip
    gsd_endqstrip.restype = None
    gsd_endqstrip.argtypes = []

# C:/msys64/usr/src/grass741/dist.x86_64-w64-mingw32/include/grass/defs/ogsf.h: 500
if hasattr(_libs['grass_ogsf.7.4.1'], 'gsd_bgntmesh'):
    gsd_bgntmesh = _libs['grass_ogsf.7.4.1'].gsd_bgntmesh
    gsd_bgntmesh.restype = None
    gsd_bgntmesh.argtypes = []

# C:/msys64/usr/src/grass741/dist.x86_64-w64-mingw32/include/grass/defs/ogsf.h: 501
if hasattr(_libs['grass_ogsf.7.4.1'], 'gsd_endtmesh'):
    gsd_endtmesh = _libs['grass_ogsf.7.4.1'].gsd_endtmesh
    gsd_endtmesh.restype = None
    gsd_endtmesh.argtypes = []

# C:/msys64/usr/src/grass741/dist.x86_64-w64-mingw32/include/grass/defs/ogsf.h: 502
if hasattr(_libs['grass_ogsf.7.4.1'], 'gsd_bgntstrip'):
    gsd_bgntstrip = _libs['grass_ogsf.7.4.1'].gsd_bgntstrip
    gsd_bgntstrip.restype = None
    gsd_bgntstrip.argtypes = []

# C:/msys64/usr/src/grass741/dist.x86_64-w64-mingw32/include/grass/defs/ogsf.h: 503
if hasattr(_libs['grass_ogsf.7.4.1'], 'gsd_endtstrip'):
    gsd_endtstrip = _libs['grass_ogsf.7.4.1'].gsd_endtstrip
    gsd_endtstrip.restype = None
    gsd_endtstrip.argtypes = []

# C:/msys64/usr/src/grass741/dist.x86_64-w64-mingw32/include/grass/defs/ogsf.h: 504
if hasattr(_libs['grass_ogsf.7.4.1'], 'gsd_bgntfan'):
    gsd_bgntfan = _libs['grass_ogsf.7.4.1'].gsd_bgntfan
    gsd_bgntfan.restype = None
    gsd_bgntfan.argtypes = []

# C:/msys64/usr/src/grass741/dist.x86_64-w64-mingw32/include/grass/defs/ogsf.h: 505
if hasattr(_libs['grass_ogsf.7.4.1'], 'gsd_endtfan'):
    gsd_endtfan = _libs['grass_ogsf.7.4.1'].gsd_endtfan
    gsd_endtfan.restype = None
    gsd_endtfan.argtypes = []

# C:/msys64/usr/src/grass741/dist.x86_64-w64-mingw32/include/grass/defs/ogsf.h: 506
if hasattr(_libs['grass_ogsf.7.4.1'], 'gsd_swaptmesh'):
    gsd_swaptmesh = _libs['grass_ogsf.7.4.1'].gsd_swaptmesh
    gsd_swaptmesh.restype = None
    gsd_swaptmesh.argtypes = []

# C:/msys64/usr/src/grass741/dist.x86_64-w64-mingw32/include/grass/defs/ogsf.h: 507
if hasattr(_libs['grass_ogsf.7.4.1'], 'gsd_bgnpolygon'):
    gsd_bgnpolygon = _libs['grass_ogsf.7.4.1'].gsd_bgnpolygon
    gsd_bgnpolygon.restype = None
    gsd_bgnpolygon.argtypes = []

# C:/msys64/usr/src/grass741/dist.x86_64-w64-mingw32/include/grass/defs/ogsf.h: 508
if hasattr(_libs['grass_ogsf.7.4.1'], 'gsd_endpolygon'):
    gsd_endpolygon = _libs['grass_ogsf.7.4.1'].gsd_endpolygon
    gsd_endpolygon.restype = None
    gsd_endpolygon.argtypes = []

# C:/msys64/usr/src/grass741/dist.x86_64-w64-mingw32/include/grass/defs/ogsf.h: 509
if hasattr(_libs['grass_ogsf.7.4.1'], 'gsd_bgnline'):
    gsd_bgnline = _libs['grass_ogsf.7.4.1'].gsd_bgnline
    gsd_bgnline.restype = None
    gsd_bgnline.argtypes = []

# C:/msys64/usr/src/grass741/dist.x86_64-w64-mingw32/include/grass/defs/ogsf.h: 510
if hasattr(_libs['grass_ogsf.7.4.1'], 'gsd_endline'):
    gsd_endline = _libs['grass_ogsf.7.4.1'].gsd_endline
    gsd_endline.restype = None
    gsd_endline.argtypes = []

# C:/msys64/usr/src/grass741/dist.x86_64-w64-mingw32/include/grass/defs/ogsf.h: 511
if hasattr(_libs['grass_ogsf.7.4.1'], 'gsd_shademodel'):
    gsd_shademodel = _libs['grass_ogsf.7.4.1'].gsd_shademodel
    gsd_shademodel.restype = None
    gsd_shademodel.argtypes = [c_int]

# C:/msys64/usr/src/grass741/dist.x86_64-w64-mingw32/include/grass/defs/ogsf.h: 512
if hasattr(_libs['grass_ogsf.7.4.1'], 'gsd_getshademodel'):
    gsd_getshademodel = _libs['grass_ogsf.7.4.1'].gsd_getshademodel
    gsd_getshademodel.restype = c_int
    gsd_getshademodel.argtypes = []

# C:/msys64/usr/src/grass741/dist.x86_64-w64-mingw32/include/grass/defs/ogsf.h: 513
if hasattr(_libs['grass_ogsf.7.4.1'], 'gsd_bothbuffers'):
    gsd_bothbuffers = _libs['grass_ogsf.7.4.1'].gsd_bothbuffers
    gsd_bothbuffers.restype = None
    gsd_bothbuffers.argtypes = []

# C:/msys64/usr/src/grass741/dist.x86_64-w64-mingw32/include/grass/defs/ogsf.h: 514
if hasattr(_libs['grass_ogsf.7.4.1'], 'gsd_frontbuffer'):
    gsd_frontbuffer = _libs['grass_ogsf.7.4.1'].gsd_frontbuffer
    gsd_frontbuffer.restype = None
    gsd_frontbuffer.argtypes = []

# C:/msys64/usr/src/grass741/dist.x86_64-w64-mingw32/include/grass/defs/ogsf.h: 515
if hasattr(_libs['grass_ogsf.7.4.1'], 'gsd_backbuffer'):
    gsd_backbuffer = _libs['grass_ogsf.7.4.1'].gsd_backbuffer
    gsd_backbuffer.restype = None
    gsd_backbuffer.argtypes = []

# C:/msys64/usr/src/grass741/dist.x86_64-w64-mingw32/include/grass/defs/ogsf.h: 516
if hasattr(_libs['grass_ogsf.7.4.1'], 'gsd_swapbuffers'):
    gsd_swapbuffers = _libs['grass_ogsf.7.4.1'].gsd_swapbuffers
    gsd_swapbuffers.restype = None
    gsd_swapbuffers.argtypes = []

# C:/msys64/usr/src/grass741/dist.x86_64-w64-mingw32/include/grass/defs/ogsf.h: 517
if hasattr(_libs['grass_ogsf.7.4.1'], 'gsd_popmatrix'):
    gsd_popmatrix = _libs['grass_ogsf.7.4.1'].gsd_popmatrix
    gsd_popmatrix.restype = None
    gsd_popmatrix.argtypes = []

# C:/msys64/usr/src/grass741/dist.x86_64-w64-mingw32/include/grass/defs/ogsf.h: 518
if hasattr(_libs['grass_ogsf.7.4.1'], 'gsd_pushmatrix'):
    gsd_pushmatrix = _libs['grass_ogsf.7.4.1'].gsd_pushmatrix
    gsd_pushmatrix.restype = None
    gsd_pushmatrix.argtypes = []

# C:/msys64/usr/src/grass741/dist.x86_64-w64-mingw32/include/grass/defs/ogsf.h: 519
if hasattr(_libs['grass_ogsf.7.4.1'], 'gsd_scale'):
    gsd_scale = _libs['grass_ogsf.7.4.1'].gsd_scale
    gsd_scale.restype = None
    gsd_scale.argtypes = [c_float, c_float, c_float]

# C:/msys64/usr/src/grass741/dist.x86_64-w64-mingw32/include/grass/defs/ogsf.h: 520
if hasattr(_libs['grass_ogsf.7.4.1'], 'gsd_translate'):
    gsd_translate = _libs['grass_ogsf.7.4.1'].gsd_translate
    gsd_translate.restype = None
    gsd_translate.argtypes = [c_float, c_float, c_float]

# C:/msys64/usr/src/grass741/dist.x86_64-w64-mingw32/include/grass/defs/ogsf.h: 521
if hasattr(_libs['grass_ogsf.7.4.1'], 'gsd_rot'):
    gsd_rot = _libs['grass_ogsf.7.4.1'].gsd_rot
    gsd_rot.restype = None
    gsd_rot.argtypes = [c_float, c_char]

# C:/msys64/usr/src/grass741/dist.x86_64-w64-mingw32/include/grass/defs/ogsf.h: 522
for _lib in _libs.values():
    if hasattr(_lib, 'gsd_checkwindow'):
        gsd_checkwindow = _lib.gsd_checkwindow
        gsd_checkwindow.restype = None
        gsd_checkwindow.argtypes = [POINTER(c_int), POINTER(c_int), POINTER(c_double), POINTER(c_double)]
        break

# C:/msys64/usr/src/grass741/dist.x86_64-w64-mingw32/include/grass/defs/ogsf.h: 523
if hasattr(_libs['grass_ogsf.7.4.1'], 'gsd_checkpoint'):
    gsd_checkpoint = _libs['grass_ogsf.7.4.1'].gsd_checkpoint
    gsd_checkpoint.restype = c_int
    gsd_checkpoint.argtypes = [POINTER(c_float), POINTER(c_int), POINTER(c_int), POINTER(c_double), POINTER(c_double)]

# C:/msys64/usr/src/grass741/dist.x86_64-w64-mingw32/include/grass/defs/ogsf.h: 524
if hasattr(_libs['grass_ogsf.7.4.1'], 'gsd_litvert_func'):
    gsd_litvert_func = _libs['grass_ogsf.7.4.1'].gsd_litvert_func
    gsd_litvert_func.restype = None
    gsd_litvert_func.argtypes = [POINTER(c_float), c_ulong, POINTER(c_float)]

# C:/msys64/usr/src/grass741/dist.x86_64-w64-mingw32/include/grass/defs/ogsf.h: 525
if hasattr(_libs['grass_ogsf.7.4.1'], 'gsd_litvert_func2'):
    gsd_litvert_func2 = _libs['grass_ogsf.7.4.1'].gsd_litvert_func2
    gsd_litvert_func2.restype = None
    gsd_litvert_func2.argtypes = [POINTER(c_float), c_ulong, POINTER(c_float)]

# C:/msys64/usr/src/grass741/dist.x86_64-w64-mingw32/include/grass/defs/ogsf.h: 526
if hasattr(_libs['grass_ogsf.7.4.1'], 'gsd_vert_func'):
    gsd_vert_func = _libs['grass_ogsf.7.4.1'].gsd_vert_func
    gsd_vert_func.restype = None
    gsd_vert_func.argtypes = [POINTER(c_float)]

# C:/msys64/usr/src/grass741/dist.x86_64-w64-mingw32/include/grass/defs/ogsf.h: 527
if hasattr(_libs['grass_ogsf.7.4.1'], 'gsd_color_func'):
    gsd_color_func = _libs['grass_ogsf.7.4.1'].gsd_color_func
    gsd_color_func.restype = None
    gsd_color_func.argtypes = [c_uint]

# C:/msys64/usr/src/grass741/dist.x86_64-w64-mingw32/include/grass/defs/ogsf.h: 528
if hasattr(_libs['grass_ogsf.7.4.1'], 'gsd_init_lightmodel'):
    gsd_init_lightmodel = _libs['grass_ogsf.7.4.1'].gsd_init_lightmodel
    gsd_init_lightmodel.restype = None
    gsd_init_lightmodel.argtypes = []

# C:/msys64/usr/src/grass741/dist.x86_64-w64-mingw32/include/grass/defs/ogsf.h: 529
if hasattr(_libs['grass_ogsf.7.4.1'], 'gsd_set_material'):
    gsd_set_material = _libs['grass_ogsf.7.4.1'].gsd_set_material
    gsd_set_material.restype = None
    gsd_set_material.argtypes = [c_int, c_int, c_float, c_float, c_int]

# C:/msys64/usr/src/grass741/dist.x86_64-w64-mingw32/include/grass/defs/ogsf.h: 530
if hasattr(_libs['grass_ogsf.7.4.1'], 'gsd_deflight'):
    gsd_deflight = _libs['grass_ogsf.7.4.1'].gsd_deflight
    gsd_deflight.restype = None
    gsd_deflight.argtypes = [c_int, POINTER(struct_lightdefs)]

# C:/msys64/usr/src/grass741/dist.x86_64-w64-mingw32/include/grass/defs/ogsf.h: 531
if hasattr(_libs['grass_ogsf.7.4.1'], 'gsd_switchlight'):
    gsd_switchlight = _libs['grass_ogsf.7.4.1'].gsd_switchlight
    gsd_switchlight.restype = None
    gsd_switchlight.argtypes = [c_int, c_int]

# C:/msys64/usr/src/grass741/dist.x86_64-w64-mingw32/include/grass/defs/ogsf.h: 532
if hasattr(_libs['grass_ogsf.7.4.1'], 'gsd_getimage'):
    gsd_getimage = _libs['grass_ogsf.7.4.1'].gsd_getimage
    gsd_getimage.restype = c_int
    gsd_getimage.argtypes = [POINTER(POINTER(c_ubyte)), POINTER(c_uint), POINTER(c_uint)]

# C:/msys64/usr/src/grass741/dist.x86_64-w64-mingw32/include/grass/defs/ogsf.h: 533
if hasattr(_libs['grass_ogsf.7.4.1'], 'gsd_blend'):
    gsd_blend = _libs['grass_ogsf.7.4.1'].gsd_blend
    gsd_blend.restype = None
    gsd_blend.argtypes = [c_int]

# C:/msys64/usr/src/grass741/dist.x86_64-w64-mingw32/include/grass/defs/ogsf.h: 534
if hasattr(_libs['grass_ogsf.7.4.1'], 'gsd_def_clipplane'):
    gsd_def_clipplane = _libs['grass_ogsf.7.4.1'].gsd_def_clipplane
    gsd_def_clipplane.restype = None
    gsd_def_clipplane.argtypes = [c_int, POINTER(c_double)]

# C:/msys64/usr/src/grass741/dist.x86_64-w64-mingw32/include/grass/defs/ogsf.h: 535
if hasattr(_libs['grass_ogsf.7.4.1'], 'gsd_set_clipplane'):
    gsd_set_clipplane = _libs['grass_ogsf.7.4.1'].gsd_set_clipplane
    gsd_set_clipplane.restype = None
    gsd_set_clipplane.argtypes = [c_int, c_int]

# C:/msys64/usr/src/grass741/dist.x86_64-w64-mingw32/include/grass/defs/ogsf.h: 536
if hasattr(_libs['grass_ogsf.7.4.1'], 'gsd_finish'):
    gsd_finish = _libs['grass_ogsf.7.4.1'].gsd_finish
    gsd_finish.restype = None
    gsd_finish.argtypes = []

# C:/msys64/usr/src/grass741/dist.x86_64-w64-mingw32/include/grass/defs/ogsf.h: 537
if hasattr(_libs['grass_ogsf.7.4.1'], 'gsd_viewport'):
    gsd_viewport = _libs['grass_ogsf.7.4.1'].gsd_viewport
    gsd_viewport.restype = None
    gsd_viewport.argtypes = [c_int, c_int, c_int, c_int]

# C:/msys64/usr/src/grass741/dist.x86_64-w64-mingw32/include/grass/defs/ogsf.h: 538
if hasattr(_libs['grass_ogsf.7.4.1'], 'gsd_makelist'):
    gsd_makelist = _libs['grass_ogsf.7.4.1'].gsd_makelist
    gsd_makelist.restype = c_int
    gsd_makelist.argtypes = []

# C:/msys64/usr/src/grass741/dist.x86_64-w64-mingw32/include/grass/defs/ogsf.h: 539
if hasattr(_libs['grass_ogsf.7.4.1'], 'gsd_bgnlist'):
    gsd_bgnlist = _libs['grass_ogsf.7.4.1'].gsd_bgnlist
    gsd_bgnlist.restype = None
    gsd_bgnlist.argtypes = [c_int, c_int]

# C:/msys64/usr/src/grass741/dist.x86_64-w64-mingw32/include/grass/defs/ogsf.h: 540
if hasattr(_libs['grass_ogsf.7.4.1'], 'gsd_endlist'):
    gsd_endlist = _libs['grass_ogsf.7.4.1'].gsd_endlist
    gsd_endlist.restype = None
    gsd_endlist.argtypes = []

# C:/msys64/usr/src/grass741/dist.x86_64-w64-mingw32/include/grass/defs/ogsf.h: 541
if hasattr(_libs['grass_ogsf.7.4.1'], 'gsd_calllist'):
    gsd_calllist = _libs['grass_ogsf.7.4.1'].gsd_calllist
    gsd_calllist.restype = None
    gsd_calllist.argtypes = [c_int]

# C:/msys64/usr/src/grass741/dist.x86_64-w64-mingw32/include/grass/defs/ogsf.h: 542
if hasattr(_libs['grass_ogsf.7.4.1'], 'gsd_deletelist'):
    gsd_deletelist = _libs['grass_ogsf.7.4.1'].gsd_deletelist
    gsd_deletelist.restype = None
    gsd_deletelist.argtypes = [GLuint, c_int]

# C:/msys64/usr/src/grass741/dist.x86_64-w64-mingw32/include/grass/defs/ogsf.h: 543
if hasattr(_libs['grass_ogsf.7.4.1'], 'gsd_calllists'):
    gsd_calllists = _libs['grass_ogsf.7.4.1'].gsd_calllists
    gsd_calllists.restype = None
    gsd_calllists.argtypes = [c_int]

# C:/msys64/usr/src/grass741/dist.x86_64-w64-mingw32/include/grass/defs/ogsf.h: 544
if hasattr(_libs['grass_ogsf.7.4.1'], 'gsd_getwindow'):
    gsd_getwindow = _libs['grass_ogsf.7.4.1'].gsd_getwindow
    gsd_getwindow.restype = None
    gsd_getwindow.argtypes = [POINTER(c_int), POINTER(c_int), POINTER(c_double), POINTER(c_double)]

# C:/msys64/usr/src/grass741/dist.x86_64-w64-mingw32/include/grass/defs/ogsf.h: 545
if hasattr(_libs['grass_ogsf.7.4.1'], 'gsd_writeView'):
    gsd_writeView = _libs['grass_ogsf.7.4.1'].gsd_writeView
    gsd_writeView.restype = c_int
    gsd_writeView.argtypes = [POINTER(POINTER(c_ubyte)), c_uint, c_uint]

# C:/msys64/usr/src/grass741/dist.x86_64-w64-mingw32/include/grass/defs/ogsf.h: 548
if hasattr(_libs['grass_ogsf.7.4.1'], 'gsd_surf'):
    gsd_surf = _libs['grass_ogsf.7.4.1'].gsd_surf
    gsd_surf.restype = c_int
    gsd_surf.argtypes = [POINTER(geosurf)]

# C:/msys64/usr/src/grass741/dist.x86_64-w64-mingw32/include/grass/defs/ogsf.h: 549
if hasattr(_libs['grass_ogsf.7.4.1'], 'gsd_surf_map'):
    gsd_surf_map = _libs['grass_ogsf.7.4.1'].gsd_surf_map
    gsd_surf_map.restype = c_int
    gsd_surf_map.argtypes = [POINTER(geosurf)]

# C:/msys64/usr/src/grass741/dist.x86_64-w64-mingw32/include/grass/defs/ogsf.h: 550
if hasattr(_libs['grass_ogsf.7.4.1'], 'gsd_surf_const'):
    gsd_surf_const = _libs['grass_ogsf.7.4.1'].gsd_surf_const
    gsd_surf_const.restype = c_int
    gsd_surf_const.argtypes = [POINTER(geosurf), c_float]

# C:/msys64/usr/src/grass741/dist.x86_64-w64-mingw32/include/grass/defs/ogsf.h: 551
if hasattr(_libs['grass_ogsf.7.4.1'], 'gsd_surf_func'):
    gsd_surf_func = _libs['grass_ogsf.7.4.1'].gsd_surf_func
    gsd_surf_func.restype = c_int
    gsd_surf_func.argtypes = [POINTER(geosurf), CFUNCTYPE(UNCHECKED(c_int), )]

# C:/msys64/usr/src/grass741/dist.x86_64-w64-mingw32/include/grass/defs/ogsf.h: 552
if hasattr(_libs['grass_ogsf.7.4.1'], 'gsd_triangulated_wall'):
    gsd_triangulated_wall = _libs['grass_ogsf.7.4.1'].gsd_triangulated_wall
    gsd_triangulated_wall.restype = c_int
    gsd_triangulated_wall.argtypes = [c_int, c_int, POINTER(geosurf), POINTER(geosurf), POINTER(Point3), POINTER(Point3), POINTER(c_float)]

# C:/msys64/usr/src/grass741/dist.x86_64-w64-mingw32/include/grass/defs/ogsf.h: 554
if hasattr(_libs['grass_ogsf.7.4.1'], 'gsd_setfc'):
    gsd_setfc = _libs['grass_ogsf.7.4.1'].gsd_setfc
    gsd_setfc.restype = None
    gsd_setfc.argtypes = [c_int]

# C:/msys64/usr/src/grass741/dist.x86_64-w64-mingw32/include/grass/defs/ogsf.h: 555
if hasattr(_libs['grass_ogsf.7.4.1'], 'gsd_getfc'):
    gsd_getfc = _libs['grass_ogsf.7.4.1'].gsd_getfc
    gsd_getfc.restype = c_int
    gsd_getfc.argtypes = []

# C:/msys64/usr/src/grass741/dist.x86_64-w64-mingw32/include/grass/defs/ogsf.h: 556
if hasattr(_libs['grass_ogsf.7.4.1'], 'gsd_ortho_wall'):
    gsd_ortho_wall = _libs['grass_ogsf.7.4.1'].gsd_ortho_wall
    gsd_ortho_wall.restype = c_int
    gsd_ortho_wall.argtypes = [c_int, c_int, POINTER(POINTER(geosurf)), POINTER(POINTER(Point3)), POINTER(c_float)]

# C:/msys64/usr/src/grass741/dist.x86_64-w64-mingw32/include/grass/defs/ogsf.h: 557
if hasattr(_libs['grass_ogsf.7.4.1'], 'gsd_wall'):
    gsd_wall = _libs['grass_ogsf.7.4.1'].gsd_wall
    gsd_wall.restype = c_int
    gsd_wall.argtypes = [POINTER(c_float), POINTER(c_float), POINTER(c_float)]

# C:/msys64/usr/src/grass741/dist.x86_64-w64-mingw32/include/grass/defs/ogsf.h: 558
if hasattr(_libs['grass_ogsf.7.4.1'], 'gsd_norm_arrows'):
    gsd_norm_arrows = _libs['grass_ogsf.7.4.1'].gsd_norm_arrows
    gsd_norm_arrows.restype = c_int
    gsd_norm_arrows.argtypes = [POINTER(geosurf)]

# C:/msys64/usr/src/grass741/dist.x86_64-w64-mingw32/include/grass/defs/ogsf.h: 561
if hasattr(_libs['grass_ogsf.7.4.1'], 'gsd_get_los'):
    gsd_get_los = _libs['grass_ogsf.7.4.1'].gsd_get_los
    gsd_get_los.restype = c_int
    gsd_get_los.argtypes = [POINTER(c_float * 3), c_short, c_short]

# C:/msys64/usr/src/grass741/dist.x86_64-w64-mingw32/include/grass/defs/ogsf.h: 562
if hasattr(_libs['grass_ogsf.7.4.1'], 'gsd_set_view'):
    gsd_set_view = _libs['grass_ogsf.7.4.1'].gsd_set_view
    gsd_set_view.restype = None
    gsd_set_view.argtypes = [POINTER(geoview), POINTER(geodisplay)]

# C:/msys64/usr/src/grass741/dist.x86_64-w64-mingw32/include/grass/defs/ogsf.h: 563
if hasattr(_libs['grass_ogsf.7.4.1'], 'gsd_check_focus'):
    gsd_check_focus = _libs['grass_ogsf.7.4.1'].gsd_check_focus
    gsd_check_focus.restype = None
    gsd_check_focus.argtypes = [POINTER(geoview)]

# C:/msys64/usr/src/grass741/dist.x86_64-w64-mingw32/include/grass/defs/ogsf.h: 564
if hasattr(_libs['grass_ogsf.7.4.1'], 'gsd_get_zup'):
    gsd_get_zup = _libs['grass_ogsf.7.4.1'].gsd_get_zup
    gsd_get_zup.restype = None
    gsd_get_zup.argtypes = [POINTER(geoview), POINTER(c_double)]

# C:/msys64/usr/src/grass741/dist.x86_64-w64-mingw32/include/grass/defs/ogsf.h: 565
if hasattr(_libs['grass_ogsf.7.4.1'], 'gsd_zup_twist'):
    gsd_zup_twist = _libs['grass_ogsf.7.4.1'].gsd_zup_twist
    gsd_zup_twist.restype = c_int
    gsd_zup_twist.argtypes = [POINTER(geoview)]

# C:/msys64/usr/src/grass741/dist.x86_64-w64-mingw32/include/grass/defs/ogsf.h: 566
if hasattr(_libs['grass_ogsf.7.4.1'], 'gsd_do_scale'):
    gsd_do_scale = _libs['grass_ogsf.7.4.1'].gsd_do_scale
    gsd_do_scale.restype = None
    gsd_do_scale.argtypes = [c_int]

# C:/msys64/usr/src/grass741/dist.x86_64-w64-mingw32/include/grass/defs/ogsf.h: 567
if hasattr(_libs['grass_ogsf.7.4.1'], 'gsd_real2model'):
    gsd_real2model = _libs['grass_ogsf.7.4.1'].gsd_real2model
    gsd_real2model.restype = None
    gsd_real2model.argtypes = [Point3]

# C:/msys64/usr/src/grass741/dist.x86_64-w64-mingw32/include/grass/defs/ogsf.h: 568
if hasattr(_libs['grass_ogsf.7.4.1'], 'gsd_model2real'):
    gsd_model2real = _libs['grass_ogsf.7.4.1'].gsd_model2real
    gsd_model2real.restype = None
    gsd_model2real.argtypes = [Point3]

# C:/msys64/usr/src/grass741/dist.x86_64-w64-mingw32/include/grass/defs/ogsf.h: 569
if hasattr(_libs['grass_ogsf.7.4.1'], 'gsd_model2surf'):
    gsd_model2surf = _libs['grass_ogsf.7.4.1'].gsd_model2surf
    gsd_model2surf.restype = None
    gsd_model2surf.argtypes = [POINTER(geosurf), Point3]

# C:/msys64/usr/src/grass741/dist.x86_64-w64-mingw32/include/grass/defs/ogsf.h: 570
if hasattr(_libs['grass_ogsf.7.4.1'], 'gsd_surf2model'):
    gsd_surf2model = _libs['grass_ogsf.7.4.1'].gsd_surf2model
    gsd_surf2model.restype = None
    gsd_surf2model.argtypes = [Point3]

# C:/msys64/usr/src/grass741/dist.x86_64-w64-mingw32/include/grass/defs/ogsf.h: 571
if hasattr(_libs['grass_ogsf.7.4.1'], 'gsd_surf2real'):
    gsd_surf2real = _libs['grass_ogsf.7.4.1'].gsd_surf2real
    gsd_surf2real.restype = None
    gsd_surf2real.argtypes = [POINTER(geosurf), Point3]

# C:/msys64/usr/src/grass741/dist.x86_64-w64-mingw32/include/grass/defs/ogsf.h: 572
if hasattr(_libs['grass_ogsf.7.4.1'], 'gsd_real2surf'):
    gsd_real2surf = _libs['grass_ogsf.7.4.1'].gsd_real2surf
    gsd_real2surf.restype = None
    gsd_real2surf.argtypes = [POINTER(geosurf), Point3]

# C:/msys64/usr/src/grass741/dist.x86_64-w64-mingw32/include/grass/defs/ogsf.h: 575
if hasattr(_libs['grass_ogsf.7.4.1'], 'gsd_wire_surf'):
    gsd_wire_surf = _libs['grass_ogsf.7.4.1'].gsd_wire_surf
    gsd_wire_surf.restype = c_int
    gsd_wire_surf.argtypes = [POINTER(geosurf)]

# C:/msys64/usr/src/grass741/dist.x86_64-w64-mingw32/include/grass/defs/ogsf.h: 576
if hasattr(_libs['grass_ogsf.7.4.1'], 'gsd_wire_surf_map'):
    gsd_wire_surf_map = _libs['grass_ogsf.7.4.1'].gsd_wire_surf_map
    gsd_wire_surf_map.restype = c_int
    gsd_wire_surf_map.argtypes = [POINTER(geosurf)]

# C:/msys64/usr/src/grass741/dist.x86_64-w64-mingw32/include/grass/defs/ogsf.h: 577
if hasattr(_libs['grass_ogsf.7.4.1'], 'gsd_coarse_surf_map'):
    gsd_coarse_surf_map = _libs['grass_ogsf.7.4.1'].gsd_coarse_surf_map
    gsd_coarse_surf_map.restype = c_int
    gsd_coarse_surf_map.argtypes = [POINTER(geosurf)]

# C:/msys64/usr/src/grass741/dist.x86_64-w64-mingw32/include/grass/defs/ogsf.h: 578
if hasattr(_libs['grass_ogsf.7.4.1'], 'gsd_wire_surf_const'):
    gsd_wire_surf_const = _libs['grass_ogsf.7.4.1'].gsd_wire_surf_const
    gsd_wire_surf_const.restype = c_int
    gsd_wire_surf_const.argtypes = [POINTER(geosurf), c_float]

# C:/msys64/usr/src/grass741/dist.x86_64-w64-mingw32/include/grass/defs/ogsf.h: 579
if hasattr(_libs['grass_ogsf.7.4.1'], 'gsd_wire_surf_func'):
    gsd_wire_surf_func = _libs['grass_ogsf.7.4.1'].gsd_wire_surf_func
    gsd_wire_surf_func.restype = c_int
    gsd_wire_surf_func.argtypes = [POINTER(geosurf), CFUNCTYPE(UNCHECKED(c_int), )]

# C:/msys64/usr/src/grass741/dist.x86_64-w64-mingw32/include/grass/defs/ogsf.h: 580
if hasattr(_libs['grass_ogsf.7.4.1'], 'gsd_wire_arrows'):
    gsd_wire_arrows = _libs['grass_ogsf.7.4.1'].gsd_wire_arrows
    gsd_wire_arrows.restype = c_int
    gsd_wire_arrows.argtypes = [POINTER(geosurf)]

# C:/msys64/usr/src/grass741/dist.x86_64-w64-mingw32/include/grass/defs/ogsf.h: 583
if hasattr(_libs['grass_ogsf.7.4.1'], 'gsdiff_set_SDscale'):
    gsdiff_set_SDscale = _libs['grass_ogsf.7.4.1'].gsdiff_set_SDscale
    gsdiff_set_SDscale.restype = None
    gsdiff_set_SDscale.argtypes = [c_float]

# C:/msys64/usr/src/grass741/dist.x86_64-w64-mingw32/include/grass/defs/ogsf.h: 584
if hasattr(_libs['grass_ogsf.7.4.1'], 'gsdiff_get_SDscale'):
    gsdiff_get_SDscale = _libs['grass_ogsf.7.4.1'].gsdiff_get_SDscale
    gsdiff_get_SDscale.restype = c_float
    gsdiff_get_SDscale.argtypes = []

# C:/msys64/usr/src/grass741/dist.x86_64-w64-mingw32/include/grass/defs/ogsf.h: 585
if hasattr(_libs['grass_ogsf.7.4.1'], 'gsdiff_set_SDref'):
    gsdiff_set_SDref = _libs['grass_ogsf.7.4.1'].gsdiff_set_SDref
    gsdiff_set_SDref.restype = None
    gsdiff_set_SDref.argtypes = [POINTER(geosurf)]

# C:/msys64/usr/src/grass741/dist.x86_64-w64-mingw32/include/grass/defs/ogsf.h: 586
if hasattr(_libs['grass_ogsf.7.4.1'], 'gsdiff_get_SDref'):
    gsdiff_get_SDref = _libs['grass_ogsf.7.4.1'].gsdiff_get_SDref
    gsdiff_get_SDref.restype = POINTER(geosurf)
    gsdiff_get_SDref.argtypes = []

# C:/msys64/usr/src/grass741/dist.x86_64-w64-mingw32/include/grass/defs/ogsf.h: 587
if hasattr(_libs['grass_ogsf.7.4.1'], 'gsdiff_do_SD'):
    gsdiff_do_SD = _libs['grass_ogsf.7.4.1'].gsdiff_do_SD
    gsdiff_do_SD.restype = c_float
    gsdiff_do_SD.argtypes = [c_float, c_int]

# C:/msys64/usr/src/grass741/dist.x86_64-w64-mingw32/include/grass/defs/ogsf.h: 590
if hasattr(_libs['grass_ogsf.7.4.1'], 'gsdrape_set_surface'):
    gsdrape_set_surface = _libs['grass_ogsf.7.4.1'].gsdrape_set_surface
    gsdrape_set_surface.restype = c_int
    gsdrape_set_surface.argtypes = [POINTER(geosurf)]

# C:/msys64/usr/src/grass741/dist.x86_64-w64-mingw32/include/grass/defs/ogsf.h: 591
if hasattr(_libs['grass_ogsf.7.4.1'], 'seg_intersect_vregion'):
    seg_intersect_vregion = _libs['grass_ogsf.7.4.1'].seg_intersect_vregion
    seg_intersect_vregion.restype = c_int
    seg_intersect_vregion.argtypes = [POINTER(geosurf), POINTER(c_float), POINTER(c_float)]

# C:/msys64/usr/src/grass741/dist.x86_64-w64-mingw32/include/grass/defs/ogsf.h: 592
if hasattr(_libs['grass_ogsf.7.4.1'], 'gsdrape_get_segments'):
    gsdrape_get_segments = _libs['grass_ogsf.7.4.1'].gsdrape_get_segments
    gsdrape_get_segments.restype = POINTER(Point3)
    gsdrape_get_segments.argtypes = [POINTER(geosurf), POINTER(c_float), POINTER(c_float), POINTER(c_int)]

# C:/msys64/usr/src/grass741/dist.x86_64-w64-mingw32/include/grass/defs/ogsf.h: 593
if hasattr(_libs['grass_ogsf.7.4.1'], 'gsdrape_get_allsegments'):
    gsdrape_get_allsegments = _libs['grass_ogsf.7.4.1'].gsdrape_get_allsegments
    gsdrape_get_allsegments.restype = POINTER(Point3)
    gsdrape_get_allsegments.argtypes = [POINTER(geosurf), POINTER(c_float), POINTER(c_float), POINTER(c_int)]

# C:/msys64/usr/src/grass741/dist.x86_64-w64-mingw32/include/grass/defs/ogsf.h: 594
if hasattr(_libs['grass_ogsf.7.4.1'], 'interp_first_last'):
    interp_first_last = _libs['grass_ogsf.7.4.1'].interp_first_last
    interp_first_last.restype = None
    interp_first_last.argtypes = [POINTER(geosurf), POINTER(c_float), POINTER(c_float), Point3, Point3]

# C:/msys64/usr/src/grass741/dist.x86_64-w64-mingw32/include/grass/defs/ogsf.h: 595
if hasattr(_libs['grass_ogsf.7.4.1'], '_viewcell_tri_interp'):
    _viewcell_tri_interp = _libs['grass_ogsf.7.4.1']._viewcell_tri_interp
    _viewcell_tri_interp.restype = c_int
    _viewcell_tri_interp.argtypes = [POINTER(geosurf), Point3]

# C:/msys64/usr/src/grass741/dist.x86_64-w64-mingw32/include/grass/defs/ogsf.h: 596
if hasattr(_libs['grass_ogsf.7.4.1'], 'viewcell_tri_interp'):
    viewcell_tri_interp = _libs['grass_ogsf.7.4.1'].viewcell_tri_interp
    viewcell_tri_interp.restype = c_int
    viewcell_tri_interp.argtypes = [POINTER(geosurf), POINTER(typbuff), Point3, c_int]

# C:/msys64/usr/src/grass741/dist.x86_64-w64-mingw32/include/grass/defs/ogsf.h: 597
if hasattr(_libs['grass_ogsf.7.4.1'], 'in_vregion'):
    in_vregion = _libs['grass_ogsf.7.4.1'].in_vregion
    in_vregion.restype = c_int
    in_vregion.argtypes = [POINTER(geosurf), POINTER(c_float)]

# C:/msys64/usr/src/grass741/dist.x86_64-w64-mingw32/include/grass/defs/ogsf.h: 598
if hasattr(_libs['grass_ogsf.7.4.1'], 'order_intersects'):
    order_intersects = _libs['grass_ogsf.7.4.1'].order_intersects
    order_intersects.restype = c_int
    order_intersects.argtypes = [POINTER(geosurf), Point3, Point3, c_int, c_int, c_int]

# C:/msys64/usr/src/grass741/dist.x86_64-w64-mingw32/include/grass/defs/ogsf.h: 599
if hasattr(_libs['grass_ogsf.7.4.1'], 'get_vert_intersects'):
    get_vert_intersects = _libs['grass_ogsf.7.4.1'].get_vert_intersects
    get_vert_intersects.restype = c_int
    get_vert_intersects.argtypes = [POINTER(geosurf), POINTER(c_float), POINTER(c_float), POINTER(c_float)]

# C:/msys64/usr/src/grass741/dist.x86_64-w64-mingw32/include/grass/defs/ogsf.h: 600
if hasattr(_libs['grass_ogsf.7.4.1'], 'get_horz_intersects'):
    get_horz_intersects = _libs['grass_ogsf.7.4.1'].get_horz_intersects
    get_horz_intersects.restype = c_int
    get_horz_intersects.argtypes = [POINTER(geosurf), POINTER(c_float), POINTER(c_float), POINTER(c_float)]

# C:/msys64/usr/src/grass741/dist.x86_64-w64-mingw32/include/grass/defs/ogsf.h: 601
if hasattr(_libs['grass_ogsf.7.4.1'], 'get_diag_intersects'):
    get_diag_intersects = _libs['grass_ogsf.7.4.1'].get_diag_intersects
    get_diag_intersects.restype = c_int
    get_diag_intersects.argtypes = [POINTER(geosurf), POINTER(c_float), POINTER(c_float), POINTER(c_float)]

# C:/msys64/usr/src/grass741/dist.x86_64-w64-mingw32/include/grass/defs/ogsf.h: 602
if hasattr(_libs['grass_ogsf.7.4.1'], 'segs_intersect'):
    segs_intersect = _libs['grass_ogsf.7.4.1'].segs_intersect
    segs_intersect.restype = c_int
    segs_intersect.argtypes = [c_float, c_float, c_float, c_float, c_float, c_float, c_float, c_float, POINTER(c_float), POINTER(c_float)]

# C:/msys64/usr/src/grass741/dist.x86_64-w64-mingw32/include/grass/defs/ogsf.h: 604
if hasattr(_libs['grass_ogsf.7.4.1'], 'Point_on_plane'):
    Point_on_plane = _libs['grass_ogsf.7.4.1'].Point_on_plane
    Point_on_plane.restype = c_int
    Point_on_plane.argtypes = [Point3, Point3, Point3, Point3]

# C:/msys64/usr/src/grass741/dist.x86_64-w64-mingw32/include/grass/defs/ogsf.h: 605
if hasattr(_libs['grass_ogsf.7.4.1'], 'XY_intersect_plane'):
    XY_intersect_plane = _libs['grass_ogsf.7.4.1'].XY_intersect_plane
    XY_intersect_plane.restype = c_int
    XY_intersect_plane.argtypes = [POINTER(c_float), POINTER(c_float)]

# C:/msys64/usr/src/grass741/dist.x86_64-w64-mingw32/include/grass/defs/ogsf.h: 606
if hasattr(_libs['grass_ogsf.7.4.1'], 'P3toPlane'):
    P3toPlane = _libs['grass_ogsf.7.4.1'].P3toPlane
    P3toPlane.restype = c_int
    P3toPlane.argtypes = [Point3, Point3, Point3, POINTER(c_float)]

# C:/msys64/usr/src/grass741/dist.x86_64-w64-mingw32/include/grass/defs/ogsf.h: 607
if hasattr(_libs['grass_ogsf.7.4.1'], 'V3Cross'):
    V3Cross = _libs['grass_ogsf.7.4.1'].V3Cross
    V3Cross.restype = c_int
    V3Cross.argtypes = [Point3, Point3, Point3]

# C:/msys64/usr/src/grass741/dist.x86_64-w64-mingw32/include/grass/defs/ogsf.h: 610
if hasattr(_libs['grass_ogsf.7.4.1'], 'gsds_findh'):
    gsds_findh = _libs['grass_ogsf.7.4.1'].gsds_findh
    gsds_findh.restype = c_int
    gsds_findh.argtypes = [String, POINTER(c_uint), POINTER(c_uint), c_int]

# C:/msys64/usr/src/grass741/dist.x86_64-w64-mingw32/include/grass/defs/ogsf.h: 611
if hasattr(_libs['grass_ogsf.7.4.1'], 'gsds_newh'):
    gsds_newh = _libs['grass_ogsf.7.4.1'].gsds_newh
    gsds_newh.restype = c_int
    gsds_newh.argtypes = [String]

# C:/msys64/usr/src/grass741/dist.x86_64-w64-mingw32/include/grass/defs/ogsf.h: 612
if hasattr(_libs['grass_ogsf.7.4.1'], 'gsds_get_typbuff'):
    gsds_get_typbuff = _libs['grass_ogsf.7.4.1'].gsds_get_typbuff
    gsds_get_typbuff.restype = POINTER(typbuff)
    gsds_get_typbuff.argtypes = [c_int, c_uint]

# C:/msys64/usr/src/grass741/dist.x86_64-w64-mingw32/include/grass/defs/ogsf.h: 613
if hasattr(_libs['grass_ogsf.7.4.1'], 'gsds_get_name'):
    gsds_get_name = _libs['grass_ogsf.7.4.1'].gsds_get_name
    gsds_get_name.restype = ReturnString
    gsds_get_name.argtypes = [c_int]

# C:/msys64/usr/src/grass741/dist.x86_64-w64-mingw32/include/grass/defs/ogsf.h: 614
if hasattr(_libs['grass_ogsf.7.4.1'], 'gsds_free_datah'):
    gsds_free_datah = _libs['grass_ogsf.7.4.1'].gsds_free_datah
    gsds_free_datah.restype = c_int
    gsds_free_datah.argtypes = [c_int]

# C:/msys64/usr/src/grass741/dist.x86_64-w64-mingw32/include/grass/defs/ogsf.h: 615
if hasattr(_libs['grass_ogsf.7.4.1'], 'gsds_free_data_buff'):
    gsds_free_data_buff = _libs['grass_ogsf.7.4.1'].gsds_free_data_buff
    gsds_free_data_buff.restype = c_int
    gsds_free_data_buff.argtypes = [c_int, c_int]

# C:/msys64/usr/src/grass741/dist.x86_64-w64-mingw32/include/grass/defs/ogsf.h: 616
if hasattr(_libs['grass_ogsf.7.4.1'], 'free_data_buffs'):
    free_data_buffs = _libs['grass_ogsf.7.4.1'].free_data_buffs
    free_data_buffs.restype = c_size_t
    free_data_buffs.argtypes = [POINTER(dataset), c_int]

# C:/msys64/usr/src/grass741/dist.x86_64-w64-mingw32/include/grass/defs/ogsf.h: 617
if hasattr(_libs['grass_ogsf.7.4.1'], 'gsds_alloc_typbuff'):
    gsds_alloc_typbuff = _libs['grass_ogsf.7.4.1'].gsds_alloc_typbuff
    gsds_alloc_typbuff.restype = c_size_t
    gsds_alloc_typbuff.argtypes = [c_int, POINTER(c_int), c_int, c_int]

# C:/msys64/usr/src/grass741/dist.x86_64-w64-mingw32/include/grass/defs/ogsf.h: 618
if hasattr(_libs['grass_ogsf.7.4.1'], 'gsds_get_changed'):
    gsds_get_changed = _libs['grass_ogsf.7.4.1'].gsds_get_changed
    gsds_get_changed.restype = c_int
    gsds_get_changed.argtypes = [c_int]

# C:/msys64/usr/src/grass741/dist.x86_64-w64-mingw32/include/grass/defs/ogsf.h: 619
if hasattr(_libs['grass_ogsf.7.4.1'], 'gsds_set_changed'):
    gsds_set_changed = _libs['grass_ogsf.7.4.1'].gsds_set_changed
    gsds_set_changed.restype = c_int
    gsds_set_changed.argtypes = [c_int, c_uint]

# C:/msys64/usr/src/grass741/dist.x86_64-w64-mingw32/include/grass/defs/ogsf.h: 620
if hasattr(_libs['grass_ogsf.7.4.1'], 'gsds_get_type'):
    gsds_get_type = _libs['grass_ogsf.7.4.1'].gsds_get_type
    gsds_get_type.restype = c_int
    gsds_get_type.argtypes = [c_int]

# C:/msys64/usr/src/grass741/dist.x86_64-w64-mingw32/include/grass/defs/ogsf.h: 623
if hasattr(_libs['grass_ogsf.7.4.1'], 'get_mapatt'):
    get_mapatt = _libs['grass_ogsf.7.4.1'].get_mapatt
    get_mapatt.restype = c_int
    get_mapatt.argtypes = [POINTER(typbuff), c_int, POINTER(c_float)]

# C:/msys64/usr/src/grass741/dist.x86_64-w64-mingw32/include/grass/defs/ogsf.h: 626
if hasattr(_libs['grass_ogsf.7.4.1'], 'gv_get_vect'):
    gv_get_vect = _libs['grass_ogsf.7.4.1'].gv_get_vect
    gv_get_vect.restype = POINTER(geovect)
    gv_get_vect.argtypes = [c_int]

# C:/msys64/usr/src/grass741/dist.x86_64-w64-mingw32/include/grass/defs/ogsf.h: 627
if hasattr(_libs['grass_ogsf.7.4.1'], 'gv_get_prev_vect'):
    gv_get_prev_vect = _libs['grass_ogsf.7.4.1'].gv_get_prev_vect
    gv_get_prev_vect.restype = POINTER(geovect)
    gv_get_prev_vect.argtypes = [c_int]

# C:/msys64/usr/src/grass741/dist.x86_64-w64-mingw32/include/grass/defs/ogsf.h: 628
if hasattr(_libs['grass_ogsf.7.4.1'], 'gv_num_vects'):
    gv_num_vects = _libs['grass_ogsf.7.4.1'].gv_num_vects
    gv_num_vects.restype = c_int
    gv_num_vects.argtypes = []

# C:/msys64/usr/src/grass741/dist.x86_64-w64-mingw32/include/grass/defs/ogsf.h: 629
if hasattr(_libs['grass_ogsf.7.4.1'], 'gv_get_last_vect'):
    gv_get_last_vect = _libs['grass_ogsf.7.4.1'].gv_get_last_vect
    gv_get_last_vect.restype = POINTER(geovect)
    gv_get_last_vect.argtypes = []

# C:/msys64/usr/src/grass741/dist.x86_64-w64-mingw32/include/grass/defs/ogsf.h: 630
if hasattr(_libs['grass_ogsf.7.4.1'], 'gv_get_new_vect'):
    gv_get_new_vect = _libs['grass_ogsf.7.4.1'].gv_get_new_vect
    gv_get_new_vect.restype = POINTER(geovect)
    gv_get_new_vect.argtypes = []

# C:/msys64/usr/src/grass741/dist.x86_64-w64-mingw32/include/grass/defs/ogsf.h: 631
if hasattr(_libs['grass_ogsf.7.4.1'], 'gv_update_drapesurfs'):
    gv_update_drapesurfs = _libs['grass_ogsf.7.4.1'].gv_update_drapesurfs
    gv_update_drapesurfs.restype = None
    gv_update_drapesurfs.argtypes = []

# C:/msys64/usr/src/grass741/dist.x86_64-w64-mingw32/include/grass/defs/ogsf.h: 632
if hasattr(_libs['grass_ogsf.7.4.1'], 'gv_set_defaults'):
    gv_set_defaults = _libs['grass_ogsf.7.4.1'].gv_set_defaults
    gv_set_defaults.restype = c_int
    gv_set_defaults.argtypes = [POINTER(geovect)]

# C:/msys64/usr/src/grass741/dist.x86_64-w64-mingw32/include/grass/defs/ogsf.h: 633
if hasattr(_libs['grass_ogsf.7.4.1'], 'gv_init_vect'):
    gv_init_vect = _libs['grass_ogsf.7.4.1'].gv_init_vect
    gv_init_vect.restype = c_int
    gv_init_vect.argtypes = [POINTER(geovect)]

# C:/msys64/usr/src/grass741/dist.x86_64-w64-mingw32/include/grass/defs/ogsf.h: 634
if hasattr(_libs['grass_ogsf.7.4.1'], 'gv_delete_vect'):
    gv_delete_vect = _libs['grass_ogsf.7.4.1'].gv_delete_vect
    gv_delete_vect.restype = None
    gv_delete_vect.argtypes = [c_int]

# C:/msys64/usr/src/grass741/dist.x86_64-w64-mingw32/include/grass/defs/ogsf.h: 635
if hasattr(_libs['grass_ogsf.7.4.1'], 'gv_free_vect'):
    gv_free_vect = _libs['grass_ogsf.7.4.1'].gv_free_vect
    gv_free_vect.restype = c_int
    gv_free_vect.argtypes = [POINTER(geovect)]

# C:/msys64/usr/src/grass741/dist.x86_64-w64-mingw32/include/grass/defs/ogsf.h: 636
if hasattr(_libs['grass_ogsf.7.4.1'], 'gv_free_vectmem'):
    gv_free_vectmem = _libs['grass_ogsf.7.4.1'].gv_free_vectmem
    gv_free_vectmem.restype = None
    gv_free_vectmem.argtypes = [POINTER(geovect)]

# C:/msys64/usr/src/grass741/dist.x86_64-w64-mingw32/include/grass/defs/ogsf.h: 637
if hasattr(_libs['grass_ogsf.7.4.1'], 'gv_set_drapesurfs'):
    gv_set_drapesurfs = _libs['grass_ogsf.7.4.1'].gv_set_drapesurfs
    gv_set_drapesurfs.restype = None
    gv_set_drapesurfs.argtypes = [POINTER(geovect), POINTER(c_int), c_int]

# C:/msys64/usr/src/grass741/dist.x86_64-w64-mingw32/include/grass/defs/ogsf.h: 640
if hasattr(_libs['grass_ogsf.7.4.1'], 'gv_line_length'):
    gv_line_length = _libs['grass_ogsf.7.4.1'].gv_line_length
    gv_line_length.restype = c_float
    gv_line_length.argtypes = [POINTER(geoline)]

# C:/msys64/usr/src/grass741/dist.x86_64-w64-mingw32/include/grass/defs/ogsf.h: 641
if hasattr(_libs['grass_ogsf.7.4.1'], 'gln_num_points'):
    gln_num_points = _libs['grass_ogsf.7.4.1'].gln_num_points
    gln_num_points.restype = c_int
    gln_num_points.argtypes = [POINTER(geoline)]

# C:/msys64/usr/src/grass741/dist.x86_64-w64-mingw32/include/grass/defs/ogsf.h: 642
if hasattr(_libs['grass_ogsf.7.4.1'], 'gv_num_points'):
    gv_num_points = _libs['grass_ogsf.7.4.1'].gv_num_points
    gv_num_points.restype = c_int
    gv_num_points.argtypes = [POINTER(geovect)]

# C:/msys64/usr/src/grass741/dist.x86_64-w64-mingw32/include/grass/defs/ogsf.h: 643
if hasattr(_libs['grass_ogsf.7.4.1'], 'gv_decimate_lines'):
    gv_decimate_lines = _libs['grass_ogsf.7.4.1'].gv_decimate_lines
    gv_decimate_lines.restype = c_int
    gv_decimate_lines.argtypes = [POINTER(geovect)]

# C:/msys64/usr/src/grass741/dist.x86_64-w64-mingw32/include/grass/defs/ogsf.h: 646
if hasattr(_libs['grass_ogsf.7.4.1'], 'gs_clip_segment'):
    gs_clip_segment = _libs['grass_ogsf.7.4.1'].gs_clip_segment
    gs_clip_segment.restype = c_int
    gs_clip_segment.argtypes = [POINTER(geosurf), POINTER(c_float), POINTER(c_float), POINTER(c_float)]

# C:/msys64/usr/src/grass741/dist.x86_64-w64-mingw32/include/grass/defs/ogsf.h: 647
if hasattr(_libs['grass_ogsf.7.4.1'], 'gvd_vect'):
    gvd_vect = _libs['grass_ogsf.7.4.1'].gvd_vect
    gvd_vect.restype = c_int
    gvd_vect.argtypes = [POINTER(geovect), POINTER(geosurf), c_int]

# C:/msys64/usr/src/grass741/dist.x86_64-w64-mingw32/include/grass/defs/ogsf.h: 648
if hasattr(_libs['grass_ogsf.7.4.1'], 'gvd_draw_lineonsurf'):
    gvd_draw_lineonsurf = _libs['grass_ogsf.7.4.1'].gvd_draw_lineonsurf
    gvd_draw_lineonsurf.restype = None
    gvd_draw_lineonsurf.argtypes = [POINTER(geosurf), POINTER(c_float), POINTER(c_float), c_int]

# C:/msys64/usr/src/grass741/dist.x86_64-w64-mingw32/include/grass/defs/ogsf.h: 651
if hasattr(_libs['grass_ogsf.7.4.1'], 'gvl_get_vol'):
    gvl_get_vol = _libs['grass_ogsf.7.4.1'].gvl_get_vol
    gvl_get_vol.restype = POINTER(geovol)
    gvl_get_vol.argtypes = [c_int]

# C:/msys64/usr/src/grass741/dist.x86_64-w64-mingw32/include/grass/defs/ogsf.h: 652
if hasattr(_libs['grass_ogsf.7.4.1'], 'gvl_get_prev_vol'):
    gvl_get_prev_vol = _libs['grass_ogsf.7.4.1'].gvl_get_prev_vol
    gvl_get_prev_vol.restype = POINTER(geovol)
    gvl_get_prev_vol.argtypes = [c_int]

# C:/msys64/usr/src/grass741/dist.x86_64-w64-mingw32/include/grass/defs/ogsf.h: 653
if hasattr(_libs['grass_ogsf.7.4.1'], 'gvl_getall_vols'):
    gvl_getall_vols = _libs['grass_ogsf.7.4.1'].gvl_getall_vols
    gvl_getall_vols.restype = c_int
    gvl_getall_vols.argtypes = [POINTER(POINTER(geovol))]

# C:/msys64/usr/src/grass741/dist.x86_64-w64-mingw32/include/grass/defs/ogsf.h: 654
if hasattr(_libs['grass_ogsf.7.4.1'], 'gvl_num_vols'):
    gvl_num_vols = _libs['grass_ogsf.7.4.1'].gvl_num_vols
    gvl_num_vols.restype = c_int
    gvl_num_vols.argtypes = []

# C:/msys64/usr/src/grass741/dist.x86_64-w64-mingw32/include/grass/defs/ogsf.h: 655
if hasattr(_libs['grass_ogsf.7.4.1'], 'gvl_get_last_vol'):
    gvl_get_last_vol = _libs['grass_ogsf.7.4.1'].gvl_get_last_vol
    gvl_get_last_vol.restype = POINTER(geovol)
    gvl_get_last_vol.argtypes = []

# C:/msys64/usr/src/grass741/dist.x86_64-w64-mingw32/include/grass/defs/ogsf.h: 656
if hasattr(_libs['grass_ogsf.7.4.1'], 'gvl_get_new_vol'):
    gvl_get_new_vol = _libs['grass_ogsf.7.4.1'].gvl_get_new_vol
    gvl_get_new_vol.restype = POINTER(geovol)
    gvl_get_new_vol.argtypes = []

# C:/msys64/usr/src/grass741/dist.x86_64-w64-mingw32/include/grass/defs/ogsf.h: 657
if hasattr(_libs['grass_ogsf.7.4.1'], 'gvl_init_vol'):
    gvl_init_vol = _libs['grass_ogsf.7.4.1'].gvl_init_vol
    gvl_init_vol.restype = c_int
    gvl_init_vol.argtypes = [POINTER(geovol), c_double, c_double, c_double, c_int, c_int, c_int, c_double, c_double, c_double]

# C:/msys64/usr/src/grass741/dist.x86_64-w64-mingw32/include/grass/defs/ogsf.h: 659
if hasattr(_libs['grass_ogsf.7.4.1'], 'gvl_delete_vol'):
    gvl_delete_vol = _libs['grass_ogsf.7.4.1'].gvl_delete_vol
    gvl_delete_vol.restype = None
    gvl_delete_vol.argtypes = [c_int]

# C:/msys64/usr/src/grass741/dist.x86_64-w64-mingw32/include/grass/defs/ogsf.h: 660
if hasattr(_libs['grass_ogsf.7.4.1'], 'gvl_free_vol'):
    gvl_free_vol = _libs['grass_ogsf.7.4.1'].gvl_free_vol
    gvl_free_vol.restype = c_int
    gvl_free_vol.argtypes = [POINTER(geovol)]

# C:/msys64/usr/src/grass741/dist.x86_64-w64-mingw32/include/grass/defs/ogsf.h: 661
if hasattr(_libs['grass_ogsf.7.4.1'], 'gvl_free_volmem'):
    gvl_free_volmem = _libs['grass_ogsf.7.4.1'].gvl_free_volmem
    gvl_free_volmem.restype = None
    gvl_free_volmem.argtypes = [POINTER(geovol)]

# C:/msys64/usr/src/grass741/dist.x86_64-w64-mingw32/include/grass/defs/ogsf.h: 662
if hasattr(_libs['grass_ogsf.7.4.1'], 'print_vol_fields'):
    print_vol_fields = _libs['grass_ogsf.7.4.1'].print_vol_fields
    print_vol_fields.restype = None
    print_vol_fields.argtypes = [POINTER(geovol)]

# C:/msys64/usr/src/grass741/dist.x86_64-w64-mingw32/include/grass/defs/ogsf.h: 663
if hasattr(_libs['grass_ogsf.7.4.1'], 'gvl_get_xextents'):
    gvl_get_xextents = _libs['grass_ogsf.7.4.1'].gvl_get_xextents
    gvl_get_xextents.restype = c_int
    gvl_get_xextents.argtypes = [POINTER(geovol), POINTER(c_float), POINTER(c_float)]

# C:/msys64/usr/src/grass741/dist.x86_64-w64-mingw32/include/grass/defs/ogsf.h: 664
if hasattr(_libs['grass_ogsf.7.4.1'], 'gvl_get_yextents'):
    gvl_get_yextents = _libs['grass_ogsf.7.4.1'].gvl_get_yextents
    gvl_get_yextents.restype = c_int
    gvl_get_yextents.argtypes = [POINTER(geovol), POINTER(c_float), POINTER(c_float)]

# C:/msys64/usr/src/grass741/dist.x86_64-w64-mingw32/include/grass/defs/ogsf.h: 665
if hasattr(_libs['grass_ogsf.7.4.1'], 'gvl_get_zextents'):
    gvl_get_zextents = _libs['grass_ogsf.7.4.1'].gvl_get_zextents
    gvl_get_zextents.restype = c_int
    gvl_get_zextents.argtypes = [POINTER(geovol), POINTER(c_float), POINTER(c_float)]

# C:/msys64/usr/src/grass741/dist.x86_64-w64-mingw32/include/grass/defs/ogsf.h: 666
if hasattr(_libs['grass_ogsf.7.4.1'], 'gvl_get_xrange'):
    gvl_get_xrange = _libs['grass_ogsf.7.4.1'].gvl_get_xrange
    gvl_get_xrange.restype = c_int
    gvl_get_xrange.argtypes = [POINTER(c_float), POINTER(c_float)]

# C:/msys64/usr/src/grass741/dist.x86_64-w64-mingw32/include/grass/defs/ogsf.h: 667
if hasattr(_libs['grass_ogsf.7.4.1'], 'gvl_get_yrange'):
    gvl_get_yrange = _libs['grass_ogsf.7.4.1'].gvl_get_yrange
    gvl_get_yrange.restype = c_int
    gvl_get_yrange.argtypes = [POINTER(c_float), POINTER(c_float)]

# C:/msys64/usr/src/grass741/dist.x86_64-w64-mingw32/include/grass/defs/ogsf.h: 668
if hasattr(_libs['grass_ogsf.7.4.1'], 'gvl_get_zrange'):
    gvl_get_zrange = _libs['grass_ogsf.7.4.1'].gvl_get_zrange
    gvl_get_zrange.restype = c_int
    gvl_get_zrange.argtypes = [POINTER(c_float), POINTER(c_float)]

# C:/msys64/usr/src/grass741/dist.x86_64-w64-mingw32/include/grass/defs/ogsf.h: 670
if hasattr(_libs['grass_ogsf.7.4.1'], 'gvl_isosurf_init'):
    gvl_isosurf_init = _libs['grass_ogsf.7.4.1'].gvl_isosurf_init
    gvl_isosurf_init.restype = c_int
    gvl_isosurf_init.argtypes = [POINTER(geovol_isosurf)]

# C:/msys64/usr/src/grass741/dist.x86_64-w64-mingw32/include/grass/defs/ogsf.h: 671
if hasattr(_libs['grass_ogsf.7.4.1'], 'gvl_isosurf_freemem'):
    gvl_isosurf_freemem = _libs['grass_ogsf.7.4.1'].gvl_isosurf_freemem
    gvl_isosurf_freemem.restype = c_int
    gvl_isosurf_freemem.argtypes = [POINTER(geovol_isosurf)]

# C:/msys64/usr/src/grass741/dist.x86_64-w64-mingw32/include/grass/defs/ogsf.h: 672
if hasattr(_libs['grass_ogsf.7.4.1'], 'gvl_isosurf_get_isosurf'):
    gvl_isosurf_get_isosurf = _libs['grass_ogsf.7.4.1'].gvl_isosurf_get_isosurf
    gvl_isosurf_get_isosurf.restype = POINTER(geovol_isosurf)
    gvl_isosurf_get_isosurf.argtypes = [c_int, c_int]

# C:/msys64/usr/src/grass741/dist.x86_64-w64-mingw32/include/grass/defs/ogsf.h: 673
if hasattr(_libs['grass_ogsf.7.4.1'], 'gvl_isosurf_get_att_src'):
    gvl_isosurf_get_att_src = _libs['grass_ogsf.7.4.1'].gvl_isosurf_get_att_src
    gvl_isosurf_get_att_src.restype = c_int
    gvl_isosurf_get_att_src.argtypes = [POINTER(geovol_isosurf), c_int]

# C:/msys64/usr/src/grass741/dist.x86_64-w64-mingw32/include/grass/defs/ogsf.h: 674
if hasattr(_libs['grass_ogsf.7.4.1'], 'gvl_isosurf_set_att_src'):
    gvl_isosurf_set_att_src = _libs['grass_ogsf.7.4.1'].gvl_isosurf_set_att_src
    gvl_isosurf_set_att_src.restype = c_int
    gvl_isosurf_set_att_src.argtypes = [POINTER(geovol_isosurf), c_int, c_int]

# C:/msys64/usr/src/grass741/dist.x86_64-w64-mingw32/include/grass/defs/ogsf.h: 675
if hasattr(_libs['grass_ogsf.7.4.1'], 'gvl_isosurf_set_att_const'):
    gvl_isosurf_set_att_const = _libs['grass_ogsf.7.4.1'].gvl_isosurf_set_att_const
    gvl_isosurf_set_att_const.restype = c_int
    gvl_isosurf_set_att_const.argtypes = [POINTER(geovol_isosurf), c_int, c_float]

# C:/msys64/usr/src/grass741/dist.x86_64-w64-mingw32/include/grass/defs/ogsf.h: 676
if hasattr(_libs['grass_ogsf.7.4.1'], 'gvl_isosurf_set_att_map'):
    gvl_isosurf_set_att_map = _libs['grass_ogsf.7.4.1'].gvl_isosurf_set_att_map
    gvl_isosurf_set_att_map.restype = c_int
    gvl_isosurf_set_att_map.argtypes = [POINTER(geovol_isosurf), c_int, String]

# C:/msys64/usr/src/grass741/dist.x86_64-w64-mingw32/include/grass/defs/ogsf.h: 677
if hasattr(_libs['grass_ogsf.7.4.1'], 'gvl_isosurf_set_att_changed'):
    gvl_isosurf_set_att_changed = _libs['grass_ogsf.7.4.1'].gvl_isosurf_set_att_changed
    gvl_isosurf_set_att_changed.restype = c_int
    gvl_isosurf_set_att_changed.argtypes = [POINTER(geovol_isosurf), c_int]

# C:/msys64/usr/src/grass741/dist.x86_64-w64-mingw32/include/grass/defs/ogsf.h: 679
if hasattr(_libs['grass_ogsf.7.4.1'], 'gvl_slice_init'):
    gvl_slice_init = _libs['grass_ogsf.7.4.1'].gvl_slice_init
    gvl_slice_init.restype = c_int
    gvl_slice_init.argtypes = [POINTER(geovol_slice)]

# C:/msys64/usr/src/grass741/dist.x86_64-w64-mingw32/include/grass/defs/ogsf.h: 680
if hasattr(_libs['grass_ogsf.7.4.1'], 'gvl_slice_get_slice'):
    gvl_slice_get_slice = _libs['grass_ogsf.7.4.1'].gvl_slice_get_slice
    gvl_slice_get_slice.restype = POINTER(geovol_slice)
    gvl_slice_get_slice.argtypes = [c_int, c_int]

# C:/msys64/usr/src/grass741/dist.x86_64-w64-mingw32/include/grass/defs/ogsf.h: 681
if hasattr(_libs['grass_ogsf.7.4.1'], 'gvl_slice_freemem'):
    gvl_slice_freemem = _libs['grass_ogsf.7.4.1'].gvl_slice_freemem
    gvl_slice_freemem.restype = c_int
    gvl_slice_freemem.argtypes = [POINTER(geovol_slice)]

# C:/msys64/usr/src/grass741/dist.x86_64-w64-mingw32/include/grass/defs/ogsf.h: 684
if hasattr(_libs['grass_ogsf.7.4.1'], 'P_scale'):
    P_scale = _libs['grass_ogsf.7.4.1'].P_scale
    P_scale.restype = None
    P_scale.argtypes = [c_float, c_float, c_float]

# C:/msys64/usr/src/grass741/dist.x86_64-w64-mingw32/include/grass/defs/ogsf.h: 685
if hasattr(_libs['grass_ogsf.7.4.1'], 'P_transform'):
    P_transform = _libs['grass_ogsf.7.4.1'].P_transform
    P_transform.restype = None
    P_transform.argtypes = [c_int, POINTER(c_float * 4), POINTER(c_float * 4)]

# C:/msys64/usr/src/grass741/dist.x86_64-w64-mingw32/include/grass/defs/ogsf.h: 686
if hasattr(_libs['grass_ogsf.7.4.1'], 'P_pushmatrix'):
    P_pushmatrix = _libs['grass_ogsf.7.4.1'].P_pushmatrix
    P_pushmatrix.restype = c_int
    P_pushmatrix.argtypes = []

# C:/msys64/usr/src/grass741/dist.x86_64-w64-mingw32/include/grass/defs/ogsf.h: 687
if hasattr(_libs['grass_ogsf.7.4.1'], 'P_popmatrix'):
    P_popmatrix = _libs['grass_ogsf.7.4.1'].P_popmatrix
    P_popmatrix.restype = c_int
    P_popmatrix.argtypes = []

# C:/msys64/usr/src/grass741/dist.x86_64-w64-mingw32/include/grass/defs/ogsf.h: 688
if hasattr(_libs['grass_ogsf.7.4.1'], 'P_rot'):
    P_rot = _libs['grass_ogsf.7.4.1'].P_rot
    P_rot.restype = None
    P_rot.argtypes = [c_float, c_char]

# C:/msys64/usr/src/grass741/dist.x86_64-w64-mingw32/include/grass/defs/ogsf.h: 691
if hasattr(_libs['grass_ogsf.7.4.1'], 'gvl_file_get_volfile'):
    gvl_file_get_volfile = _libs['grass_ogsf.7.4.1'].gvl_file_get_volfile
    gvl_file_get_volfile.restype = POINTER(geovol_file)
    gvl_file_get_volfile.argtypes = [c_int]

# C:/msys64/usr/src/grass741/dist.x86_64-w64-mingw32/include/grass/defs/ogsf.h: 692
if hasattr(_libs['grass_ogsf.7.4.1'], 'gvl_file_get_name'):
    gvl_file_get_name = _libs['grass_ogsf.7.4.1'].gvl_file_get_name
    gvl_file_get_name.restype = ReturnString
    gvl_file_get_name.argtypes = [c_int]

# C:/msys64/usr/src/grass741/dist.x86_64-w64-mingw32/include/grass/defs/ogsf.h: 693
if hasattr(_libs['grass_ogsf.7.4.1'], 'gvl_file_get_file_type'):
    gvl_file_get_file_type = _libs['grass_ogsf.7.4.1'].gvl_file_get_file_type
    gvl_file_get_file_type.restype = c_int
    gvl_file_get_file_type.argtypes = [POINTER(geovol_file)]

# C:/msys64/usr/src/grass741/dist.x86_64-w64-mingw32/include/grass/defs/ogsf.h: 694
if hasattr(_libs['grass_ogsf.7.4.1'], 'gvl_file_get_data_type'):
    gvl_file_get_data_type = _libs['grass_ogsf.7.4.1'].gvl_file_get_data_type
    gvl_file_get_data_type.restype = c_int
    gvl_file_get_data_type.argtypes = [POINTER(geovol_file)]

# C:/msys64/usr/src/grass741/dist.x86_64-w64-mingw32/include/grass/defs/ogsf.h: 695
if hasattr(_libs['grass_ogsf.7.4.1'], 'gvl_file_newh'):
    gvl_file_newh = _libs['grass_ogsf.7.4.1'].gvl_file_newh
    gvl_file_newh.restype = c_int
    gvl_file_newh.argtypes = [String, c_uint]

# C:/msys64/usr/src/grass741/dist.x86_64-w64-mingw32/include/grass/defs/ogsf.h: 696
if hasattr(_libs['grass_ogsf.7.4.1'], 'gvl_file_free_datah'):
    gvl_file_free_datah = _libs['grass_ogsf.7.4.1'].gvl_file_free_datah
    gvl_file_free_datah.restype = c_int
    gvl_file_free_datah.argtypes = [c_int]

# C:/msys64/usr/src/grass741/dist.x86_64-w64-mingw32/include/grass/defs/ogsf.h: 697
if hasattr(_libs['grass_ogsf.7.4.1'], 'gvl_file_start_read'):
    gvl_file_start_read = _libs['grass_ogsf.7.4.1'].gvl_file_start_read
    gvl_file_start_read.restype = c_int
    gvl_file_start_read.argtypes = [POINTER(geovol_file)]

# C:/msys64/usr/src/grass741/dist.x86_64-w64-mingw32/include/grass/defs/ogsf.h: 698
if hasattr(_libs['grass_ogsf.7.4.1'], 'gvl_file_end_read'):
    gvl_file_end_read = _libs['grass_ogsf.7.4.1'].gvl_file_end_read
    gvl_file_end_read.restype = c_int
    gvl_file_end_read.argtypes = [POINTER(geovol_file)]

# C:/msys64/usr/src/grass741/dist.x86_64-w64-mingw32/include/grass/defs/ogsf.h: 699
if hasattr(_libs['grass_ogsf.7.4.1'], 'gvl_file_get_value'):
    gvl_file_get_value = _libs['grass_ogsf.7.4.1'].gvl_file_get_value
    gvl_file_get_value.restype = c_int
    gvl_file_get_value.argtypes = [POINTER(geovol_file), c_int, c_int, c_int, POINTER(None)]

# C:/msys64/usr/src/grass741/dist.x86_64-w64-mingw32/include/grass/defs/ogsf.h: 700
if hasattr(_libs['grass_ogsf.7.4.1'], 'gvl_file_is_null_value'):
    gvl_file_is_null_value = _libs['grass_ogsf.7.4.1'].gvl_file_is_null_value
    gvl_file_is_null_value.restype = c_int
    gvl_file_is_null_value.argtypes = [POINTER(geovol_file), POINTER(None)]

# C:/msys64/usr/src/grass741/dist.x86_64-w64-mingw32/include/grass/defs/ogsf.h: 701
if hasattr(_libs['grass_ogsf.7.4.1'], 'gvl_file_set_mode'):
    gvl_file_set_mode = _libs['grass_ogsf.7.4.1'].gvl_file_set_mode
    gvl_file_set_mode.restype = c_int
    gvl_file_set_mode.argtypes = [POINTER(geovol_file), c_uint]

# C:/msys64/usr/src/grass741/dist.x86_64-w64-mingw32/include/grass/defs/ogsf.h: 702
if hasattr(_libs['grass_ogsf.7.4.1'], 'gvl_file_set_slices_param'):
    gvl_file_set_slices_param = _libs['grass_ogsf.7.4.1'].gvl_file_set_slices_param
    gvl_file_set_slices_param.restype = c_int
    gvl_file_set_slices_param.argtypes = [POINTER(geovol_file), c_int, c_int]

# C:/msys64/usr/src/grass741/dist.x86_64-w64-mingw32/include/grass/defs/ogsf.h: 703
if hasattr(_libs['grass_ogsf.7.4.1'], 'gvl_file_get_min_max'):
    gvl_file_get_min_max = _libs['grass_ogsf.7.4.1'].gvl_file_get_min_max
    gvl_file_get_min_max.restype = None
    gvl_file_get_min_max.argtypes = [POINTER(geovol_file), POINTER(c_double), POINTER(c_double)]

# C:/msys64/usr/src/grass741/dist.x86_64-w64-mingw32/include/grass/defs/ogsf.h: 706
if hasattr(_libs['grass_ogsf.7.4.1'], 'Gvl_load_colors_data'):
    Gvl_load_colors_data = _libs['grass_ogsf.7.4.1'].Gvl_load_colors_data
    Gvl_load_colors_data.restype = c_int
    Gvl_load_colors_data.argtypes = [POINTER(POINTER(None)), String]

# C:/msys64/usr/src/grass741/dist.x86_64-w64-mingw32/include/grass/defs/ogsf.h: 707
if hasattr(_libs['grass_ogsf.7.4.1'], 'Gvl_unload_colors_data'):
    Gvl_unload_colors_data = _libs['grass_ogsf.7.4.1'].Gvl_unload_colors_data
    Gvl_unload_colors_data.restype = c_int
    Gvl_unload_colors_data.argtypes = [POINTER(None)]

# C:/msys64/usr/src/grass741/dist.x86_64-w64-mingw32/include/grass/defs/ogsf.h: 708
if hasattr(_libs['grass_ogsf.7.4.1'], 'Gvl_get_color_for_value'):
    Gvl_get_color_for_value = _libs['grass_ogsf.7.4.1'].Gvl_get_color_for_value
    Gvl_get_color_for_value.restype = c_int
    Gvl_get_color_for_value.argtypes = [POINTER(None), POINTER(c_float)]

# C:/msys64/usr/src/grass741/dist.x86_64-w64-mingw32/include/grass/defs/ogsf.h: 711
if hasattr(_libs['grass_ogsf.7.4.1'], 'gvl_isosurf_calc'):
    gvl_isosurf_calc = _libs['grass_ogsf.7.4.1'].gvl_isosurf_calc
    gvl_isosurf_calc.restype = c_int
    gvl_isosurf_calc.argtypes = [POINTER(geovol)]

# C:/msys64/usr/src/grass741/dist.x86_64-w64-mingw32/include/grass/defs/ogsf.h: 712
if hasattr(_libs['grass_ogsf.7.4.1'], 'gvl_slices_calc'):
    gvl_slices_calc = _libs['grass_ogsf.7.4.1'].gvl_slices_calc
    gvl_slices_calc.restype = c_int
    gvl_slices_calc.argtypes = [POINTER(geovol)]

# C:/msys64/usr/src/grass741/dist.x86_64-w64-mingw32/include/grass/defs/ogsf.h: 713
if hasattr(_libs['grass_ogsf.7.4.1'], 'gvl_write_char'):
    gvl_write_char = _libs['grass_ogsf.7.4.1'].gvl_write_char
    gvl_write_char.restype = None
    gvl_write_char.argtypes = [c_int, POINTER(POINTER(c_ubyte)), c_ubyte]

# C:/msys64/usr/src/grass741/dist.x86_64-w64-mingw32/include/grass/defs/ogsf.h: 714
if hasattr(_libs['grass_ogsf.7.4.1'], 'gvl_read_char'):
    gvl_read_char = _libs['grass_ogsf.7.4.1'].gvl_read_char
    gvl_read_char.restype = c_ubyte
    gvl_read_char.argtypes = [c_int, POINTER(c_ubyte)]

# C:/msys64/usr/src/grass741/dist.x86_64-w64-mingw32/include/grass/defs/ogsf.h: 715
if hasattr(_libs['grass_ogsf.7.4.1'], 'gvl_align_data'):
    gvl_align_data = _libs['grass_ogsf.7.4.1'].gvl_align_data
    gvl_align_data.restype = None
    gvl_align_data.argtypes = [c_int, POINTER(POINTER(c_ubyte))]

# C:/msys64/usr/src/grass741/dist.x86_64-w64-mingw32/include/grass/defs/ogsf.h: 718
if hasattr(_libs['grass_ogsf.7.4.1'], 'gvld_vol'):
    gvld_vol = _libs['grass_ogsf.7.4.1'].gvld_vol
    gvld_vol.restype = c_int
    gvld_vol.argtypes = [POINTER(geovol)]

# C:/msys64/usr/src/grass741/dist.x86_64-w64-mingw32/include/grass/defs/ogsf.h: 719
if hasattr(_libs['grass_ogsf.7.4.1'], 'gvld_wire_vol'):
    gvld_wire_vol = _libs['grass_ogsf.7.4.1'].gvld_wire_vol
    gvld_wire_vol.restype = c_int
    gvld_wire_vol.argtypes = [POINTER(geovol)]

# C:/msys64/usr/src/grass741/dist.x86_64-w64-mingw32/include/grass/defs/ogsf.h: 720
if hasattr(_libs['grass_ogsf.7.4.1'], 'gvld_isosurf'):
    gvld_isosurf = _libs['grass_ogsf.7.4.1'].gvld_isosurf
    gvld_isosurf.restype = c_int
    gvld_isosurf.argtypes = [POINTER(geovol)]

# C:/msys64/usr/src/grass741/dist.x86_64-w64-mingw32/include/grass/defs/ogsf.h: 721
if hasattr(_libs['grass_ogsf.7.4.1'], 'gvld_wire_isosurf'):
    gvld_wire_isosurf = _libs['grass_ogsf.7.4.1'].gvld_wire_isosurf
    gvld_wire_isosurf.restype = c_int
    gvld_wire_isosurf.argtypes = [POINTER(geovol)]

# C:/msys64/usr/src/grass741/dist.x86_64-w64-mingw32/include/grass/defs/ogsf.h: 722
if hasattr(_libs['grass_ogsf.7.4.1'], 'gvld_slices'):
    gvld_slices = _libs['grass_ogsf.7.4.1'].gvld_slices
    gvld_slices.restype = c_int
    gvld_slices.argtypes = [POINTER(geovol)]

# C:/msys64/usr/src/grass741/dist.x86_64-w64-mingw32/include/grass/defs/ogsf.h: 723
if hasattr(_libs['grass_ogsf.7.4.1'], 'gvld_slice'):
    gvld_slice = _libs['grass_ogsf.7.4.1'].gvld_slice
    gvld_slice.restype = c_int
    gvld_slice.argtypes = [POINTER(geovol), c_int]

# C:/msys64/usr/src/grass741/dist.x86_64-w64-mingw32/include/grass/defs/ogsf.h: 724
if hasattr(_libs['grass_ogsf.7.4.1'], 'gvld_wire_slices'):
    gvld_wire_slices = _libs['grass_ogsf.7.4.1'].gvld_wire_slices
    gvld_wire_slices.restype = c_int
    gvld_wire_slices.argtypes = [POINTER(geovol)]

# C:/msys64/usr/src/grass741/dist.x86_64-w64-mingw32/include/grass/defs/ogsf.h: 725
if hasattr(_libs['grass_ogsf.7.4.1'], 'gvld_wind3_box'):
    gvld_wind3_box = _libs['grass_ogsf.7.4.1'].gvld_wind3_box
    gvld_wind3_box.restype = c_int
    gvld_wind3_box.argtypes = [POINTER(geovol)]

# C:/msys64/usr/src/grass741/dist.x86_64-w64-mingw32/include/grass/defs/ogsf.h: 728
if hasattr(_libs['grass_ogsf.7.4.1'], 'gsd_display_fringe'):
    gsd_display_fringe = _libs['grass_ogsf.7.4.1'].gsd_display_fringe
    gsd_display_fringe.restype = None
    gsd_display_fringe.argtypes = [POINTER(geosurf), c_ulong, c_float, c_int * 4]

# C:/msys64/usr/src/grass741/dist.x86_64-w64-mingw32/include/grass/defs/ogsf.h: 729
if hasattr(_libs['grass_ogsf.7.4.1'], 'gsd_fringe_horiz_poly'):
    gsd_fringe_horiz_poly = _libs['grass_ogsf.7.4.1'].gsd_fringe_horiz_poly
    gsd_fringe_horiz_poly.restype = None
    gsd_fringe_horiz_poly.argtypes = [c_float, POINTER(geosurf), c_int, c_int]

# C:/msys64/usr/src/grass741/dist.x86_64-w64-mingw32/include/grass/defs/ogsf.h: 730
if hasattr(_libs['grass_ogsf.7.4.1'], 'gsd_fringe_horiz_line'):
    gsd_fringe_horiz_line = _libs['grass_ogsf.7.4.1'].gsd_fringe_horiz_line
    gsd_fringe_horiz_line.restype = None
    gsd_fringe_horiz_line.argtypes = [c_float, POINTER(geosurf), c_int, c_int]

# C:/msys64/usr/src/grass741/dist.x86_64-w64-mingw32/include/grass/defs/ogsf.h: 731
if hasattr(_libs['grass_ogsf.7.4.1'], 'gsd_fringe_vert_poly'):
    gsd_fringe_vert_poly = _libs['grass_ogsf.7.4.1'].gsd_fringe_vert_poly
    gsd_fringe_vert_poly.restype = None
    gsd_fringe_vert_poly.argtypes = [c_float, POINTER(geosurf), c_int, c_int]

# C:/msys64/usr/src/grass741/dist.x86_64-w64-mingw32/include/grass/defs/ogsf.h: 732
if hasattr(_libs['grass_ogsf.7.4.1'], 'gsd_fringe_vert_line'):
    gsd_fringe_vert_line = _libs['grass_ogsf.7.4.1'].gsd_fringe_vert_line
    gsd_fringe_vert_line.restype = None
    gsd_fringe_vert_line.argtypes = [c_float, POINTER(geosurf), c_int, c_int]

# C:/msys64/usr/src/grass741/dist.x86_64-w64-mingw32/include/grass/defs/ogsf.h: 735
if hasattr(_libs['grass_ogsf.7.4.1'], 'gsd_put_legend'):
    gsd_put_legend = _libs['grass_ogsf.7.4.1'].gsd_put_legend
    gsd_put_legend.restype = GLuint
    gsd_put_legend.argtypes = [String, GLuint, c_int, POINTER(c_int), POINTER(c_float), POINTER(c_int)]

# C:/msys64/usr/src/grass741/dist.x86_64-w64-mingw32/include/grass/defs/ogsf.h: 736
if hasattr(_libs['grass_ogsf.7.4.1'], 'gsd_bgn_legend_viewport'):
    gsd_bgn_legend_viewport = _libs['grass_ogsf.7.4.1'].gsd_bgn_legend_viewport
    gsd_bgn_legend_viewport.restype = None
    gsd_bgn_legend_viewport.argtypes = [GLint, GLint, GLint, GLint]

# C:/msys64/usr/src/grass741/dist.x86_64-w64-mingw32/include/grass/defs/ogsf.h: 737
if hasattr(_libs['grass_ogsf.7.4.1'], 'gsd_end_legend_viewport'):
    gsd_end_legend_viewport = _libs['grass_ogsf.7.4.1'].gsd_end_legend_viewport
    gsd_end_legend_viewport.restype = None
    gsd_end_legend_viewport.argtypes = []

# C:/msys64/usr/src/grass741/dist.x86_64-w64-mingw32/include/grass/defs/ogsf.h: 738
if hasattr(_libs['grass_ogsf.7.4.1'], 'gsd_make_nice_number'):
    gsd_make_nice_number = _libs['grass_ogsf.7.4.1'].gsd_make_nice_number
    gsd_make_nice_number.restype = c_int
    gsd_make_nice_number.argtypes = [POINTER(c_float)]

# C:\\msys64\\usr\\src\\grass741\\dist.x86_64-w64-mingw32\\include\\grass\\ogsf.h: 30
try:
    GS_UNIT_SIZE = 1000.0
except:
    pass

# C:\\msys64\\usr\\src\\grass741\\dist.x86_64-w64-mingw32\\include\\grass\\ogsf.h: 31
def BETWEEN(x, a, b):
    return (((x > a) and (x < b)) or ((x > b) and (x < a)))

# C:\\msys64\\usr\\src\\grass741\\dist.x86_64-w64-mingw32\\include\\grass\\ogsf.h: 35
try:
    MAX_SURFS = 12
except:
    pass

# C:\\msys64\\usr\\src\\grass741\\dist.x86_64-w64-mingw32\\include\\grass\\ogsf.h: 35
try:
    MAX_VECTS = 50
except:
    pass

# C:\\msys64\\usr\\src\\grass741\\dist.x86_64-w64-mingw32\\include\\grass\\ogsf.h: 35
try:
    MAX_SITES = 50
except:
    pass

# C:\\msys64\\usr\\src\\grass741\\dist.x86_64-w64-mingw32\\include\\grass\\ogsf.h: 35
try:
    MAX_VOLS = 12
except:
    pass

# C:\\msys64\\usr\\src\\grass741\\dist.x86_64-w64-mingw32\\include\\grass\\ogsf.h: 35
try:
    MAX_DSP = 12
except:
    pass

# C:\\msys64\\usr\\src\\grass741\\dist.x86_64-w64-mingw32\\include\\grass\\ogsf.h: 35
try:
    MAX_ATTS = 7
except:
    pass

# C:\\msys64\\usr\\src\\grass741\\dist.x86_64-w64-mingw32\\include\\grass\\ogsf.h: 35
try:
    MAX_LIGHTS = 3
except:
    pass

# C:\\msys64\\usr\\src\\grass741\\dist.x86_64-w64-mingw32\\include\\grass\\ogsf.h: 35
try:
    MAX_CPLANES = 6
except:
    pass

# C:\\msys64\\usr\\src\\grass741\\dist.x86_64-w64-mingw32\\include\\grass\\ogsf.h: 35
try:
    MAX_ISOSURFS = 12
except:
    pass

# C:\\msys64\\usr\\src\\grass741\\dist.x86_64-w64-mingw32\\include\\grass\\ogsf.h: 35
try:
    MAX_SLICES = 12
except:
    pass

# C:\\msys64\\usr\\src\\grass741\\dist.x86_64-w64-mingw32\\include\\grass\\ogsf.h: 37
try:
    MAX_VOL_SLICES = 4
except:
    pass

# C:\\msys64\\usr\\src\\grass741\\dist.x86_64-w64-mingw32\\include\\grass\\ogsf.h: 37
try:
    MAX_VOL_FILES = 100
except:
    pass

# C:\\msys64\\usr\\src\\grass741\\dist.x86_64-w64-mingw32\\include\\grass\\ogsf.h: 39
try:
    DM_GOURAUD = 256
except:
    pass

# C:\\msys64\\usr\\src\\grass741\\dist.x86_64-w64-mingw32\\include\\grass\\ogsf.h: 39
try:
    DM_FLAT = 512
except:
    pass

# C:\\msys64\\usr\\src\\grass741\\dist.x86_64-w64-mingw32\\include\\grass\\ogsf.h: 40
try:
    DM_FRINGE = 16
except:
    pass

# C:\\msys64\\usr\\src\\grass741\\dist.x86_64-w64-mingw32\\include\\grass\\ogsf.h: 41
try:
    DM_WIRE = 1
except:
    pass

# C:\\msys64\\usr\\src\\grass741\\dist.x86_64-w64-mingw32\\include\\grass\\ogsf.h: 41
try:
    DM_COL_WIRE = 2
except:
    pass

# C:\\msys64\\usr\\src\\grass741\\dist.x86_64-w64-mingw32\\include\\grass\\ogsf.h: 41
try:
    DM_POLY = 4
except:
    pass

# C:\\msys64\\usr\\src\\grass741\\dist.x86_64-w64-mingw32\\include\\grass\\ogsf.h: 41
try:
    DM_WIRE_POLY = 8
except:
    pass

# C:\\msys64\\usr\\src\\grass741\\dist.x86_64-w64-mingw32\\include\\grass\\ogsf.h: 42
try:
    DM_GRID_WIRE = 1024
except:
    pass

# C:\\msys64\\usr\\src\\grass741\\dist.x86_64-w64-mingw32\\include\\grass\\ogsf.h: 42
try:
    DM_GRID_SURF = 2048
except:
    pass

# C:\\msys64\\usr\\src\\grass741\\dist.x86_64-w64-mingw32\\include\\grass\\ogsf.h: 43
try:
    WC_COLOR_ATT = 4278190080L
except:
    pass

IFLAG = c_uint # C:\\msys64\\usr\\src\\grass741\\dist.x86_64-w64-mingw32\\include\\grass\\ogsf.h: 44

# C:\\msys64\\usr\\src\\grass741\\dist.x86_64-w64-mingw32\\include\\grass\\ogsf.h: 46
try:
    ATT_NORM = 0
except:
    pass

# C:\\msys64\\usr\\src\\grass741\\dist.x86_64-w64-mingw32\\include\\grass\\ogsf.h: 46
try:
    ATT_TOPO = 1
except:
    pass

# C:\\msys64\\usr\\src\\grass741\\dist.x86_64-w64-mingw32\\include\\grass\\ogsf.h: 46
try:
    ATT_COLOR = 2
except:
    pass

# C:\\msys64\\usr\\src\\grass741\\dist.x86_64-w64-mingw32\\include\\grass\\ogsf.h: 46
try:
    ATT_MASK = 3
except:
    pass

# C:\\msys64\\usr\\src\\grass741\\dist.x86_64-w64-mingw32\\include\\grass\\ogsf.h: 46
try:
    ATT_TRANSP = 4
except:
    pass

# C:\\msys64\\usr\\src\\grass741\\dist.x86_64-w64-mingw32\\include\\grass\\ogsf.h: 46
try:
    ATT_SHINE = 5
except:
    pass

# C:\\msys64\\usr\\src\\grass741\\dist.x86_64-w64-mingw32\\include\\grass\\ogsf.h: 46
try:
    ATT_EMIT = 6
except:
    pass

# C:\\msys64\\usr\\src\\grass741\\dist.x86_64-w64-mingw32\\include\\grass\\ogsf.h: 46
def LEGAL_ATT(a):
    return ((a >= 0) and (a < MAX_ATTS))

# C:\\msys64\\usr\\src\\grass741\\dist.x86_64-w64-mingw32\\include\\grass\\ogsf.h: 48
try:
    NOTSET_ATT = 0
except:
    pass

# C:\\msys64\\usr\\src\\grass741\\dist.x86_64-w64-mingw32\\include\\grass\\ogsf.h: 48
try:
    MAP_ATT = 1
except:
    pass

# C:\\msys64\\usr\\src\\grass741\\dist.x86_64-w64-mingw32\\include\\grass\\ogsf.h: 48
try:
    CONST_ATT = 2
except:
    pass

# C:\\msys64\\usr\\src\\grass741\\dist.x86_64-w64-mingw32\\include\\grass\\ogsf.h: 48
try:
    FUNC_ATT = 3
except:
    pass

# C:\\msys64\\usr\\src\\grass741\\dist.x86_64-w64-mingw32\\include\\grass\\ogsf.h: 48
def LEGAL_SRC(s):
    return ((((s == NOTSET_ATT) or (s == MAP_ATT)) or (s == CONST_ATT)) or (s == FUNC_ATT))

# C:\\msys64\\usr\\src\\grass741\\dist.x86_64-w64-mingw32\\include\\grass\\ogsf.h: 50
try:
    ST_X = 1
except:
    pass

# C:\\msys64\\usr\\src\\grass741\\dist.x86_64-w64-mingw32\\include\\grass\\ogsf.h: 50
try:
    ST_BOX = 2
except:
    pass

# C:\\msys64\\usr\\src\\grass741\\dist.x86_64-w64-mingw32\\include\\grass\\ogsf.h: 50
try:
    ST_SPHERE = 3
except:
    pass

# C:\\msys64\\usr\\src\\grass741\\dist.x86_64-w64-mingw32\\include\\grass\\ogsf.h: 50
try:
    ST_CUBE = 4
except:
    pass

# C:\\msys64\\usr\\src\\grass741\\dist.x86_64-w64-mingw32\\include\\grass\\ogsf.h: 50
try:
    ST_DIAMOND = 5
except:
    pass

# C:\\msys64\\usr\\src\\grass741\\dist.x86_64-w64-mingw32\\include\\grass\\ogsf.h: 50
try:
    ST_DEC_TREE = 6
except:
    pass

# C:\\msys64\\usr\\src\\grass741\\dist.x86_64-w64-mingw32\\include\\grass\\ogsf.h: 50
try:
    ST_CON_TREE = 7
except:
    pass

# C:\\msys64\\usr\\src\\grass741\\dist.x86_64-w64-mingw32\\include\\grass\\ogsf.h: 50
try:
    ST_ASTER = 8
except:
    pass

# C:\\msys64\\usr\\src\\grass741\\dist.x86_64-w64-mingw32\\include\\grass\\ogsf.h: 50
try:
    ST_GYRO = 9
except:
    pass

# C:\\msys64\\usr\\src\\grass741\\dist.x86_64-w64-mingw32\\include\\grass\\ogsf.h: 50
try:
    ST_HISTOGRAM = 10
except:
    pass

# C:\\msys64\\usr\\src\\grass741\\dist.x86_64-w64-mingw32\\include\\grass\\ogsf.h: 52
try:
    GSD_FRONT = 1
except:
    pass

# C:\\msys64\\usr\\src\\grass741\\dist.x86_64-w64-mingw32\\include\\grass\\ogsf.h: 52
try:
    GSD_BACK = 2
except:
    pass

# C:\\msys64\\usr\\src\\grass741\\dist.x86_64-w64-mingw32\\include\\grass\\ogsf.h: 52
try:
    GSD_BOTH = 3
except:
    pass

# C:\\msys64\\usr\\src\\grass741\\dist.x86_64-w64-mingw32\\include\\grass\\ogsf.h: 54
try:
    FC_OFF = 0
except:
    pass

# C:\\msys64\\usr\\src\\grass741\\dist.x86_64-w64-mingw32\\include\\grass\\ogsf.h: 54
try:
    FC_ABOVE = 1
except:
    pass

# C:\\msys64\\usr\\src\\grass741\\dist.x86_64-w64-mingw32\\include\\grass\\ogsf.h: 54
try:
    FC_BELOW = 2
except:
    pass

# C:\\msys64\\usr\\src\\grass741\\dist.x86_64-w64-mingw32\\include\\grass\\ogsf.h: 54
try:
    FC_BLEND = 3
except:
    pass

# C:\\msys64\\usr\\src\\grass741\\dist.x86_64-w64-mingw32\\include\\grass\\ogsf.h: 54
try:
    FC_GREY = 4
except:
    pass

# C:\\msys64\\usr\\src\\grass741\\dist.x86_64-w64-mingw32\\include\\grass\\ogsf.h: 56
try:
    LT_DISCRETE = 256
except:
    pass

# C:\\msys64\\usr\\src\\grass741\\dist.x86_64-w64-mingw32\\include\\grass\\ogsf.h: 56
try:
    LT_CONTINUOUS = 512
except:
    pass

# C:\\msys64\\usr\\src\\grass741\\dist.x86_64-w64-mingw32\\include\\grass\\ogsf.h: 57
try:
    LT_LIST = 16
except:
    pass

# C:\\msys64\\usr\\src\\grass741\\dist.x86_64-w64-mingw32\\include\\grass\\ogsf.h: 59
try:
    LT_RANGE_LOWSET = 1
except:
    pass

# C:\\msys64\\usr\\src\\grass741\\dist.x86_64-w64-mingw32\\include\\grass\\ogsf.h: 59
try:
    LT_RANGE_HISET = 2
except:
    pass

# C:\\msys64\\usr\\src\\grass741\\dist.x86_64-w64-mingw32\\include\\grass\\ogsf.h: 59
try:
    LT_RANGE_LOW_HI = 3
except:
    pass

# C:\\msys64\\usr\\src\\grass741\\dist.x86_64-w64-mingw32\\include\\grass\\ogsf.h: 59
try:
    LT_INVERTED = 8
except:
    pass

# C:\\msys64\\usr\\src\\grass741\\dist.x86_64-w64-mingw32\\include\\grass\\ogsf.h: 60
try:
    LT_SHOW_VALS = 4096
except:
    pass

# C:\\msys64\\usr\\src\\grass741\\dist.x86_64-w64-mingw32\\include\\grass\\ogsf.h: 60
try:
    LT_SHOW_LABELS = 8192
except:
    pass

# C:\\msys64\\usr\\src\\grass741\\dist.x86_64-w64-mingw32\\include\\grass\\ogsf.h: 62
try:
    VOL_FTYPE_RASTER3D = 0
except:
    pass

# C:\\msys64\\usr\\src\\grass741\\dist.x86_64-w64-mingw32\\include\\grass\\ogsf.h: 64
try:
    VOL_DTYPE_FLOAT = 0
except:
    pass

# C:\\msys64\\usr\\src\\grass741\\dist.x86_64-w64-mingw32\\include\\grass\\ogsf.h: 64
try:
    VOL_DTYPE_DOUBLE = 1
except:
    pass

# C:\\msys64\\usr\\src\\grass741\\dist.x86_64-w64-mingw32\\include\\grass\\ogsf.h: 68
try:
    X = 0
except:
    pass

# C:\\msys64\\usr\\src\\grass741\\dist.x86_64-w64-mingw32\\include\\grass\\ogsf.h: 68
try:
    Y = 1
except:
    pass

# C:\\msys64\\usr\\src\\grass741\\dist.x86_64-w64-mingw32\\include\\grass\\ogsf.h: 68
try:
    Z = 2
except:
    pass

# C:\\msys64\\usr\\src\\grass741\\dist.x86_64-w64-mingw32\\include\\grass\\ogsf.h: 68
try:
    W = 3
except:
    pass

# C:\\msys64\\usr\\src\\grass741\\dist.x86_64-w64-mingw32\\include\\grass\\ogsf.h: 68
try:
    FROM = 0
except:
    pass

# C:\\msys64\\usr\\src\\grass741\\dist.x86_64-w64-mingw32\\include\\grass\\ogsf.h: 68
try:
    TO = 1
except:
    pass

# C:\\msys64\\usr\\src\\grass741\\dist.x86_64-w64-mingw32\\include\\grass\\ogsf.h: 70
try:
    CM_COLOR = 0
except:
    pass

# C:\\msys64\\usr\\src\\grass741\\dist.x86_64-w64-mingw32\\include\\grass\\ogsf.h: 70
try:
    CM_EMISSION = 1
except:
    pass

# C:\\msys64\\usr\\src\\grass741\\dist.x86_64-w64-mingw32\\include\\grass\\ogsf.h: 70
try:
    CM_AMBIENT = 2
except:
    pass

# C:\\msys64\\usr\\src\\grass741\\dist.x86_64-w64-mingw32\\include\\grass\\ogsf.h: 70
try:
    CM_DIFFUSE = 3
except:
    pass

# C:\\msys64\\usr\\src\\grass741\\dist.x86_64-w64-mingw32\\include\\grass\\ogsf.h: 70
try:
    CM_SPECULAR = 4
except:
    pass

# C:\\msys64\\usr\\src\\grass741\\dist.x86_64-w64-mingw32\\include\\grass\\ogsf.h: 70
try:
    CM_AD = 5
except:
    pass

# C:\\msys64\\usr\\src\\grass741\\dist.x86_64-w64-mingw32\\include\\grass\\ogsf.h: 70
try:
    CM_NULL = 6
except:
    pass

# C:\\msys64\\usr\\src\\grass741\\dist.x86_64-w64-mingw32\\include\\grass\\ogsf.h: 71
try:
    CM_WIRE = CM_COLOR
except:
    pass

# C:\\msys64\\usr\\src\\grass741\\dist.x86_64-w64-mingw32\\include\\grass\\ogsf.h: 72
try:
    NULL_COLOR = 16777215
except:
    pass

GS_CHAR8 = c_char # C:\\msys64\\usr\\src\\grass741\\dist.x86_64-w64-mingw32\\include\\grass\\ogsf.h: 74

GS_SHORT16 = c_short # C:\\msys64\\usr\\src\\grass741\\dist.x86_64-w64-mingw32\\include\\grass\\ogsf.h: 74

GS_INT32 = c_int # C:\\msys64\\usr\\src\\grass741\\dist.x86_64-w64-mingw32\\include\\grass\\ogsf.h: 74

# C:\\msys64\\usr\\src\\grass741\\dist.x86_64-w64-mingw32\\include\\grass\\ogsf.h: 76
try:
    ATTY_NULL = 32
except:
    pass

# C:\\msys64\\usr\\src\\grass741\\dist.x86_64-w64-mingw32\\include\\grass\\ogsf.h: 76
try:
    ATTY_MASK = 16
except:
    pass

# C:\\msys64\\usr\\src\\grass741\\dist.x86_64-w64-mingw32\\include\\grass\\ogsf.h: 76
try:
    ATTY_FLOAT = 8
except:
    pass

# C:\\msys64\\usr\\src\\grass741\\dist.x86_64-w64-mingw32\\include\\grass\\ogsf.h: 76
try:
    ATTY_INT = 4
except:
    pass

# C:\\msys64\\usr\\src\\grass741\\dist.x86_64-w64-mingw32\\include\\grass\\ogsf.h: 76
try:
    ATTY_SHORT = 2
except:
    pass

# C:\\msys64\\usr\\src\\grass741\\dist.x86_64-w64-mingw32\\include\\grass\\ogsf.h: 76
try:
    ATTY_CHAR = 1
except:
    pass

# C:\\msys64\\usr\\src\\grass741\\dist.x86_64-w64-mingw32\\include\\grass\\ogsf.h: 76
try:
    ATTY_ANY = 63
except:
    pass

# C:\\msys64\\usr\\src\\grass741\\dist.x86_64-w64-mingw32\\include\\grass\\ogsf.h: 76
def LEGAL_TYPE(t):
    return (((((t == ATTY_MASK) or (t == ATTY_FLOAT)) or (t == ATTY_INT)) or (t == ATTY_SHORT)) or (t == ATTY_CHAR))

# C:\\msys64\\usr\\src\\grass741\\dist.x86_64-w64-mingw32\\include\\grass\\ogsf.h: 78
try:
    MAXDIMS = 4
except:
    pass

# C:\\msys64\\usr\\src\\grass741\\dist.x86_64-w64-mingw32\\include\\grass\\ogsf.h: 79
def FUDGE(gs):
    return ((((gs.contents.zmax_nz).value) - ((gs.contents.zmin_nz).value)) / 500.0)

# C:\\msys64\\usr\\src\\grass741\\dist.x86_64-w64-mingw32\\include\\grass\\ogsf.h: 79
def DOT3(a, b):
    return ((((a [X]) * (b [X])) + ((a [Y]) * (b [Y]))) + ((a [Z]) * (b [Z])))

# C:\\msys64\\usr\\src\\grass741\\dist.x86_64-w64-mingw32\\include\\grass\\ogsf.h: 81
try:
    CF_NOT_CHANGED = 0
except:
    pass

# C:\\msys64\\usr\\src\\grass741\\dist.x86_64-w64-mingw32\\include\\grass\\ogsf.h: 81
try:
    CF_COLOR_PACKED = 1
except:
    pass

# C:\\msys64\\usr\\src\\grass741\\dist.x86_64-w64-mingw32\\include\\grass\\ogsf.h: 81
try:
    CF_USR_CHANGED = 16
except:
    pass

# C:\\msys64\\usr\\src\\grass741\\dist.x86_64-w64-mingw32\\include\\grass\\ogsf.h: 81
try:
    CF_CHARSCALED = 256
except:
    pass

# C:\\msys64\\usr\\src\\grass741\\dist.x86_64-w64-mingw32\\include\\grass\\ogsf.h: 82
try:
    MAX_TF = 6
except:
    pass

# C:\\msys64\\usr\\src\\grass741\\dist.x86_64-w64-mingw32\\include\\grass\\ogsf.h: 83
try:
    MASK_TL = 268435456
except:
    pass

# C:\\msys64\\usr\\src\\grass741\\dist.x86_64-w64-mingw32\\include\\grass\\ogsf.h: 83
try:
    MASK_TR = 16777216
except:
    pass

# C:\\msys64\\usr\\src\\grass741\\dist.x86_64-w64-mingw32\\include\\grass\\ogsf.h: 83
try:
    MASK_BR = 1048576
except:
    pass

# C:\\msys64\\usr\\src\\grass741\\dist.x86_64-w64-mingw32\\include\\grass\\ogsf.h: 83
try:
    MASK_BL = 65536
except:
    pass

# C:\\msys64\\usr\\src\\grass741\\dist.x86_64-w64-mingw32\\include\\grass\\ogsf.h: 83
try:
    MASK_NPTS = 7
except:
    pass

# C:\\msys64\\usr\\src\\grass741\\dist.x86_64-w64-mingw32\\include\\grass\\ogsf.h: 84
try:
    OGSF_POINT = 1
except:
    pass

# C:\\msys64\\usr\\src\\grass741\\dist.x86_64-w64-mingw32\\include\\grass\\ogsf.h: 84
try:
    OGSF_LINE = 2
except:
    pass

# C:\\msys64\\usr\\src\\grass741\\dist.x86_64-w64-mingw32\\include\\grass\\ogsf.h: 84
try:
    OGSF_POLYGON = 3
except:
    pass

# C:\\msys64\\usr\\src\\grass741\\dist.x86_64-w64-mingw32\\include\\grass\\ogsf.h: 85
try:
    RED_MASK = 255
except:
    pass

# C:\\msys64\\usr\\src\\grass741\\dist.x86_64-w64-mingw32\\include\\grass\\ogsf.h: 85
try:
    GRN_MASK = 65280
except:
    pass

# C:\\msys64\\usr\\src\\grass741\\dist.x86_64-w64-mingw32\\include\\grass\\ogsf.h: 85
try:
    BLU_MASK = 16711680
except:
    pass

# C:\\msys64\\usr\\src\\grass741\\dist.x86_64-w64-mingw32\\include\\grass\\ogsf.h: 390
try:
    KF_FROMX_MASK = 1
except:
    pass

# C:\\msys64\\usr\\src\\grass741\\dist.x86_64-w64-mingw32\\include\\grass\\ogsf.h: 390
try:
    KF_FROMY_MASK = 2
except:
    pass

# C:\\msys64\\usr\\src\\grass741\\dist.x86_64-w64-mingw32\\include\\grass\\ogsf.h: 390
try:
    KF_FROMZ_MASK = 4
except:
    pass

# C:\\msys64\\usr\\src\\grass741\\dist.x86_64-w64-mingw32\\include\\grass\\ogsf.h: 390
try:
    KF_FROM_MASK = 7
except:
    pass

# C:\\msys64\\usr\\src\\grass741\\dist.x86_64-w64-mingw32\\include\\grass\\ogsf.h: 391
try:
    KF_DIRX_MASK = 8
except:
    pass

# C:\\msys64\\usr\\src\\grass741\\dist.x86_64-w64-mingw32\\include\\grass\\ogsf.h: 391
try:
    KF_DIRY_MASK = 16
except:
    pass

# C:\\msys64\\usr\\src\\grass741\\dist.x86_64-w64-mingw32\\include\\grass\\ogsf.h: 391
try:
    KF_DIRZ_MASK = 32
except:
    pass

# C:\\msys64\\usr\\src\\grass741\\dist.x86_64-w64-mingw32\\include\\grass\\ogsf.h: 391
try:
    KF_DIR_MASK = 56
except:
    pass

# C:\\msys64\\usr\\src\\grass741\\dist.x86_64-w64-mingw32\\include\\grass\\ogsf.h: 392
try:
    KF_FOV_MASK = 64
except:
    pass

# C:\\msys64\\usr\\src\\grass741\\dist.x86_64-w64-mingw32\\include\\grass\\ogsf.h: 392
try:
    KF_TWIST_MASK = 128
except:
    pass

# C:\\msys64\\usr\\src\\grass741\\dist.x86_64-w64-mingw32\\include\\grass\\ogsf.h: 393
try:
    KF_ALL_MASK = 255
except:
    pass

# C:\\msys64\\usr\\src\\grass741\\dist.x86_64-w64-mingw32\\include\\grass\\ogsf.h: 394
try:
    KF_NUMFIELDS = 8
except:
    pass

# C:\\msys64\\usr\\src\\grass741\\dist.x86_64-w64-mingw32\\include\\grass\\ogsf.h: 395
try:
    KF_LINEAR = 111
except:
    pass

# C:\\msys64\\usr\\src\\grass741\\dist.x86_64-w64-mingw32\\include\\grass\\ogsf.h: 395
try:
    KF_SPLINE = 222
except:
    pass

# C:\\msys64\\usr\\src\\grass741\\dist.x86_64-w64-mingw32\\include\\grass\\ogsf.h: 395
def KF_LEGAL_MODE(m):
    return ((m == KF_LINEAR) or (m == KF_SPLINE))

# C:\\msys64\\usr\\src\\grass741\\dist.x86_64-w64-mingw32\\include\\grass\\ogsf.h: 396
try:
    KF_FROMX = 0
except:
    pass

# C:\\msys64\\usr\\src\\grass741\\dist.x86_64-w64-mingw32\\include\\grass\\ogsf.h: 396
try:
    KF_FROMY = 1
except:
    pass

# C:\\msys64\\usr\\src\\grass741\\dist.x86_64-w64-mingw32\\include\\grass\\ogsf.h: 396
try:
    KF_FROMZ = 2
except:
    pass

# C:\\msys64\\usr\\src\\grass741\\dist.x86_64-w64-mingw32\\include\\grass\\ogsf.h: 396
try:
    KF_DIRX = 3
except:
    pass

# C:\\msys64\\usr\\src\\grass741\\dist.x86_64-w64-mingw32\\include\\grass\\ogsf.h: 396
try:
    KF_DIRY = 4
except:
    pass

# C:\\msys64\\usr\\src\\grass741\\dist.x86_64-w64-mingw32\\include\\grass\\ogsf.h: 396
try:
    KF_DIRZ = 5
except:
    pass

# C:\\msys64\\usr\\src\\grass741\\dist.x86_64-w64-mingw32\\include\\grass\\ogsf.h: 396
try:
    KF_FOV = 6
except:
    pass

# C:\\msys64\\usr\\src\\grass741\\dist.x86_64-w64-mingw32\\include\\grass\\ogsf.h: 396
try:
    KF_TWIST = 7
except:
    pass

# C:\\msys64\\usr\\src\\grass741\\dist.x86_64-w64-mingw32\\include\\grass\\ogsf.h: 397
try:
    FM_VECT = 1
except:
    pass

# C:\\msys64\\usr\\src\\grass741\\dist.x86_64-w64-mingw32\\include\\grass\\ogsf.h: 397
try:
    FM_SITE = 2
except:
    pass

# C:\\msys64\\usr\\src\\grass741\\dist.x86_64-w64-mingw32\\include\\grass\\ogsf.h: 397
try:
    FM_PATH = 4
except:
    pass

# C:\\msys64\\usr\\src\\grass741\\dist.x86_64-w64-mingw32\\include\\grass\\ogsf.h: 397
try:
    FM_VOL = 8
except:
    pass

# C:\\msys64\\usr\\src\\grass741\\dist.x86_64-w64-mingw32\\include\\grass\\ogsf.h: 397
try:
    FM_LABEL = 16
except:
    pass

g_surf = struct_g_surf # C:\\msys64\\usr\\src\\grass741\\dist.x86_64-w64-mingw32\\include\\grass\\ogsf.h: 257

g_vect_style = struct_g_vect_style # C:\\msys64\\usr\\src\\grass741\\dist.x86_64-w64-mingw32\\include\\grass\\ogsf.h: 286

g_vect_style_thematic = struct_g_vect_style_thematic # C:\\msys64\\usr\\src\\grass741\\dist.x86_64-w64-mingw32\\include\\grass\\ogsf.h: 311

line_cats = struct_line_cats # C:\\msys64\\usr\\src\\grass741\\dist.x86_64-w64-mingw32\\include\\grass\\ogsf.h: 322

g_line = struct_g_line # C:\\msys64\\usr\\src\\grass741\\dist.x86_64-w64-mingw32\\include\\grass\\ogsf.h: 314

g_vect = struct_g_vect # C:\\msys64\\usr\\src\\grass741\\dist.x86_64-w64-mingw32\\include\\grass\\ogsf.h: 330

g_point = struct_g_point # C:\\msys64\\usr\\src\\grass741\\dist.x86_64-w64-mingw32\\include\\grass\\ogsf.h: 352

g_site = struct_g_site # C:\\msys64\\usr\\src\\grass741\\dist.x86_64-w64-mingw32\\include\\grass\\ogsf.h: 365

g_vol = struct_g_vol # C:\\msys64\\usr\\src\\grass741\\dist.x86_64-w64-mingw32\\include\\grass\\ogsf.h: 434

lightdefs = struct_lightdefs # C:\\msys64\\usr\\src\\grass741\\dist.x86_64-w64-mingw32\\include\\grass\\ogsf.h: 461

georot = struct_georot # C:\\msys64\\usr\\src\\grass741\\dist.x86_64-w64-mingw32\\include\\grass\\ogsf.h: 470

view_node = struct_view_node # C:\\msys64\\usr\\src\\grass741\\dist.x86_64-w64-mingw32\\include\\grass\\ogsf.h: 543

key_node = struct_key_node # C:\\msys64\\usr\\src\\grass741\\dist.x86_64-w64-mingw32\\include\\grass\\ogsf.h: 545

# No inserted files

