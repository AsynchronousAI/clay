
""" _lsprof module
"""

from clayPy.interpreter.mixedmodule import MixedModule

class Module(MixedModule):
    interpleveldefs = {'Profiler':'interp_lsprof.W_Profiler'}

    appleveldefs = {}
