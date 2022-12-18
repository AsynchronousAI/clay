# Package initialisation
from clayPy.interpreter.mixedmodule import MixedModule


class Module(MixedModule):
    appleveldefs = {
    }

    interpleveldefs = {
        "file": "interp_file.W_File",
        "set_file_encoding": "interp_file.set_file_encoding",
    }

    def shutdown(self, space):
        # at shutdown, flush all open streams.  Ignore I/O errors.
        from clayPy.module._file.interp_file import getopenstreams, StreamErrors
        openstreams = getopenstreams(space)
        while openstreams:
            for stream in openstreams.keys():
                try:
                    del openstreams[stream]
                except KeyError:
                    pass    # key was removed in the meantime
                else:
                    try:
                        stream.flush()
                    except StreamErrors:
                        pass

    def setup_after_space_initialization(self):
        from clayPy.module._file.interp_file import W_File
        from clayPy.objspace.std.transparent import register_proxyable
        register_proxyable(self.space, W_File)
