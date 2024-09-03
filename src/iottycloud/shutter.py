"""Entity Class for iotty Shutter."""

import logging
from enum import Enum

from iottycloud.device import Device
from iottycloud.verbs import STATUS_STATIONATRY

_LOGGER = logging.getLogger(__name__)

class ShutterState(Enum):
    """Possible Shutter States."""

    STATIONARY = 0
    OPENING = 1
    CLOSING = 2

class Shutter(Device): # pylint: disable=too-few-public-methods
    """Entity Class for iotty Shutter."""

    status: ShutterState
    percentage: int

    def __init__(
            self, device_id: str, sn_: str, device_type: str, device_name: str
    ) -> None:
        """Build the iotty SH."""
        super().__init__(device_id, sn_, device_type, device_name)
        _LOGGER.debug("New Device %s %s", self.device_id, self.device_type)
        self.status = STATUS_STATIONATRY
        self.percentage = 0

    def update_status(self, status: str) -> None:
        """Update internal status of a device."""
        _LOGGER.debug("[%s] updating status to '%s'", self.name, status)
