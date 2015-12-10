"""Python package for using the Urban Airship API"""
from .core import Airship
from .common import AirshipFailure, Unauthorized
from .push import (
    Push,
    ScheduledPush,
    all_,
    ios_channel,
    android_channel,
    amazon_channel,
    device_token,
    device_pin,
    apid,
    wns,
    mpns,
    tag,
    alias,
    segment,
    and_,
    or_,
    not_,
    location,
    recent_date,
    absolute_date,
    notification,
    ios,
    android,
    amazon,
    blackberry,
    wns_payload,
    mpns_payload,
    message,
    device_types,
    options,
    actions,
    interactive,
    scheduled_time,
    local_scheduled_time,
)

from .devices import (
    ChannelList,
    ChannelInfo,
    DevicePINInfo,
    DeviceTokenList,
    DevicePINList,
    APIDList,
    Feedback,
    TagList,
    Tag,
    DeleteTag,
    BatchTag,
    ChannelTags,
    Segment,
    SegmentList,
    ChannelUninstall,
    NamedUser,
    NamedUserList,
    StaticList,
    StaticLists,
    LocationFinder,
)

from .reports import (
    PerPushDetail,
    PerPushSeries,
    IndividualResponseStats,
    ResponseList,
    DevicesReport,
    OptInList,
    OptOutList,
    PushList,
    ResponseReportList,
    AppOpensList,
    TimeInAppList,
)

__all__ = [
    Airship,
    AirshipFailure,
    Unauthorized,
    all_,
    Push,
    ScheduledPush,
    ios_channel,
    android_channel,
    amazon_channel,
    device_token,
    device_pin,
    apid,
    wns,
    mpns,
    tag,
    alias,
    segment,
    and_,
    or_,
    not_,
    location,
    recent_date,
    absolute_date,
    notification,
    ios,
    android,
    amazon,
    blackberry,
    wns_payload,
    mpns_payload,
    message,
    options,
    actions,
    interactive,
    device_types,
    scheduled_time,
    local_scheduled_time,
    ChannelList,
    ChannelInfo,
    DevicePINInfo,
    DeviceTokenList,
    DevicePINList,
    APIDList,
    TagList,
    Tag,
    DeleteTag,
    BatchTag,
    Feedback,
    Segment,
    SegmentList,
    ChannelUninstall,
    PerPushDetail,
    PerPushSeries,
    NamedUser,
    NamedUserList,
    IndividualResponseStats,
    ResponseList,
    DevicesReport,
    OptInList,
    OptOutList,
    PushList,
    ResponseReportList,
    AppOpensList,
    TimeInAppList,
    StaticList,
    StaticLists,
    LocationFinder,
]

# Silence urllib3 INFO logging by default

import logging
logging.getLogger('requests.packages.urllib3.connectionpool').setLevel(logging.WARNING)
