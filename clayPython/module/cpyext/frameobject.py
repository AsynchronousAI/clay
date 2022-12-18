from rpython.rtyper.lltypesystem import rffi, lltype
from clayPy.module.cpyext.api import (
    cpython_api, bootstrap_function, PyObjectFields, cpython_struct,
    CANNOT_FAIL, slot_function)
from clayPy.module.cpyext.pyobject import (
    PyObject, decref, make_ref, from_ref, track_reference,
    make_typedescr, get_typedescr)
from clayPy.module.cpyext.state import State
from clayPy.module.cpyext.pystate import PyThreadState
from clayPy.module.cpyext.funcobject import PyCodeObject
from clayPy.interpreter.pyframe import PyFrame
from clayPy.interpreter.pycode import PyCode
from clayPy.interpreter.pytraceback import PyTraceback

PyFrameObjectStruct = lltype.ForwardReference()
PyFrameObject = lltype.Ptr(PyFrameObjectStruct)
PyFrameObjectFields = (PyObjectFields +
    (("f_code", PyCodeObject),
     ("f_globals", PyObject),
     ("f_locals", PyObject),
     ("f_lineno", rffi.INT),
     ))
cpython_struct("PyFrameObject", PyFrameObjectFields, PyFrameObjectStruct)

@bootstrap_function
def init_frameobject(space):
    make_typedescr(PyFrame.typedef,
                   basestruct=PyFrameObject.TO,
                   attach=frame_attach,
                   dealloc=frame_dealloc,
                   realize=frame_realize)

def frame_attach(space, py_obj, w_obj, w_userdata=None):
    "Fills a newly allocated PyFrameObject with a frame object"
    frame = space.interp_w(PyFrame, w_obj)
    py_frame = rffi.cast(PyFrameObject, py_obj)
    py_frame.c_f_code = rffi.cast(PyCodeObject, make_ref(space, frame.pycode))
    py_frame.c_f_globals = make_ref(space, frame.get_w_globals())
    py_frame.c_f_locals = make_ref(space, frame.get_w_locals())
    rffi.setintfield(py_frame, 'c_f_lineno', frame.getorcreatedebug().f_lineno)

@slot_function([PyObject], lltype.Void)
def frame_dealloc(space, py_obj):
    py_frame = rffi.cast(PyFrameObject, py_obj)
    py_code = rffi.cast(PyObject, py_frame.c_f_code)
    decref(space, py_code)
    decref(space, py_frame.c_f_globals)
    decref(space, py_frame.c_f_locals)
    from clayPy.module.cpyext.object import _dealloc
    _dealloc(space, py_obj)

def frame_realize(space, py_obj):
    """
    Creates the frame in the interpreter. The PyFrameObject structure must not
    be modified after this call.
    """
    py_frame = rffi.cast(PyFrameObject, py_obj)
    py_code = rffi.cast(PyObject, py_frame.c_f_code)
    w_code = from_ref(space, py_code)
    code = space.interp_w(PyCode, w_code)
    w_globals = from_ref(space, py_frame.c_f_globals)

    frame = space.FrameClass(space, code, w_globals, outer_func=None)
    d = frame.getorcreatedebug()
    d.f_lineno = rffi.getintfield(py_frame, 'c_f_lineno')
    track_reference(space, py_obj, frame)
    return frame

@cpython_api([PyThreadState, PyCodeObject, PyObject, PyObject], PyFrameObject,
             result_is_ll=True)
def PyFrame_New(space, tstate, w_code, w_globals, w_locals):
    typedescr = get_typedescr(PyFrame.typedef)
    py_obj = typedescr.allocate(space, space.gettypeobject(PyFrame.typedef))
    py_frame = rffi.cast(PyFrameObject, py_obj)
    space.interp_w(PyCode, w_code) # sanity check
    py_frame.c_f_code = rffi.cast(PyCodeObject, make_ref(space, w_code))
    py_frame.c_f_globals = make_ref(space, w_globals)
    py_frame.c_f_locals = make_ref(space, w_locals)
    return py_frame

@cpython_api([PyFrameObject], rffi.INT_real, error=-1)
def PyTraceBack_Here(space, w_frame):
    from clayPy.interpreter.pytraceback import record_application_traceback
    state = space.fromcache(State)
    if state.get_exception() is None:
        return -1
    frame = space.interp_w(PyFrame, w_frame)
    record_application_traceback(space, state.get_exception(), frame, 0)
    return 0

@cpython_api([PyObject], rffi.INT_real, error=CANNOT_FAIL)
def PyTraceBack_Check(space, w_obj):
    return isinstance(w_obj, PyTraceback)