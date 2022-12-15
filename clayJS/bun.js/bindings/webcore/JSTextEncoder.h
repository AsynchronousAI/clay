/*
    This file is part of the WebKit open source project.
    This file has been generated by generate-bindings.pl. DO NOT MODIFY!

    This library is free software; you can redistribute it and/or
    modify it under the terms of the GNU Library General Public
    License as published by the Free Software Foundation; either
    version 2 of the License, or (at your option) any later version.

    This library is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
    Library General Public License for more details.

    You should have received a copy of the GNU Library General Public License
    along with this library; see the file COPYING.LIB.  If not, write to
    the Free Software Foundation, Inc., 51 Franklin Street, Fifth Floor,
    Boston, MA 02110-1301, USA.
*/

#pragma once

#include "root.h"

#include "JSDOMConvertDictionary.h"
#include "JSDOMWrapper.h"
#include "TextEncoder.h"
#include <wtf/NeverDestroyed.h>

namespace WebCore {

class JSTextEncoder : public JSDOMWrapper<TextEncoder> {
public:
    using Base = JSDOMWrapper<TextEncoder>;
    static JSTextEncoder* create(JSC::Structure* structure, JSDOMGlobalObject* globalObject, Ref<TextEncoder>&& impl)
    {
        JSTextEncoder* ptr = new (NotNull, JSC::allocateCell<JSTextEncoder>(globalObject->vm())) JSTextEncoder(structure, *globalObject, WTFMove(impl));
        ptr->finishCreation(globalObject->vm());
        return ptr;
    }

    static JSC::JSObject* createPrototype(JSC::VM&, JSDOMGlobalObject&);
    static JSC::JSObject* prototype(JSC::VM&, JSDOMGlobalObject&);
    static TextEncoder* toWrapped(JSC::VM&, JSC::JSValue);
    static void destroy(JSC::JSCell*);

    DECLARE_INFO;

    static JSC::Structure* createStructure(JSC::VM& vm, JSC::JSGlobalObject* globalObject, JSC::JSValue prototype)
    {
        return JSC::Structure::create(vm, globalObject, prototype, JSC::TypeInfo(JSC::ObjectType, StructureFlags), info(), JSC::NonArray);
    }

    static JSC::JSValue getConstructor(JSC::VM&, const JSC::JSGlobalObject*);
    template<typename, JSC::SubspaceAccess mode> static JSC::GCClient::IsoSubspace* subspaceFor(JSC::VM& vm)
    {
        if constexpr (mode == JSC::SubspaceAccess::Concurrently)
            return nullptr;
        return subspaceForImpl(vm);
    }
    static JSC::GCClient::IsoSubspace* subspaceForImpl(JSC::VM& vm);
    static void analyzeHeap(JSCell*, JSC::HeapAnalyzer&);

protected:
    JSTextEncoder(JSC::Structure*, JSDOMGlobalObject&, Ref<TextEncoder>&&);

    void finishCreation(JSC::VM&);
};

class JSTextEncoderOwner final : public JSC::WeakHandleOwner {
public:
    bool isReachableFromOpaqueRoots(JSC::Handle<JSC::Unknown>, void* context, JSC::AbstractSlotVisitor&, const char**) final;
    void finalize(JSC::Handle<JSC::Unknown>, void* context) final;
};

inline JSC::WeakHandleOwner* wrapperOwner(DOMWrapperWorld&, TextEncoder*)
{
    static NeverDestroyed<JSTextEncoderOwner> owner;
    return &owner.get();
}

inline void* wrapperKey(TextEncoder* wrappableObject)
{
    return wrappableObject;
}

JSC::JSValue toJS(JSC::JSGlobalObject*, JSDOMGlobalObject*, TextEncoder&);
inline JSC::JSValue toJS(JSC::JSGlobalObject* lexicalGlobalObject, JSDOMGlobalObject* globalObject, TextEncoder* impl) { return impl ? toJS(lexicalGlobalObject, globalObject, *impl) : JSC::jsNull(); }
JSC::JSValue toJSNewlyCreated(JSC::JSGlobalObject*, JSDOMGlobalObject*, Ref<TextEncoder>&&);
inline JSC::JSValue toJSNewlyCreated(JSC::JSGlobalObject* lexicalGlobalObject, JSDOMGlobalObject* globalObject, RefPtr<TextEncoder>&& impl) { return impl ? toJSNewlyCreated(lexicalGlobalObject, globalObject, impl.releaseNonNull()) : JSC::jsNull(); }

template<> struct JSDOMWrapperConverterTraits<TextEncoder> {
    using WrapperClass = JSTextEncoder;
    using ToWrappedReturnType = TextEncoder*;
};
template<> TextEncoder::EncodeIntoResult convertDictionary<TextEncoder::EncodeIntoResult>(JSC::JSGlobalObject&, JSC::JSValue);

JSC::JSObject* convertDictionaryToJS(JSC::JSGlobalObject&, JSDOMGlobalObject&, const TextEncoder::EncodeIntoResult&);

} // namespace WebCore
