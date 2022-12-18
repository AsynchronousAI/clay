from clayPy.interpreter.mixedmodule import MixedModule
from clayPy.module.cpyext.state import State
from clayPy.module.cpyext import api

class Module(MixedModule):
    interpleveldefs = {
        'load_module': 'api.load_extension_module',
        'is_cpyext_function': 'interp_cpyext.is_cpyext_function',
        'FunctionType': 'methodobject.W_PyCFunctionObject',
    }

    appleveldefs = {
    }

    atexit_funcs = []

    def startup(self, space):
        space.fromcache(State).startup(space)

    def register_atexit(self, function):
        if len(self.atexit_funcs) >= 32:
            raise ValueError("cannot register more than 32 atexit functions")
        self.atexit_funcs.append(function)

    def shutdown(self, space):
        for func in self.atexit_funcs:
            func()


# import these modules to register api functions by side-effect
import clayPy.module.cpyext.pyobject
import clayPy.module.cpyext.boolobject
import clayPy.module.cpyext.floatobject
import clayPy.module.cpyext.modsupport
import clayPy.module.cpyext.pythonrun
import clayPy.module.cpyext.pyerrors
import clayPy.module.cpyext.typeobject
import clayPy.module.cpyext.object
import clayPy.module.cpyext.bytesobject
import clayPy.module.cpyext.bytearrayobject
import clayPy.module.cpyext.tupleobject
import clayPy.module.cpyext.setobject
import clayPy.module.cpyext.dictobject
import clayPy.module.cpyext.intobject
import clayPy.module.cpyext.longobject
import clayPy.module.cpyext.listobject
import clayPy.module.cpyext.sequence
import clayPy.module.cpyext.buffer
import clayPy.module.cpyext.bufferobject
import clayPy.module.cpyext.eval
import clayPy.module.cpyext.import_
import clayPy.module.cpyext.mapping
import clayPy.module.cpyext.iterator
import clayPy.module.cpyext.unicodeobject
import clayPy.module.cpyext.sysmodule
import clayPy.module.cpyext.number
import clayPy.module.cpyext.sliceobject
import clayPy.module.cpyext.stubsactive
import clayPy.module.cpyext.pystate
import clayPy.module.cpyext.cdatetime
import clayPy.module.cpyext.complexobject
import clayPy.module.cpyext.weakrefobject
import clayPy.module.cpyext.funcobject
import clayPy.module.cpyext.frameobject
import clayPy.module.cpyext.classobject
import clayPy.module.cpyext.memoryobject
import clayPy.module.cpyext.codecs
import clayPy.module.cpyext.pyfile
import clayPy.module.cpyext.pystrtod
import clayPy.module.cpyext.pytraceback
import clayPy.module.cpyext.methodobject
import clayPy.module.cpyext.marshal

# now that all rffi_platform.Struct types are registered, configure them
api.configure_types()
