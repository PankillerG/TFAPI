import sys, os

import inspect
from random import randint

# proto
sys.path.insert(0, '../transport/messages_types_python/')
import get_market_candles_pb2

from schemas import (
    KafkaMessageTopic,
    ProtoBufClass
)

class RequestCaster():
    def __init__(self, service_name: str, use_sandbox: bool):
        self.service_name = service_name
        self.use_sandbox = use_sandbox
        self.random_size = [0, 2**10]
    
    def _generate_request_topic(self) -> KafkaMessageTopic:
        prevprev_frame_name = inspect.currentframe().f_back.f_back.f_code.co_name
        request_topic = 'connector' + '.' + prevprev_frame_name
        request_topic = request_topic.replace('_', '.')
        return request_topic

    def _generate_response_topic(self) -> KafkaMessageTopic:
        prevprev_frame_name = inspect.currentframe().f_back.f_back.f_code.co_name
        return self.service_name + '.' + prevprev_frame_name + '.' + str(randint(*self.random_size))

    def _fill_basic_request_info(self, pb) -> ProtoBufClass:
        pb.basic_request_info.type = 'sync'
        pb.basic_request_info.use_sandbox = self.use_sandbox
        pb.basic_request_info.request_topic = self._generate_request_topic()
        pb.basic_request_info.response_topic = self._generate_response_topic()
        return pb
    
    
    def get_market_candles(self, figi, from_, to_, interval) -> ProtoBufClass:
        pb = get_market_candles_pb2.GetMarketCandles()
        pb.figi = figi
        pb.from_ = from_
        pb.to_ = to_
        pb.interval = interval
        pb = self._fill_basic_request_info(pb)
        return pb