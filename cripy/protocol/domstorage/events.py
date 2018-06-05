from typing import Any, List, Optional, Union
from types import SimpleNamespace

try:
    from cripy.protocol.domstorage.types import *
except ImportError:
    pass


class DomStorageItemAddedEvent(object):

    event = "DOMStorage.domStorageItemAdded"

    def __init__(
        self, storageId: Union[StorageId, dict], key: str, newValue: str
    ) -> None:
        """
        :param storageId: The storageId
        :type storageId: dict
        :param key: The key
        :type key: str
        :param newValue: The newValue
        :type newValue: str
        """
        super().__init__()
        self.storageId = StorageId.safe_create(storageId)
        self.key = key
        self.newValue = newValue

    def __contains__(self, item):
        return item in self.__dict__

    def __getitem__(self, k) -> Any:
        return self.__dict__[k]

    def get(self, what, default=None) -> Any:
        return self.__dict__.get(what, default)

    def __repr__(self) -> str:
        repr_args = []
        if self.storageId is not None:
            repr_args.append("storageId={!r}".format(self.storageId))
        if self.key is not None:
            repr_args.append("key={!r}".format(self.key))
        if self.newValue is not None:
            repr_args.append("newValue={!r}".format(self.newValue))
        return "DomStorageItemAddedEvent(" + ", ".join(repr_args) + ")"

    @staticmethod
    def safe_create(
        init: Optional[dict]
    ) -> Optional[Union["DomStorageItemAddedEvent", dict]]:
        if init is not None:
            try:
                ourselves = DomStorageItemAddedEvent(**init)
                return ourselves
            except Exception:
                return init
        else:
            return init

    @staticmethod
    def safe_create_from_list(
        init: Optional[List[dict]]
    ) -> Optional[List[Union["DomStorageItemAddedEvent", dict]]]:
        if init is not None:
            list_of_self = []
            for it in init:
                list_of_self.append(DomStorageItemAddedEvent.safe_create(it))
            return list_of_self
        else:
            return init


class DomStorageItemRemovedEvent(object):

    event = "DOMStorage.domStorageItemRemoved"

    def __init__(self, storageId: Union[StorageId, dict], key: str) -> None:
        """
        :param storageId: The storageId
        :type storageId: dict
        :param key: The key
        :type key: str
        """
        super().__init__()
        self.storageId = StorageId.safe_create(storageId)
        self.key = key

    def __contains__(self, item):
        return item in self.__dict__

    def __getitem__(self, k) -> Any:
        return self.__dict__[k]

    def get(self, what, default=None) -> Any:
        return self.__dict__.get(what, default)

    def __repr__(self) -> str:
        repr_args = []
        if self.storageId is not None:
            repr_args.append("storageId={!r}".format(self.storageId))
        if self.key is not None:
            repr_args.append("key={!r}".format(self.key))
        return "DomStorageItemRemovedEvent(" + ", ".join(repr_args) + ")"

    @staticmethod
    def safe_create(
        init: Optional[dict]
    ) -> Optional[Union["DomStorageItemRemovedEvent", dict]]:
        if init is not None:
            try:
                ourselves = DomStorageItemRemovedEvent(**init)
                return ourselves
            except Exception:
                return init
        else:
            return init

    @staticmethod
    def safe_create_from_list(
        init: Optional[List[dict]]
    ) -> Optional[List[Union["DomStorageItemRemovedEvent", dict]]]:
        if init is not None:
            list_of_self = []
            for it in init:
                list_of_self.append(DomStorageItemRemovedEvent.safe_create(it))
            return list_of_self
        else:
            return init


