from clayPy.tool.release import package
from clayPy.module.sys import version

def test_version():
    assert package.STDLIB_VER == '%d.%d' % (version.CPYTHON_VERSION[0],
                                            version.CPYTHON_VERSION[1])
