import sys

import trade_brokers.tinkoff.tinkoff as trade_broker
import trade_brokers.tinkoff.tinkoff_request_caster as request_caster

sys.path.append('transport/messages_types_python')
import get_market_candles_pb2

from typing import Union
BrokerClient = Union[trade_broker.SyncClient, trade_broker.AsyncClient]
from schemas import (
    KafkaMessage,
    KafkaMessageTopic,
    KafkaMessageValue,
    ProtoBufClass
)

class MessageDistributor:
    def __init__(self):
        self.sync_client = trade_broker.SyncClient(use_sandbox=False)
        self.async_client = trade_broker.AsyncClient(use_sandbox=False)
        self.sandbox_sync_client = trade_broker.SyncClient()
        self.sandbox_async_client = trade_broker.AsyncClient()
        self.request_caster = request_caster.RequestCaster()

    def _choose_client(self, pb: ProtoBufClass) -> BrokerClient:
        if pb.basic_request_info.use_sandbox:
            if pb.basic_request_info.type == 'sync':
                return self.sandbox_sync_client
            elif pb.basic_request_info.type == 'async':
                return self.sandbox_async_client
        elif not pb.basic_request_info.use_sandbox:
            if pb.basic_request_info.type == 'sync':
                return self.sync_client
            elif pb.basic_request_info.type == 'async':
                return self.async_client

    def _get_market_candles(self, message: KafkaMessage) -> [KafkaMessageValue, KafkaMessageTopic]:
        pb = get_market_candles_pb2.GetMarketCandles()
        pb.ParseFromString(message.value)
        client = self._choose_client(pb)
        argv = self.request_caster.get_market_candles(pb)
        response = client.get_market_candles(*argv)
        return response, pb.basic_request_info.response_topic

    def distribute_message(self, message: KafkaMessage) -> [KafkaMessageValue, KafkaMessageTopic]:        
        if message.topic == 'connector.get.market.candles':
            return self._get_market_candles(message)

        # if message.topic == ''
        # other topics