from typing import Any, List, Optional, Set, Union
from cripy.helpers import PayloadMixin, BaseEvent, ChromeTypeBase

CacheId = str


class DataEntry(ChromeTypeBase):

    def __init__(
        self,
        requestURL: str,
        requestMethod: str,
        requestHeaders: List["Header"],
        responseTime: float,
        responseStatus: int,
        responseStatusText: str,
        responseHeaders: List["Header"],
    ) -> None:
        super().__init__()
        self.requestURL: str = requestURL
        self.requestMethod: str = requestMethod
        self.requestHeaders: List[Header] = requestHeaders
        self.responseTime: float = responseTime
        self.responseStatus: int = responseStatus
        self.responseStatusText: str = responseStatusText
        self.responseHeaders: List[Header] = responseHeaders


class Cache(ChromeTypeBase):

    def __init__(self, cacheId: "CacheId", securityOrigin: str, cacheName: str) -> None:
        super().__init__()
        self.cacheId: CacheId = cacheId
        self.securityOrigin: str = securityOrigin
        self.cacheName: str = cacheName


class Header(ChromeTypeBase):

    def __init__(self, name: str, value: str) -> None:
        super().__init__()
        self.name: str = name
        self.value: str = value


class CachedResponse(ChromeTypeBase):

    def __init__(self, body: str) -> None:
        super().__init__()
        self.body: str = body