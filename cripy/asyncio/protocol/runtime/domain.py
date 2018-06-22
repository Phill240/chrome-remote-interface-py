from typing import Any, List, Optional, Union
from cripy.asyncio.protocol.runtime import events as Events
from cripy.asyncio.protocol.runtime import types as Types

__all__ = ["Runtime"]


class Runtime(object):
    """
    Runtime domain exposes JavaScript runtime by means of remote evaluation and mirror objects.
Evaluation results are returned as mirror object that expose object type, string representation
and unique identifier that can be used for further object reference. Original objects are
maintained in memory unless they are either explicitly released or are released along with the
other objects in their object group.
    """

    events = Events.RUNTIME_EVENTS_NS

    def __init__(self, chrome):
        """
        Construct a new Runtime object

        :param chrome: An instance of the devtools protocol client
        """
        self.chrome = chrome

    async def awaitPromise(self, promiseObjectId: str, returnByValue: Optional[bool] = None, generatePreview: Optional[bool] = None) -> Optional[dict]:
        """
        Add handler to promise with given promise object id.

        :param promiseObjectId: Identifier of the promise.
        :type promiseObjectId: str
        :param returnByValue: Whether the result is expected to be a JSON object that should be sent by value.
        :type returnByValue: Optional[bool]
        :param generatePreview: Whether preview should be generated for the result.
        :type generatePreview: Optional[bool]
        """
        msg_dict = dict()
        if promiseObjectId is not None:
            msg_dict['promiseObjectId'] = promiseObjectId
        if returnByValue is not None:
            msg_dict['returnByValue'] = returnByValue
        if generatePreview is not None:
            msg_dict['generatePreview'] = generatePreview
        mayberes = await self.chrome.send('Runtime.awaitPromise', msg_dict)
        res = await mayberes
        res['result'] = Types.RemoteObject.safe_create(res['result'])
        res['exceptionDetails'] = Types.ExceptionDetails.safe_create(res['exceptionDetails'])
        return res

    async def callFunctionOn(self, functionDeclaration: str, objectId: Optional[str] = None, arguments: Optional[List[dict]] = None, silent: Optional[bool] = None, returnByValue: Optional[bool] = None, generatePreview: Optional[bool] = None, userGesture: Optional[bool] = None, awaitPromise: Optional[bool] = None, executionContextId: Optional[int] = None, objectGroup: Optional[str] = None) -> Optional[dict]:
        """
        Calls function with given declaration on the given object. Object group of the result is
inherited from the target object.

        :param functionDeclaration: Declaration of the function to call.
        :type functionDeclaration: str
        :param objectId: Identifier of the object to call function on. Either objectId or executionContextId should be specified.
        :type objectId: Optional[str]
        :param arguments: Call arguments. All call arguments must belong to the same JavaScript world as the target object.
        :type arguments: Optional[List[dict]]
        :param silent: In silent mode exceptions thrown during evaluation are not reported and do not pause execution. Overrides `setPauseOnException` state.
        :type silent: Optional[bool]
        :param returnByValue: Whether the result is expected to be a JSON object which should be sent by value.
        :type returnByValue: Optional[bool]
        :param generatePreview: Whether preview should be generated for the result.
        :type generatePreview: Optional[bool]
        :param userGesture: Whether execution should be treated as initiated by user in the UI.
        :type userGesture: Optional[bool]
        :param awaitPromise: Whether execution should `await` for resulting value and return once awaited promise is resolved.
        :type awaitPromise: Optional[bool]
        :param executionContextId: Specifies execution context which global object will be used to call function on. Either executionContextId or objectId should be specified.
        :type executionContextId: Optional[int]
        :param objectGroup: Symbolic group name that can be used to release multiple objects. If objectGroup is not specified and objectId is, objectGroup will be inherited from object.
        :type objectGroup: Optional[str]
        """
        msg_dict = dict()
        if functionDeclaration is not None:
            msg_dict['functionDeclaration'] = functionDeclaration
        if objectId is not None:
            msg_dict['objectId'] = objectId
        if arguments is not None:
            msg_dict['arguments'] = arguments
        if silent is not None:
            msg_dict['silent'] = silent
        if returnByValue is not None:
            msg_dict['returnByValue'] = returnByValue
        if generatePreview is not None:
            msg_dict['generatePreview'] = generatePreview
        if userGesture is not None:
            msg_dict['userGesture'] = userGesture
        if awaitPromise is not None:
            msg_dict['awaitPromise'] = awaitPromise
        if executionContextId is not None:
            msg_dict['executionContextId'] = executionContextId
        if objectGroup is not None:
            msg_dict['objectGroup'] = objectGroup
        mayberes = await self.chrome.send('Runtime.callFunctionOn', msg_dict)
        res = await mayberes
        res['result'] = Types.RemoteObject.safe_create(res['result'])
        res['exceptionDetails'] = Types.ExceptionDetails.safe_create(res['exceptionDetails'])
        return res

    async def compileScript(self, expression: str, sourceURL: str, persistScript: bool, executionContextId: Optional[int] = None) -> Optional[dict]:
        """
        Compiles expression.

        :param expression: Expression to compile.
        :type expression: str
        :param sourceURL: Source url to be set for the script.
        :type sourceURL: str
        :param persistScript: Specifies whether the compiled script should be persisted.
        :type persistScript: bool
        :param executionContextId: Specifies in which execution context to perform script run. If the parameter is omitted the evaluation will be performed in the context of the inspected page.
        :type executionContextId: Optional[int]
        """
        msg_dict = dict()
        if expression is not None:
            msg_dict['expression'] = expression
        if sourceURL is not None:
            msg_dict['sourceURL'] = sourceURL
        if persistScript is not None:
            msg_dict['persistScript'] = persistScript
        if executionContextId is not None:
            msg_dict['executionContextId'] = executionContextId
        mayberes = await self.chrome.send('Runtime.compileScript', msg_dict)
        res = await mayberes
        res['exceptionDetails'] = Types.ExceptionDetails.safe_create(res['exceptionDetails'])
        return res

    async def disable(self) -> Optional[dict]:
        """
        Disables reporting of execution contexts creation.
        """
        mayberes = await self.chrome.send('Runtime.disable')
        return mayberes

    async def discardConsoleEntries(self) -> Optional[dict]:
        """
        Discards collected exceptions and console API calls.
        """
        mayberes = await self.chrome.send('Runtime.discardConsoleEntries')
        return mayberes

    async def enable(self) -> Optional[dict]:
        """
        Enables reporting of execution contexts creation by means of `executionContextCreated` event.
When the reporting gets enabled the event will be sent immediately for each existing execution
context.
        """
        mayberes = await self.chrome.send('Runtime.enable')
        return mayberes

    async def evaluate(self, expression: str, objectGroup: Optional[str] = None, includeCommandLineAPI: Optional[bool] = None, silent: Optional[bool] = None, contextId: Optional[int] = None, returnByValue: Optional[bool] = None, generatePreview: Optional[bool] = None, userGesture: Optional[bool] = None, awaitPromise: Optional[bool] = None, throwOnSideEffect: Optional[bool] = None, timeout: Optional[float] = None) -> Optional[dict]:
        """
        Evaluates expression on global object.

        :param expression: Expression to evaluate.
        :type expression: str
        :param objectGroup: Symbolic group name that can be used to release multiple objects.
        :type objectGroup: Optional[str]
        :param includeCommandLineAPI: Determines whether Command Line API should be available during the evaluation.
        :type includeCommandLineAPI: Optional[bool]
        :param silent: In silent mode exceptions thrown during evaluation are not reported and do not pause execution. Overrides `setPauseOnException` state.
        :type silent: Optional[bool]
        :param contextId: Specifies in which execution context to perform evaluation. If the parameter is omitted the evaluation will be performed in the context of the inspected page.
        :type contextId: Optional[int]
        :param returnByValue: Whether the result is expected to be a JSON object that should be sent by value.
        :type returnByValue: Optional[bool]
        :param generatePreview: Whether preview should be generated for the result.
        :type generatePreview: Optional[bool]
        :param userGesture: Whether execution should be treated as initiated by user in the UI.
        :type userGesture: Optional[bool]
        :param awaitPromise: Whether execution should `await` for resulting value and return once awaited promise is resolved.
        :type awaitPromise: Optional[bool]
        :param throwOnSideEffect: Whether to throw an exception if side effect cannot be ruled out during evaluation.
        :type throwOnSideEffect: Optional[bool]
        :param timeout: Terminate execution after timing out (number of milliseconds).
        :type timeout: Optional[float]
        """
        msg_dict = dict()
        if expression is not None:
            msg_dict['expression'] = expression
        if objectGroup is not None:
            msg_dict['objectGroup'] = objectGroup
        if includeCommandLineAPI is not None:
            msg_dict['includeCommandLineAPI'] = includeCommandLineAPI
        if silent is not None:
            msg_dict['silent'] = silent
        if contextId is not None:
            msg_dict['contextId'] = contextId
        if returnByValue is not None:
            msg_dict['returnByValue'] = returnByValue
        if generatePreview is not None:
            msg_dict['generatePreview'] = generatePreview
        if userGesture is not None:
            msg_dict['userGesture'] = userGesture
        if awaitPromise is not None:
            msg_dict['awaitPromise'] = awaitPromise
        if throwOnSideEffect is not None:
            msg_dict['throwOnSideEffect'] = throwOnSideEffect
        if timeout is not None:
            msg_dict['timeout'] = timeout
        mayberes = await self.chrome.send('Runtime.evaluate', msg_dict)
        res = await mayberes
        res['result'] = Types.RemoteObject.safe_create(res['result'])
        res['exceptionDetails'] = Types.ExceptionDetails.safe_create(res['exceptionDetails'])
        return res

    async def getIsolateId(self) -> Optional[dict]:
        """
        Returns the isolate id.
        """
        mayberes = await self.chrome.send('Runtime.getIsolateId')
        res = await mayberes
        return res

    async def getHeapUsage(self) -> Optional[dict]:
        """
        Returns the JavaScript heap usage.
It is the total usage of the corresponding isolate not scoped to a particular Runtime.
        """
        mayberes = await self.chrome.send('Runtime.getHeapUsage')
        res = await mayberes
        return res

    async def getProperties(self, objectId: str, ownProperties: Optional[bool] = None, accessorPropertiesOnly: Optional[bool] = None, generatePreview: Optional[bool] = None) -> Optional[dict]:
        """
        Returns properties of a given object. Object group of the result is inherited from the target
object.

        :param objectId: Identifier of the object to return properties for.
        :type objectId: str
        :param ownProperties: If true, returns properties belonging only to the element itself, not to its prototype chain.
        :type ownProperties: Optional[bool]
        :param accessorPropertiesOnly: If true, returns accessor properties (with getter/setter) only; internal properties are not returned either.
        :type accessorPropertiesOnly: Optional[bool]
        :param generatePreview: Whether preview should be generated for the results.
        :type generatePreview: Optional[bool]
        """
        msg_dict = dict()
        if objectId is not None:
            msg_dict['objectId'] = objectId
        if ownProperties is not None:
            msg_dict['ownProperties'] = ownProperties
        if accessorPropertiesOnly is not None:
            msg_dict['accessorPropertiesOnly'] = accessorPropertiesOnly
        if generatePreview is not None:
            msg_dict['generatePreview'] = generatePreview
        mayberes = await self.chrome.send('Runtime.getProperties', msg_dict)
        res = await mayberes
        res['result'] = Types.PropertyDescriptor.safe_create_from_list(res['result'])
        res['internalProperties'] = Types.InternalPropertyDescriptor.safe_create_from_list(res['internalProperties'])
        res['exceptionDetails'] = Types.ExceptionDetails.safe_create(res['exceptionDetails'])
        return res

    async def globalLexicalScopeNames(self, executionContextId: Optional[int] = None) -> Optional[dict]:
        """
        Returns all let, const and class variables from global scope.

        :param executionContextId: Specifies in which execution context to lookup global scope variables.
        :type executionContextId: Optional[int]
        """
        msg_dict = dict()
        if executionContextId is not None:
            msg_dict['executionContextId'] = executionContextId
        mayberes = await self.chrome.send('Runtime.globalLexicalScopeNames', msg_dict)
        res = await mayberes
        return res

    async def queryObjects(self, prototypeObjectId: str, objectGroup: Optional[str] = None) -> Optional[dict]:
        """
        :param prototypeObjectId: Identifier of the prototype to return objects for.
        :type prototypeObjectId: str
        :param objectGroup: Symbolic group name that can be used to release the results.
        :type objectGroup: Optional[str]
        """
        msg_dict = dict()
        if prototypeObjectId is not None:
            msg_dict['prototypeObjectId'] = prototypeObjectId
        if objectGroup is not None:
            msg_dict['objectGroup'] = objectGroup
        mayberes = await self.chrome.send('Runtime.queryObjects', msg_dict)
        res = await mayberes
        res['objects'] = Types.RemoteObject.safe_create(res['objects'])
        return res

    async def releaseObject(self, objectId: str) -> Optional[dict]:
        """
        Releases remote object with given id.

        :param objectId: Identifier of the object to release.
        :type objectId: str
        """
        msg_dict = dict()
        if objectId is not None:
            msg_dict['objectId'] = objectId
        mayberes = await self.chrome.send('Runtime.releaseObject', msg_dict)
        return mayberes

    async def releaseObjectGroup(self, objectGroup: str) -> Optional[dict]:
        """
        Releases all remote objects that belong to a given group.

        :param objectGroup: Symbolic object group name.
        :type objectGroup: str
        """
        msg_dict = dict()
        if objectGroup is not None:
            msg_dict['objectGroup'] = objectGroup
        mayberes = await self.chrome.send('Runtime.releaseObjectGroup', msg_dict)
        return mayberes

    async def runIfWaitingForDebugger(self) -> Optional[dict]:
        """
        Tells inspected instance to run if it was waiting for debugger to attach.
        """
        mayberes = await self.chrome.send('Runtime.runIfWaitingForDebugger')
        return mayberes

    async def runScript(self, scriptId: str, executionContextId: Optional[int] = None, objectGroup: Optional[str] = None, silent: Optional[bool] = None, includeCommandLineAPI: Optional[bool] = None, returnByValue: Optional[bool] = None, generatePreview: Optional[bool] = None, awaitPromise: Optional[bool] = None) -> Optional[dict]:
        """
        Runs script with given id in a given context.

        :param scriptId: Id of the script to run.
        :type scriptId: str
        :param executionContextId: Specifies in which execution context to perform script run. If the parameter is omitted the evaluation will be performed in the context of the inspected page.
        :type executionContextId: Optional[int]
        :param objectGroup: Symbolic group name that can be used to release multiple objects.
        :type objectGroup: Optional[str]
        :param silent: In silent mode exceptions thrown during evaluation are not reported and do not pause execution. Overrides `setPauseOnException` state.
        :type silent: Optional[bool]
        :param includeCommandLineAPI: Determines whether Command Line API should be available during the evaluation.
        :type includeCommandLineAPI: Optional[bool]
        :param returnByValue: Whether the result is expected to be a JSON object which should be sent by value.
        :type returnByValue: Optional[bool]
        :param generatePreview: Whether preview should be generated for the result.
        :type generatePreview: Optional[bool]
        :param awaitPromise: Whether execution should `await` for resulting value and return once awaited promise is resolved.
        :type awaitPromise: Optional[bool]
        """
        msg_dict = dict()
        if scriptId is not None:
            msg_dict['scriptId'] = scriptId
        if executionContextId is not None:
            msg_dict['executionContextId'] = executionContextId
        if objectGroup is not None:
            msg_dict['objectGroup'] = objectGroup
        if silent is not None:
            msg_dict['silent'] = silent
        if includeCommandLineAPI is not None:
            msg_dict['includeCommandLineAPI'] = includeCommandLineAPI
        if returnByValue is not None:
            msg_dict['returnByValue'] = returnByValue
        if generatePreview is not None:
            msg_dict['generatePreview'] = generatePreview
        if awaitPromise is not None:
            msg_dict['awaitPromise'] = awaitPromise
        mayberes = await self.chrome.send('Runtime.runScript', msg_dict)
        res = await mayberes
        res['result'] = Types.RemoteObject.safe_create(res['result'])
        res['exceptionDetails'] = Types.ExceptionDetails.safe_create(res['exceptionDetails'])
        return res

    async def setAsyncCallStackDepth(self, maxDepth: int) -> Optional[dict]:
        """
        Enables or disables async call stacks tracking.

        :param maxDepth: Maximum depth of async call stacks. Setting to `0` will effectively disable collecting async call stacks (default).
        :type maxDepth: int
        """
        msg_dict = dict()
        if maxDepth is not None:
            msg_dict['maxDepth'] = maxDepth
        mayberes = await self.chrome.send('Runtime.setAsyncCallStackDepth', msg_dict)
        return mayberes

    async def setCustomObjectFormatterEnabled(self, enabled: bool) -> Optional[dict]:
        """
        :param enabled: The enabled
        :type enabled: bool
        """
        msg_dict = dict()
        if enabled is not None:
            msg_dict['enabled'] = enabled
        mayberes = await self.chrome.send('Runtime.setCustomObjectFormatterEnabled', msg_dict)
        return mayberes

    async def setMaxCallStackSizeToCapture(self, size: int) -> Optional[dict]:
        """
        :param size: The size
        :type size: int
        """
        msg_dict = dict()
        if size is not None:
            msg_dict['size'] = size
        mayberes = await self.chrome.send('Runtime.setMaxCallStackSizeToCapture', msg_dict)
        return mayberes

    async def terminateExecution(self) -> Optional[dict]:
        """
        Terminate current or next JavaScript execution.
Will cancel the termination when the outer-most script execution ends.
        """
        mayberes = await self.chrome.send('Runtime.terminateExecution')
        return mayberes

    async def addBinding(self, name: str, executionContextId: Optional[int] = None) -> Optional[dict]:
        """
        If executionContextId is empty, adds binding with the given name on the
global objects of all inspected contexts, including those created later,
bindings survive reloads.
If executionContextId is specified, adds binding only on global object of
given execution context.
Binding function takes exactly one argument, this argument should be string,
in case of any other input, function throws an exception.
Each binding function call produces Runtime.bindingCalled notification.

        :param name: The name
        :type name: str
        :param executionContextId: The executionContextId
        :type executionContextId: Optional[int]
        """
        msg_dict = dict()
        if name is not None:
            msg_dict['name'] = name
        if executionContextId is not None:
            msg_dict['executionContextId'] = executionContextId
        mayberes = await self.chrome.send('Runtime.addBinding', msg_dict)
        return mayberes

    async def removeBinding(self, name: str) -> Optional[dict]:
        """
        This method does not remove binding function from global object but
unsubscribes current runtime agent from Runtime.bindingCalled notifications.

        :param name: The name
        :type name: str
        """
        msg_dict = dict()
        if name is not None:
            msg_dict['name'] = name
        mayberes = await self.chrome.send('Runtime.removeBinding', msg_dict)
        return mayberes

    @staticmethod
    def get_event_classes() -> Optional[dict]:
        """
        Retrieve a dictionary of events emitted by the  domain to their python class

        If  has events this method returns a dictionary of
        fully qualified event name (str) to it python class

        :return: Dictionary of the  domain event classes
        :retype: Optional[dict]
        """
        return Events.RUNTIME_EVENTS_TO_CLASS
