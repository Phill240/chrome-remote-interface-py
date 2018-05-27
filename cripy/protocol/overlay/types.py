from typing import Any, List, Optional, Set, Union
from cripy.helpers import PayloadMixin, BaseEvent, ChromeTypeBase
from cripy.protocol.dom import types as DOM

InspectMode = str


class HighlightConfig(ChromeTypeBase):

    def __init__(
        self,
        showInfo: Optional[bool] = None,
        showRulers: Optional[bool] = None,
        showExtensionLines: Optional[bool] = None,
        displayAsMaterial: Optional[bool] = None,
        contentColor: Optional["DOM.RGBA"] = None,
        paddingColor: Optional["DOM.RGBA"] = None,
        borderColor: Optional["DOM.RGBA"] = None,
        marginColor: Optional["DOM.RGBA"] = None,
        eventTargetColor: Optional["DOM.RGBA"] = None,
        shapeColor: Optional["DOM.RGBA"] = None,
        shapeMarginColor: Optional["DOM.RGBA"] = None,
        selectorList: Optional[str] = None,
        cssGridColor: Optional["DOM.RGBA"] = None,
    ) -> None:
        super().__init__()
        self.showInfo: Optional[bool] = showInfo
        self.showRulers: Optional[bool] = showRulers
        self.showExtensionLines: Optional[bool] = showExtensionLines
        self.displayAsMaterial: Optional[bool] = displayAsMaterial
        self.contentColor: Optional[DOM.RGBA] = contentColor
        self.paddingColor: Optional[DOM.RGBA] = paddingColor
        self.borderColor: Optional[DOM.RGBA] = borderColor
        self.marginColor: Optional[DOM.RGBA] = marginColor
        self.eventTargetColor: Optional[DOM.RGBA] = eventTargetColor
        self.shapeColor: Optional[DOM.RGBA] = shapeColor
        self.shapeMarginColor: Optional[DOM.RGBA] = shapeMarginColor
        self.selectorList: Optional[str] = selectorList
        self.cssGridColor: Optional[DOM.RGBA] = cssGridColor