import trade_brokers.tinkoff.tinkoff as trade_broker

import get_market_candles_pb2

class MessageDistributor:
    def __init__(self):
        self.sync_client = trade_broker.SyncClient(use_sandbox=False)
        self.async_client = trade_broker.AsyncClient(use_sandbox=False)
        self.sandbox_sync_client = trade_broker.SyncClient()
        self.sandbox_async_client = trade_broker.AsyncClient()


    def _get_market_candles(self, message):
        pb = get_market_candles_pb2.GetMarketCandles()
        pb.ParseFromString(message.value)
        some_value = self.sandbox_sync_client.get_market_candles(pb.figi, pb.from_, pb.to_, pb.interval)
        return pb.basic_message_info.response_topic, some_value


    def distribute_message(self, message):
        
        if message.topic == 'connector.get.market.candles':
            return self._get_market_candles(message)

        # if message.topic == ''
        # other topics