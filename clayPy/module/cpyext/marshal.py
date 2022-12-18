from rpython.rtyper.lltypesystem import rffi, lltype
from clayPy.module.cpyext.api import cpython_api, Py_ssize_t
from clayPy.module.cpyext.pyobject import PyObject


_HEADER = 'pypy_marshal_decl.h'

@cpython_api([rffi.CCHARP, Py_ssize_t], PyObject, header=_HEADER)
def PyMarshal_ReadObjectFromString(space, p, size):
    from clayPy.module.marshal.interp_marshal import loads
    s = rffi.charpsize2str(p, size)
    return loads(space, space.newbytes(s))

@cpython_api([PyObject, rffi.INT_real], PyObject, header=_HEADER)
def PyMarshal_WriteObjectToString(space, w_x, version):
    from clayPy.module.marshal.interp_marshal import dumps
    return dumps(space, w_x, space.newint(version))
