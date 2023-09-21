"""Test for creation of CloudApi proxy"""

from .helpers import CloudApiConcrete

def test_creation_noparams_error():
   cc = CloudApiConcrete(None, "host", "client_id")