"""Verbs for iotty CloudApi protocol."""

HTTP_HEADER_CLIENT_ID = "Iotty-Client-Id"

DEVICE_TYPE = "device_type"
DEVICE_ID = "device_id"
DEVICE_NAME = "device_name"
SERIAL_NUMBER = "serial_number"

RESULT = "Result"
"""Root for the results."""

STATUS = "status"
STATUS_ON = "on"
STATUS_OFF = "off"

STATUS_OPENING = "opening"
STATUS_CLOSING = "closing"
STATUS_STATIONATRY = "stationary"
OPEN_PERCENTAGE = "open_percentage"

COMMAND_TURNON = "turnon"
COMMAND_TURNOFF = "turnoff"

COMMAND_OPEN = "open"
COMMAND_CLOSE = "close"
COMMAND_STOP = "stop"
COMMAND_MOVE_TO_PERCENTAGE = "moveto"

LS_DEVICE_TYPE_UID = "com.iotty.lightswitch"
SH_DEVICE_TYPE_UID = "com.iotty.shutter"
OU_DEVICE_TYPE_UID = "com.iotty.outlet"

SUPPORTED_DEVICE_TYPES = [LS_DEVICE_TYPE_UID, SH_DEVICE_TYPE_UID, OU_DEVICE_TYPE_UID]
