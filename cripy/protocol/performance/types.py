from typing import Any, List, Optional, Union, TypeVar
from cripy.helpers import ProtocolType


class Metric(object):
    """
    Run-time execution metric.
    """

    def __init__(self, name: str, value: float) -> None:
        """
        :param name: Metric name.
        :type name: str
        :param value: Metric value.
        :type value: float
        """
        super().__init__()
        self.name = name
        self.value = value

    def __contains__(self, item):
        return item in self.__dict__

    def __getitem__(self, k) -> Any:
        return self.__dict__[k]

    def get(self, what, default=None) -> Any:
        return self.__dict__.get(what, default)

    def __repr__(self) -> str:
        repr_args = []
        if self.name is not None:
            repr_args.append("name={!r}".format(self.name))
        if self.value is not None:
            repr_args.append("value={!r}".format(self.value))
        return "Metric(" + ", ".join(repr_args) + ")"

    @staticmethod
    def safe_create(init: Optional[dict]) -> Optional[Union["Metric", dict]]:
        if init is not None:
            try:
                ourselves = Metric(**init)
                return ourselves
            except Exception:
                return init
        else:
            return init

    @staticmethod
    def safe_create_from_list(
        init: Optional[List[dict]]
    ) -> Optional[List[Union["Metric", dict]]]:
        if init is not None:
            list_of_self = []
            for it in init:
                list_of_self.append(Metric.safe_create(it))
            return list_of_self
        else:
            return init


TYPE_TO_OBJECT = {"Metric": Metric}
