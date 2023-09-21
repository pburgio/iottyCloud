"""Exceptions for iottyCloud."""


class UnauthorizedException(Exception):
    """Unauthorized access to iotty Cloud."""


class BadRequestException(Exception):
    """Bad request for iotty Cloud."""


class ForbiddenException(Exception):
    """Forbidden access to iotty Cloud."""


class NotFoundException(Exception):
    """Access to a non-existing EP for iotty Cloud."""
