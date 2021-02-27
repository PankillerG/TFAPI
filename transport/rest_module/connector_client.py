# sys/os
import sys, os
sys.path.append(os.getcwd() + '/messages_types_python')
from random import randint
import inspect

# standart
from random import randint

# rest_module
from rest_module.transport_client import TransportClient

# proto
from messages_types_python import get_market_candles_pb2

class ConnectorClient:
    def __init__(self, use_sandbox=True, service_name = None):
        self.use_sandbox = use_sandbox
        self.transport_client = TransportClient(service_name=service_name)
        self.service_name = service_name
        self.random_size = [0, 2**10]

    def __generate_response_topic(self):
        prevprev_frame_name = inspect.currentframe().f_back.f_back.f_code.co_name
        return self.service_name + '.' + prevprev_frame_name + '.' + str(randint(*self.random_size))

    def __fill_basic_request_info(self, msg):
        response_topic = self.__generate_response_topic()
        msg.basic_request_info.type = 'sync'
        msg.basic_request_info.use_sandbox = self.use_sandbox
        msg.basic_request_info.response_topic = response_topic
        return msg

    def get_market_candles(self, figi, from_, to_, interval):
        msg = get_market_candles_pb2.GetMarketCandles()
        msg = self.__fill_basic_request_info(msg)
        msg.figi = figi
        msg.from_ = from_
        msg.to_ = to_
        msg.interval = interval

        msg2 = get_market_candles_pb2.GetMarketCandlesResponse()
        response = self.transport_client.send_poll(
            topic='connector.get.market.candles',
            value=msg.SerializeToString(),
            response_topic=msg.basic_request_info.response_topic)
        for partition in response:
            for message in response[partition]:
                msg2.ParseFromString(message.value)
                break
        return msg2