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

#include "config.h"
#include "JSReadableStreamDefaultController.h"

#include "ExtendedDOMClientIsoSubspaces.h"
#include "ExtendedDOMIsoSubspaces.h"
#include "JSDOMAttribute.h"
#include "JSDOMBinding.h"
#include "JSDOMBuiltinConstructor.h"
#include "JSDOMExceptionHandling.h"
#include "JSDOMGlobalObjectInlines.h"
#include "JSDOMOperation.h"
#include "JSDOMWrapperCache.h"
#include "ReadableStreamDefaultControllerBuiltins.h"
#include "WebCoreJSClientData.h"
#include <JavaScriptCore/FunctionPrototype.h>
#include <JavaScriptCore/JSCInlines.h>
#include <JavaScriptCore/JSDestructibleObjectHeapCellType.h>
#include <JavaScriptCore/SlotVisitorMacros.h>
#include <JavaScriptCore/SubspaceInlines.h>
#include <wtf/GetPtr.h>
#include <wtf/PointerPreparations.h>

namespace WebCore {
using namespace JSC;

// Functions

// Attributes

static JSC_DECLARE_CUSTOM_GETTER(jsReadableStreamDefaultControllerConstructor);

class JSReadableStreamDefaultControllerPrototype final : public JSC::JSNonFinalObject {
public:
    using Base = JSC::JSNonFinalObject;
    static JSReadableStreamDefaultControllerPrototype* create(JSC::VM& vm, JSDOMGlobalObject* globalObject, JSC::Structure* structure)
    {
        JSReadableStreamDefaultControllerPrototype* ptr = new (NotNull, JSC::allocateCell<JSReadableStreamDefaultControllerPrototype>(vm)) JSReadableStreamDefaultControllerPrototype(vm, globalObject, structure);
        ptr->finishCreation(vm);
        return ptr;
    }

    DECLARE_INFO;
    template<typename CellType, JSC::SubspaceAccess>
    static JSC::GCClient::IsoSubspace* subspaceFor(JSC::VM& vm)
    {
        STATIC_ASSERT_ISO_SUBSPACE_SHARABLE(JSReadableStreamDefaultControllerPrototype, Base);
        return &vm.plainObjectSpace();
    }
    static JSC::Structure* createStructure(JSC::VM& vm, JSC::JSGlobalObject* globalObject, JSC::JSValue prototype)
    {
        return JSC::Structure::create(vm, globalObject, prototype, JSC::TypeInfo(JSC::ObjectType, StructureFlags), info());
    }

private:
    JSReadableStreamDefaultControllerPrototype(JSC::VM& vm, JSC::JSGlobalObject*, JSC::Structure* structure)
        : JSC::JSNonFinalObject(vm, structure)
    {
    }

