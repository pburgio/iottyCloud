"""Generic iotty Device."""

from abc import abstractmethod


class Device:
    """Generic iotty Device."""

    def __init__(
            self, device_id: str, sn_: str, device_type: str, device_name: str
    ) -> None:
        """Build the generic iotty Device."""
        self.device_id = device_id
        self.serial_number = sn_
        self.device_type = device_type
        self.device_name = device_name

    @property
    def name(self) -> str:
        """Human-readable name of the device."""
        return f"{self.device_name} ({self.serial_number})"

    @abstractmethod
    def update_status(self, status: str) -> None:
        """Update internal status of a device."""
