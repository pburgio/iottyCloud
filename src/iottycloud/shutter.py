"""Entity Class for iotty Shutter."""

import logging
from enum import Enum

import iottycloud.verbs as verbs
from iottycloud.device import Device
from iottycloud.verbs import (
    COMMAND_CLOSE,
    COMMAND_MOVE_TO_PERCENTAGE,
    COMMAND_OPEN,
    COMMAND_STOP,
    STATUS_STATIONATRY
)

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
        match status:
            case verbs.STATUS_OPENING:
                self.status = ShutterState.OPENING
            case verbs.STATUS_CLOSING:
                self.status = ShutterState.CLOSING
            case verbs.STATUS_STATIONATRY:
                self.status = ShutterState.STATIONARY
            case _:
                _LOGGER.error("Unknown shutter status")
                raise ValueError(status)
            
        _LOGGER.debug("[%s] updating status to '%s'", self.name, status)

    def update_percentage(self, percentage: int) -> None:
        """Update open percentage of a device."""
        self.percentage = percentage
        _LOGGER.debug("[%s] updating percentage to '%s'", self.name, percentage)


    def cmd_open(self) -> str:
        """Create a request to turn on the LS"""
        return COMMAND_OPEN

    def cmd_close(self) -> str:
        """Create a request to turn on the LS"""
        return COMMAND_CLOSE

    def cmd_stop(self) -> str:
        """Create a request to turn on the LS"""
        return COMMAND_STOP

    def cmd_move_to(self) -> str:
        """Create a request to turn on the LS"""
        return COMMAND_MOVE_TO_PERCENTAGE
