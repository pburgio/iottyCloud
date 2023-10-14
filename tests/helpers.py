"""helpers."""

from iottycloud.cloudapi import CloudApi

class CloudApiConcrete(CloudApi):
    """Concrete class to enable testing"""

    async def async_get_access_token(self) -> str:
        return "some-token"