class DomStorageItemUpdatedEvent(object):

    event = "DOMStorage.domStorageItemUpdated"

    def __init__(
        self, storageId: Union[StorageId, dict], key: str, oldValue: str, newValue: str
    ) -> None:
        """
        :param storageId: The storageId
        :type storageId: dict
        :param key: The key
        :type key: str
        :param oldValue: The oldValue
        :type oldValue: str
        :param newValue: The newValue
        :type newValue: str
        """
        super().__init__()
        self.storageId = StorageId.safe_create(storageId)
        self.key = key
        self.oldValue = oldValue
        self.newValue = newValue

    def __contains__(self, item):
        return item in self.__dict__

    def __getitem__(self, k) -> Any:
        return self.__dict__[k]

    def get(self, what, default=None) -> Any:
        return self.__dict__.get(what, default)

    def __repr__(self) -> str:
        repr_args = []
        if self.storageId is not None:
            repr_args.append("storageId={!r}".format(self.storageId))
        if self.key is not None:
            repr_args.append("key={!r}".format(self.key))
        if self.oldValue is not None:
            repr_args.append("oldValue={!r}".format(self.oldValue))
        if self.newValue is not None:
            repr_args.append("newValue={!r}".format(self.newValue))
        return "DomStorageItemUpdatedEvent(" + ", ".join(repr_args) + ")"

    @staticmethod
    def safe_create(
        init: Optional[dict]
    ) -> Optional[Union["DomStorageItemUpdatedEvent", dict]]:
        if init is not None:
            try:
                ourselves = DomStorageItemUpdatedEvent(**init)
                return ourselves
            except Exception:
                return init
        else:
            return init

    @staticmethod
    def safe_create_from_list(
        init: Optional[List[dict]]
    ) -> Optional[List[Union["DomStorageItemUpdatedEvent", dict]]]:
        if init is not None:
            list_of_self = []
            for it in init:
                list_of_self.append(DomStorageItemUpdatedEvent.safe_create(it))
            return list_of_self
        else:
            return init


class DomStorageItemsClearedEvent(object):

    event = "DOMStorage.domStorageItemsCleared"

    def __init__(self, storageId: Union[StorageId, dict]) -> None:
        """
        :param storageId: The storageId
        :type storageId: dict
        """
        super().__init__()
        self.storageId = StorageId.safe_create(storageId)

    def __contains__(self, item):
        return item in self.__dict__

    def __getitem__(self, k) -> Any:
        return self.__dict__[k]

    def get(self, what, default=None) -> Any:
        return self.__dict__.get(what, default)

    def __repr__(self) -> str:
        repr_args = []
        if self.storageId is not None:
            repr_args.append("storageId={!r}".format(self.storageId))
        return "DomStorageItemsClearedEvent(" + ", ".join(repr_args) + ")"

    @staticmethod
    def safe_create(
        init: Optional[dict]
    ) -> Optional[Union["DomStorageItemsClearedEvent", dict]]:
        if init is not None:
            try:
                ourselves = DomStorageItemsClearedEvent(**init)
                return ourselves
            except Exception:
                return init
        else:
            return init

    @staticmethod
    def safe_create_from_list(
        init: Optional[List[dict]]
    ) -> Optional[List[Union["DomStorageItemsClearedEvent", dict]]]:
        if init is not None:
            list_of_self = []
            for it in init:
                list_of_self.append(DomStorageItemsClearedEvent.safe_create(it))
            return list_of_self
        else:
            return init


EVENT_TO_CLASS = {
    "DOMStorage.domStorageItemAdded": DomStorageItemAddedEvent,
    "DOMStorage.domStorageItemRemoved": DomStorageItemRemovedEvent,
    "DOMStorage.domStorageItemUpdated": DomStorageItemUpdatedEvent,
    "DOMStorage.domStorageItemsCleared": DomStorageItemsClearedEvent,
}

EVENT_NS = SimpleNamespace(
    DomStorageItemAdded="DOMStorage.domStorageItemAdded",
    DomStorageItemRemoved="DOMStorage.domStorageItemRemoved",
    DomStorageItemUpdated="DOMStorage.domStorageItemUpdated",
    DomStorageItemsCleared="DOMStorage.domStorageItemsCleared",
)
