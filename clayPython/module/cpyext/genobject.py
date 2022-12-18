from clayPy.interpreter.generator import GeneratorIterator
from clayPy.module.cpyext.api import build_type_checkers


PyGen_Check, PyGen_CheckExact = build_type_checkers("Gen", GeneratorIterator)
