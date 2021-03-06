"""This is an auto-generated file. Modify at your own risk"""
from typing import Awaitable, Any, Callable, Dict, List, Optional, Union, TYPE_CHECKING

if TYPE_CHECKING:
    from cripy import ConnectionType, SessionType

__all__ = ["Inspector"]


class Inspector:
    """
    Status: Experimental
     
    See `https://chromedevtools.github.io/devtools-protocol/tot/Inspector`
    """

    __slots__ = ["client"]

    def __init__(self, client: Union["ConnectionType", "SessionType"]) -> None:
        """Initialize a new instance of Inspector

        :param client: The client instance to be used to communicate with the remote browser instance
        """
        self.client: Union["ConnectionType", "SessionType"] = client

    def disable(self) -> Awaitable[Dict]:
        """
        Disables inspector domain notifications.

        See `https://chromedevtools.github.io/devtools-protocol/tot/Inspector#method-disable`

        :return: The results of the command
        """
        return self.client.send("Inspector.disable", {})

    def enable(self) -> Awaitable[Dict]:
        """
        Enables inspector domain notifications.

        See `https://chromedevtools.github.io/devtools-protocol/tot/Inspector#method-enable`

        :return: The results of the command
        """
        return self.client.send("Inspector.enable", {})

    def detached(
        self, listener: Optional[Callable[[Dict[str, Any]], Any]] = None
    ) -> Any:
        """
        Fired when remote debugging connection is about to be terminated. Contains detach reason.

        See `https://chromedevtools.github.io/devtools-protocol/tot/Inspector#event-detached`

        :param listener: Optional listener function
        :return: If a listener was supplied the return value is a callable that
        will remove the supplied listener otherwise a future that resolves
        with the value of the event
        """
        event_name = "Inspector.detached"
        if listener is None:
            future = self.client.loop.create_future()

            def _listener(event: Optional[Dict] = None) -> None:
                future.set_result(event)

            self.client.once(event_name, _listener)

            return future

        self.client.on(event_name, listener)
        return lambda: self.client.remove_listener(event_name, listener)

    def targetCrashed(self, listener: Optional[Callable[[Any], Any]] = None) -> Any:
        """
        Fired when debugging target has crashed

        See `https://chromedevtools.github.io/devtools-protocol/tot/Inspector#event-targetCrashed`

        :param listener: Optional listener function
        :return: If a listener was supplied the return value is a callable that
        will remove the supplied listener otherwise a future that resolves
        with the value of the event
        """
        event_name = "Inspector.targetCrashed"
        if listener is None:
            future = self.client.loop.create_future()

            def _listener(event: Optional[Dict] = None) -> None:
                future.set_result(event)

            self.client.once(event_name, _listener)

            return future

        self.client.on(event_name, listener)
        return lambda: self.client.remove_listener(event_name, listener)

    def targetReloadedAfterCrash(
        self, listener: Optional[Callable[[Any], Any]] = None
    ) -> Any:
        """
        Fired when debugging target has reloaded after crash

        See `https://chromedevtools.github.io/devtools-protocol/tot/Inspector#event-targetReloadedAfterCrash`

        :param listener: Optional listener function
        :return: If a listener was supplied the return value is a callable that
        will remove the supplied listener otherwise a future that resolves
        with the value of the event
        """
        event_name = "Inspector.targetReloadedAfterCrash"
        if listener is None:
            future = self.client.loop.create_future()

            def _listener(event: Optional[Dict] = None) -> None:
                future.set_result(event)

            self.client.once(event_name, _listener)

            return future

        self.client.on(event_name, listener)
        return lambda: self.client.remove_listener(event_name, listener)
