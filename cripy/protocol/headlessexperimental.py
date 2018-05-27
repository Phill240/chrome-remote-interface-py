# noinspection PyPep8
# noinspection PyArgumentList

"""
AUTO-GENERATED BY `scripts/generate_protocol.py` using `data/browser_protocol.json`
and `data/js_protocol.json` as inputs! Please do not modify this file.
"""

import logging
from typing import Any, Optional, Union

from cripy.helpers import PayloadMixin, BaseEvent, ChromeTypeBase

log = logging.getLogger(__name__)
from cripy.protocol import runtime as Runtime
from cripy.protocol import page as Page

# ScreenshotParams: Encoding options for a screenshot.
class ScreenshotParams(ChromeTypeBase):

    def __init__(self, format: Optional["str"] = None, quality: Optional["int"] = None):

        self.format = format
        self.quality = quality


class HeadlessExperimental(PayloadMixin):
    """ This domain provides experimental commands only supported in headless mode.
    """

    @classmethod
    def beginFrame(
        cls,
        frameTimeTicks: Optional["float"] = None,
        interval: Optional["float"] = None,
        noDisplayUpdates: Optional["bool"] = None,
        screenshot: Optional["ScreenshotParams"] = None,
    ):
        """Sends a BeginFrame to the target and returns when the frame was completed. Optionally captures a
screenshot from the resulting frame. Requires that the target was created with enabled
BeginFrameControl. Designed for use with --run-all-compositor-stages-before-draw, see also
https://goo.gl/3zHXhB for more background.
        :param frameTimeTicks: Timestamp of this BeginFrame in Renderer TimeTicks (milliseconds of uptime). If not set,
the current time will be used.
        :type frameTimeTicks: float
        :param interval: The interval between BeginFrames that is reported to the compositor, in milliseconds.
Defaults to a 60 frames/second interval, i.e. about 16.666 milliseconds.
        :type interval: float
        :param noDisplayUpdates: Whether updates should not be committed and drawn onto the display. False by default. If
true, only side effects of the BeginFrame will be run, such as layout and animations, but
any visual updates may not be visible on the display or in screenshots.
        :type noDisplayUpdates: bool
        :param screenshot: If set, a screenshot of the frame will be captured and returned in the response. Otherwise,
no screenshot will be captured. Note that capturing a screenshot can fail, for example,
during renderer initialization. In such a case, no screenshot data will be returned.
        :type screenshot: ScreenshotParams
        """
        return (
            cls.build_send_payload(
                "beginFrame",
                {
                    "frameTimeTicks": frameTimeTicks,
                    "interval": interval,
                    "noDisplayUpdates": noDisplayUpdates,
                    "screenshot": screenshot,
                },
            ),
            cls.convert_payload(
                {
                    "hasDamage": {"class": bool, "optional": False},
                    "screenshotData": {"class": str, "optional": True},
                }
            ),
        )

    @classmethod
    def disable(cls):
        """Disables headless events for the target.
        """
        return (cls.build_send_payload("disable", {}), None)

    @classmethod
    def enable(cls):
        """Enables headless events for the target.
        """
        return (cls.build_send_payload("enable", {}), None)


class NeedsBeginFramesChangedEvent(BaseEvent):

    js_name = "Headlessexperimental.needsBeginFramesChanged"
    hashable = []
    is_hashable = False

    def __init__(self, needsBeginFrames: Union["bool", dict]):
        if isinstance(needsBeginFrames, dict):
            needsBeginFrames = bool(**needsBeginFrames)
        elif isinstance(needsBeginFrames, list):
            needsBeginFrames = [bool(**item) for item in needsBeginFrames]
        self.needsBeginFrames = needsBeginFrames

    @classmethod
    def build_hash(cls):
        raise ValueError("Unable to build hash for non-hashable type")
