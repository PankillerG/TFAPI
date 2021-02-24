import trade_brokers.tinkoff.tinkoff as trade_broker

import get_market_candles_pb2

class MessageDistributor:
    def __init__(self):
        self.sync_client = trade_broker.SyncClient(use_sandbox=False)
        self.async_client = trade_broker.AsyncClient(use_sandbox=False)
        self.sandbox_sync_client = trade_broker.SyncClient()
        self.sandbox_async_client = trade_broker.AsyncClient()

    def __choose_client(self, pb):
        if not pb.basic_request_info.use_sandbox:
            if pb.basic_request_info.type == 'sync':
                return self.sync_client
            elif pb.basic_request_info.type == 'async':
                return self.async_client
        elif pb.basic_request_info.use_sandbox:
            if pb.basic_request_info.type == 'sync':
                return self.sandbox_sync_client
            elif pb.basic_request_info.type == 'async':
                return self.sandbox_async_client

    def __get_market_candles(self, message):
        pb = get_market_candles_pb2.GetMarketCandles()
        pb.ParseFromString(message.value)
        client = self.__choose_client(pb)
        candles = client.get_market_candles(pb.figi, pb.from_, pb.to_, pb.interval)
        return candles, pb.basic_request_info.response_topic


    def distribute_message(self, message):
        
        if message.topic == 'connector.get.market.candles':
            return self.__get_market_candles(message)

        # if message.topic == ''
        # other topics