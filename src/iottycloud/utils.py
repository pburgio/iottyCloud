"""Utilities."""
import logging
from typing import Any

from iottycloud.lightswitch import LightSwitch
from iottycloud.shutter import Shutter
from iottycloud.verbs import (
    DEVICE_ID,
    DEVICE_NAME,
    DEVICE_TYPE,
    SERIAL_NUMBER,
    LS_DEVICE_TYPE_UID,
    SH_DEVICE_TYPE_UID
)

_LOGGER = logging.getLogger(__name__)


class Factory: # pylint: disable=too-few-public-methods
    """Helps creating objects iotty Device."""

    @staticmethod
    def create_device(json_dict: dict) -> Any:
        """Build the generic iotty Device from a JSON object."""

        if DEVICE_TYPE not in json_dict:
            _LOGGER.warning("Missing '%s' field in JSON", DEVICE_TYPE)
            return None

        if DEVICE_ID not in json_dict:
            _LOGGER.warning("Missing '%s' field in JSON", DEVICE_ID)
            return None

        if DEVICE_NAME not in json_dict:
            _LOGGER.warning("Missing '%s' field in JSON", DEVICE_NAME)
            return None

        device_type = json_dict[DEVICE_TYPE]

        if device_type == LS_DEVICE_TYPE_UID:
            return LightSwitch(
                json_dict[DEVICE_ID],
                json_dict[SERIAL_NUMBER],
                json_dict[DEVICE_TYPE],
                json_dict[DEVICE_NAME],
            )

        if device_type == SH_DEVICE_TYPE_UID:
            return Shutter(
                json_dict[DEVICE_ID],
                json_dict[SERIAL_NUMBER],
                json_dict[DEVICE_TYPE],
                json_dict[DEVICE_NAME],
            )

        _LOGGER.warning("Unknown iotty Device type '%s'", device_type)
        return None
