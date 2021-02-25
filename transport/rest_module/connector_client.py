# sys/os
import sys, os
sys.path.append(os.getcwd() + '/messages_types_python')

# standart
from random import randint

# rest_module
from rest_module.transport_client import TransportClient

# proto
from messages_types_python import get_market_candles_pb2

class ConnectorClient:
    def __init__(self, use_sandbox=True, service_name = None):
        self.transport_client = TransportClient(service_name=service_name)
        self.use_sandbox = use_sandbox

    def __fill_basic_request_info(self, msg, response_topic='test_topic'):
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

        return self.transport_client.send_poll('connector.get.market.candles', value=msg.SerializeToString())

        # self.transport_client.send('connector.get.market.candles', value=msg.SerializeToString())
        # self.transport_client.subscribe('test_topic')
        # return self.transport_client.poll()
        # self.transport_client.pool()

