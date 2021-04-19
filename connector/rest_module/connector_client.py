# sys/os
import sys, os

# rest_module
from .request_caster import RequestCaster
from .response_caster import ResponseCaster
from .transport_client import TransportClient

from typing import Union
from schemas import (
    ProtoBufClass
)

class ConnectorClient:
    service_name: Union[str, None]
    use_sandbox: bool

    def __init__(self, service_name: Union[str, None]=None, use_sandbox: bool=True):
        self.service_name = service_name
        self.use_sandbox = use_sandbox
        self.transport_client = TransportClient(service_name=service_name)
        self.request_caster = RequestCaster(service_name, use_sandbox)
        self.response_caster = ResponseCaster()

    def get_market_candles(self, figi, from_, to_, interval) -> ProtoBufClass:
        pb = self.request_caster.get_market_candles(figi, from_, to_, interval)
        response = self.transport_client.send_poll(pb)
        return self.response_caster.get_market_candles(response)