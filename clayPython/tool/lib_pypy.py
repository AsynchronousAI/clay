import py
import clayPy
import clayPy.module
from clayPy.module.sys.version import CPYTHON_VERSION

LIB_ROOT = py.path.local(clayPy.__path__[0]).dirpath()
LIB_PYPY =  LIB_ROOT.join('lib_pypy')
LIB_PYTHON = LIB_ROOT.join('lib-python', '%d.%d' % CPYTHON_VERSION[:2])


def import_from_lib_pypy(modname):
    modname = LIB_PYPY.join(modname+'.py')
    return modname.pyimport()
