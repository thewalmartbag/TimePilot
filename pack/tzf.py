# time things

import time

def get_timezone_offset(timezone_name):
    """
    offset timeone
    """
    timezone_offset = time.timezone
    if time.daylight and time.localtime().tm_isdst:
        timezone_offset += 3600
    return timezone_offset

def get_current_time(timezone_name, format="default"):
    """
    return current time
    ANNDDDD formats
    """
    timezone_offset = get_timezone_offset(timezone_name)
    current_time = time.time() + timezone_offset
    if format == "hour":
        return time.strftime("%H", time.localtime(current_time))
    elif format == "minute":
        return time.strftime("%M", time.localtime(current_time))
    elif format == "second":
        return time.strftime("%S", time.localtime(current_time))
    elif format == "hour_minute":
        return time.strftime("%H:%M", time.localtime(current_time))
    elif format == "hour_second":
        return time.strftime("%H:%S", time.localtime(current_time))
    elif format == "minute_second":
        return time.strftime("%M:%S", time.localtime(current_time))
    elif format == "hour_minute_second":
        return time.strftime("%H:%M:%S", time.localtime(current_time))
    else:
        return time.strftime("%Y-%m-%d %H:%M:%S %Z%z", time.localtime(current_time))
