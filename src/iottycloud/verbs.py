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

LS_DEVICE_TYPE_UID = "com.iotty.lightswitch"

SUPPORTED_DEVICE_TYPES = [LS_DEVICE_TYPE_UID]
