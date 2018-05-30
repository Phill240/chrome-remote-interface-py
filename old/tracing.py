# noinspection PyPep8
# noinspection PyArgumentList

"""
AUTO-GENERATED BY `scripts/generate_protocol.py` using `data/browser_protocol.json`
and `data/js_protocol.json` as inputs! Please do not modify this file.
"""

import logging
from typing import Any, Optional, Union

from cripy.helpers import PayloadMixin, BaseEvent, ProtocolType

log = logging.getLogger(__name__)
from cripy.protocol import io as IO

# MemoryDumpConfig: Configuration for memory dump. Used only when "memory-infra" category is enabled.
MemoryDumpConfig = dict

# TraceConfig: 
class TraceConfig(ProtocolType):
    def __init__(self,
                 recordMode: Optional['str'] = None,
                 enableSampling: Optional['bool'] = None,
                 enableSystrace: Optional['bool'] = None,
                 enableArgumentFilter: Optional['bool'] = None,
                 includedCategories: Optional['[]'] = None,
                 excludedCategories: Optional['[]'] = None,
                 syntheticDelays: Optional['[]'] = None,
                 memoryDumpConfig: Optional['MemoryDumpConfig'] = None,
                 ):

        self.recordMode = recordMode
        self.enableSampling = enableSampling
        self.enableSystrace = enableSystrace
        self.enableArgumentFilter = enableArgumentFilter
        self.includedCategories = includedCategories
        self.excludedCategories = excludedCategories
        self.syntheticDelays = syntheticDelays
        self.memoryDumpConfig = memoryDumpConfig


# StreamCompression: Compression type to use for traces returned via streams.
StreamCompression = str

class Tracing(PayloadMixin):
    """ 
    """
    @classmethod
    def end(cls):
        """Stop trace events collection.
        """
        return (
            cls.build_send_payload("end", {
            }),
            None
        )

    @classmethod
    def getCategories(cls):
        """Gets supported tracing categories.
        """
        return (
            cls.build_send_payload("getCategories", {
            }),
            cls.convert_payload({
                "categories": {
                    "class": [],
                    "optional": False
                },
            })
        )

    @classmethod
    def recordClockSyncMarker(cls,
                              syncId: Union['str'],
                              ):
        """Record a clock sync marker in the trace.
        :param syncId: The ID of this clock sync marker
        :type syncId: str
        """
        return (
            cls.build_send_payload("recordClockSyncMarker", {
                "syncId": syncId,
            }),
            None
        )

    @classmethod
    def requestMemoryDump(cls):
        """Request a global memory dump.
        """
        return (
            cls.build_send_payload("requestMemoryDump", {
            }),
            cls.convert_payload({
                "dumpGuid": {
                    "class": str,
                    "optional": False
                },
                "success": {
                    "class": bool,
                    "optional": False
                },
            })
        )

    @classmethod
    def start(cls,
              categories: Optional['str'] = None,
              options: Optional['str'] = None,
              bufferUsageReportingInterval: Optional['float'] = None,
              transferMode: Optional['str'] = None,
              streamCompression: Optional['StreamCompression'] = None,
              traceConfig: Optional['TraceConfig'] = None,
              ):
        """Start trace events collection.
        :param categories: Category/tag filter
        :type categories: str
        :param options: Tracing options
        :type options: str
        :param bufferUsageReportingInterval: If set, the agent will issue bufferUsage events at this interval, specified in milliseconds
        :type bufferUsageReportingInterval: float
        :param transferMode: Whether to report trace events as series of dataCollected events or to save trace to a
stream (defaults to `ReportEvents`).
        :type transferMode: str
        :param streamCompression: Compression format to use. This only applies when using `ReturnAsStream`
transfer mode (defaults to `none`)
        :type streamCompression: StreamCompression
        :param traceConfig: 
        :type traceConfig: TraceConfig
        """
        return (
            cls.build_send_payload("start", {
                "categories": categories,
                "options": options,
                "bufferUsageReportingInterval": bufferUsageReportingInterval,
                "transferMode": transferMode,
                "streamCompression": streamCompression,
                "traceConfig": traceConfig,
            }),
            None
        )



class BufferUsageEvent(BaseEvent):

    js_name = 'Tracing.bufferUsage'
    hashable = []
    is_hashable = False

    def __init__(self,
                 percentFull: Union['float', dict, None] = None,
                 eventCount: Union['float', dict, None] = None,
                 value: Union['float', dict, None] = None,
                 ):
        if isinstance(percentFull, dict):
            percentFull = float(**percentFull)
        elif isinstance(percentFull, list):
            percentFull = [float(**item) for item in percentFull]
        self.percentFull = percentFull
        if isinstance(eventCount, dict):
            eventCount = float(**eventCount)
        elif isinstance(eventCount, list):
            eventCount = [float(**item) for item in eventCount]
        self.eventCount = eventCount
        if isinstance(value, dict):
            value = float(**value)
        elif isinstance(value, list):
            value = [float(**item) for item in value]
        self.value = value

    @classmethod
    def build_hash(cls):
        raise ValueError('Unable to build hash for non-hashable type')


class DataCollectedEvent(BaseEvent):

    js_name = 'Tracing.dataCollected'
    hashable = []
    is_hashable = False

    def __init__(self,
                 value: Union['[]', dict],
                 ):
        if isinstance(value, dict):
            value = [](**value)
        elif isinstance(value, list):
            value = [(**item) for item in value]
        self.value = value

    @classmethod
    def build_hash(cls):
        raise ValueError('Unable to build hash for non-hashable type')


class TracingCompleteEvent(BaseEvent):

    js_name = 'Tracing.tracingComplete'
    hashable = []
    is_hashable = False

    def __init__(self,
                 stream: Union['IO.StreamHandle', dict, None] = None,
                 streamCompression: Union['StreamCompression', dict, None] = None,
                 ):
        if isinstance(stream, dict):
            stream = IO.StreamHandle(**stream)
        elif isinstance(stream, list):
            stream = [IO.StreamHandle(**item) for item in stream]
        self.stream = stream
        if isinstance(streamCompression, dict):
            streamCompression = StreamCompression(**streamCompression)
        elif isinstance(streamCompression, list):
            streamCompression = [StreamCompression(**item) for item in streamCompression]
        self.streamCompression = streamCompression

    @classmethod
    def build_hash(cls):
        raise ValueError('Unable to build hash for non-hashable type')