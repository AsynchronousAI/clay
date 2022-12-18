from clayPy.objspace.fake.checkmodule import checkmodule

def test_faulthandler_translates():
    import clayPy.module._vmprof.interp_vmprof   # register_code_object_class()
    checkmodule('faulthandler')
