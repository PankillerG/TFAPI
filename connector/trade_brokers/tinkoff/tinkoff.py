import os

import tinvest

from . import tinkoff_response_caster as response_caster

import get_market_candles_pb2

from typing import TypeVar, Union, NewType
from schemas import (
    KafkaMessageValue,
    ProtoBufClass
)

SANDBOX_TOKEN = os.environ.get('TINKOFF_SANDBOX_TOKEN')
TOKEN = os.environ.get('TINKOFF_TOKEN')

class SyncClient:
    token: str
    use_sandbox: bool

    def __init__(self, token: str=SANDBOX_TOKEN, use_sandbox: bool=True):
        self.client = tinvest.SyncClient(token, use_sandbox=use_sandbox)
        self.response_caster = response_caster.ResponseCaster()

    def get_market_candles(self, figi: str, from_: str, to_: str, interval: str) -> KafkaMessageValue:
        response = self.client.get_market_candles(figi, from_, to_, tinvest.CandleResolution(interval))
        return self.response_caster.get_market_candles(response)
    


class AsyncClient:
    def __init__(self, token='', use_sandbox=True):
        # self.client = tinvest.AsyncClient(token=token, use_sandbox=use_sandbox)
        pass