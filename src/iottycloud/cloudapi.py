"""Iotty middleware for CloudApi."""

from abc import ABC, abstractmethod
import logging
from typing import Any

from aiohttp import ClientResponse, ClientSession
from iottycloud.errors import (
    BadRequestException,
    ForbiddenException,
    NotFoundException,
    UnauthorizedException,
)
from iottycloud.utils import Factory
from iottycloud.verbs import HTTP_HEADER_CLIENT_ID

_LOGGER = logging.getLogger(__name__)


class CloudApi(ABC):
    """Class to make authenticated requests to iotty CloudApi."""

    def __init__(self, websession: ClientSession, host: str, client_id: str) -> None:
        """Initialize the auth."""
        #_LOGGER.debug("__init__ host %s", host)

        if websession is None:
            raise ValueError("websession")
        if host is None:
            raise ValueError("host")
        if client_id is None:
            raise ValueError("client_id")

        self.websession = websession
        self.host = host
        self._client_id = client_id

    @abstractmethod
    async def async_get_access_token(self) -> str:
        """Return a valid access token."""

    async def get_devices(self) -> list:
        """Return iotty devices for a specific user."""

        response = await self.__request("GET", "api/getdevices")

        await self.__handle_error(response)

        devices = await response.json()
        _LOGGER.debug("Got %d iotty Devices", len(devices))

        ret = []
        for _d in devices:
            new_device = Factory.create_device(_d)
            if new_device is not None:
                ret.append(new_device)

        return ret

    async def get_status(self, device_id: str) -> Any:
        """Check device status EP."""
        response = await self.__request("GET", f"api/device/{device_id}/getstatus")

        await self.__handle_error(response)

        res = await response.json()

        return res

    async def __handle_error(self, response: ClientResponse) -> None:
        """Handle possible errors from a request."""

        if response.status == 400:
            raise BadRequestException("Bad request")
        if response.status == 401:
            raise UnauthorizedException("Unauthorized")
        if response.status == 403:
            raise ForbiddenException("Forbidden")
        if response.status == 404:
            raise NotFoundException("Not found")

    async def __request(self, method: str, url: str, **kwargs) -> ClientResponse:
        """Make a request."""
        headers = kwargs.get("headers")

        if headers is None:
            headers = {}
        else:
            headers = dict(headers)

        access_token = await self.async_get_access_token()

        headers["Authorization"] = f"Bearer {access_token}"
        headers[HTTP_HEADER_CLIENT_ID] = self._client_id

        return await self.websession.request(
            method,
            f"{self.host}/{url}",
            **kwargs,
            headers=headers,
        )