    void finishCreation(JSC::VM&);
};
STATIC_ASSERT_ISO_SUBSPACE_SHARABLE(JSReadableStreamDefaultControllerPrototype, JSReadableStreamDefaultControllerPrototype::Base);

using JSReadableStreamDefaultControllerDOMConstructor = JSDOMBuiltinConstructor<JSReadableStreamDefaultController>;

template<> const ClassInfo JSReadableStreamDefaultControllerDOMConstructor::s_info = { "ReadableStreamDefaultController"_s, &Base::s_info, nullptr, nullptr, CREATE_METHOD_TABLE(JSReadableStreamDefaultControllerDOMConstructor) };

template<> JSValue JSReadableStreamDefaultControllerDOMConstructor::prototypeForStructure(JSC::VM& vm, const JSDOMGlobalObject& globalObject)
{
    UNUSED_PARAM(vm);
    return globalObject.functionPrototype();
}

template<> void JSReadableStreamDefaultControllerDOMConstructor::initializeProperties(VM& vm, JSDOMGlobalObject& globalObject)
{
    putDirect(vm, vm.propertyNames->length, jsNumber(4), JSC::PropertyAttribute::ReadOnly | JSC::PropertyAttribute::DontEnum);
    JSString* nameString = jsNontrivialString(vm, "ReadableStreamDefaultController"_s);
    m_originalName.set(vm, this, nameString);
    putDirect(vm, vm.propertyNames->name, nameString, JSC::PropertyAttribute::ReadOnly | JSC::PropertyAttribute::DontEnum);
    putDirect(vm, vm.propertyNames->prototype, JSReadableStreamDefaultController::prototype(vm, globalObject), JSC::PropertyAttribute::ReadOnly | JSC::PropertyAttribute::DontEnum | JSC::PropertyAttribute::DontDelete);
}

template<> FunctionExecutable* JSReadableStreamDefaultControllerDOMConstructor::initializeExecutable(VM& vm)
{
    return readableStreamDefaultControllerInitializeReadableStreamDefaultControllerCodeGenerator(vm);
}

/* Hash table for prototype */

static const HashTableValue JSReadableStreamDefaultControllerPrototypeTableValues[] = {
    { "constructor"_s, static_cast<unsigned>(JSC::PropertyAttribute::DontEnum), NoIntrinsic, { HashTableValue::GetterSetterType, jsReadableStreamDefaultControllerConstructor, 0 } },
    { "desiredSize"_s, static_cast<unsigned>(JSC::PropertyAttribute::DontEnum | JSC::PropertyAttribute::ReadOnly | JSC::PropertyAttribute::Accessor | JSC::PropertyAttribute::Builtin), NoIntrinsic, { HashTableValue::BuiltinGeneratorType, readableStreamDefaultControllerDesiredSizeCodeGenerator, 0 } },
    { "enqueue"_s, static_cast<unsigned>(JSC::PropertyAttribute::DontEnum | JSC::PropertyAttribute::Builtin), NoIntrinsic, { HashTableValue::BuiltinGeneratorType, readableStreamDefaultControllerEnqueueCodeGenerator, 0 } },
    { "close"_s, static_cast<unsigned>(JSC::PropertyAttribute::DontEnum | JSC::PropertyAttribute::Builtin), NoIntrinsic, { HashTableValue::BuiltinGeneratorType, readableStreamDefaultControllerCloseCodeGenerator, 0 } },
    { "error"_s, static_cast<unsigned>(JSC::PropertyAttribute::DontEnum | JSC::PropertyAttribute::Builtin), NoIntrinsic, { HashTableValue::BuiltinGeneratorType, readableStreamDefaultControllerErrorCodeGenerator, 0 } },
};

const ClassInfo JSReadableStreamDefaultControllerPrototype::s_info = { "ReadableStreamDefaultController"_s, &Base::s_info, nullptr, nullptr, CREATE_METHOD_TABLE(JSReadableStreamDefaultControllerPrototype) };

void JSReadableStreamDefaultControllerPrototype::finishCreation(VM& vm)
{
    Base::finishCreation(vm);
    reifyStaticProperties(vm, JSReadableStreamDefaultController::info(), JSReadableStreamDefaultControllerPrototypeTableValues, *this);
    JSC_TO_STRING_TAG_WITHOUT_TRANSITION();

    auto clientData = WebCore::clientData(vm);
    this->putDirect(vm, clientData->builtinNames().sinkPublicName(), jsUndefined(), JSC::PropertyAttribute::DontDelete | 0);
}

const ClassInfo JSReadableStreamDefaultController::s_info = { "ReadableStreamDefaultController"_s, &Base::s_info, nullptr, nullptr, CREATE_METHOD_TABLE(JSReadableStreamDefaultController) };

JSReadableStreamDefaultController::JSReadableStreamDefaultController(Structure* structure, JSDOMGlobalObject& globalObject)
    : JSDOMObject(structure, globalObject)
{
}

void JSReadableStreamDefaultController::finishCreation(VM& vm)
{
    Base::finishCreation(vm);
    ASSERT(inherits(info()));
}

JSObject* JSReadableStreamDefaultController::createPrototype(VM& vm, JSDOMGlobalObject& globalObject)
{
    return JSReadableStreamDefaultControllerPrototype::create(vm, &globalObject, JSReadableStreamDefaultControllerPrototype::createStructure(vm, &globalObject, globalObject.objectPrototype()));
}

JSObject* JSReadableStreamDefaultController::prototype(VM& vm, JSDOMGlobalObject& globalObject)
{
    return getDOMPrototype<JSReadableStreamDefaultController>(vm, globalObject);
}

JSValue JSReadableStreamDefaultController::getConstructor(VM& vm, const JSGlobalObject* globalObject)
{
    return getDOMConstructor<JSReadableStreamDefaultControllerDOMConstructor, DOMConstructorID::ReadableStreamDefaultController>(vm, *jsCast<const JSDOMGlobalObject*>(globalObject));
}

void JSReadableStreamDefaultController::destroy(JSC::JSCell* cell)
{
    JSReadableStreamDefaultController* thisObject = static_cast<JSReadableStreamDefaultController*>(cell);
    thisObject->JSReadableStreamDefaultController::~JSReadableStreamDefaultController();
}

JSC_DEFINE_CUSTOM_GETTER(jsReadableStreamDefaultControllerConstructor, (JSGlobalObject * lexicalGlobalObject, EncodedJSValue thisValue, PropertyName))
{
    VM& vm = JSC::getVM(lexicalGlobalObject);
    auto throwScope = DECLARE_THROW_SCOPE(vm);
    auto* prototype = jsDynamicCast<JSReadableStreamDefaultControllerPrototype*>(JSValue::decode(thisValue));
    if (UNLIKELY(!prototype))
        return throwVMTypeError(lexicalGlobalObject, throwScope);
    return JSValue::encode(JSReadableStreamDefaultController::getConstructor(JSC::getVM(lexicalGlobalObject), prototype->globalObject()));
}

JSC::GCClient::IsoSubspace* JSReadableStreamDefaultController::subspaceForImpl(JSC::VM& vm)
{
    return WebCore::subspaceForImpl<JSReadableStreamDefaultController, UseCustomHeapCellType::No>(
        vm,
        [](auto& spaces) { return spaces.m_clientSubspaceForReadableStreamDefaultController.get(); },
        [](auto& spaces, auto&& space) { spaces.m_clientSubspaceForReadableStreamDefaultController = WTFMove(space); },
        [](auto& spaces) { return spaces.m_subspaceForReadableStreamDefaultController.get(); },
        [](auto& spaces, auto&& space) { spaces.m_subspaceForReadableStreamDefaultController = WTFMove(space); });
}

}
