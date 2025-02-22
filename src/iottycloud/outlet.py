"""Entity Class for iotty Outlet."""

import logging

from iottycloud.device import Device
from iottycloud.verbs import STATUS_ON, COMMAND_TURNOFF, COMMAND_TURNON

_LOGGER = logging.getLogger(__name__)


class Outlet(Device): # pylint: disable=too-few-public-methods
    """Entity Class for iotty Outlet."""

    is_on: bool

    def __init__(
            self, device_id: str, sn_: str, device_type: str, device_name: str
    ) -> None:
        """Build the iotty OU."""
        super().__init__(device_id, sn_, device_type, device_name)
        _LOGGER.debug("New Device %s %s", self.device_id, self.device_type)
        self.is_on = False

    def cmd_turn_off(self) -> str:
        """Create a request to turn off the OU"""
        return COMMAND_TURNOFF

    def cmd_turn_on(self) -> str:
        """Create a request to turn on the OU"""
        return COMMAND_TURNON

    def update_status(self, status: str) -> None:
        """Update internal status of a device."""
        _LOGGER.debug("[%s] updating status to '%s'", self.name, status)
        self.is_on = status == STATUS_ON
