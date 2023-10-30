"""Test for creation of CloudApi proxy."""
import requests

from .helpers import CloudApiConcrete

def test_creation_noparams_ws_error():
    """No 'WS' param causing errors."""
    try:
        _ = CloudApiConcrete(None, "host", "client_id")
    except ValueError as excinfo:
        assert str(excinfo) == "websession"

def test_creation_noparams_host_error():
    """No 'host' param causing errors."""
    try:
        _ = CloudApiConcrete(requests.Session(), None, "client_id")
    except ValueError as excinfo:
        assert str(excinfo) == "host"

def test_creation_noparams_clientid_error():
    """No 'clientid' param causing errors."""
    try:
        _ = CloudApiConcrete(requests.Session(), "host", None)
    except ValueError as excinfo:
        assert str(excinfo) == "client_id"

def test_creation_ok():
    """Creation completed succesfully."""

    sut = CloudApiConcrete(requests.Session(), "host", "client_id")

    assert sut is not None
