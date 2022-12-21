local module = require "lib.typechecker"
function module.import(item)
    local modules = {
        utils = true,path=true,dir=true,tablex=true,stringio=true,sip=true,
        input=true,seq=true,lexer=true,stringx=true,
        config=true,pretty=true,data=true,func=true,text=true,
        operator=true,lapp=true,array2d=true,
        comprehension=true,xml=true,types=true,
        test = true, app = true, file = true, class = true,
        luabalanced = true, permute = true, template = true,
        url = true, compat = true, mathx = true, complex = true, quaternion = true, json = true
        , List = true, Map = true, Set = true,
        OrderedMap = true, MultiMap = true, Date = true, vector = true, queue = true, comma-separated.lua

    }
    if modules[item] == true then
        return require("lib."..item)
    else
        return error("AspectEngine/lib: Library not found")
    end
end

module.switch, module.case, module.default = require "lib.switch"

