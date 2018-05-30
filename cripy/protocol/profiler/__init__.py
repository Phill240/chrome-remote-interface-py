from typing import Any, List, Optional, Union
from cripy.protocol.profiler import events as Events
from cripy.protocol.profiler import types as Types


class Profiler(object):
    dependencies = ['Runtime', 'Debugger']

    def __init__(self, chrome):
        self.chrome = chrome

    async def disable(self) -> Optional[dict]:
        res = await self.chrome.send('Profiler.disable')
        return res

    async def enable(self) -> Optional[dict]:
        res = await self.chrome.send('Profiler.enable')
        return res

    async def getBestEffortCoverage(self) -> Optional[dict]:
        res = await self.chrome.send('Profiler.getBestEffortCoverage')
        res['result'] = Types.ScriptCoverage.safe_create_from_list(res['result'])
        return res

    async def setSamplingInterval(self, interval: int) -> Optional[dict]:
        """
        :param interval: New sampling interval in microseconds.
        :type interval: int
        """
        msg_dict = dict()
        if interval is not None:
            msg_dict['interval'] = interval
        res = await self.chrome.send('Profiler.setSamplingInterval', msg_dict)
        return res

    async def start(self) -> Optional[dict]:
        res = await self.chrome.send('Profiler.start')
        return res

    async def startPreciseCoverage(self, callCount: Optional[bool] = None, detailed: Optional[bool] = None) -> Optional[dict]:
        """
        :param callCount: Collect accurate call counts beyond simple 'covered' or 'not covered'.
        :type callCount: Optional[bool]
        :param detailed: Collect block-based coverage.
        :type detailed: Optional[bool]
        """
        msg_dict = dict()
        if callCount is not None:
            msg_dict['callCount'] = callCount
        if detailed is not None:
            msg_dict['detailed'] = detailed
        res = await self.chrome.send('Profiler.startPreciseCoverage', msg_dict)
        return res

    async def startTypeProfile(self) -> Optional[dict]:
        res = await self.chrome.send('Profiler.startTypeProfile')
        return res

    async def stop(self) -> Optional[dict]:
        res = await self.chrome.send('Profiler.stop')
        res['profile'] = Types.Profile.safe_create(res['profile'])
        return res

    async def stopPreciseCoverage(self) -> Optional[dict]:
        res = await self.chrome.send('Profiler.stopPreciseCoverage')
        return res

    async def stopTypeProfile(self) -> Optional[dict]:
        res = await self.chrome.send('Profiler.stopTypeProfile')
        return res

    async def takePreciseCoverage(self) -> Optional[dict]:
        res = await self.chrome.send('Profiler.takePreciseCoverage')
        res['result'] = Types.ScriptCoverage.safe_create_from_list(res['result'])
        return res

    async def takeTypeProfile(self) -> Optional[dict]:
        res = await self.chrome.send('Profiler.takeTypeProfile')
        res['result'] = Types.ScriptTypeProfile.safe_create_from_list(res['result'])
        return res

    @staticmethod
    def get_event_classes() -> Optional[dict]:
        return Events.EVENT_TO_CLASS
